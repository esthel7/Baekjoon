-- 코드를 입력하세요
SELECT LEFT(PRODUCT_CODE,2) AS CATEGORY,COUNT(PRODUCT_ID) AS PRODUCTS FROM PRODUCT
GROUP BY LEFT(PRODUCT_CODE,2)
ORDER BY CATEGORY ASC