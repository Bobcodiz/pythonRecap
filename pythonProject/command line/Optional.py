import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, help='enter your name')
    parser.add_argument('--age', type=int, help='enter your age')

    args = parser.parse_args()
    print(args.name, "your age is" , args.age)
