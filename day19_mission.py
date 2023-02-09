def score_sort(ary):
    n = len(ary)
    for end in range(1, n):
        for i in range(end, 0, -1):
            if ary[i-1][1] > ary[i][1] :
                ary[i-1], ary[i] = ary[i], ary[i-1]
    return ary

ex_array = [['선미', 88], ['초아', 99], ['화사', 71], ['영탁', 78], ['영웅', 67], ['민호', 92]]

if __name__ == "__main__":
    print(f'정렬 전 --> {ex_array}')
    print(f'정렬 후 --> {score_sort(ex_array)}')


