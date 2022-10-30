f = open("Ijones .in", "r")
line = f.readline()
temp = line.split()
nodes_first = int(temp[0])
nodes_second = int(temp[1])

matrix = [['0' for i in range(nodes_first)] for j in range(nodes_second)]

characters = []

for i in range(len(matrix)):
    line = f.readline()
    for char in line:
        characters.append(char)
    for j in range(len(matrix)):
        matrix[i][j] = characters[j]

    characters.clear()


def findPath(n, m):

    if (m == 1 or n == 1):
        return 1
    return findPath(m, n - 1)



if __name__ == '__main__':
    print(matrix)
    n = nodes_first
    m = nodes_second
    print(findPath(n, m))
