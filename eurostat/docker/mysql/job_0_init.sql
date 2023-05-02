CREATE TABLE real_location_job
  (
     id   INT PRIMARY KEY,
     name VARCHAR(255)
  );

CREATE TABLE aggregated_location_job
  (
     id          INT PRIMARY KEY,
     description VARCHAR(255)
  );

CREATE TABLE job_vacancy_ratio
  (
     id INT auto_increment PRIMARY KEY,
     ratio                  FLOAT NULL,
     location_id_real       INT NULL,
     location_id_aggregated INT NULL,
     year                   INT NULL,
     quarter                INT NULL,
     is_real                BOOLEAN NULL,
     FOREIGN KEY (location_id_real) REFERENCES real_location_job (id),
     FOREIGN KEY (location_id_aggregated) REFERENCES aggregated_location_job (id),
     CHECK ( (location_id_real IS NULL) != (location_id_aggregated IS NULL) )
  );