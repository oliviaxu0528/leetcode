class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

def mergeTwoLists(list1, list2):
    dummy= ListNode()
    head = dummy
    while list1 and list2:
        if list1.val>list2.val:
            head.next = list2
            list2 = list2.next
        else:
            head.next = list1
            list1 = list1.next

        if list1:
            head.next = list1
        if list2:
            head.next = list2
    return dummy.next
    

    