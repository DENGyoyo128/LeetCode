# Write your MySQL query statement below
select u.name as results 
from movieRating m
left join Users u on u.user_id=m.user_id
where rating =(select max(rating) from MovieRating)
union 
(select v.title
from movieRating m
left join Movies v on v.movie_id=m.movie_id
where created_at like "2020-02%" 
group by  m.movie_id 
order by avg(m.rating) desc , v.title asc
limit 1)
