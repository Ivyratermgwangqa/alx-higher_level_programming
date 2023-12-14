-- Lists all shows in the database hbtn_0d_tvshows along with their respective genre IDs.
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_shows AS tv_shows
	 LEFT JOIN tv_show_genres AS tv_show_genres
	    ON tv_shows.id = tv_show_genres.show_id
	    WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
