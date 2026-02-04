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

### TRUNCATE Command

Truncate is used to remove or delete all data from tables.

**Note:** After truncate, data cannot be rolled back.

**Syntax:**

```sql
TRUNCATE TABLE tablename;
```

### DROP Command

DROP is used to delete database and table structures.

**Syntax to drop a database:**

```sql
DROP DATABASE databasename;
```

**Syntax to drop a table:**

```sql
DROP TABLE tablename;
```

## DML (Data Manipulation Language)

DML is used to manipulate data; insert or delete or update data in a table.

### 1. INSERT Data

#### Single Data Insert

**Syntax:**

```sql
INSERT INTO tablename (columnname) VALUES('value');
```

**Example:**

```sql
INSERT INTO users (name, email, password)
VALUES('viva', 'viva@gmail.com', 2345);
```

#### Multiple Data Insert

**Syntax:**

```sql
INSERT INTO tablename (columnname) VALUES('value1'), ('value2'), ('value3');
```

**Example:**

```sql
INSERT INTO users (name, email, password)
VALUES('jolyn', 'jolyn@gmail.com', 2345), ('hiya', 'hiya@gmail.com', 3422);
```

### 2. DELETE Data

#### Delete All Data

```sql
DELETE FROM users;
```

#### Delete Particular Data

```sql
DELETE FROM users WHERE id=4;
```

#### Delete a Range of Data

```sql
DELETE FROM users WHERE id BETWEEN 1 AND 3;
```

#### Delete Multiple Data in Random Order

```sql
DELETE FROM users WHERE id IN (3, 4, 8, 9, 13);
```

### 3. UPDATE Data

```sql
UPDATE users SET name = 'preeti', email = 'preeti@gmail.com', password = '6565' WHERE id=3;
```

## DQL (Data Query Language)

DQL is used to fetch or select data from tables.

### SELECT Statement

#### Select All Data

```sql
SELECT * FROM users;
```

#### Select Particular Column

```sql
SELECT id, name FROM users;
```

#### Select Particular Row with ID

```sql
SELECT * FROM users WHERE id=1;
```

#### Select Data in a Range

```sql
SELECT * FROM users WHERE id BETWEEN 1 AND 100;
```

#### Select Data Using IN Operator

```sql
SELECT * FROM users WHERE id IN (1, 3);
```

#### Select Data Using LIMIT

```sql
SELECT * FROM users LIMIT 0, 2;
```

#### Select Data in Ascending or Descending Order

```sql
SELECT * FROM users ORDER BY name ASC;
```

```sql
SELECT * FROM users ORDER BY name DESC;
```

```sql
SELECT * FROM users ORDER BY name;
```

Note: By default, data comes in ascending order.

#### Searching for Data Starting with a Particular Character

**Search data starting with 'p':**

```sql
SELECT * FROM users WHERE name LIKE 'p%';
```

**Search data ending with 'e':**

```sql
SELECT * FROM users WHERE name LIKE '%e';
```

**Search data containing 'a' anywhere:**

```sql
SELECT * FROM users WHERE name LIKE '%a%';
```

### SQL Functions

#### 1. Aggregate Functions

- COUNT
- SUM
- MAX
- MIN
- AVG

#### 2. Scalar Functions

- FIRST (supported in Oracle, not in MySQL)
- LAST (supported in Oracle, not in MySQL)
- LCASE
- UCASE

### Aggregate Function Queries

```sql
SELECT MAX(salary) AS highest_salary FROM employee;

SELECT MIN(salary) AS lowest_salary FROM employee;

SELECT COUNT(employee_id) AS total_employees FROM employee;

SELECT SUM(salary) AS total_salary FROM employee;

SELECT AVG(salary) AS avg_salary FROM employee;
```

### Scalar Function Queries

```sql
SELECT FIRST(employee_name) FROM employee;

SELECT LAST(employee_name) FROM employee;

SELECT UCASE(employee_name) FROM employee;

SELECT LCASE(employee_name) FROM employee;
```

## Subquery in SQL

A subquery is a query within another query.

**Example:**

```sql
SELECT MAX(salary) AS second_highest_salary FROM employee WHERE salary < (SELECT MAX(salary) FROM employee);
```

## TCL : Transactional query langaue 
1. commit:
   commit will be used to save any data after delete 
   **query**
   ```
   start transaction;
   delete from users where where id=3;
   commit;
   ```

2. rollback:
   after deleting a data using commit, rollback allows you to bring it back
   **query**
   ```
   start transaction;
   select * from users where where id=3;
   rollback;
   ```
   
   **note** rollback only supported in oracle, not in mysql


## Normalisation i SQL
   1. Normalisation is used to remove redundancy (duplicate) data format from tables
   2. It's used to provide relationship between one table to another table 
   3. It's used to create a normalised format of any table 

