class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None


class DoublyLinkedList:
    def __init__(self, value):
        self.length = 0
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length += 1

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            self.traverse()
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1
            self.traverse()

    def insert_at_start(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            self.traverse()
        else:
            temp = self.head
            new_node.next = temp
            temp.prev = new_node
            self.head = new_node
            self.length += 1
            self.traverse()

    def insert_at_any_location(self, index, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            self.insert_at_start(value)
        elif index == self.length - 1:
            self.insert_at_end(value)
        elif index < 0 or index > self.length:
            print("out of loop")
        else:
            temp = self.head
            after = temp.next
            for i in range(index - 1):
                temp = after
                after = after.next
            new_node.next = after
            new_node.prev = temp
            temp.next = new_node
            after.prev = new_node
            self.length += 1
            self.traverse()

    def delete_at_end(self):
        if self.head is None:
            print("No values found")
            self.traverse()
        else:
            temp = self.tail.prev
            self.tail.prev = None
            temp.next = None
            self.tail = temp
            self.length -= 1
            self.traverse()

    def delete_at_first(self):
        if self.head is None:
            print("No values found")
            self.traverse()
        else:
            temp = self.head.next
            temp.prev = None
            self.head.next = None
            self.head = temp
            self.length -= 1
            self.traverse()

    def get_element(self, index):
        if self.head is None:
            print("empty linked list")
        else:
            if index > self.length:
                print("out of loop")
            elif index == 0:
                print(self.head.value)
            elif index == self.length - 1:
                print(self.tail.value)
            else:
                temp = self.head
                for i in range(index):
                    temp = temp.next
                print(temp.value)

    def set_value(self, index, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            if index == 0:
                self.head.value = value
                self.traverse()
            elif index == self.length - 1:
                self.tail.value = value
                self.traverse()
            for i in range(index):
                temp = temp.next
            temp.value = value
            self.traverse()

    def delete_at_any_location(self, index):
        if self.head is None:
            print("empty linked list")
        else:
            if index == 0:
                self.delete_at_first()
            elif index == self.length - 1:
                self.delete_at_end()
            elif index > self.length or index < 0:
                print("out of loop")
            else:
                temp = self.head
                current = temp
                after = temp.next
                for i in range(index):
                    current = temp
                    temp = temp.next
                    after = temp.next
                temp.next = None
                temp.prev = None
                current.next = after
                after.prev = current
                self.length -= 1
                self.traverse()

    def traverse(self):
        result = []
        if self.length == 0:
            print("no elements")
        else:
            temp = self.head
            while temp.next is not None:
                result.append(temp.value)
                temp = temp.next
            result.append(temp.value)
            print("\n")
            print("Left to Right :")
            print(result)
            result = []
            temp = self.tail
            while temp.prev is not None:
                result.append(temp.value)
                temp = temp.prev
            result.append(temp.value)
            print("Right to left :")
            print(result)
            print("Length :", self.length)
            print("\n")


if __name__ == "__main__":
    test = DoublyLinkedList(1)
    test.insert_at_end(2)
    test.insert_at_end(3)
    test.insert_at_end(4)
    test.insert_at_end(5)
    test.insert_at_end(6)
    test.insert_at_start(7)
    test.delete_at_end()
    test.delete_at_end()
    test.delete_at_first()
    test.insert_at_start(7)
    test.insert_at_start(100)
    test.insert_at_start(1000)
    test.get_element(5)
    test.set_value(1, 5000)
    test.delete_at_any_location(2)
    test.insert_at_any_location(3, 9000)
