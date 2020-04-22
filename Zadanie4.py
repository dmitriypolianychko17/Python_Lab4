def count():
    word = 'spam'
    for i in range(1,5):
        elem = word[0:i]
        yield elem
for i in count():
    print(list(i))