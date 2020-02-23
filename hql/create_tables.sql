CREATE DATABASE IF NOT EXISTS plants;

CREATE EXTERNAL TABLE IF NOT EXISTS plants.plants (
    common_name string,
    complete_data boolean,
    id long,
    link string,
    scientific_name string,
    slug string,
)
    STORE AS PARQUET
    LOCATION 'plants/plants';

CREATE EXTERNAL TABLE IF NOT EXISTS plants.genuses(
    class struct<
         id long,
         link string,
         name string,
         slug string
         >,
    division struct<
         id long,
         link string,
         name string,
         slug string
         >,
    family struct,
         common_name string,
         id long,
         link string,
         name string,
         slug string
         >,
    id long,
    kingdom struct,
         id long,
         link string,
         name string,
         slug string
         >,
    name string,
    order struct<
         id long,
         link string,
         name string,
         slug string
         >,
    slug string,
    subkingdom struct<
        id long,
        link string,
        name string,
        slug string
        >
)
    STORE AS PARQUET
    LOCATION 'plants/genuses';
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- divisions  -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CREATE EXTERNAL TABLE IF NOT EXISTS plants.divisions(
    division_classes array<
         struct<
             id long,
             link string,
             name string,
             slug string
             >
         >,
    id long,
    kingdom struct<
         id long,
         link string,
         name string,
         slug string
         >,
    name string,
    slug string
    subkingdom struct<
        id long,
        link string,
        name string,
        slug string
        >
)
    STORE AS PARQUET
    LOCATION 'plants/divisions';