drop table if exists sales cascade;
drop table if exists store cascade;

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

alter table store add contact varchar(20);
alter table sales drop column tax_amount;

drop table sales;
drop table store;