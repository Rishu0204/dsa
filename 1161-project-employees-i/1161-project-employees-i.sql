# Write your MySQL query statement below
SELECT A.project_id , ROUND(SUM(B.experience_years)/COUNT(A.project_id),2) AS average_years 
FROM Project AS A
LEFT JOIN Employee AS B
    ON A.employee_id =B.employee_id 
GROUP BY A.project_id 
;