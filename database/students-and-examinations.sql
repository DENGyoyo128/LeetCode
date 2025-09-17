# Write your MySQL query statement below
-- select e.student_id,s.student_name,e.subject_name,count(subject)
-- from examinations e
-- left join students s on s.student_id=e.student_id

SELECT
  s.student_id,
  s.student_name,
  sub.subject_name,
  COUNT(e.subject_name) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e
  ON e.student_id = s.student_id
 AND e.subject_name = sub.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name
ORDER BY s.student_id, sub.subject_name;
