# Eurostat Dashboard

Please, find submission documents using the following links:

1. [Assignment 3](https://github.com/t3ch123/databases-eurostat/blob/main/submissions/assignment_3.pdf)

# Reproduce

To run MySQL instance, use this

```bash
docker run --name eurostat -e DWITH_DEBUG=1 -e MYSQL_DATABASE=eurostat -e MYSQL_ROOT_PASSWORD=eurostat -p 3306:3306 -d mysql:latest
```

Initialize tables using the following schema. Import files `real.csv`, `aggregated.txt` and `out.csv` into the MySQL instance.

```sql
CREATE TABLE Real_Location
(
    id   INT PRIMARY KEY,
    name VARCHAR(255)
);
CREATE TABLE Aggregated_Location
(
    id          INT PRIMARY KEY,
    description VARCHAR(255)
);
CREATE TABLE House_Price
(
    id                     INT AUTO_INCREMENT,
    price                  FLOAT,
    quarter                INT,
    location_id_real       INT,
    location_id_aggregated INT,
    year                   INT,
    is_real                BOOLEAN,
    PRIMARY KEY (id),
    FOREIGN KEY (location_id_real) REFERENCES Real_Location (id),
    FOREIGN KEY (location_id_aggregated) REFERENCES
        Aggregated_Location (id),
    CHECK ((location_id_real IS NULL) != (location_id_aggregated IS NULL))
);
```

