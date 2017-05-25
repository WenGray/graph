# __author__ = "gray"


# 稀疏图
class SparseGraph:
    def __init__(self, n, directed):
        self.n = n
        # 边数
        self.m = 0
        # 初始化邻接表
        self.g = []
        for i in range(n):
            self.g.append([])
        self.directed = directed

    def add_edge(self, v, w):
        # 如果存在直接返回
        if self.has_edge(v, w):
            return
        # 将v和w两点连接, 由于是set 直接添加
        self.g[v].append(w)
        if not self.directed:
            self.g[w].append(v)
        self.m += 1

    def edges(self):
        return self.m

    def nodes(self):
        return self.n

    # 判断两点是否有边, v起点, w终点
    def has_edge(self, v, w):
        for i in self.g[v]:
            if i == w:
                return True
        return False

    def show(self):
        for i in range(self.n):
            print("{}: ".format(i), end="")
            for n in self.g[i]:
                print("{}  ".format(n), end="")
            print()

    def iter(self, v):
        # 返回一个对象的迭代器
        return SparseGraph.IterSparse(self, v).iter()

    # 迭代器
    class IterSparse:
        def __init__(self, graph, v):
            self.graph = graph
            self.v = v
            self.index = 0
            self.count = len(graph.g[v])
            self.end = False

        def iter(self):
            while True:
                if self.index >= self.count:
                    return
                yield self.graph.g[self.v][self.index]
                self.index += 1
