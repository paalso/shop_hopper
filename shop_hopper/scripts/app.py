from shop_hopper.args_parser import ArgParser
from shop_hopper.logger import Logger
from shop_hopper.shop_hopper import ShopHopper
from shop_hopper.savers import HTMLSaver, JSONSaver
from shop_hopper.config.platforms import ALL_SUPPORTED_PLATFORMS
import sys


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

    for saver in savers:
        saver.save(report, request, logger, output_dir)


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
    save_results(report, args.request, logger, args.output_dir, args.json)
    logger.info(f'Results saved to {args.output_dir}')


if __name__ == '__main__':
    main()
