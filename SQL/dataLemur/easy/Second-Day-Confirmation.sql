-- Sample num-1 | common SQL --
SELECT e.user_id 
FROM emails AS eml
JOIN texts AS txt
ON txt.email_id = eml.email_id
GROUP BY t.email_id, 
         eml.user_id
HAVING COUNT(txt.email_id) = 2
ORDER BY eml.user_id;