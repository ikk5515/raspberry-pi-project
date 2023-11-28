drop table sensor

-- auto-generated definition
create table sensor
(
    seq           int auto_increment
        primary key,
    sensor_name   varchar(50)                        not null,
    measure_value float                              not null,
    measure_time  datetime default CURRENT_TIMESTAMP null
)