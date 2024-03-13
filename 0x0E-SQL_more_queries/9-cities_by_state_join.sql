-- list all cities in hbtn_0d_usa
--      sort results in ascending order by cities.id
--      use only one select statement
SELECT cities.id, cities.name, states.name FROM cities
  JOIN states ON cities.state_id = states.id
 ORDER BY cities.id;
