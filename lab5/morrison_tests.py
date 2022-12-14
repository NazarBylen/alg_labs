import time
import KMPAlg


def test_slow():
    string = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    for i in range(15):
        string += string

    string += 'jab'
    substring = 'ajab'

    start = time.time()
    assert KMPAlg.knuth_morris_pratt(string, substring) is True

    print("it took", time.time() - start, "seconds.")

def test_middle_speed_fisrt():
    string = 'akajbakaklaklakajbakaklaklakajbakakla'
    for i in range(15):
        string += string

    string += 'akajbakaklaklj'

    substring = 'akajbakaklaklj'

    start = time.time()
    assert KMPAlg.knuth_morris_pratt(string, substring) is True

    print("it took", time.time() - start, "seconds.")

def test_middle_speed_second():
    string = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    for i in range(15):
        string += string
        if i == 8:
            string += 'c'

    substring = 'aaaac'

    start = time.time()
    assert KMPAlg.knuth_morris_pratt(string, substring) is True

    print("it took", time.time() - start, "seconds.")

def test_fast():
    string = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    for i in range(15):
        string += string

    string += 'a'
    substring = 'aaaaa'

    start = time.time()
    assert KMPAlg.knuth_morris_pratt(string, substring) is True

    print("it took", time.time() - start, "seconds.")