from shop_hopper.args_parser import ArgParser
from shop_hopper.logger import Logger
from shop_hopper.shop_hopper import ShopHopper
from shop_hopper.savers import HTMLSaver, JSONSaver
from shop_hopper.config.platforms import ALL_SUPPORTED_PLATFORMS
import sys
import webbrowser


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
    """Performs the search and returns the results."""
    shop_hopper = ShopHopper(logger, platforms)
    return shop_hopper.search(request)


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
    report = perform_search(logger, platforms, args.request)
    html_file_path = \
        save_results(report, args.request, logger, args.output_dir, args.json)
    open_in_browser(html_file_path, logger)
    logger.info(f'Results saved to {args.output_dir}')


if __name__ == '__main__':
    main()
