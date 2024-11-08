import argparse
import os
from shop_hopper.logger import Logger
from shop_hopper.shop_hopper import ShopHopper
from shop_hopper.savers import JSONSaver


def parse_args():
    parser = argparse.ArgumentParser(
        description='Search for products across multiple platforms.')

    parser.add_argument(
        'request',
        type=str,
        help='Keywords for the search request.')

    parser.add_argument(
        '-o', '--output_dir',
        type=str,
        default=os.getcwd(),
        help='Directory to save the report. Defaults to the current directory.'
    )

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    request = args.request
    output_dir = args.output_dir

    logger = Logger().get_logger()
    shop_hopper = ShopHopper(logger)

    report = shop_hopper.search(request)
    savers = [JSONSaver()]
    for saver in savers:
        saver.save(report, request, logger, output_dir)


if __name__ == '__main__':
    main()
