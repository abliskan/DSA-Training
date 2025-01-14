-- Using common sql --
SELECT 
ROUND(SUM (CAST
              (item_count as Decimal)*order_occurrences) / sum (order_occurrences), 1) AS mean
FROM items_per_order; 