# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
  def mergeTwoLists(list1, list2):
      if (not list1 and list2): return list2
      if (list1 and not list2): return list1
      if (not list1 and not list2): return None

      if (list1.val < list2.val):
          head = list1
          list1 = list1.next
      else:
          head = list2
          list2 = list2.next
          
      merge = head
      while (list1 or list2):
          if (list1 and list2):
              if (list1.val < list2.val):
                  head.next = list1
                  list1 = list1.next
              else:
                  head.next = list2
                  list2 = list2.next
          elif (list1 and not list2):
              head.next = list1
              list1 = list1.next
          elif (not list1 and list2):
              head.next = list2
              list2 = list2.next
          head = head.next
          
      return merge
