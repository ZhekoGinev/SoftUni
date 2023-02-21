SET NAMES 'utf8';

DROP DATABASE IF EXISTS bulgaria;

CREATE DATABASE bulgaria CHARACTER SET utf8 COLLATE utf8_general_ci;

GRANT ALL ON bulgaria.* TO 'web_user'@'%' IDENTIFIED BY 'Password1';

USE bulgaria;

CREATE TABLE cities (id int primary key auto_increment, city_name varchar(50), population int);

INSERT INTO cities (city_name, population) VALUES ('София', 1248452);
INSERT INTO cities (city_name, population) VALUES ('Пловдив', 343070);
INSERT INTO cities (city_name, population) VALUES ('Варна', 332686);
INSERT INTO cities (city_name, population) VALUES ('Бургас', 199571);
INSERT INTO cities (city_name, population) VALUES ('Русе', 137533);
INSERT INTO cities (city_name, population) VALUES ('Стара Загора', 124599);
INSERT INTO cities (city_name, population) VALUES ('Плевен', 93214);
INSERT INTO cities (city_name, population) VALUES ('Сливен', 83740);
INSERT INTO cities (city_name, population) VALUES ('Добрич', 79269);
INSERT INTO cities (city_name, population) VALUES ('Шумен', 72342);
