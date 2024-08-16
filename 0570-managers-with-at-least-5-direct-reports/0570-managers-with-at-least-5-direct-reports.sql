# Write your MySQL query statement below
SELECT A.name
FROM Employee A
JOIN (
    SELECT managerId 
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING COUNT(*)>=5
) AS B

    ON A.id=B.managerId
;