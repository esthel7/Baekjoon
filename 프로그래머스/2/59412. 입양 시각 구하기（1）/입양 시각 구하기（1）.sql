-- 코드를 입력하세요
SELECT DATE_FORMAT(DATETIME,'%H') as HOUR, COUNT(ANIMAL_ID) as COUNT from ANIMAL_OUTS
group by HOUR
having HOUR>=9 and HOUR<=19
order by HOUR asc