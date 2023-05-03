 SELECT CASE
         WHEN job_vacancy_ratio.is_real = 1 THEN real_location.name
         ELSE aggregated_location.description
       END AS location,
       job_vacancy_ratio.ratio
FROM   job_vacancy_ratio job_vacancy_ratio
       left join real_location_job real_location
              ON job_vacancy_ratio.location_id_real = real_location.id
       left join aggregated_location_job aggregated_location
              ON job_vacancy_ratio.location_id_aggregated = aggregated_location.id
WHERE  job_vacancy_ratio.year = %s
       AND job_vacancy_ratio.quarter = %s