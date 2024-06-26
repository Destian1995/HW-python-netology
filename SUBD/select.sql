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

