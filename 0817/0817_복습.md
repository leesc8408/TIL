# 🚩2022.08.17 DB 복습/실습

1. 테이블 셋팅

```sql
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);
```

2. 데이터 추가

```sql
.mode csv
.import users.csv users
```

3. 쿼리 복습

```sql
-- 30세 이상인 사람들
sqlite> select * from users where age>=30;
-- 30세 이상인 사람들의 이름
sqlite> select first_name,last_name from users where age>=30;
-- 30세 이상인 사람들의 이름 3명만
sqlite> select first_name,last_name from users where age>=30 limit 3;
-- 30세 이상이고 성이 김인 사람
sqlite> select * from users where age>=30 and last_name='김';
-- 30세 이상인 사람들의 숫자
sqlite> select count(*) from users where age>=30;
-- 전체 중에 가장 작은 나이
sqlite> select min(age) from users;
-- 이씨 중에 가장 작은 나이
sqlite> select min(age) from users where last_name='이';
-- 이씨 중에 가장 작은 나이를 가진 사람의 이름과 계좌잔고
sqlite> select min(age),first_name,balance from users where last_name='이';
-- 30세 이상인 사람들의 평균 나이
sqlite> select avg(age) from users where age>=30;
-- 계좌 잔액이 가장 높은 사람
sqlite> select max(balance) from users;
-- 지역번호가 02인 사람
sqlite> select * from users where phone like '02-%';
-- 준으로 끝나는 사람
sqlite> select * from users where first_name like '%준';
-- 중간번호가 5114
sqlite> select * from users where phone like '%5114%';
-- 나이 오름차순 
sqlite> select * from users order by age asc;
-- 나이, 성 순으로 오름차순
sqlite> select * from users order by age,last_name asc limit 5;
-- 계좌 잔액 순 내림차순 
sqlite> select * from users order by balance desc limit 5;
-- 계좌 잔액 내림차순(높은->낮은 것), 성 오름차순(ㄱ->ㅎ)
sqlite> select * from users order by balance desc, last_name asc limit 5;
```

