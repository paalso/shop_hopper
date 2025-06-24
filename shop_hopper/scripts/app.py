from collections import Counter
from rich import print
from rich.console import Console
from rich.table import Table
import sys
import time
import webbrowser

from shop_hopper.args_parser import ArgParser
from shop_hopper.logger import Logger
from shop_hopper.core.shop_hopper import ShopHopper
from shop_hopper.savers import HTMLSaver, JSONSaver
from shop_hopper.config.platforms import ALL_SUPPORTED_PLATFORMS


def parse_arguments():
    """Parses command-line arguments."""
    arg_parser = ArgParser()
    args = arg_parser.parse()

    platforms = args.platforms if args.platforms else ALL_SUPPORTED_PLATFORMS
    ignored_platforms = args.ignored_platforms or []
    platforms = [platform for platform in platforms
                 if platform not in ignored_platforms]

    if not platforms:
        sys.exit('Error: No platforms left to search after exclusions.')

    return args, platforms


def setup_logger():
    """Creates and returns a logger instance."""
    return Logger().get_logger()


def perform_search(logger, platforms, request):
    """Performs the search and returns results + duration in seconds."""
    shop_hopper = ShopHopper(logger, platforms)

    logger.debug(f"Starting search for '{request}' on {platforms}")
    start_time = time.time()
    search_result = shop_hopper.search(request)
    elapsed = time.time() - start_time

    logger.debug(f'Search completed in {elapsed:.2f} seconds')
    return search_result, elapsed


def print_search_summary(search_result, platforms):
    platform_counter = Counter(
        entry['platform'].get('alias') or entry['platform']['name'].lower()
        for entry in search_result
    )

    alias_to_name = {
        (entry['platform'].get('alias') or entry['platform']['name'].lower()):
        entry['platform']['name']
        for entry in search_result
    }

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Платформа", style="cyan")
    table.add_column("Найдено", justify="right", style="green")

    for alias in platforms:
        count = platform_counter.get(alias, 0)
        name = alias_to_name.get(alias, alias)
        icon = "🟢" if count > 0 else "⚪"
        table.add_row(f"{icon} {name}", str(count))

    Console().print(table)


def save_results(report, request, logger, output_dir, save_to_json):
    """Saves search results in the specified format."""
    savers = [HTMLSaver()]
    if save_to_json:
        savers.append(JSONSaver())

    html_file_path = None
    for saver in savers:
        file_path = saver.save(report, request, logger, output_dir)
        if isinstance(saver, HTMLSaver):
            html_file_path = file_path

    return html_file_path


def open_in_browser(file_path, logger):
    """Opens the HTML report in a web browser."""
    if not file_path:
        logger.warning(
            'HTML file was not saved, opening in the browser was skipped.')
        return

    try:
        chrome = webbrowser.get('google-chrome')
        chrome.open(file_path, new=2)
    except webbrowser.Error:
        logger.warning(
            'Google Chrome not found, opening in the default browser.')
        webbrowser.open(file_path, new=2)


def main():
    """
    Main entry point for the script. Handles the search process
    and saving the results.

    Steps:
        1. Parses the arguments
        2. Creates a logger instance
        3. Initializes the ShopHopper to perform the search
        4. Saves the search results to the specified directory.
    """
    args, platforms = parse_arguments()
    logger = setup_logger()
    ignored_platforms = args.ignored_platforms

    print(
        f'[bold green]🔍 Поиск:[/] [cyan]{args.request}[/] на '
        f'[yellow]{len(platforms)}[/] платформах...')

    if ignored_platforms:
        excluded = ', '.join(f'[red]{p}[/]' for p in ignored_platforms)
        print(f'[dim]🛑 Исключенные платформы:[/] {excluded}')
    else:
        print('[dim]✅ Все платформы включены в поиск[/]')

    search_result, elapsed = perform_search(logger, platforms, args.request)

    print(f'[bold green]✅ Завершено за {elapsed:.2f} секунд[/]')

    print_search_summary(search_result, platforms)

    html_file_path = save_results(
        search_result, args.request, logger, args.output_dir, args.json)
    open_in_browser(html_file_path, logger)

    logger.info(f'Results saved to {args.output_dir}')


if __name__ == '__main__':
    main()
