SELECT DISTINCT COUNT(DISTINCT qr.query_id) AS unique_queries,
       COUNT(emp.employee_id) OVER(PARTITION BY COUNT(DISTINCT qr.query_id)) AS employee_count
FROM employees AS emp
LEFT JOIN queries qr
ON emp.employee_id = qr.employee_id
AND EXTRACT(MONTH FROM qr.query_starttime) IN (7, 8, 9)
OR emp.employee_id IS NULL
GROUP BY emp.employee_id;