def hasCycle(self, head: ListNode) -> bool:
    """
    Function to check if a given linked list has a cycle or not
    returns true/false
    Uses the 2 pointer method to detect cycles
    """
    flag = 0
    if(head == None or head.next == None):
        return 0
    f = head.next
    s = head
    while((f.next != None and f.next.next != None) and not flag):
        if(s == f):
            flag = 1
            break
        f = f.next.next
        s = s.next
    if(flag):
        return 1
    return 0


def getIntersect(self, head):
    tortoise = head
    hare = head
    while hare is not None and hare.next is not None:
        tortoise = tortoise.next
        hare = hare.next.next
        if tortoise == hare:
            return tortoise
    return None


def detectCycle(self, head):
    """
    Function to locate point of intersection in a linked list with a cycle
    Returns the node if any or NULL otherwise
    """
    if head is None:
        return None
    intersect = self.getIntersect(head)
    if intersect is None:
        return None
    ptr1 = head
    ptr2 = intersect
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr1


def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    """
    Finds the point of intersection of 2 linked lists if any
    """
    if(headA == None or headB == None):
        return None
    A_pointer = headA
    B_pointer = headB
    while A_pointer != B_pointer:
        A_pointer = headB if A_pointer == None else A_pointer.next
        B_pointer = headA if B_pointer == None else B_pointer.next
    return A_pointer
