SELECT 
  advertiser_id, 
  ROUND((SUM(revenue) / SUM(spend)), 2) AS ROAS
FROM ad_campaigns
GROUP BY advertiser_id
ORDER BY advertiser_id;