# Write your MySQL query statement below
select t1.customer_id,count(*) as count_no_trans
from visits t1
left join transactions t2 on t1.visit_id = t2.visit_id
where t2.transaction_id is NULL
group by(t1.customer_id)
