def insertNodeAtSpecificPosition(head, position, value):
    newBlock = Node(value)
    if position == 1:
        newBlock.next = head 
        return newBlock
 
    index = 1 
    curr = head 
    while index != position - 1:
        curr = curr.next 
        index += 1 
 
    newBlock.next = curr.next
    curr.next = newBlock
    return head
    # 10 --> 22 --> 45 --> 67 --> 32 --> 78 --> None
# 1      2       3     4      5      6 
 
# 67 -> 790 --> 32 --> 78 --> None
 
# (1, 790)
# (position = 5)
 
 
# 2500
# (1876, 23)
# (position, value)
# head to (position - 1)
# head, position, value
 
# 1. creating newBlock for given value
# 2. 
# 10 --> 22 --> 45 --> 67 --> 790 ---> 32 --> 78 --> None
# 1      2       3     4      5      6       
 
l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
head = None 
for ele in l:
    # head = insertAtEndOfTail(head, ele)
    head = insertNodeAtSpecificPosition(head, ele)
printLinkedList(head)
head = insertNodeAtSpecificPosition(head, 1, 1009)
printLinkedList(head)
