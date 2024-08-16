# Write your MySQL query statement below
SELECT B.contest_id,ROUND((COUNT(B.user_id)/(SELECT COUNT(*) FROM Users)*100),2) AS percentage 
FROM Users AS A
LEFT JOIN Register AS B
    ON A.user_id =B.user_id 
WHERE B.contest_id IS NOT NULL
GROUP BY B.contest_id 
ORDER BY percentage DESC,B.contest_id 
;