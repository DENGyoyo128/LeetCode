# Write your MySQL query statement below
select e2.name 
from employee e1
left join employee e2 on e1.managerid=e2.id
where e1.managerid is not null
group by e1.managerid
having count(e1.managerid) >=5