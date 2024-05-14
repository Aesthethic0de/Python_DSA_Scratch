class NewNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = NewNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def insert_at_start(self, value):
        new_node = NewNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            temp = new_node
            temp.next = self.head
            self.head = temp
            self.length += 1

    def insert_at_end(self, value):
        new_node = NewNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def delete_at_start(self):
        if self.head.next is None:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            temp = self.head
            temp = temp.next
            self.head = temp
            self.length -= 1

    def delete_at_end(self):
        if self.length == 0:
            print("no values")
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

    def delete_at_index(self, index):
        if index > self.length:
            print("out of bound error")
        elif index == 0:
            self.delete_at_start()
        elif index == self.length:
            self.delete_at_end()
        else:
            prev = self.head
            next_node = self.head.next.next
            for i in range(index - 1):
                prev = prev.next
                next_node = next_node.next
            prev.next = next_node
            self.length -= 1

    def insert_at_index(self, value, index):
        new_node = NewNode(value)
        if index > self.length:
            print("out of bound index")
        elif index == self.length:
            self.insert_at_end(value)
        elif index == 0:
            self.insert_at_start(value)
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            self.head.next = new_node
            new_node.next = temp
            self.length += 1

    def get_value_from_index(self, index):
        if self.head is None:
            print(0)
        elif index == 0:
            print(self.head.value)
        elif index == self.length:
            print(self.tail.next.value)
        elif index > self.length:
            print("not found loop out of bound")
        elif index == self.length - 1:
            print("None")
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            print(temp.value)

    def traverse(self):
        linked_list = "Linked List = [ "
        if self.head is None:
            return 0
        else:
            temp = self.head
            while temp is not None:
                print_str = f"{temp.value} ---> "
                linked_list += print_str
                temp = temp.next
            linked_list += " None ]"
            print(linked_list)
            print(f"The length of LinkedList is {self.length}")

    def reverse_linked_list(self):
        if self.head is None:
            print("Linkedlist empty")
        else:
            temp = self.head
            self.head = self.tail
            self.tail = temp
            before = None
            while temp.next is not None:
                after = temp.next
                temp.next = before
                before = temp
                temp = after
            temp.next = before
            self.traverse()


if __name__ == "__main__":
    test = LinkedList(1)
    test.insert_at_end(2)
    test.traverse()
    test.insert_at_start(7)
    test.traverse()
    test.delete_at_end()
    test.traverse()
    test.insert_at_start(9)
    test.insert_at_start(10)
    test.traverse()
    test.delete_at_start()
    test.insert_at_index(100, 0)
    test.traverse()
    test.insert_at_index(1001, index=1)
    test.traverse()
    test.delete_at_index(1)
    test.traverse()
    test.get_value_from_index(3)
    test.reverse_linked_list()
