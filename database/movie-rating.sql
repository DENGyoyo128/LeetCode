# Write your MySQL query statement below
-- select u.name as results 
-- from movieRating m
-- left join Users u on u.user_id=m.user_id
-- where rating =(select max(rating) from MovieRating)
-- union 
-- (select v.title
-- from movieRating m
-- left join Movies v on v.movie_id=m.movie_id
-- where created_at like "2020-02%" 
-- group by  m.movie_id 
-- order by avg(m.rating) desc , v.title asc
-- limit 1)
(
  SELECT u.name AS results
  FROM Users u
  JOIN MovieRating mr ON mr.user_id = u.user_id
  GROUP BY u.user_id, u.name
  ORDER BY COUNT(*) DESC, u.name ASC
  LIMIT 1
)
UNION ALL
-- Best movie in Feb 2020 by average rating; tie-break by title ASC
(
  SELECT m.title AS results
  FROM Movies m
  JOIN MovieRating mr ON mr.movie_id = m.movie_id
  WHERE mr.created_at >= '2020-02-01' AND mr.created_at < '2020-03-01'
  GROUP BY m.movie_id, m.title
  ORDER BY AVG(mr.rating) DESC, m.title ASC
  LIMIT 1
);