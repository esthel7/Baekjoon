-- 코드를 입력하세요
# SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(CAR_ID) AS RECORDS FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE YEAR(START_DATE)=2022 AND 8<=MONTH(START_DATE)<=10 AND CAR_ID IN (
#     SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
#     WHERE YEAR(START_DATE)=2022 AND 8<=MONTH(START_DATE)<=10
#     GROUP BY CAR_ID
#     HAVING COUNT(CAR_ID)>=5
# )
# GROUP BY MONTH, CAR_ID
# HAVING RECORDS>0
# ORDER BY MONTH ASC, CAR_ID DESC

SELECT month(start_date) as month, car_id, count(history_id) as records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where start_date>="2022-08-01" and start_date<"2022-11-01" and car_id in (
    select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    where start_date>="2022-08-01" and start_date<"2022-11-01" 
    group by car_id 
    having count(history_id)>4
) 
group by month, car_id
having records >0
order by month, car_id desc

# CAR_ID
# SELECT CAR_ID, COUNT(CAR_ID) AS TOTAL FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# GROUP BY CAR_ID
# HAVING TOTAL>=5
# ORDER BY CAR_ID DESC

# 2 5 7 8 10 11 12 13 15 18 19 20 21 23 25 27 28