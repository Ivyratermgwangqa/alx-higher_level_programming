-- Calculate the max temperature for each state
USE hbtn_0c_0;
SELECT state, MAX(temp) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
