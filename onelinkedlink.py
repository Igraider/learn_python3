something = []
class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None
    
    def adding(self, obj):
        something.append(obj)
        
    def poop(self):
        something[len(something) - 1].pop()

    def rm(self, obj):
        something[obj].remove()

    def count(self):
        return len(something)
    
    def get(self, index):
        return something[index]

    def cl(self):
        something.clear()


def test_push():
    some_class = SingleLinkedList
    some_class.adding(sfslfjs)
    assert len(something) == 1
    print(something)
    
