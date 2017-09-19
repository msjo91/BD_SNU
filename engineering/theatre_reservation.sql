# Drop tables
drop table if exists seat cascade;
drop table if exists assign cascade;
drop table if exists audience cascade;
drop table if exists building cascade;
drop table if exists performance cascade;

# Create table
create table building
(
id INT not null AUTO_INCREMENT,
name varchar(20),
location varchar(20) ,
capacity int,
assigned int default 0,
seat int default 0,
constraint pk_building primary key(id)
);

create table performance
(
id INT not null AUTO_INCREMENT,
name varchar(20),
type varchar(20),
price int,
booked int default 0,
constraint pk_performance primary key(id)
);

create table audience
(
aud_id int not null AUTO_INCREMENT,
name varchar(20),
gender varchar(20),
age int,
constraint pk_audience primary key(aud_id)
);

create table seat
(
seat_number int,
audience_id int,
performance_id int,
constraint pk_seat_number primary key(seat_number),
constraint fk1 foreign key(audience_id) references audience(aud_id) on delete cascade,
constraint fk2 foreign key( performance_id) references performance(id) on delete cascade
);

create table assign
(
building_id int,
performance_id int,
constraint fk3 foreign key(building_id) references building(id) on delete cascade,
constraint fk4 foreign key(performance_id) references performance(id) on delete cascade
);

# Insert data
insert into building (name, location, capacity,seat)
values ('Seoul Arts Center','Seoul',5,100),('Grand Peace Palace','Seoul',3,120);

insert into performance (name,type,price)
values('Coldplay Concert','Concert',100000),('Jekyll & Hyde','Musical',70000);

insert into audience (name,gender,age)
values('Park Junghyuk','M',15),('Kim Taeuk','F',30),('Choi Jihun','M',56);