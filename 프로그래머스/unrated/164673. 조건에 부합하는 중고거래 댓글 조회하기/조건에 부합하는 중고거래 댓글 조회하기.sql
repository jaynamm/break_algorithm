-- 코드를 입력하세요
SELECT b.title, b.board_id, r.reply_id, r.writer_id, r.contents, date_format(r.created_date, "%Y-%m-%d")
FROM USED_GOODS_REPLY r
LEFT JOIN USED_GOODS_BOARD b ON r.board_id = b.board_id
WHERE b.created_date like "2022-10%"
ORDER BY r.created_date asc, b.title asc