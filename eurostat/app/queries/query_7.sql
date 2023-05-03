SELECT Avg(ratio)                                         AS average_ratio,
       Coalesce(location_id_real, location_id_aggregated) AS location_id
FROM   job_vacancy_ratio
WHERE  year BETWEEN %s AND %s
GROUP  BY location_id