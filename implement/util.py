# __author__ = "gray"
from implement import graphs


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


def read_graph_weight(file_path, graph):
    with open(file_path) as f:
        line = f.readline()
        # 更新节点数
        if graph.nodes != int(line):
            print("输入的节点个数与文件中的不符")
        line = f.readline()
        while line != '':
            # 遍历每一行
            arr = line.replace('\n', '').split(' ')
            graph.add_edge(int(arr[0]), int(arr[1]), float(arr[2]))
            line = f.readline()
        f.close()
    return graph
