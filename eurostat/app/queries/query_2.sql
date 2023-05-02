 SELECT   year,
         quarter,
         price
FROM     house_price
ORDER BY price DESC limit %s