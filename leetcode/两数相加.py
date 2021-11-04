class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkList:
    def __init__(self):
        self.head = None

    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        r = self.head
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r

    def printlist(self, head):
        if head == None: return
        node = head

        while node != None:
            print(node.val, end=' ')
            node = node.next

class Solution:
    def addTwoNumbers(self, l1, l2):
        count = 0
        ret = ListNode()
        tmp = ret
        while l1 or l2 or count:
            num = 0
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            if count:
                num += count
                #count -= 1
            count, num = divmod(num, 10)
            tmp.next = ListNode(num)
            tmp = tmp.next
        return ret.next

a = Solution()
l=LinkList()
data1= [3, 6, 6]
data2= [2, 4, 6]
l1=l.initList(data1)
l2=l.initList(data2)
l.printlist(l1)
print("\r")
l.printlist(l2)
print("\r")
m=a.addTwoNumbers(l1,l2)
l.printlist(m)
