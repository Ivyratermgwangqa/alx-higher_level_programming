-- Lists all shows from the hbtn_0d_tvshows_rate database by their ratings.
SELECT title, SUM(rating) as rating_sum
FROM tv_shows
GROUP BY title
ORDER BY rating_sum DESC;
