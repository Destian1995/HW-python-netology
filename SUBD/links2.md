# Домашнее задание «Продвинутая выборка данных»

## Задание 1
[ссылка на скрипт создания БД](https://github.com/Destian1995/HW-python-netology/blob/main/SUBD/create_DB.sql)

[ссылка на SELECT запросы](https://github.com/Destian1995/HW-python-netology/blob/main/SUBD/select.sql)
## Задание 2
1. Название и продолжительность самого длительного трека.
```
SELECT track, duration
FROM tracks
ORDER BY duration DESC
LIMIT 1;
```
![image](https://github.com/Destian1995/HW-python-netology/assets/106807250/ccefe2ee-716f-4f6d-9d41-c5734f029c6b)

2. Название треков, продолжительность которых не менее 3,5 минут.
```
SELECT track
FROM tracks
WHERE duration >= '210';
```
![image](https://github.com/Destian1995/HW-python-netology/assets/106807250/b219ec09-d0ae-4480-97a4-2841395c3692)

3. Названия сборников, вышедших в период с 2018 по 2020 год включительно.
```
SELECT names
FROM collection
WHERE releaseyear BETWEEN 2018 AND 2020;
```
![image](https://github.com/Destian1995/HW-python-netology/assets/106807250/b150b553-b019-40d3-a2a0-70b75fca3b14)

4. Исполнители, чьё имя состоит из одного слова.
```
SELECT performer
FROM performers
WHERE performer NOT LIKE '% %';
```
![image](https://github.com/Destian1995/HW-python-netology/assets/106807250/51fb69ac-f2d2-49fc-a391-458cb935ccc8)

5. Название треков, которые содержат слово «мой» или «my».
```
SELECT track
FROM tracks
WHERE track LIKE '%my%' OR track LIKE '%My%';
```
![image](https://github.com/Destian1995/HW-python-netology/assets/106807250/1df81e08-eb96-4029-9da2-cfc61d3df01f)


## Задание 3


1. Количество исполнителей в каждом жанре.
```
SELECT g.genre, COUNT(a.id) AS количество_исполнителей
FROM musicgenres g
JOIN genre_performers ag ON g.id = ag.genre_id
JOIN performers a ON ag.genre_id = a.id
GROUP BY g.genre;
```
![image](https://github.com/Destian1995/HW-python-netology/assets/106807250/35ff0ed2-440e-4dfb-8d29-26608620f3cc)



2. Количество треков, вошедших в альбомы 2019–2020 годов.
```
SELECT COUNT(t.id) AS count_tracks
FROM tracks t
JOIN albums a ON t.id = a.id
WHERE a.releaseyear BETWEEN 2019 AND 2020;
```
![image](https://github.com/Destian1995/HW-python-netology/assets/106807250/0432deb5-d424-45df-8076-dcbd562192a9)


3. Средняя продолжительность треков по каждому альбому.
Здесь вывел в секундах, в том же формате что и в таблице пока не удается, там какие-то совсем сложные запросы получатся должны с вычислениями.
```
SELECT a.album, 
       AVG((SUBSTRING(t.duration, 1, POSITION(':' IN t.duration) - 1)::INT * 60 + 
           SUBSTRING(t.duration, POSITION(':' IN t.duration) + 1)::INT)::NUMERIC) AS average_duration
FROM albums a
JOIN tracks t ON a.id = t.id
GROUP BY a.album;
```
![image](https://github.com/Destian1995/HW-python-netology/assets/106807250/5b845bf2-6675-47fb-a082-0a66893a7a4f)


4. Все исполнители, которые не выпустили альбомы в 2020 году.

```
SELECT DISTINCT p.performer
FROM performers p
LEFT JOIN performer_albums pa ON p.id = pa.performer_id
LEFT JOIN albums a ON pa.album_id = a.id
GROUP BY p.performer
HAVING SUM(CASE WHEN a.releaseyear = 2020 THEN 1 ELSE 0 END) = 0; 
```
![image](https://github.com/Destian1995/HW-python-netology/assets/106807250/440c5573-d6ba-4785-811e-880e461cb9bf)


5. Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами).
```
SELECT DISTINCT c.names
FROM collection c 
LEFT JOIN track_collections tc ON c.id = tc.collection_id
LEFT JOIN track_albums ta ON tc.track_id = ta.track_id 
LEFT JOIN performer_albums pa ON ta.albums_id = pa.album_id 
LEFT JOIN performers p ON pa.performer_id = p.id 
WHERE p.performer = 'Уэйн Статик'
GROUP BY c.names;
```

![image](https://github.com/Destian1995/HW-python-netology/assets/106807250/27f54194-7d3e-4dfa-b18d-c8310ad355ee)


