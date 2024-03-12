-- Lists all records of second_table if score >= 10
-- Results display both score and name, in that order
-- Records are are order by score, top first
SELECT score, name FROM second_table WHERE SCORE >= 10 ORDER BY score DESC;