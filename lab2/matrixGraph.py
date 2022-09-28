import numpy as np

matrix = np.loadtxt('input.txt', dtype=int)

def BFS():
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                if i > 0:
                    if j + 1 < (len(matrix[i])):
                        if matrix[i - 1][j + 1] == 1:
                            matrix[i - 1][j + 1] = -1
                    if matrix[i - 1][j] == 1:
                        matrix[i - 1][j] = -1
                elif j > 0:
                    if matrix[i][j - 1] == 1:
                        matrix[i][j - 1] = -1
                    if matrix[i - 1][j - 1] == 1:
                        matrix[i - 1][j - 1] = -1
                    if i + 1 < (len(matrix)):
                        if matrix[i + 1][j - 1] == 1:
                            matrix[i + 1][j - 1] = -1
                elif i + 1 < (len(matrix)) or j + 1 < (len(matrix[i])):
                    if matrix[i + 1][j] == 1:
                        matrix[i + 1][j] = -1
                    if matrix[i][j + 1] == 1:
                        matrix[i][j + 1] = -1
                elif i + 1 < (len(matrix)) and j + 1 < (len(matrix[i])):
                    if matrix[i + 1][j + 1] == 1:
                        matrix[i + 1][j + 1] = -1

    dist = []
    N = len(matrix)
    M = len(matrix[0])
    for i in range(N):
        dist.append([])
        for j in range(M):
            dist[i].append(-1)
        if matrix[i][0] == 1:
            dist[i][0] = 0

    visited = []
    queue = []

    for i in range(len(matrix)):
        if matrix[i][0] == 1:
            visited.append([i, 0])
    for i in range(len(matrix)):
        if matrix[i][0] == 1:
            queue.append([i, 0])

    while queue:
        m = queue.pop(0)

        """
        right
        """
        if m[1] + 1 < len(matrix[0]) and matrix[m[0]][m[1] + 1] == 1:
            if [m[0], m[1] + 1] not in visited:
                visited.append([m[0], m[1] + 1])
                queue.append([m[0], m[1] + 1])
                dist[m[0]][m[1] + 1] = dist[m[0]][m[1]] + 1
        """
        up
        """
        if m[0] - 1 > -1 and matrix[m[0] - 1][m[1]] == 1:
            if [m[0] - 1, m[1]] not in visited:
                visited.append([m[0] - 1, m[1]])
                queue.append([m[0] - 1, m[1]])
                dist[m[0] - 1][m[1]] = dist[m[0]][m[1]] + 1

        """
        down
        """
        if m[0] + 1 < len(matrix) and matrix[m[0] + 1][m[1]] == 1:
            if [m[0] + 1, m[1]] not in visited:
                visited.append([m[0] + 1, m[1]])
                queue.append([m[0] + 1, m[1]])
                dist[m[0] + 1][m[1]] = dist[m[0]][m[1]] + 1

        """
        left
        """
        if m[1] - 1 > -1 and matrix[m[0]][m[1] - 1] == 1:
            if [m[0], m[1] - 1] not in visited:
                visited.append([m[0], m[1] - 1])
                queue.append([m[0], m[1] - 1])
                dist[m[0]][m[1] - 1] = dist[m[0]][m[1]] + 1

    print(matrix)
    print(visited)

    min_dist = 0

    with open("output.txt", "w") as f:
        for i in range(len(matrix)):
            if [i, len(matrix[0]) - 1] in visited:
                if min_dist == 0 or dist[i][len(matrix[0]) - 1] < min_dist:
                    min_dist = dist[i][len(matrix[0]) - 1]

        if min_dist == 0:
            f.write('-1')
        else:
            f.write(str(min_dist) + '\n')


if __name__ == "__main__":
    print(f"matrix: \n{matrix}")
    print("/////////////")
    BFS()
