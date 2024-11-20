import argparse
import os
from shop_hopper.config.platforms import PLATFORM_ALIASES


class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description=(
                'Search for products across multiple platforms. '
                'This tool allows you to search for products based '
                'on specific keywords, select platforms, exclude certain '
                'platforms, and save the results in a desired format.'
            )
        )
        self.valid_platforms = " ".join(PLATFORM_ALIASES.keys())
        self._add_arguments()

    def _add_arguments(self):
        self.parser.add_argument(
            'request',
            type=str,
            help=(
                'Keywords for the search request. Use relevant keywords '
                'to search for products.'
            )
        )

        self.parser.add_argument(
            '-o', '--output_dir',
            type=str,
            default=os.getcwd(),
            help=(
                'Directory to save the report. Defaults to the current '
                'working directory. You can specify a different directory '
                'if needed.'
            )
        )

        self.parser.add_argument(
            '-j', '--json',
            action='store_true',
            help=(
                'If set, saves the report in JSON format. By default, '
                'the report is saved in plain text.'
            )
        )

        self.parser.add_argument(
            '-p', '--platforms',
            type=str,
            nargs='+',
            choices=PLATFORM_ALIASES,
            help=(
                'One or more platforms to search on. '
                f'Valid platforms: {self.valid_platforms}. '
                'You can specify multiple platforms by separating them with '
                'spaces (e.g., "alib olx").'
            )
        )

        self.parser.add_argument(
            '-i', '--ignored_platforms',
            type=str,
            nargs='+',
            choices=PLATFORM_ALIASES,
            help=(
                'One or more platforms to ignore in the search. '
                f'Valid platforms: {self.valid_platforms}. '
                'This option takes precedence over the platforms included '
                'using the --platforms option.'
            )
        )

    def parse(self):
        """
        Parses the command line arguments.

        Returns:
            argparse.Namespace: Parsed arguments object containing
            'request', 'output_dir', 'json', 'platforms', 'ignore_platforms'.
        """
        return self.parser.parse_args()
