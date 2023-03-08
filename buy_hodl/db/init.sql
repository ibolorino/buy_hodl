create table "user"
(
    id              serial  not null
        constraint user_pk
            primary key,
    full_name       varchar,
    email           varchar not null,
    hashed_password varchar not null,
    is_active       boolean default true,
    is_superuser    boolean default false
);

create unique index user_email_uindex
    on "user" (email);

create index user_full_name_index
    on "user" (full_name);


create table asset_type
(
    id   serial  not null
        constraint asset_type_pk
            primary key,
    name varchar not null
);

create unique index asset_type_name_uindex
    on asset_type (name);

create table asset
(
    id            serial  not null
        constraint asset_pk
            primary key,
    name          varchar not null,
    ticker        varchar not null,
    current_price decimal,
    asset_type_id integer not null
        constraint asset_asset_type_id_fk
            references asset_type
);

create unique index asset_name_uindex
    on asset (name);

create unique index asset_ticker_uindex
    on asset (ticker);



