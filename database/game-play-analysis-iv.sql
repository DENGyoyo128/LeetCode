# Write your MySQL query statement below
#先求首登日期，合并，判断首登日期+1，求比例avg(event_date=first_log_date+1)
-- with first_date as(
--     select player_id ,min(event_date) as first_log_date
--     from activity
--     group by player_id
-- )
-- select avg(event_date=first_log_date+1)/count(distinct a.player_id) as fraction
-- from activity a
-- left join first_date f on f.player_id=a.player_id 

WITH first_login AS (
  SELECT player_id, MIN(event_date) AS first_date
  FROM Activity
  GROUP BY player_id
)
SELECT ROUND(AVG(a2.player_id IS NOT NULL), 2) AS fraction
FROM first_login f
LEFT JOIN Activity a2
  ON a2.player_id = f.player_id
 AND a2.event_date = DATE_ADD(f.first_date, INTERVAL 1 DAY)