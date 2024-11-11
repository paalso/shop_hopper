import argparse
import os


class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description='Search for products across multiple platforms.')
        self._add_arguments()

    def _add_arguments(self):
        self.parser.add_argument(
            'request',
            type=str,
            help='Keywords for the search request.'
        )

        self.parser.add_argument(
            '-o', '--output_dir',
            type=str,
            default=os.getcwd(),  # Default to the current working directory
            help='Directory to save the report. '
                 'Defaults to the current directory.'
        )

        self.parser.add_argument(
            '-j', '--json',
            action='store_true',
            help='If set, saves the report in JSON format.'
        )

    def parse(self):
        """
        Parses the command line arguments.

        Returns:
            argparse.Namespace: Parsed arguments object containing
            'request' and 'output_dir'.
        """
        return self.parser.parse_args()
