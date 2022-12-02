# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode(None, head)
            prev, cur = dummy, head

            iter = 1
            
            print('======= Object init =======')
            print('dummy: ', dummy)
            print('prev: ', prev)
            print('cur: ', cur)
            
            while cur and cur.next:
                print('======= Iter #' + str(iter) + ' =======')
                print('dummy: ', dummy)
                
                prev.next = cur.next
                print('\nprev: ', prev)
                print('dummy: ', dummy)

                cur.next = cur.next.next
                print('\ncur: ', cur)
                print('prev: ', prev)
                print('dummy: ', dummy)
                
                prev.next.next = cur
                print('\nprev: ', prev)
                print('dummy: ', dummy)

                prev, cur = cur, cur.next
                print('\nprev: ', prev)
                print('cur: ', cur)
                print('dummy: ', dummy)

                iter += 1
            
            print('======= End of loop =======')
            print('dummy:', dummy)
            return dummy.next

        
