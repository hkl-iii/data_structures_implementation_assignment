from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        contains_node = Node(data)

        if self.head is None:
            self.head = contains_node
            return

        add_to_beginning = self.head

        while add_to_beginning.next is not None:
            add_to_beginning = add_to_beginning.next

        add_to_beginning.next = contains_node
