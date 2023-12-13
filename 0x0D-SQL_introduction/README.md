# SQL Introduction Tasks - Notes

This README.md provides additional notes and explanations for the SQL tasks performed in the "0x0D-SQL_introduction" directory.

## Task 0: List Databases

- **Script**: [0-list_databases.sql](0-list_databases.sql)
- **Description**: Lists all databases on the MySQL server.

## Task 1: Create a Database If Missing

- **Script**: [1-create_database_if_missing.sql](1-create_database_if_missing.sql)
- **Description**: Creates the `hbtn_0c_0` database if it doesn't already exist.

## Task 2: Delete a Database

- **Script**: [2-remove_database.sql](2-remove_database.sql)
- **Description**: Deletes the `hbtn_0c_0` database if it exists.

## Task 3: List Tables

- **Script**: [3-list_tables.sql](3-list_tables.sql)
- **Description**: Lists all tables in a specified database (`mysql` in the example).

## Task 4: First Table

- **Script**: [4-first_table.sql](4-first_table.sql)
- **Description**: Creates a table called `first_table` in the `hbtn_0c_0` database.

## Task 5: Full Table Description

- **Script**: [5-full_table.sql](5-full_table.sql)
- **Description**: Prints the full description of the `first_table` in the `hbtn_0c_0` database.

## Task 6: List All in Table

- **Script**: [6-list_values.sql](6-list_values.sql)
- **Description**: Lists all rows of the `first_table` in the `hbtn_0c_0` database.

## Task 7: First Add

- **Script**: [7-insert_value.sql](7-insert_value.sql)
- **Description**: Inserts a new row with `id = 89` and `name = "Best School"` into `first_table`.

## Task 8: Count 89

- **Script**: [8-count_89.sql](8-count_89.sql)
- **Description**: Displays the number of records with `id = 89` in `first_table`.

## Task 10: List by Best

- **Script**: [10-top_score.sql](10-top_score.sql)
- **Description**: Lists all records of `second_table` in `hbtn_0c_0`, ordered by score.

## Task 11: Select the Best

- **Script**: [11-best_score.sql](11-best_score.sql)
- **Description**: Lists all records with a score >= 10 in `second_table` of the `hbtn_0c_0` database.

## Task 12: Cheating is Bad

- **Script**: [12-no_cheating.sql](12-no_cheating.sql)
- **Description**: Updates the score of Bob to 10 in the `second_table` without using Bob's id value.

## Task 13: Score Too Low

- **Script**: [13-change_class.sql](13-change_class.sql)
- **Description**: Removes all records with a score <= 5 in `second_table` of the `hbtn_0c_0` database.

## Task 14: Average

- **Script**: [14-average.sql](14-average.sql)
- **Description**: Computes the score average of all records in `second_table` of the `hbtn_0c_0` database.

## Task 15: Number by Score

- **Script**: [15-groups.sql](15-groups.sql)
- **Description**: Lists the number of records with the same score in `second_table`, ordered by the number of records.

## Task 16: Say My Name

- **Script**: [16-no_link.sql](16-no_link.sql)
- **Description**: Lists all records of `second_table` in `hbtn_0c_0`, excluding rows without a name value.

## Task 17: Go to UTF8

- **Script**: [100-move_to_utf8.sql](100-move_to_utf8.sql)
- **Description**: Converts the `hbtn_0c_0` database, `first_table`, and the `name` field in `first_table` to UTF8.

## Task 18: Temperatures #0

- **Script**: [101-avg_temperatures.sql](101-avg_temperatures.sql)
- **Description**: Displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

## Task 19: Temperatures #1

- **Script**: [102-top_city.sql](102-top_city.sql)
- **Description**: Displays the top 3 cities' temperatures during July and August, ordered by temperature (descending).

## Task 20: Temperatures #2

- **Script**: [103-max_state.sql](103-max_state.sql)
- **Description**: Displays the max temperature of each state, ordered by state name.

Feel free to explore, modify, and run these scripts to deepen your understanding of SQL and database operations.
