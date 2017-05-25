# __author__ = "gray"


def read_graph(file_path, graph):
    with open(file_path) as f:
        line = f.readline()
        while line != '':
            # 遍历每一行
            arr = line.replace('\n', '').split(' ')
            arr = [int(i) for i in arr]
            graph.add_edge(arr[0], arr[1])
            line = f.readline()
        f.close()