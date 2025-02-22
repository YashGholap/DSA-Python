class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length  = 1

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        # if no node is present
        if self.head is None:
            return None
        #if only one node is present:
        temp = self.head
        pre = self.head
        popped_item = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_item
        #else
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        return popped_item
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head  = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            return temp
        else:
            self.head = self.head.next
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self,index,value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next, temp.next = temp.next,new_node
        self.length += 1
        return True

    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    # Important for interview
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def find_middle_node(self):
        #edge case : if head and tail is not present i.e list is empty
        if self.head and self.tail is None:
            return None
        #two pointer approach
        temp = self.head
        prev = self.head
        #looping until temp and temp.next is present
        while(temp and temp.next):
            prev = prev.next
            temp = temp.next.next
        return prev
    
    def has_loop(self):
        if self.head and self.tail is None:
            return None
        temp = self.head
        prev = self.head
        while(temp and temp.next):
            prev = prev.next
            temp = temp.next.next
            if prev == temp:
                return True
        return False
    
def findKth_node_from_end(ll, k):
    # intizializing 2 pointers
    fast = slow = ll.head
    #run fast pointer till k node
    for _ in range(k):
        #check if fast becomes None before reaching Kth Index i.e Index is out of bound.
        #if that's the case return True
        if fast == None:
            return None
        fast = fast.next
        
    while(fast):
        slow = slow.next
        fast = fast.next
    return slow

    
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 1
result = findKth_node_from_end(my_linked_list, k)

print(result.value)  # Output: 4