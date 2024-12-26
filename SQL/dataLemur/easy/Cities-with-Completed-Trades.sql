-- Sample num-1 | common SQL --
SELECT usr.city, 
       COUNT(trd.order_id) AS completed_order
FROM trades AS trd
LEFT JOIN users AS usr
ON trd.user_id = usr.user_id
WHERE trd.status = 'Completed'
GROUP BY usr.city
ORDER BY completed_order DESC
LIMIT 3;