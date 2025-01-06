-- Sample num-1 | Common SQL and using COALESCE() function --
SELECT order_id AS corrected_order_id,
       COALESCE(
        CASE WHEN order_id % 2 != 0 THEN lead(item) over(
               ORDER BY order_id)
             WHEN order_id % 2 = 0 THEN lag(item) over(
               ORDER BY order_id)
        END, item) AS item 
FROM orders 

-- Sample num-2 | Using CTE and windows function: LAG() and LEAD() --
WITH item_screening AS (
  SELECT *, 
         LAG(item) OVER(ORDER BY order_id) AS NEXT_ITEM,
         LEAD(item) OVER(ORDER BY order_id) AS PREV_ITEM
  FROM orders 
) 
SELECT order_id AS corrected_order_id, 
       CASE 
         WHEN order_id % 2 = 0 THEN next_item
         WHEN order_id % 2 != 0 
           AND id = (
              SELECT COUNT(*) 
              FROM orders) THEN  item 
         ELSE prev_item
       END AS item 
FROM item_screening;

-- Sample num-3 | Using CTE and MOD() function --
WITH change_order AS(
    SELECT * ,
       CASE WHEN MOD(order_id, 2) = 1 THEN order_id + 1
            WHEN MOD(order_id, 2) = 0 THEN order_id - 1
       END AS new_order
    FROM orders
    ORDER BY new_order ASC
)
SELECT CASE 
        WHEN new_order = (
          SELECT MAX(new_order) FROM change_order) THEN order_id
        ELSE new_order
       END AS corrected_order_id, item
FROM change_order;