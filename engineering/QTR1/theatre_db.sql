# Drop table if exists
drop table if exists book cascade;
drop table if exists audience cascade;
drop table if exists showplan cascade;
drop table if exists performance cascade;
drop table if exists seat cascade;
drop table if exists theatre cascade;
drop table if exists building cascade;

# Create tables
create table building 
(
b_id varchar(10),
b_name varchar(20) not null,
location varchar(20) not null,
constraint pk_building primary key(b_id)
);

create table theatre
(
t_id varchar(10),
t_name varchar(20) not null,
capacity int not null,
b_id varchar(10) not null,
constraint pk_theatre primary key(t_id),
constraint fk_theatre foreign key(b_id) references building(b_id)
);

create table seat
(
se_id varchar(10),
se_row varchar(3),
num int not null,
t_id varchar(10) not null,
constraint pk_seat primary key(se_id),
constraint fk_seat foreign key(t_id) references theatre(t_id)
);

create table performance
(
p_id varchar(10) not null,
title varchar(20) not null,
p_type varchar(20),
price int,
constraint pk_performance primary key(p_id)
);

create table showplan
(
s_id varchar(10) not null,
s_date date not null,
s_time time not null,
p_id varchar(10) not null,
t_id varchar(10) not null,
constraint pk_showplan primary key(s_id),
constraint fk_pshowplan foreign key(p_id) references performance(p_id),
constraint fk_tshowplan foreign key(t_id) references theatre(t_id)
);

create table audience
(
a_id varchar(10) not null,
a_name varchar(20) not null,
gender varchar(10),
age int,
constraint pk_audience primary key(a_id)
);

create table book
(
r_id varchar(10),
a_id varchar(10) not null,
s_id varchar(10) not null,
se_id varchar(10) not null,
constraint pk_book primary key(r_id),
constraint fk_abook foreign key(a_id) references audience(a_id),
constraint fk_sbook foreign key(s_id) references showplan(s_id),
constraint fk_sebook foreign key(se_id) references seat(se_id)
);
