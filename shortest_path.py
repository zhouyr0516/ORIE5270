import heapq


def find_shortest_path(name_txt_file, source, destination):

    file = open(name_txt_file, "r")

    vertex_set = []
    edge_set = dict()
    dist = dict()
    prev = dict()
    current_vertex = 0
    line_count = 1

    for line in file:

        if line[-1:] == '\n':
            line = line[:-1]

        if line_count%2 == 1:
            if int(line) not in vertex_set:
                vertex_set.append(int(line))
            current_vertex = int(line)
        else:
            tmp = eval('['+line+']')
            for x in tmp:
                if x[0] not in vertex_set:
                    vertex_set.append(x[0])
                edge_set[(current_vertex, x[0])] = x[1]

        line_count = line_count + 1

    for vertex in vertex_set:
        dist[vertex] = float('Inf')
        prev[vertex] = None

    priority_queue = []
    dist[source] = 0
    edge_list = list(edge_set.keys())
    edge_map = dict()

    for i in range(len(vertex_set)):
        edge_map[vertex_set[i]] = []

    for i in range(len(edge_list)):
        edge_map[edge_list[i][0]].append(edge_list[i][1])

    for i in range(len(vertex_set)):
        heapq.heappush(priority_queue, (dist[vertex_set[i]], vertex_set[i]))

    while priority_queue:

        u = heapq.heappop(priority_queue)

        for v in edge_map[u[1]]:
            alt_path = dist[u[1]] + edge_set[(u[1], v)]

            if alt_path < dist[v]:
                dist[v] = alt_path
                prev[v] = u[1]
                heapq.heappush(priority_queue, (alt_path, v))

    shortest_path = [destination]
    place = destination

    while prev[place]:
        shortest_path.append(prev[place])
        place = prev[place]
    if prev[place] == 0:
        shortest_path.append(prev[place])

    if len(shortest_path) == 1:
        return (float('Inf'), None)

    shortest_path = shortest_path[::-1]

    return (dist[destination], shortest_path)

#source = 0
#destination = 4
#filename = "test1.txt"
#res = find_shortest_path(filename, source, destination)
#print(res)

