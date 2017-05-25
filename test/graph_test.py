# __author__ = "gray"
from implement import graphs, util, algorithm

if __name__ == '__main__':
    file_path = '/Users/leigang/Documents/Work/python-workspace/graph/testG1.txt'
    graph = graphs.SparseGraph(9, False)
    util.read_graph(file_path, graph)
    graph.show()
    # 计算联通分量
    al = algorithm.Component(graph)
    print("计算得到 component = {}".format(al.count()))

    # Path
    path = algorithm.Path(graph, 1)
    path.show_path(4)
