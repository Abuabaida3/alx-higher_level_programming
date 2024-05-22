1 -- list all show from hbtn_0d_tvshows_rate by their rating.
2 -- Records are ordered by descending rating.
3 SELECT'title', SUM('rate') AS 'rating'
4 from 'tv_shows' AS t
5 INNER JOIN 'tv_show_ratings' AS r
6 ON t.'id' = r.'show_id'
7 GROUP BY 'title'
8 ORDER BY 'rating' DESC;
