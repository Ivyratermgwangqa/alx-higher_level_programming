# MySQL More Queries Project

```markdown

This project is designed to enhance your understanding of MySQL, focusing on various topics such as user management, privileges, constraints, and advanced SQL techniques. The learning objectives include creating and managing users, understanding primary and foreign keys, using constraints, retrieving data from multiple tables, and employing advanced SQL techniques like joins and unions.

## Prerequisites

- Ubuntu 20.04 LTS
- MySQL 8.0 (version 8.0.25)

## Installation

To install MySQL 8.0 on Ubuntu 20.04 LTS, use the following commands:

```bash
$ sudo apt update
$ sudo apt install mysql-server
$ mysql --version
```

Connect to your MySQL server:

```bash
$ sudo mysql
```

To run MySQL in a container, use "container-on-demand" with the credentials `root/root`. Connect via SSH or Web terminal.

Start MySQL in the container:

```bash
$ service mysql start
```

## Usage
```
- Execute SQL queries using allowed editors: vi, vim, emacs.
- Ensure all SQL queries have a comment just before the syntax.
- Start your SQL files with a comment describing the task.
- Use uppercase for all SQL keywords (SELECT, WHERE, etc.).
- Include a README.md file at the root of the project folder.
```
## Examples

To list the first three students in Batch ID=3, use the following SQL query:

```sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

## Database Interaction

To list databases in MySQL, use the following command:

```bash
$ cat 0-list_databases.sql | mysql -uroot -p
```

To import a SQL dump, create a database and run the following commands:

```bash
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
```

Replace `hbtn_0d_tvshows` with your desired database name.

## Learning Objectives
```
By the end of this project, you should be able to:

- Create a new MySQL user
- Manage privileges for a user to a database or table
- Understand PRIMARY KEY and FOREIGN KEY
- Use NOT NULL and UNIQUE constraints
- Retrieve data from multiple tables in one request
- Work with subqueries, JOIN, and UNION in SQL
```

## Overview

This project focuses on MySQL database management tasks, encompassing user privilege management, table creation, and complex data querying. The tasks are designed to reinforce understanding of MySQL concepts such as user management, table design, and the execution of intricate queries involving joins and subqueries.

## Table of Contents

1. [Privileges](#privileges)
2. [Root User](#root-user)
3. [Read User](#read-user)
4. [Always a Name](#always-a-name)
5. [ID Can't Be Null](#id-cant-be-null)
6. [Unique ID](#unique-id)
7. [States Table](#states-table)
8. [Cities Table](#cities-table)
9. [Cities of California](#cities-of-california)
10. [Cities by States](#cities-by-states)
11. [Genre ID by Show](#genre-id-by-show)
12. [Genre ID for All Shows](#genre-id-for-all-shows)
13. [No Genre](#no-genre)
14. [Number of Shows by Genre](#number-of-shows-by-genre)
15. [My Genres](#my-genres)
16. [Only Comedy](#only-comedy)
17. [List Shows and Genres](#list-shows-and-genres)
18. [Not My Genre](#not-my-genre)
19. [No Comedy Tonight](#no-comedy-tonight)
20. [Rotten Tomatoes](#rotten-tomatoes)
21. [Best Genre](#best-genre)

## Privileges

### Task 0

The script displays the privileges of MySQL users `user_0d_1` and `user_0d_2` on the local server.

### Task 1

This script creates the MySQL server user `user_0d_1`.

### Task 2

The script creates the database `hbtn_0d_2` and the user `user_0d_2`.

### Task 3

This script creates the table `force_name` on the MySQL server.

### Task 4

The script creates the table `id_not_null` on the MySQL server.

### Task 5

This script creates the table `unique_id` on the MySQL server.

### Task 6

It creates the database `hbtn_0d_usa` and the table `states` within it.

### Task 7

This script creates the database `hbtn_0d_usa` and the table `cities` within it.

### Task 8

The script lists all cities of California from the database `hbtn_0d_usa`.

### Task 9

This script lists all cities in the database `hbtn_0d_usa` along with their respective state names.

### Task 10

It lists all shows in `hbtn_0d_tvshows` that have at least one linked genre.

### Task 11

The script lists all shows in the database `hbtn_0d_tvshows` along with their respective genre IDs.

### Task 12

This script lists all shows in `hbtn_0d_tvshows` without a linked genre.

### Task 13

It lists all genres from `hbtn_0d_tvshows` along with the number of linked shows for each genre.

### Task 14

This script lists all genres of the show "Dexter" from the `hbtn_0d_tvshows` database.

### Task 15

It lists all Comedy shows in the `hbtn_0d_tvshows` database.

### Task 16

This script lists all shows and their linked genres from the `hbtn_0d_tvshows` database.
Certainly! Below is the continuation of the README with the descriptions for the specified tasks:

### Task 17
This script lists all genres not linked to the show "Dexter" in the `hbtn_0d_tvshows` database.

### Task 18
It lists all shows in the `hbtn_0d_tvshows` database without the Comedy genre.

### Task 19
This script lists all shows from the `hbtn_0d_tvshows_rate` database by their ratings.

### Task 20
It lists all genres in the `hbtn_0d_tvshows_rate` database by their ratings.

## Conclusion

These SQL scripts cover a range of tasks, from user management to table creation and complex data querying. Each script addresses a specific requirement, contributing to a comprehensive understanding of MySQL concepts in a TV shows database context. Refer to individual scripts for detailed implementations.
