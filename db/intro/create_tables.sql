drop table items;
drop table categories;

-- \c postgres
-- drop database store_db;
-- create database store_db;
-- \c store_db

create table categories (
    id serial primary key,

    name varchar(50) not null,
    description text
);

create table items (
    id serial primary key,

    name varchar(100) not null,
    description text not null,
    categories_id integer not null,

    foreign key (categories_id) references categories(id)
);

insert into categories (name, description) values
    ('Electronics', 'Gadgets to make life easier'),
    ('Car Parts', 'Expensive stuff for the box on 4 wheels'),
    ('Sports', 'Get out and play!'),
    ('Video Games', 'Stay in and play!')
    ;
