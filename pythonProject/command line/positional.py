import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('number1', type=int, help='First number')
    parser.add_argument("number2", type=int, help='Second number')
    parser.add_argument("operation", type=str, help= "operation to perform")

    args = parser.parse_args()

    if args.operation == "add":
        print(args.number1 + args.number2)
    elif args.operation == "subtract":
        print(args.number1 - args.number2)
    elif args.operation == "multiplication":
        print(args.number1 * args.number2)
    elif args.operation == "division":
        print(args.number1 / args.number2)