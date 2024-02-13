# these are simplified versions of iterators

def next_item():
    yield "bob" # yield is like pass , however it retains the last memory of the item
    yield "okinyi"
    yield "mirowe"
    yield "Larry"

next_item = next_item()
print(next(next_item))
print(next(next_item))
print(next(next_item))