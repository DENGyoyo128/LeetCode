# Write your MySQL query statement below
with accept as
(select accepter_id as id,count(accepter_id) as num
from requestaccepted
group by accepter_id
order by num desc),
request as
(select requester_id as id,count(requester_id) as num
from requestaccepted
group by accepter_id
order by num desc
)
select a.id ,a.num+r.num as num
from request r
join accept a on a.id=r.id
order by num desc
limit 1

