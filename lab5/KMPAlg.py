import numpy as np


def knuth_morris_pratt(string, substring):
    def build_sub(string):
        j = 0
        i = 1

        substring = np.full((len(string)), -1)

        while i < len(string):
            if string[i] == string[j]:
                substring[i] = j
                i, j = i + 1, j + 1
            elif j > 0:
                j = substring[j - 1] + 1
            else:
                i += 1
        print(substring)
        return substring

    def matcher(string, substring, pattern):
        i, j = 0, 0
        while i < len(string):
            if string[i] == substring[j]:
                if j == len(substring) - 1:
                    return True
                i, j = i + 1, j + 1
            elif j > 0:
                j = pattern[j - 1] + 1
            else:
                i += 1
        return False

    pattern = build_sub(substring)
    return matcher(string, substring, pattern)
