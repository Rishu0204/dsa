# Write your MySQL query statement below
SELECT A.user_id,ROUND(
        COALESCE(SUM(CASE WHEN B.action = 'confirmed' THEN 1 ELSE 0 END), 0) / 
        COUNT(A.user_id), 2
    ) AS confirmation_rate  
FROM Signups  A
LEFT JOIN Confirmations  B
    ON A.user_id=B.user_iD
GROUP BY A.user_id
;