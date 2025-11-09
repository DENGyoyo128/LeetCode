# Write your MySQL query statement below
SELECT user_id, name, mail
FROM Users
WHERE mail LIKE '%@leetcode.com'                               -- 结尾域名
  AND LEFT(mail, 1) REGEXP '^[A-Za-z]$'                        -- 首字符是字母
  AND SUBSTRING_INDEX(mail, '@', 1) REGEXP '^[A-Za-z0-9_.-]+$'