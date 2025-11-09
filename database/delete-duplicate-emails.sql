# Write your MySQL query statement below
-- select id,email in (
--     select id, email
-- ) 
-- from


WITH ranked AS (
  SELECT id,
         ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
  FROM Person
)
DELETE FROM Person
WHERE id IN (SELECT id FROM ranked WHERE rn > 1)