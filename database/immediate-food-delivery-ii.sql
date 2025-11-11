# Write your MySQL query statement below
-- select round(sum(case when order_date=customer_pref_delivery_date then 1 else 0)/count(*),2)*100 as immediate_percentage 
-- from delivery
-- group by delivery_id

WITH first_order AS (
  SELECT customer_id, MIN(order_date) AS first_order_date
  FROM Delivery
  GROUP BY customer_id
)
SELECT ROUND(
         100 * AVG(d.order_date = d.customer_pref_delivery_date),
         2
       ) AS immediate_percentage
FROM Delivery d
JOIN first_order f
  ON d.customer_id = f.customer_id
 AND d.order_date  = f.first_order_date;

--  AVG(condition) 在 MySQL 中会把 TRUE/ FALSE 当 1/0 求均值，天然就是“比例”