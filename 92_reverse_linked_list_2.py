class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if head.next == None or (left == right):
            return head
        count = 1
        p1Start = p2Start = p3Start = p1End = p2End = None
       
        temp = head
        
        while temp:
            if count == (left-1):
                p1End = temp
                p2Start = temp.next
                temp = temp.next
                p1End.next = None
            elif (count == right):
                p2End = temp
                p3Start = temp.next
                temp = temp.next
                p2End.next = None
                #break
            else:
                temp = temp.next
            count += 1
        #start = None
        
        if left == 1:
            p2Start = head
        start = end = None
        while p2Start:
            temp = p2Start
            p2Start = p2Start.next
            temp.next = None
            
            if end == None:
                start = end = temp
                
            else:
                temp.next = start
                start = temp

                # p1End.next = p2Start
                # p2End.next = p3Start
        if p1End:
           p1End.next = start
        
        else:
            head = start
        
        end.next = p3Start

        return head