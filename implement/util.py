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


# 最小堆
class MinHeap:
    def __init__(self, capacity):
        self.list_arr = [None] * capacity
        # 容量
        self.capacity = capacity
        # 已有元素个数
        self.size = 0

    def insert(self, item):
        if self.size >= self.capacity:
            print('insert error, size >= capacity')
            return
        self.list_arr[self.size] = item
        # 处理元素
        self._shift_up_(self.size)
        self.size += 1

    # 取出堆顶元素
    def extract(self):
        if self.size == 0:
            return None
        r = self.list_arr[0]
        # 将最后一个元素替换到第一个元素
        self.list_arr[0] = self.list_arr[self.size - 1]
        self.list_arr[self.size - 1] = None
        self.size -= 1
        self._shift_down(0)
        return r

    # 将序号为w的元素上移
    def _shift_up_(self, w):
        parent = int((w - 1) / 2)
        if w > 0 and self.list_arr[parent] > self.list_arr[w]:
            # swap
            temp = self.list_arr[parent]
            self.list_arr[parent] = self.list_arr[w]
            self.list_arr[w] = temp
            self._shift_up_(parent)

    def _shift_down(self, w):
        child_smaller = w * 2 + 1
        if child_smaller >= self.size:
            return
        # 找到子元素中较小的一个
        if child_smaller + 1 < self.size and self.list_arr[child_smaller] > self.list_arr[child_smaller + 1]:
            child_smaller += 1
        # 比较是否交换
        if self.list_arr[w] > self.list_arr[child_smaller]:
            # swap
            temp = self.list_arr[child_smaller]
            self.list_arr[child_smaller] = self.list_arr[w]
            self.list_arr[w] = temp
            self._shift_down(child_smaller)

    def empty(self):
        return self.size == 0
