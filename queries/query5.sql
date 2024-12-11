-- Query 5: Delete records where the email domain is not from a specific list
DELETE FROM users
WHERE SUBSTRING(email FROM '@(.*)') NOT IN ('gmail.com', 'yahoo.com', 'example.com');
