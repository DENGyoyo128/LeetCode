# Write your MySQL query statement below
-- select class
-- from courses
-- where count(distinct student)>=5
-- group by class

select class
from courses
group by class
-- 筛选分组后的条件要用 HAVING
having count(distinct student)>=5