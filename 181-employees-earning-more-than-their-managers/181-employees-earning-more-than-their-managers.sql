# Write your MySQL query statement below
SELECT e.name as Employee
From Employee e, Employee m
WHERE e.managerID is not NULL and e.managerID = m.id and e.salary > m.salary