-- The Number of Employees Which Report to Each Employee
-- https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description/?envType=study-plan-v2&envId=top-sql-50
-- Easy
SELECT e2.employee_id, e2.name, 
    COUNT(*) as reports_count,  
    ROUND(AVG(e1.age)) as average_age 
FROM Employees e1
JOIN Employees e2
ON e1.reports_to = e2.employee_id
GROUP BY e1.reports_to
ORDER BY e2.employee_id


-- Primary Department for Each Employee
-- https://leetcode.com/problems/primary-department-for-each-employee/description/?envType=study-plan-v2&envId=top-sql-50
-- Easy
--
(
    SELECT employee_id, department_id 
    FROM Employee
    WHERE primary_flag = 'Y'
)
UNION
(
    SELECT employee_id, department_id 
    FROM Employee
    GROUP BY employee_id 
    HAVING COUNT(department_id) = 1
)



-- Triangle Judgement
-- https://leetcode.com/problems/triangle-judgement/description/?envType=study-plan-v2&envId=top-sql-50
-- Easy
SELECT *, IF(x+y>z and z+y>x and x+z>y, "Yes", "No") as triangle
FROM Triangle


-- Consecutive Numbers
-- https://leetcode.com/problems/consecutive-numbers/description/?envType=study-plan-v2&envId=top-sql-50
-- Medium
SELECT DISTINCT
    l1.Num AS ConsecutiveNums
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num


-- Product Price at a Given Date
-- https://leetcode.com/problems/product-price-at-a-given-date/description/?envType=study-plan-v2&envId=top-sql-50
-- Medium
SELECT
  product_id,
  10 AS price
FROM
  Products
GROUP BY
  product_id
HAVING
  MIN(change_date) > '2019-08-16'
UNION ALL

SELECT product_id, IFNULL(new_price, 10)
FROM Products
WHERE (product_id, change_date) IN (
    SELECT
        product_id,
        MAX(change_date)
    FROM Products 
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
)


-- Last Person to Fit in the Bus
-- https://leetcode.com/problems/last-person-to-fit-in-the-bus/description/?envType=study-plan-v2&envId=top-sql-50
-- Medium
SELECT
    person_name 
FROM (
    SELECT
        person_name,
        SUM(weight) OVER (ORDER BY turn) as Total_Weight
    FROM Queue
) as slide_table
WHERE Total_Weight <= 1000
ORDER BY Total_Weight DESC
LIMIT 1



-- Count Salary Categories
-- https://leetcode.com/problems/count-salary-categories/description/?envType=study-plan-v2&envId=top-sql-50
-- Medium
(select 
"Low Salary" as category,
(select count(*)  from Accounts where income < 20000) as accounts_count)
union all
(select 
"Average Salary" as category,
(select count(*) from Accounts where income >= 20000 and income <= 50000) as accounts_count)
union all 
(select 
"High Salary" as category,
(select count(*) from Accounts where income > 50000) as accounts_count)
