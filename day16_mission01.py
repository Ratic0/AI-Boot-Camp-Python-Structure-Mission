# 문제 2
class Node() :
    def __init__ (self) :
        self.data = None
        self.nlink = None
        self.plink = None

def printNodes(start):
    current = start
    if current.nlink == None : #None 값이 있다면 선형 리스트에서는 정지를 해야되니까
        return
    print("정방향 ")
    print(current.data, end=' ')
    while current.nlink != None:
        current = current.nlink
        print(current.data, end=' ')
    print()

    print("역방향 ")
    print(current.data, end=' ')

    while current.plink != None:
        current = current.plink
        print(current.data, end=' ')
    print()



## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드 부분 ##
if __name__ == "__main__" :

    node = Node()		# 첫 번째 노드
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:] :	# 두 번째 이후 노드
        pre = node
        node = Node()
        node.data = data
        pre.nlink = node
        node.plink = pre
        memory.append(node)

    printNodes(head)