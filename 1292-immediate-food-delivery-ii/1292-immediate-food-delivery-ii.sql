# Write your MySQL query statement below
SELECT ROUND( SUM( CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END)*100/COUNT(*),2) AS immediate_percentage
FROM(
    SELECT A.*
    FROM Delivery A
    JOIN(
        SELECT customer_id,MIN(order_date ) AS first_day
        FROM Delivery 
        GROUP BY customer_id 
    ) B
        ON A.customer_id =B.customer_id AND A.order_date = B.first_day
) immediate