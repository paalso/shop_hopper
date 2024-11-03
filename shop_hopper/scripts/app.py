import argparse
import os
from shop_hopper.shop_hopper import ShopHopper


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
    print("Hello! It's Shop Hopper")

    args = parse_args()
    request = args.request

    shop_hopper = ShopHopper()
    report = shop_hopper.search(request)
    print(report)


if __name__ == '__main__':
    main()
