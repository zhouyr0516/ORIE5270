def find_negative_cycles(name_txt_file):

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
            tmp = eval('[' + line + ']')
            for x in tmp:
                if x[0] not in vertex_set:
                    vertex_set.append(x[0])
                edge_set[(current_vertex, x[0])] = x[1]

        line_count = line_count + 1

    # dummpy vertex 't'
    for v in vertex_set:
        edge_set[('t', v)] = 0
    vertex_set.append('t')


    for vertex in vertex_set:
        dist[vertex] = float('Inf')
        prev[vertex] = None

    source = vertex_set[-1]
    dist[source] = 0
    edge_list = list(edge_set.keys())
    edge_map = dict()

    for i in range(len(vertex_set)):
        edge_map[vertex_set[i]] = []

    for i in range(len(edge_list)):
        edge_map[edge_list[i][0]].append(edge_list[i][1])

    for i in range(len(vertex_set) - 1):
        for e in edge_list:
            if dist[e[0]] + edge_set[e] < dist[e[1]]:
                dist[e[1]] = dist[e[0]] + edge_set[e]
                prev[e[1]] = e[0]

    for e in edge_list:
        if dist[e[0]] + edge_set[e] < dist[e[1]]:
            place = e[1]
            negative_path = [e[1]]
            while prev[place] not in negative_path:
                negative_path.append(prev[place])
                place = prev[place]
            negative_path = negative_path[::-1]
            return negative_path

    return None

#filename = 'test3.txt'
#res = find_negative_cycles(filename)
#print(res)


