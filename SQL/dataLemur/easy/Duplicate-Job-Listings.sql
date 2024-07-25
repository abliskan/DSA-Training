-- Sample num-1 | common SQL --
SELECT 
    COUNT(DISTINCT t1.company_id) AS duplicate_companies
FROM  
    job_listings AS t1
JOIN 
    job_listings AS t2 
ON 
    t1.company_id = t2.company_id
WHERE t1.title = t2.title 
AND t1.description = t2.description 
AND t1.job_id !=t2.job_id;