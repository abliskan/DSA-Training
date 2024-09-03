-- Sample num-1 | subquery SQL --
SELECT MAX(salary) AS second_highest_salary
FROM employee 
WHERE salary < (
  SELECT max(salary) 
  FROM employee
);