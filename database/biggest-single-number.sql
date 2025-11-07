# Write your MySQL query statement below
-- select max count(num) as num
-- from mynumbers

SELECT MAX(num) AS num
FROM (
  SELECT num
  FROM MyNumbers
  GROUP BY num
  HAVING COUNT(*) = 1
) AS t
