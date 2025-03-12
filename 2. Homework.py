class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy  

    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            current.next = l1  
            l1 = l1.next  
        else:
            current.next = l2  
            l2 = l2.next  
        current = current.next  

    if l1 is not None:
        current.next = l1
    else:
        current.next = l2

    return dummy.next
