-- Not Boring Movies
-- https://leetcode.com/problems/not-boring-movies/description/?envType=study-plan-v2&envId=top-sql-50
-- Easy
SELECT * 
FROM Cinema
WHERE id % 2 = 1 and description != "boring"
ORDER BY rating DESC


-- Average Selling Price
-- https://leetcode.com/problems/average-selling-price/description/?envType=study-plan-v2&envId=top-sql-50
-- Easy
SELECT p.product_id, IFNULL(ROUND(SUM(units * price)/SUM(units) , 2), 0)  as average_price 
FROM Prices p
LEFT JOIN UnitsSold u ON u.product_id = p.product_id 
    AND (u.purchase_date >= p.start_date AND u.purchase_date <= p.end_date)
GROUP BY p.product_id



-- Project Employees I
-- https://leetcode.com/problems/project-employees-i/description/?envType=study-plan-v2&envId=top-sql-50
-- Easy
SELECT p.project_id , ROUND(AVG(experience_years), 2) as average_years
FROM Project p
JOIN Employee e
ON p.employee_id = e. employee_id
GROUP BY p.project_id


-- Percentage of Users Attended a Contest
-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/?envType=study-plan-v2&envId=top-sql-50
-- Easy
SELECT r.contest_id, 
    ROUND(COUNT(*) * 100 / (SELECT COUNT(*) FROM Users) , 2) as percentage
FROM Register r
GROUP BY r.contest_id 
ORDER BY percentage DESC, r.contest_id ASC



-- Queries Quality and Percentage
-- https://leetcode.com/problems/queries-quality-and-percentage/description/?envType=study-plan-v2&envId=top-sql-50
-- Easy
SELECT 
    query_name, 
    ROUND(AVG(rating / position), 2) AS quality,  
    ROUND(AVG(rating < 3) * 100, 2) as poor_query_percentage 
FROM Queries 
GROUP BY query_name 



-- Monthly Transactions I
-- https://leetcode.com/problems/monthly-transactions-i/description/?envType=study-plan-v2&envId=top-sql-50
-- Medium
SELECT 
    DATE_FORMAT(trans_date,'%Y-%m') as month,
    country,
    COUNT(*) AS trans_count,
    SUM(state = 'approved') AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM((state = 'approved') * amount) AS approved_total_amount
FROM Transactions 
GROUP BY DATE_FORMAT(trans_date,'%Y-%m'), country


-- Immediate Food Delivery II
-- https://leetcode.com/problems/immediate-food-delivery-ii/description/?envType=study-plan-v2&envId=top-sql-50
-- Medium
SELECT 
    ROUND(AVG(order_date = customer_pref_delivery_date) * 100, 2) as immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT 
        customer_id, 
        MIN(order_date) 
    FROM Delivery 
    GROUP BY customer_id
) 


-- Game Play Analysis IV
-- https://leetcode.com/problems/game-play-analysis-iv/description/?envType=study-plan-v2&envId=top-sql-50
-- Medium
SELECT ROUND(COUNT(*)/ (SELECT COUNT(DISTINCT player_id) FROM Activity a3) , 2) AS fraction
FROM Activity a1
JOIN Activity a2
ON (a1.player_id = a2.player_id AND DATEDIFF(a1.event_date, a2.event_date) = -1)
WHERE (a1.player_id, a1.event_date) IN (
    SELECT player_id, MIN(event_date)
    FROM Activity a4
    GROUP BY player_id
)
-- # 2 key points:
-- # 1: do tính ngày đầu login nên phải có điều kiện WHERE IN MIN (event_date)
-- # 2: với bảng gốc là a1 thì phải SELF JOIN với a2 để lấy các bản ghi có 2 date sát ngày