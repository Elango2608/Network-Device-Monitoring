drop database network_inventory;
create database network_inventory;

use network_inventory;


create table engineers (
    engineer_id int primary key auto_increment,
    engineer_name varchar(100) not null,
    phone varchar(15),
    email varchar(100)
);


create table locations (
    location_id int primary key auto_increment,
    location_name varchar(100) not null
);


create table devices (
    device_id int primary key auto_increment,
    device_name varchar(100) not null,
    device_type varchar(100) not null,
    ip_address varchar(50) unique,
    status varchar(20) default 'Active',
    location_id int,
    engineer_id int,

    foreign key (location_id) references locations(location_id),
    foreign key (engineer_id) references engineers(engineer_id)
);


create table maintenance (
    maintenance_id int primary key auto_increment,
    device_id int,
    maintenance_date date,
    description varchar(255),
    engineer_id int,

    foreign key (device_id) references devices(device_id),
    foreign key (engineer_id) references engineers(engineer_id)
);

insert into engineers (engineer_name, phone, email)
values
('Alice', '1234567890', 'alice@gmail.com'),
('Bob', '2134567890', 'bob@gmail.com');


insert into locations (location_name)
values
('Server Room'),
('Computer Lab'),
('Main Office');


insert into devices
(device_name, device_type, ip_address, status, location_id, engineer_id)
values
('Router-01', 'Router', '192.168.1.1', 'Active', 1, 1),
('Switch-01', 'Switch', '192.168.1.2', 'Active', 2, 2),
('Firewall-01', 'Firewall', '192.168.1.3', 'Maintenance', 1, 1);

select * from engineers;

select * from locations;

select * from devices;

select * from maintenance;

select d.device_id,d.device_name,d.device_type,d.ip_address,d.status,l.location_name,e.engineer_name
from devices d join locations l
on d.location_id = l.location_id join engineers e
on d.engineer_id = e.engineer_id;