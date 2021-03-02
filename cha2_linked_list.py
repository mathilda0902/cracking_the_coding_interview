class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes:
            node = Node(nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(elem)
                node = node.next
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def remove_dups(self, head):
        if self.head is None or self.head.next is None:
            return self.head
        
        current = self.head
        hash = set()
        hash.add(current.data)

        while current.next:
            if current.next.data in hash:
                current.next = current.next.next
            else:
                hash.add(current.next.data)
                current = current.next
        
        return head


if __name__ == '__main__':
    llist = LinkedList(nodes=[0,1,2,3,2,3,3,3,5])

    llist.remove_dups(llist.head)
    for node in llist:
        print(node.data)

