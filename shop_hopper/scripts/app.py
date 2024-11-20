from shop_hopper.args_parser import ArgParser
from shop_hopper.logger import Logger
from shop_hopper.shop_hopper import ShopHopper
from shop_hopper.savers import HTMLSaver, JSONSaver
from shop_hopper.config.platforms import PLATFORMS


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
    platforms = args.platforms if args.platforms else PLATFORMS.values()

    logger = Logger().get_logger()
    shop_hopper = ShopHopper(logger, platforms)
    report = shop_hopper.search(request)

    savers = [HTMLSaver()]
    if save_to_json:
        savers.append(JSONSaver())

    for saver in savers:
        saver.save(report, request, logger, output_dir)


if __name__ == '__main__':
    main()
