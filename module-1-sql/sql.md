# what is SQL?
1. sql stands for structured query language 
2. sql is case-insensitive language
    examples:
    ```
    inset or INSERT or Insert
    ```
3. sql is used to create a database | table structure
4. sql is fast to create structures
5. sql is no-procedural based language
6. join tables
7. create and store procedures 
8. create a view
9. create and manage a structured type of data

# types of sql commands or query 
1. DDL (data definition language)
2. DML (data manipulation langauge)
3. DQL (data query language)
4. TCL (transactional control langauge)

## DDL 
1. DDL stands for data definition langaue
2. create database and tables structure
3. used to provide some query
    examples: create, alter, rename, truncate, drop, change

## what is a database
```
A database is used to store information of users in form of tables. 
```

## what is a table 
```
A table contains rows and columns. They give us a structured data format
```

1. how to create a database
    **syntax**
    ```
    create database name;
    example: create database flipcart_db
            or create database amazondb
    ```

2. how to create a table in database
    **syntax**
    ```
    (id datatype(size) primary key auto_increment
    name datatype(size)
    email datatype(size)
     password datatype(size)
     subject varchar (255)
     phone bigINT
     comment text
     )
    create table name;
    example: create database flipcart_db
            or create database amazondb
    ```

## chart of tables of data types
1. char
2. varchar
3. int
4. bigINT
5. float
6. blob
7. data
8. datetime
9. text 
10. enum