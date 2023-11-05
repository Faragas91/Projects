# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialisiere den Dummy-Knoten, der als Startpunkt für die Ergebnisliste dient
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            # Hole die Werte von l1 und l2, wenn sie vorhanden sind, sonst 0
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Berechne die Summe und den Übertrag
            total = x + y + carry
            carry = total // 10

            # Füge einen neuen Knoten zur Ergebnisliste hinzu
            current.next = ListNode(total % 10)
            current = current.next

            # Bewege dich zu den nächsten Knoten, wenn vorhanden
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Der Dummy-Knoten war nur ein Platzhalter, die Ergebnisliste beginnt mit dem nächsten Knoten
        return dummy_head.next

# Definition der beiden verknüpften Listen
list1 = ListNode(2)
list1.next = ListNode(4)
list1.next.next = ListNode(3)

list2 = ListNode(5)
list2.next = ListNode(6)
list2.next.next = ListNode(4)

# Erzeuge eine Instanz der Solution-Klasse und rufe die Funktion auf
solution = Solution()
result = solution.addTwoNumbers(list1, list2)

# Gib das Ergebnis aus, indem du die verknüpfte Liste durchläufst
while result:
    print(result.val, end=" -> ")
    result = result.next
  

# list1 = [2,4,3]
# list2 = [5,6,4]
# bla = 0
# neue_liste = []

# for i, j in zip(list1, list2):
#     sum = i+j+bla
#     if sum >= 10:
#        bla = 0
#        neue_liste.append(0)
#        bla += 1
#     else:
#        neue_liste.append(sum)
# neue_liste.reverse()
 
# print(neue_liste)
