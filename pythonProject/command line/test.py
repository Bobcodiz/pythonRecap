import argparse

parser = argparse.ArgumentParser()
print("this is a test")
parser.add_argument("--time", type=str, help="time")
parser.add_argument("--duration", type=int, help="duration")
parser.add_argument("--bye", type=str, help="bye")

args = parser.parse_args()

print(args.time, args.duration, args.bye)