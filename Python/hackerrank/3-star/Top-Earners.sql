SELECT CONCAT(MAX(months * salary),' ', COUNT(name)) 
FROM Employee 
GROUP BY months * salary 
ORDER BY months * salary DESC 
LIMIT 1;