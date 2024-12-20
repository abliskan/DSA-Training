-- Sample num-1 | using 2 CTE and window function --
WITH TR_RK AS (
  SELECT transaction_date,
         user_id,
         COUNT(transaction_date) as purchase_count,
         dense_rank() over(PARTITION BY user_id ORDER BY transaction_date desc) AS transaction_rank
  FROM user_transactions
  GROUP BY transaction_date,
           user_id
)
SELECT transaction_date,
       user_id,
       purchase_count
FROM TR_RK
WHERE transaction_rank = 1
ORDER BY transaction_date;