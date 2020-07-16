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

 def removeElements(self, head: ListNode, val: int) -> ListNode:
     """
     Removes all nodes with value == val
     """
    if(head==None):
        return head
    if(head.next==None and head.val==val):
        return None
    p1=head
    while(p1!=None and p1.val==val):
        p1=p1.next
    if(p1==None):
        return None
    head=p1
    p2=p1
    p1=p1.next
    while(p1!=None):
        if(p1.val==val):
            p2.next=p1.next
            p1=p1.next
        else:
            p2=p1
            p1=p1.next
    return head

def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    """
    Removes nth node from the end of the linked list in a single pass
    """
    t=1
    p1=head
    p2=head
    p3=None
    if(head.next==None):
        return None
    while(p1.next!=None):
        p1=p1.next
        t+=1
        if(t>n):
            p3=p2
            p2=p2.next
            print(p1.val,p2.val,p3.val)
    if(p3!=None):
        p3.next=p2.next
    else:
        p3=p2.next
        head=p3
    return head

def oddEvenList(self, head: ListNode) -> ListNode:
    heven=None
    hodd=None
    ceven=None
    codd=None
    p1=head
    if(head==None or head.next==None):
        return head
    n=3
    hodd=head
    codd=head
    p1=p1.next
    heven=p1
    ceven=p1
    p1=p1.next
    while(p1!=None):
        if(n%2==1):
            codd.next=p1
            codd=p1
        else:
            ceven.next=p1
            ceven=p1
        p1=p1.next
        n+=1
    codd.next=heven
    ceven.next=None
    head=hodd
    return head

def oddEvenListVal(self, head: ListNode) -> ListNode:
    heven=None
    hodd=None
    ceven=None
    codd=None
    p1=head
    if(head==None or head.next==None):
        return head
    while(p1!=None and p1.val%2==1):
        p1=p1.next
    if(p1==None):
        return head
    if(p1!=head):
        hodd=head
        codd=hodd
        heven=p1
        ceven=p1
    else:
        while(p1!=None and p1.val%2==0):
            p1=p1.next
        if(p1==None):
            return head
        heven=head
        ceven=heven
        hodd=p1
        codd=p1
    p1=p1.next
    while(p1!=None):
        if(p1.val%2==1):
            codd.next=p1
            codd=p1
        else:
            ceven.next=p1
            ceven=p1
        p1=p1.next
    codd.next=heven
    ceven.next=None
    head=hodd
    return head
