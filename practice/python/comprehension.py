students = ['몽키', '선샤인', '시와', '톰']

# 번호를 key로 갖고 이름을 value로 가지는 dictionary 만들기

for number, name in enumerate(students):
    print('{}번의 이름은 {}입니다'.format(number+1, name))

students_dic = {
    '{}번'.format(number+1) : name for number, name in enumerate(students)
}

print(students_dic)

# zip
# 2개 이상의 리스트나 스트링을 받아서 인덱스에 맞게 for in문에서 하나씩 던져줄 수있게 만들어준다.
students = ['몽키', '선샤인', '시와', '톰']
scores = [85, 92, 78, 100]

for x, y in zip(students, scores):
    print(x, y)


# for 문으로 zip을 활용해서 dictionary comprehension 만들기
score_dic = {
    students : score for students, score in zip(students, scores)
}

print(score_dic)
