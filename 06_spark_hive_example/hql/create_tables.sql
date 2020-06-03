set hivevar:db_path=/user/yashiro/plants;
CREATE DATABASE IF NOT EXISTS plants;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- subkingdoms  -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CREATE EXTERNAL TABLE IF NOT EXISTS plants.subkingdoms(
    id BIGINT,
    link STRING,
    name STRING,
    slug STRING
)
    STORED AS PARQUET
    LOCATION "${db_path}/subkingdoms";

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- kingdoms  -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CREATE EXTERNAL TABLE IF NOT EXISTS plants.kingdoms(
    id BIGINT ,
    name STRING ,
    slug STRING ,
    subkingdoms array<
          struct <
             id: BIGINT,
             link: STRING,
             name: STRING,
             slug: STRING
           >
     >
)
    STORED AS PARQUET
    LOCATION "${db_path}/kingdoms";

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- divisions  -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CREATE EXTERNAL TABLE IF NOT EXISTS plants.divisions(
    division_classes array<
         struct<
            id: BIGINT,
            link: STRING,
            name: STRING,
            slug: STRING
             >
         >,
    id BIGINT,
    kingdom struct<
        id: BIGINT,
        link: STRING,
        name: STRING,
        slug: STRING
         >,
    name STRING,
    slug STRING,
    subkingdom struct<
        id: BIGINT,
        link: STRING,
        name: STRING,
        slug: STRING
        >
)
    STORED AS PARQUET
    LOCATION "${db_path}/divisions";

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- families  -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CREATE EXTERNAL TABLE IF NOT EXISTS plants.families(
    common_name STRING,
    division struct <
        id: BIGINT,
        link: STRING,
        name: STRING,
        slug: STRING
        >,
    division_class struct <
        id: BIGINT,
        link: STRING,
        name: STRING,
        slug: STRING
        >,
    division_order struct <
        id: BIGINT,
        link: STRING,
        name: STRING,
        slug: STRING
        >,
    genuses array <
         struct <
            id: BIGINT,
            link: STRING,
            name: STRING,
            slug: STRING
         >
     >,
    id BIGINT,
    kingdom struct <
            id: BIGINT,
            link: STRING,
            name: STRING,
            slug: STRING
            >,
    name STRING,
    slug STRING,
    subkingdom struct <
            id: BIGINT,
            link: STRING,
            name: STRING,
            slug: STRING
            >
    )
    STORED AS PARQUET
    LOCATION "${db_path}/families";

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- Genus  -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CREATE EXTERNAL TABLE IF NOT EXISTS plants.genuses(
    class struct<
         id: BIGINT,
         link: STRING,
         name: STRING,
         slug: STRING
         >,
    division struct<
         id: BIGINT,
         link: STRING,
         name: STRING,
         slug: STRING
         >,
    family struct<
         common_name: STRING,
         id: BIGINT,
         link: STRING,
         name: STRING,
         slug: STRING
         >,
    id BIGINT,
    kingdom struct<
         id: BIGINT,
         link: STRING,
         name: STRING,
         slug: STRING
         >,
    name STRING,
    `order` struct<
         id: BIGINT,
         link: STRING,
         name: STRING,
         slug: STRING
         >,
    slug STRING,
    subkingdom struct<
        id: BIGINT,
        link: STRING,
        name: STRING,
        slug: STRING
        >
)
    STORED AS PARQUET
    LOCATION "${db_path}/genuses";

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- plants  -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

CREATE EXTERNAL TABLE IF NOT EXISTS plants.plants (
    common_name STRING,
    complete_data BOOLEAN,
    id BIGINT,
    link STRING,
    scientific_name STRING,
    slug STRING
    )
    STORED AS PARQUET
    LOCATION "${db_path}/plants";

