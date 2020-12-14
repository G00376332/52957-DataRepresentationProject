create database baltic;
use baltic;

create table harvest (
id int NOT NULL,
employeeName VARCHAR (250),
fieldSection VARCHAR (250),
variety VARCHAR (250),
quantity INT,
PRIMARY KEY(id));

insert into harvest (id, employeeName, fieldSection, variety, quantity) values
('100','Jan Kowalski', 'A1', 'Patriot', '300'),
('101','Roman Malinowski', 'A3', 'Duke', '150'),
('105','Zbyszek Dzik', 'C2', 'Toro', '420'),
('107','Ola Miodek', 'B3', 'Brigitta', '180'),
('120','Maja Nowak', 'C1', 'Bluecrop', '260'),
('135','Beata Cichy', 'B2', 'Nelson', '200');

create table users (
id int NOT NULL auto_increment,
username varchar(250),
password varchar(250),
PRIMARY KEY(id));

insert into users (username, password) values ("admin", "password");
