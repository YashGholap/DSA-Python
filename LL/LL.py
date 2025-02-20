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



my_linked_list = LinkedList(1)

my_linked_list.append(2)

my_linked_list.append(3)
# print("Before pop")
# my_linked_list.print_list()

# print("popped item")
# print(my_linked_list.pop())

# my_linked_list.prepend(0)
# print("LL after prepend")
# # my_linked_list.print_list()
# my_linked_list.pop_first()
# my_linked_list.append(5)
# my_linked_list.append(4)
# my_linked_list.append(6)
# print("Getting node at index 2: ", my_linked_list.get(2).value)
# print("Setting value of node 2 to 3:", my_linked_list.set_value(2,3))
# # my_linked_list.print_list()

# # print(my_linked_list.insert(3,5))
# my_linked_list.set_value(4,5)
# # my_linked_list.print_list()
# my_linked_list.remove(4)
# my_linked_list.print_list()
my_linked_list.reverse()
my_linked_list.print_list()

# print(my_linked_list.print_list())
