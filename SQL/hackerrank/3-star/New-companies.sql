SELECT c.company_code, c.founder,
       COUNT(DISTINCT lead_manager_code),
       COUNT(DISTINCT senior_manager_code),
       COUNT(DISTINCT manager_code),
       COUNT(DISTINCT employee_code)
FROM employee e, company c 
WHERE e.company_code = c.company_code
GROUP BY c.company_code, c.founder 
ORDER BY c.company_code;