class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    def push_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop_front(self):
        if self.head:
            value = self.head.data
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self.size -= 1
            return value
    
    def pop_back(self):
        if self.tail:
            value = self.tail.data
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            self.size -= 1
            return value

    def get_size(self):
        return self.size
    
    def is_empty(self):
        return 1 if self.size == 0 else 0

    def get_front(self):
        return self.head.data if self.head else None

    def get_back(self):
        return self.tail.data if self.tail else None

def main():
    N = int(input())
    sll = LinkedList()

    for _ in range(N):
        command = input().split()

        if command[0] == "push_front":
            sll.push_front(int(command[1]))
        elif command[0] == "push_back":
            sll.push_back(int(command[1]))
        elif command[0] == "pop_front":
            print(sll.pop_front())
        elif command[0] == "pop_back":
            print(sll.pop_back())
        elif command[0] == "size":
            print(sll.get_size())
        elif command[0] == "empty":
            print(sll.is_empty())
        elif command[0] == "front":
            print(sll.get_front())
        elif command[0] == "back":
            print(sll.get_back())

if __name__ == "__main__":
    main()