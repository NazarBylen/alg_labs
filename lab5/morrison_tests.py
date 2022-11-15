import time
import KMPAlg


def test_slow():
    string = 'abbabiaabbabaaiabbabbabaabbabaiaabb'
    for i in range(15):
        string = string + string

    string = string + 'ababiaiai'
    substring = 'ababiaiai'

    start = time.time()
    assert KMPAlg.knuth_morris_pratt(string, substring) == True

    print("it took", time.time() - start, "seconds.")

def test_mid_speed_fisrt():
    string = 'suissuiffiussissuiffiufiussissuiffius'
    for i in range(10):
        string = string + string

    string = string + 'iusiusiu'
    substring = 'siusiusiu'

    start = time.time()
    assert KMPAlg.knuth_morris_pratt(string, substring) == True

    print("it took", time.time() - start, "seconds.")

def test_mid_speed_second():
    string = 'afffauoafffaaafafffauoafffaaaffa'
    for i in range(11):
        string = string + string

    string = string + 'fafafa'
    substring = 'fafafafa'

    start = time.time()
    assert KMPAlg.knuth_morris_pratt(string, substring) == True

    print("it took", time.time() - start, "seconds.")

def test_fast():
    string = 'aasssaassdasaaassaasaasssas'
    for i in range(7):
        string = string + string

    string = string + 'as'
    substring = 'asas'

    start = time.time()
    assert KMPAlg.knuth_morris_pratt(string, substring) == True

    print("it took", time.time() - start, "seconds.")