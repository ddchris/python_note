import timeit

def test():
    words = 'lettersdfsddsdfwe'
    letter_counter = {char:words.count(char) for char in set(words)}
    return letter_counter

def test2():
    words = 'lettersewreewerre'
    letter_counter = {}
    for x in set(words):
        letter_counter[x] = words.count(x)
    return letter_counter

print(test())
print(test2())

if __name__ == '__main__':
    print(timeit.timeit("test()", setup="from __main__ import test"))
    print(timeit.timeit("test2()", setup="from __main__ import test2"))
