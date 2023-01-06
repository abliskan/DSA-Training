SELECT IF(X < Y, X, Y) AS f1,
       IF(X > Y, X, Y) AS f2
FROM Functions
GROUP BY f1, f2
HAVING COUNT(*) > 1 
ORDER BY f1;