# Task
Create db for a bookstore

## Description - Design
Problem: A database that handles the data of a bookstore

Track Book Inventory  
Customers
Orders


### Tables 
+ books (id, isbn, name, amount, price)
+ address(id,street,coutry,postal_code)
+ customers(id, name, email, password)
+ orders(id, customer_id, amount)
+ book_order(book_order_id, order_id, book_id, amount)

# SQL
## Create Tables and DB
~~~~sql
-- create db
create database bookstore;

-- use db
use bookstore;

-- tables
create table books
(
    id int auto_increment,
    isbn varchar(17) not null,
    title varchar(50) not null,
    author varchar(50),
    release_year int,
    amount int,
    price float,
    primary key(id)
);

create table address
(
    id int auto_increment,
    street varchar(100),
    country varchar(100),
    postal_code varchar(20),
    primary key(id)
);

create table customers
(
    id int auto_increment,
    first_name varchar(50),
    last_name varchar(50),
    email varchar(50) not null,
    password varchar(100) not null,
    address_id int not null,
    primary key(id),
    foreign key(address_id) references address(id)
);

create table orders
(
    id int auto_increment,
    customer_id int not null,
    order_date date,
    order_state enum('paid','in delivery','delivered'),
    delivery_id varchar(50),
    primary key(id),
    foreign key(customer_id) references customers(id)
);

create table book_order
(
    id int auto_increment,
    order_id int not null,
    book_id int not null,
    order_amount int not null,
    primary key(id),
    foreign key(order_id) references orders(id),
    foreign key(book_id) references books(id)
);

~~~~
