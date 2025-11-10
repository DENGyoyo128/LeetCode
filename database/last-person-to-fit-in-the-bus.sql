# Write your MySQL query statement below
-- select  *
-- from queue
-- order by turn asc
-- having weight < 1000

SELECT person_name
FROM (
  SELECT
    person_name,
    SUM(weight) OVER (ORDER BY turn) AS run_w
  FROM Queue
) q
WHERE run_w <= 1000
ORDER BY q.run_w DESC  
LIMIT 1