import random
import math


## 클래스와 함수 선언 부분 ##
class Node():
    def __init__(self):
        self.data = None
        self.link = None


def print_store(start):
    current = start
    if current.link == head:
        return

    while current.link != start:
        current = current.link
        x = current.data[1]
        y = current.data[2]
        print(current.data[0], '편의점 거리: ', math.sqrt(x * x + y * y))
    print()


def sort_store(store_name):
    global memory, head, current, pre

    node = Node()
    node.data = store_name
    memory.append(node)

    if head == None:
        head = node
        node.link = head
        return

    node_reach = math.sqrt(node.data[1] * node.data[1] + node.data[2] * node.data[2])
    head_reach = math.sqrt(head.data[1] * head.data[1] + head.data[2] * head.data[2])

    if head_reach > node_reach:
        node.link = head
        last = head
        while last.link != head:
            last = last.link

        last.link = node
        head = node
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        curx = current.data[1]
        cury = current.data[2]
        cur_reach = math.sqrt(curx * curx + cury * cury)
        if cur_reach > node_reach:
            pre.link = node
            node.link = current
            return

    current.link = node
    node.link = head


## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
name = []
## 메인 코드 부분 ##
if __name__ == "__main__":

    store_array = []
    store_start = 'A'
    for _ in range(10):
        store = (store_start, random.randint(1, 100), random.randint(1, 100))
        store_array.append(store)
        store_start = chr(ord(store_start) + 1)

    for store in store_array:
        sort_store(store)
    print_store(head)
