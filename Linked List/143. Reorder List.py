# https://leetcode.com/problems/reorder-list/
def reorderList(head):
    #find the middle
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    #reverse the second part
    second = slow.next
    prev = None

    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp

    #merge two list
    first, second = head, prev
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2
    
    