-- Создание таблицы "Список жанров музыки"
CREATE TABLE MusicGenres (
    id SERIAL PRIMARY KEY,
    Genre VARCHAR(255) UNIQUE NOT NULL
);


-- Создание таблицы "Список исполнителей"
CREATE TABLE Performers (
    id SERIAL PRIMARY KEY,
    Performer VARCHAR(255) UNIQUE NOT NULL
);


-- Создание таблицы "Список альбомов"
CREATE TABLE Albums (
    id SERIAL PRIMARY KEY,
    Album VARCHAR(255) UNIQUE NOT NULL,
    ReleaseYear INT NOT NULL CHECK (ReleaseYear >= 1900)
);


-- Создание таблицы "Список трэков"
CREATE TABLE Tracks (
    id SERIAL PRIMARY KEY,
    Track VARCHAR(255) UNIQUE NOT NULL,
    Duration VARCHAR(255) NOT NULL
);

-- Создание таблицы "Сборник"
CREATE TABLE Collection (
    id SERIAL PRIMARY KEY,
    Names VARCHAR(255) UNIQUE NOT NULL,
    ReleaseYear INT NOT NULL CHECK (ReleaseYear >= 1900)
	
);
-- Таблица связь жанров и исполнителей
CREATE TABLE Genre_Performers (
    Genre_id INT REFERENCES MusicGenres(id),
    Performer_id INT REFERENCES Performers(id),
    PRIMARY KEY (Genre_id, Performer_id)
);

-- Создание таблицы "Связь сборника и треков"
CREATE TABLE Track_Collections (
    Track_id INT REFERENCES Tracks(id),
    Collection_id INT REFERENCES Collection(id),
    PRIMARY KEY (Track_id, Collection_id)
);

-- Создание таблицы "Связь исполнителей и альбомов"
CREATE TABLE Performer_Albums (
    Performer_id INT REFERENCES Performers(id),
    Album_id INT REFERENCES Albums(id),
    PRIMARY KEY (Performer_id, Album_id)
);

-- Создание таблицы "Связь трэков и альбомов"
CREATE TABLE Track_Albums (
    Track_id INT REFERENCES Tracks(id),
    Albums_id INT REFERENCES Albums(id),
    PRIMARY KEY (Track_id, Albums_id)
);

-- Вставка данных в таблицу "Список жанров музыки"
INSERT INTO MusicGenres (Genre) VALUES
    ('Рок'),
    ('Поп'),
    ('Блюз'),
    ('Джаз'),
    ('Металл'),
    ('Электропоп'),
    ('Постпанк');

-- Вставка данных в таблицу "Список исполнителей"
INSERT INTO Performers (Performer) VALUES
    ('Уэйн Статик'),
    ('Бритни Спирс'),
    ('Дани Клейн'),
    ('Честер Беннингон');

-- Вставка данных в таблицу "Список альбомов"
INSERT INTO Albums (Album, ReleaseYear) VALUES
    ('Shadow Zone', 2003),
    ('Start a War', 2005),
    ('Cannibal', 2007),
    ('Blackout', 2007),
    ('The Promise', 2004),
    ('Meteora', 2003);

-- Вставка данных в таблицу "Список трэков"
INSERT INTO Tracks (Track, Duration) VALUES
    ('Electric Pulse', '2:40'),
    ('No Submission', '2:42'),
    ('Reptile', '2:31'),
    ('Set it Off', '3:55'),
    ('La Liriona', '3:44'),
    ('Je te veux', '3:22'),
    ('Toy Soldier', '4:19'),
    ('Price of Me', '3:32'),
    ('Somewhere I Belong', '3:34');

-- Вставка данных в таблицу "Сборник"
INSERT INTO Collection (Names, ReleaseYear) VALUES
    ('Популярные хиты 2007', 2008),
    ('Shadow', 2021),
    ('Легенды рока', 2019),
    ('Дух блюза', 2023);

-- Вставка данных в таблицу "Связь жанров и исполнителей"
INSERT INTO Genre_Performers (Genre_id, Performer_id) VALUES
    ((SELECT id FROM MusicGenres WHERE Genre = 'Рок'), (SELECT id FROM Performers WHERE Performer = 'Уэйн Статик')),
    ((SELECT id FROM MusicGenres WHERE Genre = 'Металл'), (SELECT id FROM Performers WHERE Performer = 'Уэйн Статик')),
    ((SELECT id FROM MusicGenres WHERE Genre = 'Постпанк'), (SELECT id FROM Performers WHERE Performer = 'Уэйн Статик')),
    ((SELECT id FROM MusicGenres WHERE Genre = 'Поп'), (SELECT id FROM Performers WHERE Performer = 'Бритни Спирс')),
    ((SELECT id FROM MusicGenres WHERE Genre = 'Блюз'), (SELECT id FROM Performers WHERE Performer = 'Бритни Спирс')),
    ((SELECT id FROM MusicGenres WHERE Genre = 'Блюз'), (SELECT id FROM Performers WHERE Performer = 'Дани Клейн')),
    ((SELECT id FROM MusicGenres WHERE Genre = 'Электропоп'), (SELECT id FROM Performers WHERE Performer = 'Бритни Спирс')),
    ((SELECT id FROM MusicGenres WHERE Genre = 'Рок'), (SELECT id FROM Performers WHERE Performer = 'Честер Беннингон')),
    ((SELECT id FROM MusicGenres WHERE Genre = 'Электропоп'), (SELECT id FROM Performers WHERE Performer = 'Уэйн Статик'));


