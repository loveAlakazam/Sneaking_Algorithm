-- https://programmers.co.kr/learn/courses/30/lessons/59041
-- 코드를 입력하세요
SELECT NAME, COUNT(NAME)
FROM ANIMAL_INS
GROUP BY NAME
HAVING NAME IS NOT NULL AND COUNT(NAME)>=2
