class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val, self.prev, self.next = val, prev, next

class MyLinkedList:

    def __init__(self):
        self.left, self.right = Node(0), Node(0)
        self.left.next, self.right.prev = self.right, self.left
        self.size = 0

    def getPrev(self, index):
        if index < self.size // 2:
            cur = self.left
            for i in range(index):
                cur = cur.next
        else:
            cur = self.right
            for i in range(self.size - index + 1):
                cur = cur.prev
        return cur

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        return self.getPrev(index).next.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        node = Node(val)
        prev, nxt = self.getPrev(index), self.getPrev(index).next
        node.prev, node.next = prev, nxt
        prev.next, nxt.prev = node, node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        node = self.getPrev(index).next
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)