-- dexter
SELECT g.name
FROM tv_genres g , tv_show_genres sg , tv_shows s
WHERE  s.id=sg.show_id
AND g.id = sg.genre_id
  AND s.title = 'Dexter'
ORDER BY g.name;
