# __author__ = "gray"
import queue


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
        print("DFS: ")
        for index, node in enumerate(paths[::-1]):
            if index == len(paths) - 1:
                print(node)
            else:
                print("{} -->".format(node), end=" ")


class ShortestPath:
    def __init__(self, graph, s):
        self.s = s
        self.graph = graph
        self.visited = [False] * graph.nodes()
        self.visit_from = [-1] * graph.nodes()
        # 一个记录当前距离的数组
        self.ord = [-1] * graph.nodes()
        # 广度优先
        q = queue.Queue()
        q.put(s)
        self.visited[s] = True
        self.ord[s] = 0
        while not q.empty():
            t = q.get()
            it = self.graph.iter(t)
            for node in it:
                if not self.visited[node]:
                    # 未被访问
                    q.put(node)
                    self.visited[node] = True
                    self.visit_from[node] = t
                    self.ord[node] = self.ord[t] + 1

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
        print("BFS: 距离: {}".format(self.ord[w]))
        for index, node in enumerate(paths[::-1]):
            if index == len(paths) - 1:
                print(node)
            else:
                print("{} -->".format(node), end=" ")


class MultiShortestPath:
    def __init__(self, graph, s):
        self.s = s
        self.graph = graph
        self.visited = [False] * graph.nodes()
        self.visit_from = [[]] * graph.nodes()
        # 一个记录当前距离的数组
        self.ord = [-1] * graph.nodes()
        self.m_path = []
        self.temp_single = []
        # 广度优先
        q = queue.Queue()
        q.put(s)
        self.visited[s] = True
        self.ord[s] = 0
        while not q.empty():
            t = q.get()
            it = self.graph.iter(t)
            for node in it:
                if not self.visited[node]:
                    # 未被访问
                    q.put(node)
                    self.visited[node] = True
                    self.visit_from[node] = [t]
                    self.ord[node] = self.ord[t] + 1
                elif self.ord[node] == self.ord[t] + 1:
                    self.visit_from[node].append(t)

    # 计算路线
    def path(self, w):
        self.m_path.clear()
        # 对visit_from 进行深度遍历
        self.m_path.append([w])
        self.dfs_path(w)

    def dfs_path(self, v):
        f = self.visit_from[v]
        if len(f) == 0:
            return
        elif len(f) == 1:
            # 添加到数组后面
            self.append_after(f[0], v)
            self.dfs_path(f[0])
        else:
            # 找到以v结尾的路线, 复制 len(f) - 1 条
            cp = len(f) - 1
            self.copy_with_last(v, cp)
            # 添加到结尾
            for i in f:
                self.append_after(i, v)
                self.dfs_path(i)

    # 在某个元素后面添加(某个元素为数组最后一个元素) 只append一次
    def append_after(self, i, after):
        for path in self.m_path:
            if path[-1] == after:
                path.append(i)
                return

    # 复制以 last 结尾的数组 copies 次 (last 不需要在数组结尾)
    def copy_with_last(self, last, copies):
        temp_arr = []
        for path in self.m_path:
            # 查看是否在其中
            try:
                index = path.index(last)
                temp_arr.append(path[0: index + 1])
            except ValueError:
                pass
        # 循环copy
        for i in range(0, copies):
            for arr in temp_arr:
                self.m_path.append(arr.copy())


    def show_path(self, w):
        self.path(w)
        print("M_BFS: 距离: {}".format(self.ord[w]))
        for path in self.m_path:
            for index, node in enumerate(path[::-1]):
                if index == len(path) - 1:
                    print(node)
                else:
                    print("{} -->".format(node), end=" ")
