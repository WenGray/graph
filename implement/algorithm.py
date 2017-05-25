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
        it = self.graph.iter(v)
        for node in it:
            if not self.visited[node]:
                self.dfs(node)

    def count(self):
        return self.component_count


class Path:
    def __init__(self, graph, source):
        self.graph = graph
        self.visit_from = [-1] * graph.nodes()
        self.visited = [False] * graph.nodes()
        self.dfs(source)

    def dfs(self, v):
        self.visited[v] = True
        it = self.graph.iter(v)
        for node in it:
            if not self.visited[node]:
                self.visit_from[node] = v
                self.dfs(node)

    # 计算路线
    def path(self, w):
        paths = [w]
        t = self.visit_from[w]
        while t != -1:
            paths.append(t)
            t = self.visit_from[t]
        return paths

    def show_path(self, w):
        paths = self.path(w)
        for index, node in enumerate(paths[::-1]):
            if index == len(paths) - 1:
                print(node)
            else:
                print("{} -->".format(node), end=" ")
