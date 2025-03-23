-- 코드를 입력하세요
SELECT
    i.REST_ID,
    i.REST_NAME,
    i.FOOD_TYPE,
    i.FAVORITES,
    i.ADDRESS,
    round(avg(r.REVIEW_SCORE), 2) as SCORE
from rest_info i 
inner join rest_review r on r.rest_id = i.rest_id
where i.address like '서울%'
group by 
    i.REST_ID,
    i.REST_NAME,
    i.FOOD_TYPE,
    i.FAVORITES,
    i.ADDRESS
order by
    SCORE desc,
    i.FAVORITES desc
;