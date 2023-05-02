CREATE TABLE IF NOT EXISTS eurostat.aggregated_location
  (
     id          INT NOT NULL PRIMARY KEY,
     description VARCHAR(255) NULL
  );

CREATE TABLE IF NOT EXISTS eurostat.real_location
  (
     id   INT NOT NULL PRIMARY KEY,
     name VARCHAR(255) NULL
  );

CREATE TABLE IF NOT EXISTS eurostat.house_price
  (
     id                     INT auto_increment PRIMARY KEY,
     price                  FLOAT NULL,
     quarter                INT NULL,
     location_id_real       INT NULL,
     location_id_aggregated INT NULL,
     year                   INT NULL,
     is_real                TINYINT(1) NULL,
     CONSTRAINT house_price_ibfk_1 FOREIGN KEY (location_id_real) REFERENCES
     eurostat.real_location (id),
     CONSTRAINT house_price_ibfk_2 FOREIGN KEY (location_id_aggregated)
     REFERENCES eurostat.aggregated_location (id),
     CHECK ((`location_id_real` IS NULL) <> (`location_id_aggregated` IS NULL))
  ); 