-- Calculate the top 3 cities' average temperatures for July and August
USE hbtn_0c_0;
SELECT city, AVG(temp) as avg_temp
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
