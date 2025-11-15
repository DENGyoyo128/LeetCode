class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}  # key -> Node

        # 虚拟头尾节点，方便操作
        self.head = Node(0, 0)  # head.next 是最近使用的
        self.tail = Node(0, 0)  # tail.prev 是最久未使用的
        self.head.next = self.tail
        self.tail.prev = self.head

    # 在头部后面插入一个节点（标记为最近使用）
    def _add_node(self, node: Node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    # 把某个节点从链表中删除
    def _remove_node(self, node: Node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # 把节点挪到头部（最近使用）
    def _move_to_head(self, node: Node):
        self._remove_node(node)
        self._add_node(node)

    # 弹出尾部前面的那个节点（真正的 LRU）
    def _pop_tail(self) -> Node:
        lru = self.tail.prev
        self._remove_node(lru)
        return lru

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if not node:
            return -1
        # 用过了，挪到头部
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key)

        if node:
            # 更新值 + 挪到头部
            node.value = value
            self._move_to_head(node)
        else:
            # 新节点
            new_node = Node(key, value)
            self.map[key] = new_node
            self._add_node(new_node)

            if len(self.map) > self.capacity:
                # 超容量，删除 LRU
                tail = self._pop_tail()
                del self.map[tail.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)