book = {}

book['bob'] = {
    'author': 'Bob',
    'title': 'life journey',
    'year': '2024',
    'isbn': '0-001'
}
book['Stephen'] = {
    'author': 'Stephen',
    'title': 'mount kenya journey',
    'year': '2020',
    'isbn': '0-002'
}

c = book['bob']['isbn']
print(c)
h = book['Stephen']['title']
print(h)