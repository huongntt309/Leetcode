-- Employees Whose Manager Left the Company
-- https://leetcode.com/problems/employees-whose-manager-left-the-company/description/?envType=study-plan-v2&envId=top-sql-50
-- Easy
SELECT e1.employee_id 
FROM Employees e1
WHERE e1.salary < 30000 AND e1.manager_id  NOT IN (
    SELECT employee_id FROM Employees e2
) 
ORDER BY e1.employee_id 


-- Exchange Seats
-- https://leetcode.com/problems/exchange-seats/description/?envType=study-plan-v2&envId=top-sql-50
-- Medium
SELECT s1.id, IFNULL(s2.student, s1.student) AS student 
FROM Seat s1
    LEFT JOIN Seat s2 
    ON (s1.id % 2 = 1 AND s2.id = s1.id + 1) OR (s1.id % 2 = 0 AND s2.id = s1.id - 1)



-- Movie Rating
-- https://leetcode.com/problems/movie-rating/description/?envType=study-plan-v2&envId=top-sql-50
-- Medium
(SELECT u.name AS results 
FROM MovieRating m
    JOIN Users  u ON m.user_id = u.user_id
GROUP BY m.user_id 
ORDER BY COUNT(rating) DESC, u.name ASC
LIMIT 1)
UNION ALL
(SELECT m.title AS results 
FROM MovieRating mr
    JOIN Movies m ON m.movie_id = mr.movie_id    
WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY mr.movie_id     
ORDER BY AVG(rating * 1.0) DESC, m.title ASC
LIMIT 1)


-- Restaurant Growth
-- https://leetcode.com/problems/restaurant-growth/description/?envType=study-plan-v2&envId=top-sql-50
-- Medium
SELECT DISTINCT
    visited_on ,
    SUM(amount) 
        OVER (ORDER BY visited_on 
            RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) 
        AS amount,
    ROUND(
        (SUM(amount) 
        OVER (ORDER BY visited_on 
            RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW))/7,
        2)        
        AS average_amount
FROM 
    Customer 
LIMIT 10000
OFFSET 6


-- Friend Requests II: Who Has the Most Friends
-- https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description/?envType=study-plan-v2&envId=top-sql-50
-- Medium
SELECT id, COUNT(*) as num
FROM 
(
    (SELECT requester_id AS id
    FROM RequestAccepted)
UNION ALL
    (SELECT accepter_id AS id
    FROM RequestAccepted)
) as union_table
GROUP BY id
ORDER BY num DESC
LIMIT 1


-- Investments in 2016
-- https://leetcode.com/problems/investments-in-2016/description/?envType=study-plan-v2&envId=top-sql-50
-- Medium
SELECT ROUND(SUM(tiv_2016), 2) as tiv_2016  FROM Insurance
WHERE (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance 
    GROUP BY concat(lat, '_', lon)
    HAVING COUNT(*) = 1
) AND tiv_2015 IN (
    SELECT tiv_2015 FROM Insurance
    GROUP BY tiv_2015 
    HAVING COUNT(*) > 1
)



-- Department Top Three Salaries
-- https://leetcode.com/problems/department-top-three-salaries/description/?envType=study-plan-v2&envId=top-sql-50
-- Hard
SELECT 
    d.name as Department ,
    e.name as Employee ,
    e.salary as Salary ,
    DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) as rank_sl
FROM Employee e
JOIN Department d ON e.departmentId = d.id AND rank_sl <=3
    

