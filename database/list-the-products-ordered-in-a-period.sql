# Write your MySQL query statement below
-- p.product_name,sum(o.unit) as unit
select  p.product_name,sum(o.unit) as unit
from orders o
left join products p on p.product_id=o.product_id
where o.order_date like "%-02-%" 
group by p.product_id
having unit>=100