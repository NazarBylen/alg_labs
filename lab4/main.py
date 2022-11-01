import numpy


with open("Ijones.in") as file:
    lines = [line.rstrip() for line in file]

input = [list(i) for i in lines[1:]]
width = int(lines[0].split(' ')[0])
height = int(lines[0].split(' ')[1])


def transpose(input):

    transposed_input = numpy.transpose(input)
    for middle_rows in transposed_input[-1:]:
        middle_rows[1:-1] = ""
    print(transposed_input)
    return transposed_input

def dist_for_element(transpose_matrix, width):
    unique_values = numpy.unique(transpose_matrix)
    routes = dict((key, numpy.zeros(width)) for key in unique_values)
    relatives = dict((key, numpy.zeros(width)) for key in unique_values)

    for i, i_value in enumerate(transpose_matrix):
        for j, j_value in enumerate(i_value):
            if not j_value:
                continue
            print(j_value)
            routes[j_value][i] += 1

            if i > 0 and j_value != transpose_matrix[i - 1][j]:
                relatives[j_value][i] += 1
                prev = transpose_matrix[i - 1][j]
                routes[j_value][i] *= routes[prev][i - 1]

        if i == 0:
            continue
        for element in set(i_value):
            if element and sum((routes[element])[:i]) != 0:
                routes[element][i] *= sum((routes[element])[:i])
                routes[element][i] += relatives[element][i]
        print("======================================")
        print("======================================")
    return routes

def count_paths(routes):
    return numpy.sum([value[-1] for value in routes.values()])

def to_file(routes):
    with open("Ijones .out", "w") as out:
        out.write(str(count_paths(routes)))

if __name__ == "__main__":
    new_input = transpose(input)
    paths = dist_for_element(new_input, width)
    to_file(paths)