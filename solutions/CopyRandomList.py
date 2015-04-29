from sets import Set
def copyRandomList(self, head):
    
    randomFromTo = {}
    labels = Set()
    
    result_head = RandomListNode(head.label)
    result = {head.label: result_head}
    i = head.next
    
    while i:
        result[i.label] = RandomListNode(i.label)
        i = i.next
    
    
    current = head
    while current is not None:
        if current.next:
            result[current.label].next = result[current.next.label]  
        labels.add(current.label)
        
        if current.random:
            crl = current.random.label
            randomFromTo[current.label] = result[crl] if result.has_key(crl) else RandomListNode(crl) 
        
        current = current.next if current.next else current.random 
    
    for k,v in result.items():
        v.random = randomFromTo[k] if randomFromTo.has_key(k) else None
    
    for k,v in result.items():
        if v.label == head.label:
            return v
    
def print_list(head):
    
    i = head
    while i:
        print("{0} {1} {2}".format(i.label, i.next.label if i.next else None, i.random.label  if i.random else None))
        i = i.next
    
    
class RandomListNode:
     
     def __init__(self, x, n = None, r = None):
         self.label = x
         self.next = n
         self.random = r    
    
root =  RandomListNode(1)
root.next = RandomListNode(2)
root.next.next = RandomListNode(3)
root.next.next.next = RandomListNode(4)
root.next.next.next.next = RandomListNode(5)
root.next.next.next.random = root.next.next
root.next.next.random = root.next
root.next.random = root


def test(expected, result):
    print("expected:")
    print_list(expected)
    print("result:")
    print_list(result)
    if compare(expected, result):
        print("ok")
    else:
        print("expected {0} result {1}".format(expected, result))

def compare(a, b):
    while a:
        if not b or a.label != b.label:
            return False
        if (a.next and not b.next) or (b.next and not a.next):
            return False
        if (a.random and not b.random) or (b.random and not a.random):
            return False
        elif a.random:
            if a.random.label != b.random.label:
                return False
        
        if a.next:
            a = a.next
            b = b.next  
        else:
            return True

test(root.next, copyRandomList(None, root.next))
test({}, copyRandomList(None, RandomListNode(5)))

