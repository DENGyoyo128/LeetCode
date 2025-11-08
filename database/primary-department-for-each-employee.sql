# Write your MySQL query statement below
-- select *
-- from (
--     select employee_id,department_id,primary_flag,count(employee_id) as cnt
--     from employee
--     group by employee_id
--     having cnt=1
-- ) 
-- union
-- (
--     select employee_id,department_id,primary_flag,count(employee_id) as cnt
--     from employee
--     where primary_flag="Y"
--     group by employee_id
-- ) 


SELECT employee_id, department_id
FROM employee
GROUP BY employee_id
HAVING COUNT(*) = 1
UNION
SELECT employee_id, department_id
FROM employee
WHERE primary_flag = 'Y'