/* DATA TABLE INPUT
| product_id | low_fats | recyclable |
| ---------- | -------- | ---------- |
| 0          | Y        | N          |
| 1          | Y        | Y          |
| 2          | N        | Y          |
| 3          | Y        | Y          |
| 4          | N        | N          |
*/

-- Write your PostgreSQL query statement below
SELECT product_id
FROM Products
WHERE low_fats = 'Y'
AND recyclable = 'Y';

/* DATA TABLE OUTPUT
Output:
| product_id |
| ---------- |
| 1          |
| 3          |
*/