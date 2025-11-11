# Write your MySQL query statement below
-- 1) Aggregate to daily revenue
-- WITH daily AS (
--   SELECT visited_on, SUM(amount) AS amount
--   FROM Customer
--   GROUP BY visited_on
-- )
-- -- 2) 7-day rolling window (inclusive of current day)
-- SELECT
--   d1.visited_on,
--   SUM(d2.amount) AS amount,
--   ROUND(SUM(d2.amount) / 7, 2) AS average_amount
-- FROM daily d1
-- JOIN daily d2
--   ON d2.visited_on BETWEEN DATE_SUB(d1.visited_on, INTERVAL 6 DAY) AND d1.visited_on
-- GROUP BY d1.visited_on
-- HAVING COUNT(*) = 7
-- ORDER BY d1.visited_on;


-- -- 先按天汇总
WITH daily AS (
  SELECT visited_on, SUM(amount) AS amount
  FROM Customer
  GROUP BY visited_on
),
win AS (
  SELECT
    visited_on,
    -- 7 天滚动总额
    SUM(amount)  OVER (
      ORDER BY visited_on
      ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS amount_7d,
    -- 当前窗口内的天数（用于判断是否满 7 天）
    COUNT(*) OVER (
      ORDER BY visited_on
      ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS cnt_7d
  FROM daily
)
SELECT
  visited_on,
  amount_7d AS amount,
  ROUND(amount_7d / 7, 2) AS average_amount
FROM win
WHERE cnt_7d = 7          -- 仅保留完整 7 天窗口
ORDER BY visited_on;