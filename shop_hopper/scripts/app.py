from shop_hopper.args_parser import ArgParser
from shop_hopper.logger import Logger
from shop_hopper.shop_hopper import ShopHopper
from shop_hopper.savers import HTMLSaver, JSONSaver
from shop_hopper.config.platforms import ALL_SUPPORTED_PLATFORMS
import sys


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
    arg_parser = ArgParser()
    args = arg_parser.parse()
    request = args.request
    output_dir = args.output_dir
    save_to_json = args.json
    platforms = args.platforms if args.platforms else ALL_SUPPORTED_PLATFORMS
    ignored_platforms = args.ignored_platforms or []

    platforms = [platform for platform in platforms
                 if platform not in ignored_platforms]

    logger = Logger().get_logger()

    if not platforms:
        logger.error(
            'No platforms left to search after excluding ignored platforms.')
        sys.exit(1)

    shop_hopper = ShopHopper(logger, platforms)
    report = shop_hopper.search(request)

    savers = [HTMLSaver()]
    if save_to_json:
        savers.append(JSONSaver())

    for saver in savers:
        saver.save(report, request, logger, output_dir)

    logger.info(f'Results saved to {output_dir}')


if __name__ == '__main__':
    main()
