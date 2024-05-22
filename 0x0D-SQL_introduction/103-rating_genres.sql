SELECT tv_genres.name, SUM(rating) AS rating_sum
FROM tv_genres
JOIN tv_show ON tv_genres.id = tv_shows.genre_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
