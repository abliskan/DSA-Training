-- Sample num-1 | using 2 CTE and window function --
WITH artists_song as(
  SELECT s.song_id, 
         a.artist_name, 
         r.rank
  FROM songs AS s 
  JOIN artists AS a 
  ON s.artist_id = a.artist_id
  RIGHT join global_song_rank AS r 
  ON s.song_id = r.song_id
),
global_ranks as(  
  SELECT artist_name,
         dense_rank() over(order by count(*) desc) as the_rank
  FROM artists_song
  WHERE rank <= 10
  GROUP BY artist_name
)

SELECT artist_name,
       the_rank
FROM global_ranks
WHERE the_rank <= 5;