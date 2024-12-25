-- Sample num-1 | CTE --
WITH activation AS(
  SELECT DISTINCT eml.email_id
  FROM texts AS txt
  JOIN emails eml
  ON txt.email_id = eml.email_id
  WHERE txt.signup_action = 'Confirmed'
)
SELECT ROUND(COUNT(email_id) / (
    SELECT COUNT(DISTINCT email_id) 
    FROM emails
    )::DECIMAL, 2) AS confirm_rate
FROM activation;