import time
import KMPAlg


def test_slow():
    string = 'abbabiaabbabaaiabbabbabaabbabaaaabb'
    for i in range(10):
        string = string + string

    string = string + 'abab'
    substring = 'abab'

    start = time.time()
    assert KMPAlg.knuth_morris_pratt(string, substring) == True

    print("it took", time.time() - start, "seconds.")

def test_mid_speed_fisrt():
    string = 'ryoputhuytuitrurstutusiutyrtyts'
    for i in range(10):
        string = string + string

    string = string + 'iusiusiu'
    substring = 'siusiusiu'

    start = time.time()
    assert KMPAlg.knuth_morris_pratt(string, substring) == True

    print("it took", time.time() - start, "seconds.")

def test_mid_speed_second():
    string = 'iiiooklfkdlfalblppskvlfalojffa'
    for i in range(10):
        string = string + string

    string = string + 'fafafa'
    substring = 'fafafafa'

    start = time.time()
    assert KMPAlg.knuth_morris_pratt(string, substring) == True

    print("it took", time.time() - start, "seconds.")

def test_fast():
    string = 'uuirieofkirokfgorgrpgp'
    for i in range(10):
        string = string + string

    string = string + 'as'
    substring = 'as'

    start = time.time()
    assert KMPAlg.knuth_morris_pratt(string, substring) == True

    print("it took", time.time() - start, "seconds.")