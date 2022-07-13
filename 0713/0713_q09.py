# 득표수 세기
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

cnt = 0
for a in students:
    if a == '이영희':
        cnt += 1
print(cnt)

# upgarade

print(students.count('이영희'))
# 출력(리스트에서.카운팅('이것을'))