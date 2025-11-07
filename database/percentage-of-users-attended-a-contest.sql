# Write your MySQL query statement below
select r.contest_id,round(100*count(distinct r.user_id)/tu.total_users,2) as percentage 
from register r
CROSS JOIN (SELECT COUNT(*) AS total_users FROM Users) AS tu
group by r.contest_id
order by percentage desc,r.contest_id ASC
