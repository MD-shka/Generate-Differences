import argparse


def parse_args():
    pars = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    pars.add_argument(
        "-f", "--format",
        help="set format of output",
        choices=["stylish", "plain", "json"],
        default="stylish"
    )
    pars.add_argument("first_file")
    pars.add_argument("second_file")
    args = pars.parse_args()

    return args.first_file, args.second_file, args.format
