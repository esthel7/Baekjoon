-- 코드를 입력하세요
SELECT HISTORY_ID,CAR_ID,DATE_FORMAT(START_DATE,'%Y-%m-%d') AS START_DATE,DATE_FORMAT(END_DATE,'%Y-%m-%d') AS END_DATE,(
    CASE 
    WHEN DATE_FORMAT(END_DATE,'%Y')>2022 OR DATE_FORMAT(END_DATE,'%Y-%m')>'2022-10'
    THEN '장기 대여'
    WHEN  DATE_FORMAT(END_DATE,'%Y-%m-%d')='2022-09-01' AND DATE_FORMAT(END_DATE,'%Y-%m-%d')='2022-09-30'
    THEN '장기 대여'
    WHEN  DATE_FORMAT(END_DATE,'%Y-%m')='2022-10' AND DATE_FORMAT(END_DATE,'%d')+1>=DATE_FORMAT(START_DATE,'%d')
    THEN '장기 대여'
    ELSE '단기 대여'
    END
) AS RENT_TYPE FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE DATE_FORMAT(START_DATE,'%Y-%m')='2022-09'
ORDER BY HISTORY_ID DESC