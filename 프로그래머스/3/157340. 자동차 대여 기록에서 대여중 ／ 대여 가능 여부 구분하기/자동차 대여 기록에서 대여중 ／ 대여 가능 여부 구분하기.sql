-- 코드를 입력하세요
SELECT CAR_ID, MAX(
    CASE
        WHEN DATE_FORMAT(START_DATE,'%Y-%m-%d')<='2022-10-16' AND DATE_FORMAT(END_DATE,'%Y-%m-%d')>='2022-10-16'
        THEN '대여중'
        ELSE '대여 가능'
    END
) as 'AVAILABILITY'
from CAR_RENTAL_COMPANY_RENTAL_HISTORY C
group by CAR_ID
order by CAR_ID desc