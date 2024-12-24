-- Sample num-1 | common SQL --
SELECT
    p.page_id
FROM
    pages AS p
    LEFT JOIN page_likes AS pl
    ON p.page_id = pl.page_id
WHERE
    pl.page_id IS NULL;