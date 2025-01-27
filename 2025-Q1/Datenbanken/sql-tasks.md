# Joins
## Example
~~~~sql
SELECT u.name AS user_name, r.name AS role_name
FROM Users AS u 
LEFT JOIN role_user
ON u.id = role_user.user_id
LEFT JOIN roles AS r 
ON role_user.role_id = r.id 
LIMIT 20;
~~~~

# Tasks 

## Create table store database 
~~~~sql
create table stores (
    id int auto_increment,
    primary key(id),
    name varchar(255),
    location varchar(255),
);
~~~~sql
~~~~

## solution prof
~~~~sql
create table store (
    id int aut_increment primary key,
    fruit_id int not null,
    quantity decimal(10,2) not null default 0,
    unit enum('kg', 'Liter', 'piece')
);
~~~~

## subqueries mapping fruits to country
~~~~sql
select name as fruit_name,
    (select name 
     from countries 
     where countries.id = fruits.origin)
     as country
from fruits;

-- join approach:
select fruits.name as fruit_name, countries.name
from fruits
left join countries
on countries.id = fruits.origin;
~~~~

## Task get average storage period with fruits
~~~~sql
select fruits.seasonality, fruits.storage_period, 
    (select avg(f.storage_period) from fruits as f where f.seasonality = fruits.seasonality)
    as avg_st_period
from fruits;
~~~~

## Task  list each fruits name and the total number of images associated with it
~~~~sql
select name as fruit_name,
    (select count(*) from fruit_images as fi where fi.fruit_id = fruits.id)
        as images_count
    from fruits;
--Find fruits stored in the same storage place as the fruit "Mango"
select fruits.name
    from fruits 
    where fruits.storage_place = 
        (select f.storage_place from fruits as f where f.name = "Mangosteen");
~~~~

## List all fruits along with the total number of images per fruit
~~~~sql 
select name, fi.image_count 
from fruits 
left join 
    (
    select fruit_id, count(*) as image_count 
    from fruit_images
    group by fruit_id
    )
    as fi 
on fi.fruit_id = fruits.id;
-- opt 2
select fruits.id, name, count(fi.id) as images_count
from fruits 
left join fruit_images as fi
on fi.fruit_id = fruits.id
group by fruits.id, fruits.name;
~~~~

## Find fruits with storage period the as "Mangosteen"
~~~~sql
select distinct name
from fruits 
where storage_period in 
    (
    select distinct storage_period 
    from fruits 
    where name ='Mangosteen'
    );
~~~~

## Count fruits per continent
~~~~sql
select continent, count(*) as fruit_count
from 
    (
    select countries.continent, fruits.name 
    from fruits 
    join countries 
    on fruits.origin = countries.id
    )
    as subquery
group by continent;

~~~~

## Procedures
~~~~sql
delimiter // 
create procedure GetFruitsBySeason(in season varchar(20))
begin
    select * from fruits where seasonality = season; 
end; // 
delimiter;

~~~~

### If procedure
~~~~sql
create procedure CheckFruitSeason(in fruit_id int, out result varchar(50))
begin   
    declare season varchar(20);
    select seasonality into season from fruits where id = fruit_id;
    
    if season = "Summer" then
        set result = "This fruit is available in Summer";
    else
        set result = "This fruit is not available in Summer";
    end if;
end;
~~~~

### Update Procedures
~~~~sql
create procedure UpdateFruitSeason(in fruit_id int, in new_season enum("Summer", "Winter"))
begin
    update fruits set seasonality = new_season where id = fruit_id;
end;
~~~~

### Procedure with json_table
~~~~sql
create procedure UpdateMultipleFruits(in ids text, in new_storage enum("Fridge","WoodBox"))
begin
    update fruits set storage_place = new_storage where id in (select id from json_table(ids,"$[*]" columns (id int path "$")));
end;
~~~~


### Normal form
~~~~sql
alter table goods add column supplier_name varchar(255) after price, add column supplier_address varchar(255) after supplier_name;

update goods set supplier_name = substring_index(supplier_info, ' - ',1),supplier_address = substring_index(supplier_info, ' - ',-1);

alter table goods drop column supplier_info;

~~~~

# Transactions
## setup
~~~~sql
create table accounts(
    id int auto_increment primary key,
    name varchar(50),
    balance decimal(10,2)
);

insert into accounts (name,balance) values ("Alice", 500), ("Bob", 300);
~~~~
