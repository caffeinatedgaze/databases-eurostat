 SELECT CASE
         WHEN consumer_price.is_real = 1 THEN real_location.name
         ELSE aggregated_location.description
       END AS location,
       consumer_price.price
FROM   consumer_price consumer_price
       left join real_location_consumer real_location
              ON consumer_price.location_id_real = real_location.id
       left join aggregated_location_consumer aggregated_location
              ON consumer_price.location_id_aggregated = aggregated_location.id
WHERE  consumer_price.year = %s