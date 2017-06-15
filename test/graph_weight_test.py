# __author__ = "gray"
from implement import graphs, util, algorithm
import os

if __name__ == '__main__':
    folder_path = os.path.abspath(os.path.dirname(os.getcwd()) + os.path.sep + ".")
    file_path = folder_path + os.path.sep + 'testGraphWeight.txt'
    graph = graphs.SparseGraphWeight(8, False)
    util.read_graph_weight(file_path, graph)

    graph.show()
    mst = algorithm.MST(graph)
    print(mst.wt())
