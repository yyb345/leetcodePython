from problem.ListNode import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result


def main():
    solution = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)

    l2 = ListNode(7)
    l2.next = ListNode(6)


    l3 = solution.addTwoNumbers(l1,l2)

    while l3 is not None:
        print(l3.val)
        l3 = l3.next

if __name__ == '__main__':
    main()