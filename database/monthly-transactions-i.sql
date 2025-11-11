-- # Write your MySQL query statement below
-- select left(trans_date,7) as month, 
--         country ,
--         count(state) in (select left(trans_date,7) as month,count(state) from transactions group by country, month) as trans_count,
--         count(*) as approved_count,
--         sum(amount) in (select left(trans_date,7) as month,count(state),sum(amount) from transactions group by country, month) as trans_total_amount,
--         sum(amount) as approved_total_amount 
-- from transactions 
-- where state='approved'
-- group by country, month



SELECT
  DATE_FORMAT(trans_date, '%Y-%m') AS month,
  country,
  COUNT(*) AS trans_count,                                             -- 全部交易数
  SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,      -- 已批准数量
  SUM(amount) AS trans_total_amount,                                   -- 全部交易金额
  SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount -- 已批准金额
FROM Transactions
GROUP BY DATE_FORMAT(trans_date, '%Y-%m'), country
ORDER BY month, country