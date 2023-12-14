-- Lists all cities in the database hbtn_0d_usa along with their respective state names.
SELECT cities.id, cities.name, states.name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id;
