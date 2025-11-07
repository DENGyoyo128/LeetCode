# Write your MySQL query statement below
select activity_date as day , count(distinct user_id) as  active_users
from activity
-- where  acivity_date > '2019-07-27'- 30 and acivity_date <= '2019-07-27'
WHERE activity_date >= DATE_SUB('2019-07-27', INTERVAL 29 DAY)
  AND activity_date <= '2019-07-27'
group by activity_date