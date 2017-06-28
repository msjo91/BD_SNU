drop table if exists sales cascade;
drop table if exists store cascade;

/* 3-1. Create tables store and sales */
create table store
(
    storeNum varchar(20),
    s_name varchar(20),
    s_type varchar(20),
    city varchar(10),
    district varchar(10),
    managerNum varchar(20) unique,
    constraint pk_store primary key (storeNum)
);

create table sales
(
    timeKey date,
    itemNum varchar(20),
    storeNum varchar(20),
    employeeNum varchar(20),
    items_sold int,
    amount_sold int,
    tax_amount int,
    constraint fk_sales foreign key (storeNum) references store(storeNum),
    constraint pk_sales primary key (timeKey, itemNum, storeNum, employeeNum)
);

/* 3-2. Add and drop columns */
alter table store add contact varchar(20);
alter table sales drop column tax_amount;

/* 3-3. Drop the tables */
drop table sales;
drop table store;

/* Followed after basics.sql */

/* 3-4. Insert records into professor */
insert into professor values ('92003', '851221-2812312', '유강민', '920', '조교수', 2017);
insert into professor values ('92303', '600842-1293821', '최지헌', '923', '교수', 2000);
insert into professor values ('92503', '590605-2934212', '이한빛', '925', '교수', 1996);

/* 3-5. Give 1 more credit for 3-credit-courses */
update course set credit = credit + 1 where credit = 3;
/* Note : Once updated, it cannot be undone! (For now.) */