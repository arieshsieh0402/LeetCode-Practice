SELECT firstName, lastName, city, state
FROM Person
LEFT JOIN Address ON Person.PersonId = Address.PersonId;


--URL:https://leetcode.com/problems/combine-two-tables/
