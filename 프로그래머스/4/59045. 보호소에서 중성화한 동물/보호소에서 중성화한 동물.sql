-- 코드를 입력하세요
SELECT I.ANIMAL_ID,I.ANIMAL_TYPE,I.NAME FROM ANIMAL_INS I
INNER JOIN ANIMAL_OUTS O ON I.ANIMAL_ID=O.ANIMAL_ID
WHERE SEX_UPON_INTAKE != SEX_UPON_OUTCOME