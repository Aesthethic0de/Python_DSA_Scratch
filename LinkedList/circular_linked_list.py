class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.length = 0
        self.head = new_node
        self.tail = new_node
        self.tail.next = self.head
        self.length += 1
        self.traverse()

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
            self.length += 1
            self.traverse()
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            self.traverse()

    def traverse(self):
        result = []
        if self.head is None:
            print("empty linked list")
        else:
            temp = self.head
            for i in range(self.length):
                result.append(temp.value)
                temp = temp.next
            result.append(self.tail.next.value)
            print("\n")
            print("left to right")
            print(result)
            print("\n")


if __name__ == "__main__":
    test = CircularLinkedList(1)
    test.insert_at_end(2)
    test.insert_at_end(3)
