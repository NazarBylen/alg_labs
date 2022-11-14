import time
import KMPAlg


def test_slow():
    string = 'aaaasaaaasasaaaaaassaaaaaaaasaaasaaaaasaaaaaaaaasaaaaaaaaasaaaaaaaaasaaaaaaaaas'
    for i in range(15):
        string = string + string

    string = string + 'd'
    substring = 'asd'

    start = time.time()
    assert KMPAlg.knuth_morris_pratt(string, substring) == True

    print("it took", time.time() - start, "seconds.")

def test_mid_speed_fisrt():
    string = 'uisuissssuuuiuiuiisuiuusiiiusisiausrrgghjhusuiuhkbnffffsuiiiiuuuiiiiiiiiihhhj'
    for i in range(10):
        string = string + string

    string = string + 'suiusdf'
    substring = 'suius'

    start = time.time()
    assert KMPAlg.knuth_morris_pratt(string, substring) == True

    print("it took", time.time() - start, "seconds.")

def test_mid_speed_second():
    string = 'aaafaaafasqaaaafaaaasaaaaafaaasaaaaaaaaasaffaaaaaaasaaaaaaaafaaaaaaaaasaaafaaaaas'
    for i in range(11):
        string = string + string

    string = string + 'fffaafas'
    substring = 'fffaaf'

    start = time.time()
    assert KMPAlg.knuth_morris_pratt(string, substring) == True

    print("it took", time.time() - start, "seconds.")

def test_fast():
    string = 'asaaaaaaasdaaaaaaaasaaaaaadaasaaaaaaaaasaaaaaaaaasaaaaaaaaasaaaaaaaaasaaaaaaaaas'
    for i in range(7):
        string = string + string

    string = string + 'dsa'
    substring = 'asdsa'

    start = time.time()
    assert KMPAlg.knuth_morris_pratt(string, substring) == True

    print("it took", time.time() - start, "seconds.")