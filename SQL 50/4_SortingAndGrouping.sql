-- Number of Unique Subjects Taught by Each Teacher
-- https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/?envType=study-plan-v2&envId=top-sql-50
-- Easy
SELECT  teacher_id, COUNT(DISTINCT subject_id) AS cnt
FROM Teacher 
GROUP BY teacher_id


-- User Activity for the Past 30 Days I
-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/description/?envType=study-plan-v2&envId=top-sql-50
-- Easy
SELECT activity_date as day, COUNT(DISTINCT user_id) as active_users 
FROM Activity
WHERE activity_date BETWEEN DATE('2019-07-27') - INTERVAL 29 DAY AND '2019-07-27'
GROUP BY activity_date


-- Product Sales Analysis III
-- https://leetcode.com/problems/product-sales-analysis-iii/description/?envType=study-plan-v2&envId=top-sql-50
-- Medium
SELECT product_id, year as first_year , quantity, price 
FROM Sales
WHERE (product_id, year) IN (
    SELECT product_id, min(year)
    FROM Sales 
    GROUP BY product_id 
)


-- Classes More Than 5 Students
-- https://leetcode.com/problems/classes-more-than-5-students/description/?envType=study-plan-v2&envId=top-sql-50
-- Easy
SELECT class
FROM Courses 
GROUP BY class    
HAVING COUNT(student) >= 5


-- Find Followers Count
-- https://leetcode.com/problems/find-followers-count/description/?envType=study-plan-v2&envId=top-sql-50
-- Easy
SELECT  user_id, COUNT(*) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id ASC


-- Biggest Single Number
-- https://leetcode.com/problems/biggest-single-number/description/?envType=study-plan-v2&envId=top-sql-50
-- Easy
SELECT IFNULL(max(num), NULL) as num
FROM MyNumbers
WHERE num IN (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING count(num) = 1
) 


-- Customers Who Bought All Products
-- https://leetcode.com/problems/customers-who-bought-all-products/description/?envType=study-plan-v2&envId=top-sql-50
-- Medium
SELECT customer_id
FROM Customer
GROUP BY customer_id 
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product)