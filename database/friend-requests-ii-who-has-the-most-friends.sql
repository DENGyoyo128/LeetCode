# Write your MySQL query statement below
with all_num as
((select accepter_id as id,count(accepter_id) as num
from requestaccepted
group by accepter_id
order by num desc)
union all
(select requester_id as id,count(requester_id) as num
from requestaccepted
group by requester_id
order by num desc))
-- select id ,a.num+r.num as num
select id, sum(num) as num
from all_num
group by id 
order by num desc
limit 1