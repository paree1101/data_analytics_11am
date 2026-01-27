# What is SQL?

1. SQL stands for Structured Query Language
2. SQL is case-insensitive language
   - Examples: `INSERT` or `insert` or `Insert`
3. SQL is used to create a database and table structure
4. SQL is fast to create structures
5. SQL is a non-procedural based language
6. Join tables
7. Create and store procedures
8. Create a view
9. Create and manage a structured type of data

# Types of SQL Commands or Query

1. **DDL** (Data Definition Language)
2. **DML** (Data Manipulation Language)
3. **DQL** (Data Query Language)
4. **TCL** (Transactional Control Language)

## DDL (Data Definition Language)

1. DDL stands for Data Definition Language
2. Create database and tables structure
3. Used to provide some query
   - Examples: `CREATE`, `ALTER`, `RENAME`, `TRUNCATE`, `DROP`, `CHANGE`

## What is a Database?

> A database is used to store information of users in form of tables.

## What is a Table?

> A table contains rows and columns. They give us a structured data format.

## How to Create a Database

**Syntax:**

```sql
CREATE DATABASE database_name;
```

**Examples:**

```sql
CREATE DATABASE flipcart_db;
CREATE DATABASE amazondb;
```

## How to Create a Table in Database

**Syntax:**

```sql
CREATE TABLE table_name (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255),
    subject VARCHAR(255),
    phone BIGINT,
    comment TEXT
);
```

## Data Types Chart

| Data Type | Description |
|-----------|-------------|
| CHAR | Character string |
| VARCHAR | Variable length character string |
| INT | Integer |
| BIGINT | Big integer |
| FLOAT | Floating point number |
| BLOB | Binary large object |
| DATE | Date |
| DATETIME | Date and time |
| TEXT | Text |
| ENUM | Enumeration |

## Data Type Reference Table

| Column Name | Data Type | Size |
|------------|-----------|------|
| id | INT | default (11) |
| name | CHAR, VARCHAR | (0-255) |
| password | VARCHAR | (0-255) |
| age | INT | - |
| price | INT, FLOAT | - |
| date and time | VARCHAR, DATETIME | - |
| status | VARCHAR | - |
| address | TEXT | - |
| comment | TEXT | - |
| photo, image | VARCHAR, BLOB | - |
| mobile | BIGINT | default (20) |


## ALTER Command

ALTER is used to add, modify and update any column name after creating a table.

### How to Add a New Column in Existing Table

**Syntax:**

```sql
ALTER TABLE table_name ADD column_name datatype(size);
```

### Add a Column After a Particular Column

**Syntax:**

```sql
ALTER TABLE tbl_employee ADD photo VARCHAR(255) AFTER employee_name;
```

### Modify or Update any Column Name

**Syntax:**

```sql
ALTER TABLE tbl_employee CHANGE mobile phone BIGINT;
```

### RENAME Command

RENAME is used to change the name of a table.

**Syntax:**

```sql
RENAME TABLE tbl_employee TO employee;
```
