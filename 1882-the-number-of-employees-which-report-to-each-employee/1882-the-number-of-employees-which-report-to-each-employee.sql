# Write your MySQL query statement below
SELECT B.employee_id , B.name, 
COUNT(A.reports_to) reports_count,
ROUND(AVG(A.age)) average_age 
FROM Employees A
JOIN Employees B
    ON A.reports_to =B.employee_id 
GROUP BY B.employee_id,B.name 
ORDER BY B.employee_id;