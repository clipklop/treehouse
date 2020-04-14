# *
# ** Linked list implementation
# *

class Node:
    """
    An object for storing a single node of a linked list.
    Models two attribute - data and the link to the next list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}>"


class LinkedList:
    """
    An object for storing a single linked list.
    With 'head' attribute in a constructor and ...TODO
    """
    def __init__(self):
        self.head = None
        # Maintaining a count attribute allows for len() to be implemented in
        # constant time
        self.__count = 0

    def __repr__(self):
        """
        Return a string representation of the list 
        Take O(n) time
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            
            current = current.next_node
        return '-> '.join(nodes)
    
    def is_empty(self):
        return self.head == None
    
    def __len__(self):
        """
        Returns the length of the linked list
        Takesn O(1) time
        """
        return self.__count

    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) time
        While 'self.head' != None increment 'count'
        otherwise we're reached the end of the list - tail        
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        
        return count

    def add(self, data):
        """
        Adds new Node containing data at head of the list
        
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        self.__count += 1
    
    def search(self, key):
        """
        Search for the first node containing data that matches the 'key'
        Return the node or 'None' if not found
        
        Takes O(n) time (linear time)
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    
    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position
        Insertion takes O(1) time, but finding the node at the
        insertion point taks O(n) time.

        Takes overall O(n) time
        """
        if index >= self.__count:
            raise IndexError('Index out of range')

        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1
            
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node
        
        self.__count += 1

    def node_at_index(self, index):
        """
        Returns the Node at specified index
        Takes O(n) time
        """
        if index >= self.__count:
            raise IndexError('index out of range')

        if index == 0:
            return self.head

        current = self.head
        position = 0

        while position < index:
            current = current.next_node
            position += 1

        return current

    def remove(self, key):
        """
        Removes Node containing data that matches the key
        Returns the node or None if 'key' doesn't exist

        Takes O(n) time
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            # if it's head
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
                self.__count -= 1
                return current
            # if it's not head
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
                self.__count -= 1
                return current                
            # current node doesn't contain the data that matches the key
            else:
                previous = current
                current = current.next_node

        return current

    def remove_at_index(self, index):
        """
        Removes Node at specified index
        Takes O(n) time
        """
        if index >= self.__count:
            raise IndexError('index out of range')

        current = self.head

        if index == 0:
            self.head = current.next_node
            self.__count -= 1
            return current

        position = index

        while position > 1:
            current = current.next_node
            position -= 1

        prev_node = current
        current = current.next_node
        next_node = current.next_node

        prev_node.next_node = next_node
        self.__count -= 1

        return current

    def __iter__(self):
        current = self.head

        while current:
            yield current
            current = current.next_node


l = LinkedList()
l.add(3)
l.add(12)
l.add(99)
l.add(42)
print(l)
