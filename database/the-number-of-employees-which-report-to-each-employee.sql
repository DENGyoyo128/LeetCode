# Write your MySQL query statement below
select T1.reports_to as employee_id,T1.managename as name,T1.reports_count,T1.average_age
from (
    select e1.employee_id,count(e1.reports_to) as reports_count,e1.name,e1.reports_to,round(avg(e1.age),0) as average_age,e2.name as managename
    from employees e1
    left join employees e2 on e1.reports_to=e2.employee_id
    WHERE e1.reports_to IS NOT NULL
    group by e1.reports_to) as T1
order by employee_id asc

