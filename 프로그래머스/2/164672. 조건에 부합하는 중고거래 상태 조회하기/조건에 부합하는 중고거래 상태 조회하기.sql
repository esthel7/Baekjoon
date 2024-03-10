-- 코드를 입력하세요
SELECT BOARD_ID,WRITER_ID,TITLE,PRICE,(
    CASE
    when STATUS='SALE'
    then '판매중'
    when STATUS='RESERVED'
    then '예약중'
    when STATUS='DONE'
    then '거래완료'
    end
) as STATUS from USED_GOODS_BOARD B
where DATE_FORMAT(CREATED_DATE,'%Y %M %D')='2022 October 5th'
order by BOARD_ID desc
