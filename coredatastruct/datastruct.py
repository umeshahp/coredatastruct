class SinglyLinkedNode:
    def __init__(self, value):
        self.data = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.rear = None

    def create_newnode(self, data):
        node = SinglyLinkedNode(data)
        self.head = node
        self.rear = node
        return node

    def add_node_rear(self, value):
        newnode = SinglyLinkedNode(value)
        newnode.data = value
        self.rear.next = newnode
        self.rear = newnode

    def display(self):
        print("Current list status")
        current = self.head
        if self.head is None:
            raise Exception("Cannot remove item, list is empty")

        while current is not None:
            # if current.next is not None:
            print(current.data)
            current = current.next

    def remove_rear(self):
        current = self.head
        if self.head is None:
            raise Exception("Cannot remove item, list is empty")
        if self.head is self.rear:
            self.head = None
            self.rear = None
        prev = None
        if self.head is not self.rear:
            while current.next is not None:
                prev = current
                current = current.next
            if prev is None:
                return "List is empty"
            else:
                self.rear = prev
                self.rear.next = None
                return True

    def remove_front(self):
        if self.head is None:
            raise Exception("Cannot remove item, list is empty")
        if self.head is self.rear:
            self.head = None
            self.rear = None
            return
        else:
            self.head = self.head.next

    def len(self):
        current = self.head
        if self.head is None:
            return 0
        count = 0
        while current is not None:
            # if current.next is not None:
            count += 1
            current = current.next
        return count

    def insert(self, position, value):
        __doc__ = ''' To insert the element into particular position'''
        if position > self.len():
            raise Exception("List out of bound Error")
        if self.len() == position:
            node = self.create_newnode(self, value)
            return node
        newnode = SinglyLinkedNode(value)
        print("Current list status")
        count = 0
        current = self.head
        while current is not None:
            prev = self.head
            if position == count:
                newnode.next = current
                prev.next = newnode
            prev = current
            current = current.next
            count += 1

    def append_front(self, value):
        newnode = SinglyLinkedNode(value)
        newnode.data = value
        newnode.next = self.head
        self.head = newnode


if __name__ == "__main__":
    pass
