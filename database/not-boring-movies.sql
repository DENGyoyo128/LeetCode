# Write your MySQL query statement below
SELECT *
FROM Cinema
WHERE id % 2 = 1            -- 奇数 ID
  AND description != 'boring'  -- 描述不是 "boring"
ORDER BY rating DESC;       -- 评分降序