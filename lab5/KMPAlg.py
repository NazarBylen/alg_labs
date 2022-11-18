import numpy as np


def knuth_morris_pratt(string, substring):
    def build_sub(substring_to_match):
        j = 0
        i = 1

        pattern__of_prefixes = np.full((len(substring_to_match)), -1)

        while i < len(substring_to_match):

            if substring_to_match[i] == substring_to_match[j]:
                pattern__of_prefixes[i] = j
                i, j = i + 1, j + 1

            elif j > 0:
                j = pattern__of_prefixes[j - 1] + 1

            else:
                i += 1
        print(pattern__of_prefixes)
        return pattern__of_prefixes

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
