class Node:
    def __init__(self,key=0,val=0):
        self.key = key
        self.val = val
        self.prev= None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mp = {}

        self.left = Node()
        self.right = Node()
        #connecting both start and end node.
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):

        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self,node):

        prev_node = self.right.prev
        next_node = self.right

        prev_node.next = node
        node.prev = prev_node
        node.next = self.right
        next_node.prev = node
        

    def get(self, key: int) -> int:

        if key not in self.mp:
            return -1

        node = self.mp[key]

        #remove from list and put in the end
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.mp:
            self.remove(self.mp[key])
            del self.mp[key]

        node = Node(key,value)

        self.mp[key] = node

        self.insert(node)

        if len(self.mp) > self.cap:
            lru = self.left.next
            self.remove(lru)

            del self.mp[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)