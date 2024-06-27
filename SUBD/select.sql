-- Задание 2

-- Название и продолжительность самого длительного трека.
SELECT track, duration 
FROM tracks 
WHERE duration = (SELECT MAX(duration) FROM tracks);

-- Название треков, продолжительность которых не менее 3,5 минут.
SELECT track
FROM tracks
WHERE duration >= '210';

-- Названия сборников, вышедших в период с 2018 по 2020 год включительно.
SELECT names
FROM collection
WHERE releaseyear BETWEEN 2018 AND 2020;

-- Исполнители, чьё имя состоит из одного слова.
SELECT performer
FROM performers
WHERE performer NOT LIKE '% %';

-- Название треков, которые содержат слово «мой» или «my».
SELECT track
FROM tracks
WHERE track LIKE '%my%' OR track LIKE '%My%';

-- Задание 3

-- Количество исполнителей в каждом жанре.
SELECT g.genre, COUNT(a.id) AS количество_исполнителей
FROM musicgenres g
JOIN genre_performers ag ON g.id = ag.genre_id
JOIN performers a ON ag.genre_id = a.id
GROUP BY g.genre;

-- Количество треков, вошедших в альбомы 2019–2020 годов.
SELECT COUNT(t.id) AS count_tracks
FROM tracks t
JOIN albums a ON t.id = a.id
WHERE a.releaseyear BETWEEN 2019 AND 2020;

-- Средняя продолжительность треков по каждому альбому.
SELECT a.album, AVG(t.duration)
FROM albums a
JOIN tracks t ON a.id = t.id
GROUP BY a.album;


-- Все исполнители, которые не выпустили альбомы в 2020 году.
SELECT DISTINCT performer 
FROM performers 
WHERE id NOT IN (
    SELECT DISTINCT pa.performer_id 
    FROM performer_albums pa 
    JOIN albums a ON pa.album_id = a.id 
    WHERE a.releaseyear = 2020
);

-- Названия сборников, в которых присутствует конкретный исполнитель.
SELECT DISTINCT c.names
FROM collection c 
LEFT JOIN track_collections tc ON c.id = tc.collection_id
LEFT JOIN track_albums ta ON tc.track_id = ta.track_id 
LEFT JOIN performer_albums pa ON ta.albums_id = pa.album_id 
LEFT JOIN performers p ON pa.performer_id = p.id 
WHERE p.performer = 'Уэйн Статик';
