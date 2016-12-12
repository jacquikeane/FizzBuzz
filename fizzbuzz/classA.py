class Error (Exception): pass

class ClassA:
    def __init__(self, foo):
        self.foo = foo


    def __len__(self):
        return len(self.foo)


    def bar(self):
        return 'bar'
