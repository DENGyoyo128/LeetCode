# Write your MySQL query statement below
-- select product_id , 
--        (select min(year) as first_year from sales group by product_id) as t1 ,quantity,price
-- from sales
-- where year=t1.first_year
-- group by product_id
SELECT product_id, year AS first_year, quantity, price
FROM Sales
WHERE (product_id, year) IN (
  SELECT product_id, MIN(year)
  FROM Sales
  GROUP BY product_id
)