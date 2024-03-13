-- lists all shows that have at least one genre linked
SELECT title, genre_id FROM tv_shows
  JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id
 WHERE tv_shows.id IN (SELECT show_id FROM tv_show_genres)
 ORDER BY tv_shows_title, tv_show_genres.genre_id;
