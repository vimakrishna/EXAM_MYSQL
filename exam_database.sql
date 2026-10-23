create database shop_db;
use shop_db;
create table product(id int primary key auto_increment,name varchar(50),category varchar(100),price varchar(50),
quantity int,manufacture varchar(100));
select * from product;
