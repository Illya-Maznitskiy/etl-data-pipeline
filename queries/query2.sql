-- Query 2: List all unique email domains present in the database
SELECT DISTINCT SUBSTRING(email FROM '@(.*)') AS domain
FROM users;
