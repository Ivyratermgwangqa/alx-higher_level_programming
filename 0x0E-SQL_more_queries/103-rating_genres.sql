-- Lists all genres in the hbtn_0d_tvshows_rate database by their ratings.
SELECT tv_genres.name AS genre, AVG(tvshows_rate.rating) AS avg_rating
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
JOIN tvshows_rate ON tv_shows.id = tvshows_rate.show_id
GROUP BY tv_genres.name
ORDER BY avg_rating DESC;
