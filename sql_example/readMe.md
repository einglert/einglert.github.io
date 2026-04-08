---
date: 8 April 2026
author: Eric Inglert
title: Quickstart Guide to SQLite Database
output: html_document
---

Pandoc this file to html: ```pandoc -c "https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" -f markdown readMe.md -so readMe.html```

## Overview of Workflow

1. Create directory
1. Create/Open database ```sqlite3 mydatabase.db```
1. Create table ```CREATE TABLE students (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT NOT NULL, last_name TEXT NOT NULL, grade REAL); ```
1. Verify table ```.tables```
1. Verify schema ```.schema students```
1. Insert data ```INSERT INTO students (first_name, last_name, grade) VALUES ('Eric', 'Inglert', 'A-');```
1. View data ```SELECT * FROM students;```

## Useful sql commands

* Quit ```.quit```
* Read input from FILE ```.read FILE```
* Display output of next command in browser ```.www```
* Display output of next command in spreadsheet ```.excel```
* Remove table ```DROP TABLE table_name;```
* Insert table data ```INSERT INTO table_name (column1, column2, column3) VALUES (value1, value2, value3);```
* Remove table data ```DELETE FROM table_name WHERE id=42;```
* Create database from CSV data with header ```.mode csv``` then ```.import create.csv table_new```
* Import CSV data ```.mode csv``` then ```.import --skip 1 filename.csv table_name```
* Search on data ```SELECT * FROM table_name WHERE column_name = "name1";```
