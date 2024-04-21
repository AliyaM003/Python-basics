# Queue implementation 
 
 
10, 20, 30, 40, 50 
 
# Enqueue --> insertion at tail 
# Dequeue --> deletion at head 
 
 
# Linked-list based implementation 
 
 
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
 
def enQueue(head, val):
    # This function inserts node at tail
    newBlock = Node(val)
    if head == None:
        return newBlock 
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = newBlock
    return head
 
def deQueue(head):
    # This function deletes first node
    if head == None:
        print("Queue is empty, nothing to delete")
        return None
 
    print("Deleting", head.data)
    secondNode = head.next 
    head.next = None 
    return secondNode
 
def printQueue(head):
    if head == None:
        print("Queue is empty")
        return 
    curr = head 
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next 
    print()
 
head = None 
head = enQueue(head, 10)
head = enQueue(head, 20)
head = enQueue(head, 100)
 
printQueue(head)
# 10 --> 20 --> 100
 
head = deQueue(head)
# Deleting 10 
 
printQueue(head)
# 20 --> 100 
 
head = deQueue(head)
# Deleting 20 
 
printQueue(head)
# 100 
 
head = deQueue(head)
# Deleting 100 
 
printQueue(head)
#  Queue is empty
 
head = deQueue(head)
# Queue is empty, nothing to delete





# Nothing is present in Q
# 10  is inserted into Q
# 20  is inserted into Q
# 30  is inserted into Q
# 40  is inserted into Q
# 50  is inserted into Q
# 60  is inserted into Q
# [10, 20, 30, 40, 50, 60]
# Deleted element is 10
# [20, 30, 40, 50, 60]
# Deleted element is 20
# [30, 40, 50, 60]
# Deleted element is 30
# [40, 50, 60]
# Deleted element is 40
# [50, 60]
# Deleted element is 50
# [60]
# Deleted element is 60
# Nothing is present in Q
 
def enQueue(Q, ele):
    Q.append(ele)
    print(ele, " is inserted into Q")
 
def deQueue(Q):
    if len(Q) == 0:
        print("Queue is empty")
        return 
    ele = Q.pop(0)
    print("Deleted element is", ele)
 
def printQueue(Q):
    if len(Q) == 0:
        print("Nothing is present in Q")
        return 
    print(Q)
 
 
Q = []
printQueue(Q)
# []
enQueue(Q, 10)
enQueue(Q, 20)
enQueue(Q, 30)
enQueue(Q, 40)
enQueue(Q, 50)
enQueue(Q, 60)
 
printQueue(Q)
# [10, 20, 30, 40, 50, 60]
 
deQueue(Q)
printQueue(Q)
# [20, 30, 40, 50, 60]
 
deQueue(Q)
printQueue(Q)
# [30, 40, 50, 60]
 
deQueue(Q)
printQueue(Q)
# [40, 50, 60]
 
 
deQueue(Q)
printQueue(Q)
# [50, 60]
 
 
deQueue(Q)
printQueue(Q)
 
# [60]
 
deQueue(Q)
printQueue(Q)
 
deQueue(Q)
printQueue(Q)
 
deQueue(Q)
printQueue(Q)
