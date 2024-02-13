cord = ((1, 2), (2, 3), (4, 5), (6, 7), (8, 9))

with open("./ppt.txt", "w") as f:
    for item in cord:
        f.write(str(item) + "\n")


def count():
    with open("./ppt.txt", "r") as f:
        content = f.read()
        n = input("Enter number to search: ")

        nc = content.count(n)

        if nc > 0:
            print(f"Number {n} appears {nc} times.")
        else:
            print(f"Number {n} does not appear in the file.")


count()
