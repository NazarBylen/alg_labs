def is_client(clients, number):
    for i in range(len(clients)):
        if number == clients[i]:
            return True
    return False


f = open("gamsrv.in", "r")
line = f.readline()
temp = line.split()
num_node = int(temp[0])
num_vertice = int(temp[1])
line = f.readline()
temp = line.split()
clients = [int(i) for i in temp]
distance_matrix = [[float('inf') for i in range(num_node)] for i in range(num_node)]
for i in range(num_vertice):
    line = f.readline()
    temp = line.split()
    edge = [int(x) for x in temp]
    distance_matrix[edge[0] - 1][edge[1] - 1] = edge[2]
    distance_matrix[edge[1] - 1][edge[0] - 1] = edge[2]
f.close()

prior_matrix = [[0 for i in range(num_node)] for j in range(num_node)]
for p in range(num_node):
    for q in range(num_node):
        prior_matrix[p][q] = q
for k in range(num_node):
    for i in range(num_node):
        for j in range(num_node):
            if distance_matrix[i][j] > distance_matrix[i][k] + distance_matrix[k][j]:
                distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j]
                prior_matrix[i][j] = prior_matrix[i][k]

for i in range(num_node):
    if is_client(clients, i + 1):
        for j in range(num_node):
            distance_matrix[i][j] = 0
    else:
        for j in range(num_node):
            distance_matrix[j][i] = 0

global_max = 10000000000
for i in range(num_node):
    local_max = 0
    for j in range(num_node):
        if distance_matrix[i][j] > local_max:
            local_max = distance_matrix[i][j]
    if (local_max < global_max) & (local_max > 0):
        global_max = local_max

f = open("gamsrv.out", "w")
f.write(str(global_max))
f.close()
