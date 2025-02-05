/* DATA TABLE INPUT
#1 table: Signups 
| user_id | time_stamp          |
| ------- | ------------------- |
| 3       | 2020-03-21 10:16:13 |
| 7       | 2020-01-04 13:57:59 |
| 2       | 2020-07-29 23:09:44 |
| 6       | 2020-12-09 10:39:37 |
#2 table: Confirmations
| user_id | time_stamp          | action    |
| ------- | ------------------- | --------- |
| 3       | 2021-01-06 03:30:46 | timeout   |
| 3       | 2021-07-14 14:00:00 | timeout   |
| 7       | 2021-06-12 11:57:29 | confirmed |
| 7       | 2021-06-13 12:58:28 | confirmed |
| 7       | 2021-06-14 13:59:27 | confirmed |
| 2       | 2021-01-22 00:00:00 | confirmed |
*/

-- Write your PostgreSQL query statement below
SELECT 
    sgp.user_id,
    ROUND(AVG(
    CASE 
        WHEN cms.action = 'confirmed' 
        THEN 1.00 
        ELSE 0.00 
    END),2) AS confirmation_rate
FROM 
    Signups AS sgp
LEFT JOIN 
    Confirmations AS cms
ON 
    sgp.user_id = cms.user_id
GROUP BY 
    sgp.user_id;

/* DATA TABLE OUTPUT
Output:
| user_id | confirmation_rate |
| ------- | ----------------- |
| 3       | 0                 |
| 6       | 0                 |
| 2       | 0.5               |
| 7       | 1                 |
*/