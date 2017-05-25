# __author__ = "gray"
from implement import graphs


# 计算联通分量
class Component:
    def __init__(self, graph):
        self.graph = graph
        self.component_count = 0
        # 初始化
        self.visited = [False] * graph.nodes()
        # 深度优先遍历
        for i in range(graph.nodes()):
            if not self.visited[i]:
                self.component_count += 1
                self.dfs(i)

    def dfs(self, v):
        # 遍历v这个点
        self.visited[v] = True
        it = graphs.IterSparse(self.graph, v).iter()
        for node in it:
            if not self.visited[node]:
                self.dfs(node)

    def count(self):
        return self.component_count


class Path:
    def __init__(self, graph):
        self.graph = graph
        self.visit_from = [-1] * graph.nodes()
        self.visited = [False] * graph.nodes()

    def dfs(self, v):
        self.visited[v] = True
        it = graphs.IterSparse(self.graph, v).iter()
        for node in it:
            if not self.visited[node]:
                self.visit_from[node] = v
                self.dfs(it)