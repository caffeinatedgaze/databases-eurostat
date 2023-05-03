CREATE TABLE real_location_consumer
(
    id   INT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE aggregated_location_consumer
(
    id          INT PRIMARY KEY,
    description VARCHAR(255)
);

CREATE TABLE consumer_price
(
    id INT auto_increment PRIMARY KEY,
    price                  FLOAT,
    location_id_real       INT,
    location_id_aggregated INT,
    year                   INT,
    month                  INT,
    is_real                BOOLEAN,
    FOREIGN KEY (location_id_real) REFERENCES real_location_consumer (id),
    FOREIGN KEY (location_id_aggregated) REFERENCES aggregated_location_consumer (id),
    CHECK ((location_id_real IS NULL) != (location_id_aggregated IS NULL))
);
