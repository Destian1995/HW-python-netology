-- Задание 2

SELECT track, duration
FROM tracks
ORDER BY duration DESC
LIMIT 1;

SELECT track
FROM tracks
WHERE duration >= '210';

SELECT names
FROM collection
WHERE releaseyear BETWEEN 2018 AND 2020;

SELECT performer
FROM performers
WHERE performer NOT LIKE '% %';

SELECT track
FROM tracks
WHERE track LIKE '%my%' OR track LIKE '%My%';

-- Задание 3

SELECT g.genre, COUNT(a.id) AS count_artists
FROM musicgenres g
JOIN genre_performers ag ON g.id = ag.genre_id
JOIN performers a ON ag.genre_id = a.id
GROUP BY g.genre;

SELECT COUNT(t.id) AS count_tracks
FROM tracks t
JOIN albums a ON t.id = a.id
WHERE a.releaseyear BETWEEN 2019 AND 2020;

