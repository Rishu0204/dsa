# Write your MySQL query statement below
WITH SUMWEIGHT AS(
    SELECT person_name , weight ,turn ,
        SUM(weight) OVER (ORDER BY turn) AS sumweights
    FROM Queue
)

SELECT person_name 
FROM SUMWEIGHT
WHERE sumweights <=1000
ORDER BY sumweights DESC
LIMIT 1;




