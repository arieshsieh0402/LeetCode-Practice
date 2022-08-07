SELECT IFNULL(NULL,
              (
                  SELECT DISTINCT Employee.salary
                  FROM Employee
                  ORDER BY Employee.salary DESC LIMIT 1,1)
              
             ) AS SecondHighestSalary;
