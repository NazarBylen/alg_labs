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
        print(char)
        characters.append(char)
    for j in range(len(matrix)):
        matrix[i][j] = characters[j]

    characters.clear()

if __name__ == '__main__':
    print(matrix)
