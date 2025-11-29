-- join subquery
SELECT id, name 
FROM cities
WHERE name = California
ORDER BY cities.id ASC
