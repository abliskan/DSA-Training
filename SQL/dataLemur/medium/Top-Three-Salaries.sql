-- Sample num-1 | using 2 CTE and window function --
WITH row_salary AS (
  SELECT emp.name , 
    emp.salary, 
    dpt.department_name,
    DENSE_RANK () OVER (
      PARTITION BY dpt.department_name 
      ORDER BY emp.salary DESC) AS row_salary
  FROM employee AS emp
  JOIN department AS dpt
  ON emp.department_id = dpt.department_id
)
SELECT department_name, 
    name, 
    salary
FROM row_salary
WHERE row_salary IN (1,2,3)
ORDER BY department_name, 
    salary DESC;