-- Query 4: Find the user(s) with the most common email domain
WITH domain_counts AS (
    SELECT
        split_part(email, '@', 2) AS domain,
        COUNT(*) AS domain_count
    FROM users
    GROUP BY split_part(email, '@', 2)
)
SELECT u.*
FROM users u
JOIN domain_counts d
    ON split_part(u.email, '@', 2) = d.domain
WHERE d.domain_count = (SELECT MAX(domain_count) FROM domain_counts);
