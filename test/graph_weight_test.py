# __author__ = "gray"
from implement import graphs, util, algorithm

if __name__ == '__main__':
    file_path = '/Users/leigang/Documents/Work/python-workspace/graph/testGraphWeight.txt'
    graph = graphs.SparseGraphWeight(8, False)
    util.read_graph_weight(file_path, graph)

    print(graph.nodes)
    graph.show()
