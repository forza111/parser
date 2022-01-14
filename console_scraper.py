import os

from scraper import get_content
import argparse


def createParser():
    parser = argparse.ArgumentParser(
        # prog="console_scraper",
        description="The command allows you to receive data from the online store from the received "
                    "URL and display the result.",
        add_help=False,
        usage='%(prog)s url [options]'
    )
    group_options = parser.add_argument_group(title="Options")
    group_options.add_argument('--width', type=int, default=60, help="Line width (default=60)", metavar="INT",
                         choices=range(10,101))
    parser.add_argument('url', type=str, help="URL for data parsing")
    group_options.add_argument('--image', action='store_true', default=False, help="Parse image url")
    group_options.add_argument('--save', action='store_true', default=False, help="Save the result in file txt")
    group_options.add_argument('--help', action='help', help='Show this help message and exit')
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    path = get_content(namespace.url, namespace.width, namespace.image, namespace.save)
    with open(path, 'r') as f:
        for line in f:
            print(line)
    os.unlink(path) if not namespace.save else None