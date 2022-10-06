SELECT ROUND((LAT_N),4)
FROM 
    ( 
      SELECT ROW_NUMBER() OVER (ORDER BY LAT_N) AS row_num, LAT_N
      FROM STATION) AS sub
      WHERE row_num = (
         SELECT
         CASE
         WHEN (((COUNT(LAT_N)) % 2) = 0) THEN (COUNT((LAT_N)+1)/2)
         ELSE ((COUNT(LAT_N)/2) + 0.5)
         END as MID_ROW
         FROM STATION
);