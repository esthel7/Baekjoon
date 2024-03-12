-- 코드를 작성해주세요
SELECT SUM(SCORE) AS SCORE,E.EMP_NO,EMP_NAME,POSITION,EMAIL FROM HR_DEPARTMENT D
INNER JOIN HR_EMPLOYEES E ON D.DEPT_ID = E.DEPT_ID
INNER JOIN HR_GRADE G ON E.EMP_NO = G.EMP_NO
WHERE YEAR=2022
GROUP BY E.EMP_NO
ORDER BY SCORE DESC
LIMIT 1