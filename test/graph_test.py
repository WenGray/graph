# __author__ = "gray"
from implement import graphs, util, algorithm

if __name__ == '__main__':
    file_path = '/Users/leigang/Documents/Work/python-workspace/graph/testMultiPath.txt'
    graph = graphs.SparseGraph(9, False)
    util.read_graph(file_path, graph)
    # graph.show()
    # 计算联通分量
    # al = algorithm.Component(graph)
    # print("计算得到 component = {}".format(al.count()))

    # Path
    path = algorithm.Path(graph, 0)
    path.show_path(8)

    # ShortestPath
    s_path = algorithm.ShortestPath(graph, 0)
    s_path.show_path(8)

    # MultiShortestPath
    m_path = algorithm.MultiShortestPath(graph, 0)
    m_path.show_path(8)
