-- Retrieve rows from second_table where name is not null, ordered by score descending
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
