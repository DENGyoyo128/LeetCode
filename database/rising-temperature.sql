# Write your MySQL query statement below
WITH t AS (
    SELECT
        id,
        temperature,
        LAG(temperature, 1) OVER (ORDER BY id) AS prev_temp
    FROM weather
    order by recordDate
)
SELECT id
FROM t
WHERE temperature > prev_temp
