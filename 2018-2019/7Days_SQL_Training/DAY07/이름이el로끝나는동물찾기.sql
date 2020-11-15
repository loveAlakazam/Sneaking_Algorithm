-- https://programmers.co.kr/learn/courses/30/lessons/59047
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE='Dog' AND NAME LIKE '%EL%'
ORDER BY NAME;
