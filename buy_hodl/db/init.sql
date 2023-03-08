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
