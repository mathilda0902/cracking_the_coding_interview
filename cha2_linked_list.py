class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class LinkedList:
    def __init__(self, nodes):
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

    # remove duplicates
    def remove_dups(self, head):
        if self.head is None or self.head.next is None:
            return self.head

        current = self.head
        hash_set = set()
        hash_set.add(current.val)

        while current.next:
            if current.next.val in hash_set:
                current.next = current.next.next
            else:
                hash_set.add(current.next.val)
                current = current.next
        
        return head

    # find k-th element from last, 1 is the last element
    def find_k_last(self, head, k):
        p1 = p2 = self.head

        for i in range(k):
            if p1 == None: 
                return None
            p1 = p1.next
        
        while p1.next:
            p2 = p2.next
            p1 = p1.next
        
        return p2.next.val

    # delete middle node: given access to only node N, remove this element from a singly linked list
    def delete_middle(self, n):
        if n != None and n.next != None:
            n.val = n.next.val
            n.next = n.next.next

    # reverse linked list
    def reverse(self):
        prev = None
        current = self.head
        while(current != None):
            next_tmp = current.next
            current.next = prev
            prev = current
            current = next_tmp

        self.head = prev
        return self

    # palindrome
    def is_palindrome1(self) -> bool:
        # approach 1: reverse and compare
        reversed = self.reverse()
        for node in reversed:
            print(node.val)
        node_A = self.head
        node_B = reversed.head

        while (node_A != None and node_B != None):
            if node_A == node_B:
                node_A = node_A.next
                node_B = node_B.next
            else:
                return False
            
        return True


    def is_palindrome2(self) -> bool:
    # approach 2: iterative, fast slow pointers
        fast = slow = self.head
        stack = []
        
        while (fast != None and fast.next != None):
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next
            
        if fast != None:
            slow = slow.next
            
        while (slow != None):
            top = stack.pop()
            if slow.val != top:
                return False
            slow = slow.next
        
        return True

def is_palindrome3():
    # approach 3: recrusive
    pass


if __name__ == '__main__':
    llist = LinkedList(nodes=[0,1,2,3,2,3,3,3,5])
    llist = LinkedList(nodes=[1,2,3,2,1])
    llist = LinkedList(nodes=[1,2,2,1])

    # llist.remove_dups(llist.head)
    # for node in llist:
    #     print(node.val)

    # print(llist.find_k_last(llist.head, 7))
    reversed_llist = llist.reverse()
   
    # for node in reversed_llist:
    #     print(node.val)

    print(llist.is_palindrome2())