## Types of normalisation 
   1. 1-NF (First normalised form)
   2. 2-NF
   3. 3-NF
   4. 4-NF 
   5. 5-NF

## Create 1-NF
Basic information about a table with primary key
| user_id (pk) | Email           | Age | Salary   | Department |
|--------------|-----------------|-----|----------|------------|
| 1            | paree@gmail.com | 19  | 1000000 | IT         |

## Create 2-NF
shows relation between one table and another using foregin key

tbl_city
| city_id (pk) | city_name       |
|--------------|-----------------|
| 1            |Rajkot           |
| 2            |Dubai            |
| 3            |San Dieago       |

tbl_customer
| user_id (pk) | Email           | Age | Salary   | city_id (fk) |
|--------------|-----------------|-----|----------|--------------|
| 1            | paree@gmail.com | 19  | 1000000  | 2            |
| 2            | madhav@gmail.com | 41  | 5000000 | 3            |

**how to add foreign key**
CREATE table tbl_city
(city_id int primary key AUTO_INCREMENT,
 city_name varchar(255)
 )

CREATE table tbl_customers
(customer_id int primary key AUTO_INCREMENT,
   name varchar(255)
   email varchar(255)
   age INT
   salary INT
   city_id int REFERENCES tbl_city(city_id))

**connect both using the relation tool found in table of customer**


## Create 3-NF
shows relation between one table and another or more than 1 table using foregin key

tbl_country
| country_id (pk) | country_name       |
|--------------|-----------------------|
| 1            |UAE                    |
| 2            |USA                    |
| 3            |India                  |

tbl_state
| state_id (pk) | state_name       |
|--------------|-------------------|
| 1            |California         |
| 2            |Gujarat            |
| 3            |Gulf               |

tbl_city
| city_id (pk) | city_name       |
|--------------|-----------------|
| 1            |Rajkot           |
| 2            |Dubai            |
| 3            |San Dieago       |

tbl_customer
| user_id (pk) | Email           | Age | Salary   | city_id (fk) | state_id (fk) | country_id (fk)|
|--------------|-----------------|-----|----------|--------------|---------------|----------------|
| 1            | paree@gmail.com | 19  | 1000000  | 2            |
| 2            | madhav@gmail.com | 41  | 5000000 | 3            |



**how to add foreign key**

must add relation by going into structure tab (change all to cascade)

## Types of SQL Join 
1. inner join
2. join
3. outer join 
   a. left join
   b. right join
   c. full join 
4. cross join 

***inner join***
in customer table you want to add city name from city table

```
select tbl_customers. * , city_name from tbl_customers inner join tbl_city on tbl_customers.city_id=tbl_city.city_id
```
want to add multiple table columns into customer table:
```
select tbl_customers. * , countryname, statename, cityname from tbl_customers inner join tbl_country on tbl_customers.country_id=tbl_country.country_id inner join tbl_state on tbl_customers.state_id=tbl_state.state_id inner join tbl_city on tbl_customers.city_id=tbl_city.city_id
```

can even simply use join:
```
select tbl_customers. * , countryname, statename, cityname from tbl_customers  join tbl_country on tbl_customers.country_id=tbl_country.country_id  join tbl_state on tbl_customers.state_id=tbl_state.state_id join tbl_city on tbl_customers.city_id=tbl_city.city_id
```

if don't want to include city_id and all then don't use *
```
select tbl_customers. customer_name, email, phone , countryname, statename, cityname from tbl_customers inner join tbl_country on tbl_customers.country_id=tbl_country.country_id inner join tbl_state on tbl_customers.state_id=tbl_state.state_id inner join tbl_city on tbl_customers.city_id=tbl_city.city_id
```

**left join**

left join is used to join the first table of left rows to second table of left rows if data matches then join otherwise return null
```
select tbl_customers. * , countryname, statename, cityname from tbl_customers left join tbl_country on tbl_customers.country_id=tbl_country.country_id left join tbl_state on tbl_customers.state_id=tbl_state.state_id left join tbl_city on tbl_customers.city_id=tbl_city.city_id
```


**right join**

right join is used to join the second table of left rows to first table of right rows if data matches then join otherwise return null

```
select tbl_customers. * , countryname, statename, cityname from tbl_customers right join tbl_country on tbl_customers.country_id=tbl_country.country_id right join tbl_state on tbl_customers.state_id=tbl_state.state_id right join tbl_city on tbl_customers.city_id=tbl_city.city_id
```

**full join**
full join = left join + right join 
full join is not supported by mySQL

**cross join**
cross join is used to join more than one table and return duplicate of data

***unique key***

ALTER table 'tbl_employee' ADD UNIQUE('email')