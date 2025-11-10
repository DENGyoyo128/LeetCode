# Write your MySQL query statement below
-- select e2.name 
select e2.name 
from employee e1
left join employee e2 on e1.managerid=e2.id
group by e1.managerid
having count(e2.id) >=5 