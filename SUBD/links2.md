## Задание 1
(ссылка на скрипт создания БД)[https://github.com/Destian1995/HW-python-netology/blob/main/SUBD/create_DB.sql]

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
