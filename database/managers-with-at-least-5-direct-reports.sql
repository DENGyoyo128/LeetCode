# Write your MySQL query statement below
select e2.name 
from employee e1
left join employee e2 on e1.managerid=e2.id
group by e2.name
having count(e2.name) >=5