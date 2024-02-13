import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('greetings', help="Good Morning! You")
    print(parser.parse_args().greetings)
    return parser.parse_args()


today = parse_args()
print(today.greetings)
