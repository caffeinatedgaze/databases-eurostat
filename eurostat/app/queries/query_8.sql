 SELECT   year,
         quarter,
         ratio
FROM     job_vacancy_ratio
ORDER BY ratio DESC limit %s