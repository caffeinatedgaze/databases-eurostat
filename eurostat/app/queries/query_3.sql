 SELECT CASE
         WHEN house_price.is_real = 1 THEN real_location.name
         ELSE aggregated_location.description
       END AS location,
       house_price.price
FROM   house_price house_price
       left join real_location real_location
              ON house_price.location_id_real = real_location.id
       left join aggregated_location aggregated_location
              ON house_price.location_id_aggregated = aggregated_location.id
WHERE  house_price.year = %s
       AND house_price.quarter = %s