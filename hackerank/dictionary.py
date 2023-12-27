n=int(input())
student_marks = {}
for _ in range(n):
    name, *line = (input().split())
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = (input())
total=sum(student_marks[query_name])
print('%.2f'%total)
av=total/3.0

print('%.2f'%av)



