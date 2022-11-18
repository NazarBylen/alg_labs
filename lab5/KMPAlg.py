import numpy as np


def knuth_morris_pratt(string, substring):
    def build_sub(substring_to_match):
        start_index = 0
        end_index = 1

        pattern__of_prefixes = np.full((len(substring_to_match)), -1)

        while end_index < len(substring_to_match):

            if substring_to_match[end_index] == substring_to_match[start_index]:
                pattern__of_prefixes[end_index] = start_index
                end_index, start_index = end_index + 1, start_index + 1

            elif start_index > 0:
                start_index = pattern__of_prefixes[start_index - 1] + 1

            else:
                end_index += 1
        print(pattern__of_prefixes)
        return pattern__of_prefixes

    def matcher(string, substring, pattern):
        start_index = 0
        end_index = 0

        while end_index < len(string):

            if string[end_index] == substring[start_index]:
                if start_index == len(substring) - 1:
                    return True
                end_index, start_index = end_index + 1, start_index + 1

            elif start_index > 0:
                start_index = pattern[start_index - 1] + 1

            else:
                end_index += 1

        return False

    pattern = build_sub(substring)
    return matcher(string, substring, pattern)
