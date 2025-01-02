-- Sample num-1 | Using combination of CTE and subquery
WITH company_manager AS (
     SELECT * 
     FROM employee 
     WHERE manager_id IS NULL
)
SELECT employee_id,
       name AS employee_name
FROM employee AS emp
WHERE emp.salary > (
     SELECT salary
     FROM company_manager AS cp_mgr
     WHERE cp_mgr.employee_id = emp.manager_id
);