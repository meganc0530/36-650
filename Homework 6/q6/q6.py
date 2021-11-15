class Node(object):
    def __init__(self, data):
        self.data = data
        self.previous = None


# Class to create a Reverse Linked List
class ReverseLinkedList(object):
    def __init__(self, tail=None):
        self.tail = tail

    # Print the reverse linked list
    def print_list(self):
        if self.tail == None:
            raise ValueError("List is empty")

        current = self.tail
        while current:
            print(current.data, end="  ")
            current = current.previous
        print("\n")

    # Find length of reverse Linked List
    def size(self):
        if self.tail == None:
            return 0

        size = 0
        current = self.tail
        while current:
            size += 1
            current = current.previous

        return size

    # Insert a node in a reverse linked list
    def insert(self, data):
        new_node = Node(data)
        old_tail = self.tail
        self.tail = new_node
        new_node.previous = old_tail
        # current.tail is a pointer to a node- it's also a node

    # Delete a node in a reverse linked list
    def delete(self, data):
        if not self.tail:
            return

        temp = self.tail

        # Check if tail node is to be deleted
        if self.tail.data == data:
            self.tail= temp.previous
            print("Deleted node is " + str(self.tail.data))
            return

        while temp.previous:
            if temp.previous.data == data:
                print("Node deleted is " + str(temp.previous.data))
                temp.previous = temp.previous.previous
                return
            temp = temp.previous
        print("Node not found")
        return

    # search reverse linked list
    def search(self, data):
       current = self.tail
       while current != None:
           if current.data == data:
               return True

           current = current.previous
       return False





first_node = Node (11)
reverse_linked_list = ReverseLinkedList(first_node)
reverse_linked_list.insert(3)
reverse_linked_list.insert(6)
reverse_linked_list.insert(5)

print("The Reverse Linked List is (after insertion):")
reverse_linked_list.print_list()

reverse_linked_list.delete(6)

print("The Reverse Linked List is (after deleting 6):")
reverse_linked_list.print_list()

print("Does 5 exist in the Reverse Linked List?")
print(reverse_linked_list.search(5))

print("Does 17 exist in the Reverse Linked List?")
print(reverse_linked_list.search(17))