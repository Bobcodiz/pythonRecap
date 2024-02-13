with open("paragraph.txt", "r") as f:
    paragraph = f.read()
    for l in paragraph.split("\n"):
        w = l.split()
        print(len(w))
