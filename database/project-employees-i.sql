# Write your MySQL query statement below
select p.project_id,avg(experience_years) as average_years
from project p
left join employee e on e.employee_id=p.employee_id
group by p.project_id