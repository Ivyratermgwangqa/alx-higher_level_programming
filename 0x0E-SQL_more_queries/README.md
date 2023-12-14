Certainly! Here's the modified README.md file with the additional tasks included:

# MySQL More Queries Project

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

### Not My Genre

#### Task 17

Import the database dump from hbtn_0d_tvshows to your MySQL server: [download link](same-as-16-shows_by_genre.sql)

Write a script that uses the `hbtn_0d_tvshows` database to list all genres not linked to the show Dexter.

- The `tv_shows` table contains only one record where `title = Dexter` (but the `id` can be different).
- Each record should display: `tv_genres.name`.
- Results must be sorted in ascending order by the genre name.
- You can use a maximum of two `SELECT` statements.
- The database name will be passed as an argument of the `mysql` command.

```bash
guillaume@ubuntu:~/$ cat 100-not_my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password:
name
Adventure
Comedy
Fantasy
guillaume@ubuntu:~/$
```

#### Repo:

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x0E-SQL_more_queries`
- File: `100-not_my_genres.sql`
- [Get a sandbox](#)

### No Comedy Tonight

#### Task 18

Import the database dump from hbtn_0d_tvshows to your MySQL server: [download link](same-as-100-not_my_genres.sql)

Write a script that lists all shows without the genre Comedy in the database `hbtn_0d_tvshows`.

- The `tv_genres` table contains only one record where `name = Comedy` (but the `id` can be different).
- Each record should display: `tv_shows.title`.
- Results must be sorted in ascending order by the show title.
- You can use a maximum of two `SELECT` statements.
- The database name will be passed as an argument of the `mysql` command.

```bash
guillaume@ubuntu:~/$ cat 101-not_a_comedy.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password:
title
Better Call Saul
Breaking Bad
Dexter
Game of Thrones
Homeland
House
guillaume@ubuntu:~/$
```

#### Repo:

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x0E-SQL_more_queries`
- File: `101-not_a_comedy.sql`
- [Get a sandbox](#)

### Rotten Tomatoes

#### Task 19

Import the database `hbtn_0d_tvshows_rate` dump to your MySQL server: [download link](#)

Write a script that lists all shows from `hbtn_0d_tvshows_rate` by their rating.

- Each record should display: `tv_shows.title - rating sum`.
- Results must be sorted in descending order by the rating.
- You can use only one `SELECT` statement.
- The database name will be passed as an argument of the `mysql` command.

```bash
guillaume@ubuntu:~/$ cat 102-rating_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
Enter password:
title   rating
Better Call Saul    163
Homeland    145
Silicon Valley  82
Game of Thrones 79
Dexter  24
House   21
Breaking Bad    16
The Last Man on Earth   10
The Big Bang Theory 0
New Girl    

 0
guillaume@ubuntu:~/$
```

#### Repo:

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x0E-SQL_more_queries`
- File: `102-rating_shows.sql`
- [Get a sandbox](#)

### Best Genre

#### Task 20

Import the database dump from `hbtn_0d_tvshows_rate` to your MySQL server: [download link](same-as-102-rating_shows.sql)

Write a script that lists all genres in the database `hbtn_0d_tvshows_rate` by their rating.

- Each record should display: `tv_genres.name - rating sum`.
- Results must be sorted in descending order by their rating.
- You can use only one `SELECT` statement.
- The database name will be passed as an argument of the `mysql` command.

```bash
guillaume@ubuntu:~/$ cat 103-rating_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
Enter password:
name    rating
Drama   150
Comedy  92
Adventure   79
Fantasy 79
Mystery 45
Crime   40
Suspense    40
Thriller    40
guillaume@ubuntu:~/$
```

#### Repo:

- GitHub repository: `alx-higher_level_programming`
- Directory: `0x0E-SQL_more_queries`
- File: `103-rating_genres.sql`
- [Get a sandbox](#)

## Conclusion

These SQL scripts cover a range of tasks, from user management to table creation and complex data querying. Each script addresses a specific requirement, contributing to a comprehensive understanding of MySQL concepts in a TV shows database context. Refer to individual scripts for detailed implementations.
