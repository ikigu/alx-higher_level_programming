-- Lists all records of the table second_table
--      Don't list rows without a name value
--      Results should display score and name, in that order
--      Records should be listed in descending by descending score
SELECT score, name FROM second_table
    WHERE name IS NOT NULL
    ORDER BY score DESC;