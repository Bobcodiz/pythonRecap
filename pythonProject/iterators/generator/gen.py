def Generator():
    yield "Hello World"
    yield "good morning"
    yield "good afternoon"
    yield "good evening"
    yield "good night"
    yield ("good")

g = Generator()
for g in Generator():
    print(g)