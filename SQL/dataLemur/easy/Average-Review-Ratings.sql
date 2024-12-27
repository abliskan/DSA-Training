SELECT DATE_PART('MONTH', submit_date) AS month, 
       product_id, 
       ROUND(AVG(stars). 2)
FROM reviews
GROUP BY month, 
         product_id
ORDER BY month, 
         product_id;