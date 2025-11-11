# Write your MySQL query statement below
-- (select id+1 as id, student
-- from seat
-- where id%2 )
-- union 
-- (select id-1 as id, student
-- from seat
-- where id%2 =0) 
-- order by id


(SELECT id + 1 AS id, student
 FROM seat
 WHERE id % 2 = 1
   AND id != (SELECT MAX(id) FROM seat))
UNION
(SELECT id - 1 AS id, student
 FROM seat
 WHERE id % 2 = 0)
UNION
(SELECT id AS id, student
 FROM seat
 WHERE id = (SELECT MAX(id) FROM seat) AND id % 2 = 1)
ORDER BY id


-- SELECT
--   CASE
--     WHEN s.id % 2 = 1 AND s.id <> mx.mx_id THEN s.id + 1  -- odd, not the last -> swap forward
--     WHEN s.id % 2 = 0 THEN s.id - 1                       -- even -> swap back
--     ELSE s.id                                             -- last odd stays put
--   END AS id,
--   s.student
-- FROM Seat AS s
-- CROSS JOIN (SELECT MAX(id) AS mx_id FROM Seat) AS mx
-- ORDER BY id;