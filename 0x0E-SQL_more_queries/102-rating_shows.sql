-- Lists all shows from the hbtn_0d_tvshows_rate database by their ratings.
SELECT tv_shows.title, SUM(rating) AS rating_sum
FROM tv_shows
JOIN tvshows_rate ON tv_shows.id = tvshows_rate.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
