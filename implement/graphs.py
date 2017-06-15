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


# 边
class Edge:
    def __init__(self, v, w, weight):
        self.n1 = v
        self.n2 = w
        self.weight = weight

    def v(self):
        return self.n1

    def w(self):
        return self.n2

    def wt(self):
        return self.weight

    def other(self, v):
        assert (v == self.n1 or v == self.n2)
        return self.n1 if v == self.n2 else self.n2

    def __lt__(self, other):
        return self.wt() < other.wt()

    def __gt__(self, other):
        return self.wt() > other.wt()

    def __cmp__(self, other):
        return self.wt() == other.wt()

    def __str__(self):
        return ' {} <-> {} : {}'.format(self.n1, self.n2, self.weight)


# 有权图
class SparseGraphWeight:
    def __init__(self, n, directed):
        # 节点个数通过read 从文件中读取
        self.n = n
        # 边数
        self.m = 0
        self.directed = directed
        self.g = []
        for i in range(n):
            self.g.append([])

    def __getattr__(self, item):
        if item == 'nodes':
            return self.n
        elif item == 'edges':
            return self.m

    def add_edge(self, v, w, weight):
        # 检测是否存在
        if self.is_exist(v, w):
            return
        edge_v = Edge(v, w, weight)
        self.g[v].append(edge_v)
        if not self.directed:
            if not self.is_exist(w, v):
                edge_w = Edge(w, v, weight)
                self.g[w].append(edge_w)
        self.m += 1

    def is_exist(self, v, w):
        for edge in self.g[v]:
            if edge.other(v) == w:
                return True
        return False

    def show(self):
        for index, edges in enumerate(self.g):
            print('{} ---> '.format(index), end=' ')
            for edge in edges:
                print(edge, end=' ')
            print()

    def iter(self, v):
        # 返回一个对象的迭代器
        return SparseGraphWeight.IterGraph(self, v).iter()

        # 迭代器

    class IterGraph:
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
