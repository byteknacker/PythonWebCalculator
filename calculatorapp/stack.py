class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def parse(self, stack_string):

        temp = stack_string.split()
        if not temp:  # if stack is empty, then nothing to be done
            return False
        else:
            del self.items[:]
            try:  
                self.items += [int(i) for i in temp]
            except ValueError:  
                self.items += temp

            return True

    def __str__(self):
        return ' '.join(str(s) for s in self.items)
