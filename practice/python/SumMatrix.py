A = [[1,2], [2,3]]
B = [[3,4], [5,6]]

# answer = [[] for j in range(len(A)) ]
#
# # for i, v in enumerate(A):
# #     answer[i] = list()
# #     for x, l in enumerate(A[i]):
# #         answer[i][x] = A[i][x] + B[i][x]
#
#
# for i in range(len(A)):
#     for x in range(len(A[i])):
#         answer[i].append(A[i][x] + B[i][x])
#


C = [[c + d for c, d in zip(a, b)]for a, b in zip(A,B)]

print(C)
