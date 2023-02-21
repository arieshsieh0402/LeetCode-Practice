SELECT
Employee1.name AS Employee
FROM
Employee AS Employee1
JOIN
Employee AS Employee2
ON
Employee1.managerId = Employee2.id
WHERE
Employee1.salary > Employee2.salary
