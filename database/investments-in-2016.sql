# Write your MySQL query statement below
-- with first as 
-- (select tiv_2015,count(tiv_2015) as ct2015
-- from Insurance
-- group by tiv_2015),
-- second as(
--     select pid, concat(lat,lon) as ct ,count(*) as cnt
--     from Insurance
--     group by ct
-- )
-- select sum(i.tiv_2016) as tiv_2016
-- from Insurance i
-- left join  first f on f.tiv_2015=i.tiv_2015
-- left join second s on  i.pid=s.pid
-- having f.ct2015>=2 and s.cnt=1

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM (
  SELECT
    tiv_2016,
    COUNT(*) OVER (PARTITION BY tiv_2015) AS c2015,
    COUNT(*) OVER (PARTITION BY lat, lon) AS c_city
  FROM Insurance
) x
WHERE x.c2015 >= 2
  AND x.c_city = 1