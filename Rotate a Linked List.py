class Solution:
    
    #Function to rotate a linked list k times to the left
    def rotate(self, head, k):
        if not head or not head.next or k == 0:
            return head  # Agar list empty hai ya single node hai ya k = 0, toh rotation ka koi fayda nahi

        # Step 1: Length n find karo
        temp = head
        length = 1
        while temp.next:
            temp = temp.next
            length += 1

        # Step 2: k ko length ke mod se reduce karo (kyunki k > length ho sakta hai)
        k = k % length
        if k == 0:
            return head  # Agar k list ki length ka multiple hai toh list wahi ki wahi rahegi

        # Step 3: k-th node tak jao
        curr = head
        for _ in range(k - 1):
            curr = curr.next

        # Step 4: Rotate karo
        new_head = curr.next  # naye head pe point karo
        curr.next = None      # old list ko yahin se tod do

        temp.next = head      # purane last node ko original head se jod do

        return new_head
