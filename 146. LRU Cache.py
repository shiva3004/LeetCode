class LRUCache:

    class Node():
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.prev = None
    
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.mapper = collections.defaultdict(None)
        self.head = None
        self.tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.mapper.get(key, None)
        if node is None:
            return -1
        elif node == self.head:
            return node.value
        self.removeNode(node)
        self.insertNodeAtHead(node)
        return node.value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.mapper:
            self.removeNode(self.mapper[key])
            self.mapper.pop(key)
        if len(self.mapper) == self.capacity:
            self.mapper.pop(self.tail.key)
            self.removeNode(self.tail)
        node = self.Node(key, value)
        self.insertNodeAtHead(node)
        self.mapper[key] = node
        
        
    def removeNode(self, node):
        prev_node = node.prev; next_node = node.next
        if prev_node is None and next_node is None:
            self.head = None; self.tail = None
        elif next_node is None:
            prev_node.next = None
            self.tail = prev_node
        elif prev_node is None:
            next_node.prev = None
            self.head = next_node
        else:
            prev_node.next = next_node; next_node.prev = prev_node
        node.next = None; node.prev = None
        
        
    def insertNodeAtHead(self, node):
        if self.head is None:
            self.head = node; self.tail = node
        else:
            node.next = self.head; self.head.prev = node
            self.head = node
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