-- Вставка данных в таблицу "Связь исполнителей и альбомов"
INSERT INTO Performer_Albums (Performer_id, Album_id) VALUES
    ((SELECT id FROM Performers WHERE Performer = 'Уэйн Статик'), (SELECT id FROM Albums WHERE Album = 'Shadow Zone')),
    ((SELECT id FROM Performers WHERE Performer = 'Уэйн Статик'), (SELECT id FROM Albums WHERE Album = 'Start a War')),
    ((SELECT id FROM Performers WHERE Performer = 'Уэйн Статик'), (SELECT id FROM Albums WHERE Album = 'Cannibal')),
    ((SELECT id FROM Performers WHERE Performer = 'Уэйн Статик'), (SELECT id FROM Albums WHERE Album = 'Blackout')),
    ((SELECT id FROM Performers WHERE Performer = 'Бритни Спирс'), (SELECT id FROM Albums WHERE Album = 'Blackout')),
    ((SELECT id FROM Performers WHERE Performer = 'Бритни Спирс'), (SELECT id FROM Albums WHERE Album = 'Start a War')),
    ((SELECT id FROM Performers WHERE Performer = 'Бритни Спирс'), (SELECT id FROM Albums WHERE Album = 'The Promise')),
    ((SELECT id FROM Performers WHERE Performer = 'Дани Клейн'), (SELECT id FROM Albums WHERE Album = 'The Promise')),
    ((SELECT id FROM Performers WHERE Performer = 'Честер Беннингон'), (SELECT id FROM Albums WHERE Album = 'Meteora'));

-- Вставка данных в таблицу "Связь треков и сборников"
INSERT INTO Track_Collections (Track_id, Collection_id) VALUES
    ((SELECT id FROM Tracks WHERE Track = 'No Submission'), (SELECT id FROM Collection WHERE Names = 'Популярные хиты 2007')), 
    ((SELECT id FROM Tracks WHERE Track = 'Toy Soldier'), (SELECT id FROM Collection WHERE Names = 'Популярные хиты 2007')),
    ((SELECT id FROM Tracks WHERE Track = 'Electric Pulse'), (SELECT id FROM Collection WHERE Names = 'Популярные хиты 2007')),
    ((SELECT id FROM Tracks WHERE Track = 'Price of Me'), (SELECT id FROM Collection WHERE Names = 'Shadow')),
    ((SELECT id FROM Tracks WHERE Track = 'La Liriona'), (SELECT id FROM Collection WHERE Names = 'Дух блюза')),
    ((SELECT id FROM Tracks WHERE Track = 'Toy Soldier'), (SELECT id FROM Collection WHERE Names = 'Shadow')),
    ((SELECT id FROM Tracks WHERE Track = 'Reptile'), (SELECT id FROM Collection WHERE Names = 'Легенды рока')),
    ((SELECT id FROM Tracks WHERE Track = 'Somewhere I Belong'), (SELECT id FROM Collection WHERE Names = 'Легенды рока')),; 

-- Вставка данных в таблицу "Связь трэков и альбомов"
INSERT INTO Track_Albums (Track_id, Albums_id) VALUES
   ((SELECT id FROM Tracks WHERE Track = 'No Submission'),(SELECT id FROM Albums WHERE Album = 'Cannibal')),
   ((SELECT id FROM Tracks WHERE Track = 'Toy Soldier'),(SELECT id FROM Albums WHERE Album = 'Blackout')),
   ((SELECT id FROM Tracks WHERE Track = 'Electric Pulse'),(SELECT id FROM Albums WHERE Album = 'Cannibal')),
   ((SELECT id FROM Tracks WHERE Track = 'Price of Me'),(SELECT id FROM Albums WHERE Album = 'Shadow Zone')),
   ((SELECT id FROM Tracks WHERE Track = 'La Liriona'),(SELECT id FROM Albums WHERE Album = 'The Promise')),
   ((SELECT id FROM Tracks WHERE Track = 'Je te veux'),(SELECT id FROM Albums WHERE Album = 'The Promise')),
   ((SELECT id FROM Tracks WHERE Track = 'Set it Off'),(SELECT id FROM Albums WHERE Album = 'Start a War')),
   ((SELECT id FROM Tracks WHERE Track = 'Somewhere I Belong'),(SELECT id FROM Albums WHERE Album = 'Meteora')),
   ((SELECT id FROM Tracks WHERE Track = 'Reptile'),(SELECT id FROM Albums WHERE Album = 'Start a War'));
