SELECT Avg(price)                                         AS average_price,
       Coalesce(location_id_real, location_id_aggregated) AS location_id
FROM   consumer_price
WHERE  year BETWEEN %s AND %s
GROUP  BY location_id