-- https://leetcode.com/problems/employee-bonus/description/?envType=study-plan-v2&envId=top-sql-50
SELECT e.name, b.bonus FROM Employee e
LEFT JOIN Bonus b
ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS null



-- https://leetcode.com/problems/average-time-of-process-per-machine/?envType=study-plan-v2&envId=top-sql-50
SELECT A_st.machine_id, ROUND(AVG(A_end.timestamp - A_st.timestamp), 3) as processing_time
FROM Activity A_st
JOIN Activity A_end
ON A_st.machine_id = A_end.machine_id and A_st.process_id = A_end.process_id 
and A_st.activity_type = 'start' and A_end.activity_type = 'end'
GROUP BY A_st.machine_id



-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/?envType=study-plan-v2&envId=top-sql-50
-- Solution 1: NOT IN 
SELECT customer_id, count(*) as count_no_trans FROM Visits V
WHERE visit_id NOT IN (
    SELECT visit_id FROM Transactions
)
GROUP BY customer_id 

--  Solution 2: LEFT JOIN (faster)
SELECT customer_id, count(*) as count_no_trans FROM Visits V
LEFT JOIN Transactions T
ON T.visit_id = V.visit_id
WHERE T.visit_id IS NULL
GROUP BY customer_id


-- https://leetcode.com/problems/product-sales-analysis-i/description/?envType=study-plan-v2&envId=top-sql-50
SELECT product_name, year , price FROM Sales s
INNER JOIN Product p
WHERE s.product_id = p.product_id   


-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/?envType=study-plan-v2&envId=top-sql-50
SELECT unique_id, name FROM Employees
LEFT JOIN EmployeeUNI 
ON Employees.id = EmployeeUNI.id 


-- https://leetcode.com/problems/rising-temperature/?envType=study-plan-v2&envId=top-sql-50
SELECT w1.id as Id FROM Weather w1
JOIN Weather w2
ON DATEDIFF(w1.recordDate, w2.recordDate) = 1 
WHERE w1.temperature  > w2.temperature 


-- https://leetcode.com/problems/students-and-examinations/?envType=study-plan-v2&envId=top-sql-50
SELECT
    s.student_id, s.student_name, sub.subject_name, COUNT(e.student_id) as attended_exams 
FROM Students s
CROSS JOIN Subjects sub 
LEFT JOIN Examinations e ON (e.student_id = s.student_id AND e.subject_name = sub.subject_name) 
GROUP BY s.student_id, sub.subject_name
ORDER BY s.student_id ASC, sub.subject_name ASC


-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/?envType=study-plan-v2&envId=top-sql-50
SELECT name  
FROM Employee e
WHERE e.id IN (
    SELECT managerId
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId 
    HAVING count(*) >= 5
)


-- https://leetcode.com/problems/confirmation-rate/?envType=study-plan-v2&envId=top-sql-50
SELECT 
    s.user_id, 
    IFNULL(ROUND(SUM(c.action='confirmed') / COUNT(s.user_id), 2), 0) AS confirmation_rate 
FROM Signups s
    LEFT JOIN Confirmations c ON s.user_id = c.user_id 
GROUP BY s.user_id 
