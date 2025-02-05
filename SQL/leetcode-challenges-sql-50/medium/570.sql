/* DATA TABLE INPUT
#1 table: Employee 
| id  | name  | department | managerId |
| --- | ----- | ---------- | --------- |
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
*/

-- Write your PostgreSQL query statement below
WITH direct_reports AS (
  select managerId,
       count(*) as cnt 
  from employee
  group by managerId
  having count(*) >= 5
)
SELECT name
FROM employee as emp
JOIN direct_reports as rp
ON emp.id = rp.managerId;

/* DATA TABLE OUTPUT
Output:
| name |
| ---- |
| John |
*/