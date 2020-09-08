# from itertools import combinations
# list = []
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#
#     lst = [[a, b, c] for b in range(y + 1) for c in range(z + 1) for a in range(x + 1)]
#
#     finallst = []
#     for items in combinations(lst, 3):
#         for nums in items:
#             x = sum(nums)
#             if x != n and nums not in finallst:
#                 finallst.append(nums)
#
#     f_finallst= sorted(finallst, key=str)
#     print(f_finallst)
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())

# lists = [[i, j, k] for i in range(x + 1)
#          for j in range(y + 1)
#          for k in range(z + 1) if (i + j + k) != n]
# print(lists)

# listijk = []
# for i in range(x + 1):
#     for j in range (y + 1):
#         for k in range (z + 1):
#             if i + j + k != n: #before printing the result, it will exclude the output which 'i' + 'j' + 'k' is the same as 'n'.
#                 listijk.append([i,j,k])
# print(listijk)

# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     arr = list(set(list(arr)))
#     print(arr)
#     # ar = len(arr)
#     # arr = sorted(arr)
#     # print(arr[ar-2])

# if __name__ == '__main__':
#     total = []
#     for i in range(int(input())):
#         name = input()
#         score = float(input())
#         name_score = list((score, name))
#         total.append(name_score)
#     total.sort()
#     min_mark = total[0][0]
#     count = 0
#     for i in range(len(total)):
#         if min_mark == total[i][0]:
#             count = count+1
#     if count >= 1:
#         for j in range(count):
#             total.pop(0)
#     nd_min_mark = total[0][0]
#     for i in range(len(total)):
#         if nd_min_mark == total[i][0]:
#             print(total[i][1])

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     x = student_marks[query_name]
#     ans = 0
#     for i in range(3):
#         ans = x[i] + ans
#         i = i+1
#     print("{:.2f}".format(ans/3))

