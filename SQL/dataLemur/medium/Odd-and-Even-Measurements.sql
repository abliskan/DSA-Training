-- Sample num-1 | using 2 CTE and window function --
WITH measurement_rank AS (
  SELECT 
    measurement_id,
    CAST(measurement_time AS date) AS measurement_day,
    measurement_value,
    RANK() OVER(PARTITION BY DATE(measurement_time) ORDER BY measurement_time) AS Row_Rank
  FROM measurements)
SELECT 
  measurement_day,
  SUM(CASE WHEN MOD(Row_Rank, 2) = 1 
           THEN measurement_value
           ELSE 0
      END) AS odd_sum,
  SUM(CASE WHEN MOD(Row_Rank, 2) = 0
           THEN measurement_value
           ELSE 0
      END) AS even_sum
FROM measurement_rank
GROUP BY measurement_day;