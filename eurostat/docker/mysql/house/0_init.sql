create table if not exists eurostat.Aggregated_Location
(
    id          int          not null
        primary key,
    description varchar(255) null
);

create table if not exists eurostat.Real_Location
(
    id   int          not null
        primary key,
    name varchar(255) null
);

create table if not exists eurostat.House_Price
(
    id                     int auto_increment
        primary key,
    price                  float      null,
    quarter                int        null,
    location_id_real       int        null,
    location_id_aggregated int        null,
    year                   int        null,
    is_real                tinyint(1) null,
    constraint House_Price_ibfk_1
        foreign key (location_id_real) references eurostat.Real_Location (id),
    constraint House_Price_ibfk_2
        foreign key (location_id_aggregated) references eurostat.Aggregated_Location (id),
    check ((`location_id_real` is null) <> (`location_id_aggregated` is null))
);