-- 코드를 입력하세요
SELECT ANIMAL_TYPE, COUNT(ANIMAL_ID) as count from ANIMAL_INS
group by ANIMAL_TYPE
having ANIMAL_TYPE='Cat' or ANIMAL_TYPE='Dog'
order by ANIMAL_TYPE asc