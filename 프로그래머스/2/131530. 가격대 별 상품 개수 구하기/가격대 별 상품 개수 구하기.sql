-- 코드를 입력하세요
SELECT ROUND((PRICE-5000)/10000)*10000 AS PRICE_GROUP, COUNT(PRODUCT_ID) AS PRODUCTS FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP
