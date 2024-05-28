drop table items;
drop table categories;

create table categories (
    id serial primary key,

    -- unique constraint ensures that two categories can't have the same name
    name varchar(50) not null unique,
    description text
);

create table items (
    id serial primary key,

    name varchar(100) not null,
    description text not null,
    -- default value will be used if a new item is created without specifying stock
    stock int default 0,
    -- category is now optional ("not null" constraint removed)
    category_id integer,

    foreign key (category_id) references categories (id) on delete cascade
);

insert into categories (name, description) values 
    ('Electronics', 'Gadgets to make life easier'),
    ('Car Parts', 'Expensive stuff for the box on 4 wheels'),
    ('Sports', 'Get out and play!'),
    ('Video Games', 'Stay in and play!')
;

insert into items (name, description, stock, category_id) values
    ('Skyrim', 'Awesome open-world RPG', 5, 4),
    ('World of Warcraft', 'Popular MMORPG', 7, 4),
    ('iPhone', 'Apple''s flagship smartphone', 12, 1),
    ('Greg Norman golf clubs', 'At least you can look like a pro', 2, 3)
;

-- Separate insert statement so we can provide only name and description
-- In this case, stock will be set to it's default value, and category_id will be null
insert into items (name, description) values
    ('Flying DeLorean', 'You built a time machine ... out of a car?!')
;
