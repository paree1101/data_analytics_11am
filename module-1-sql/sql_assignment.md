# SQL Assignment

## Question 1: Create Contact Table

```sql
CREATE TABLE Contact(
    ContactID INT PRIMARY KEY AUTO_INCREMENT,
    CompanyID INT,
    FirstName VARCHAR(45),
    LastName VARCHAR(45),
    Street VARCHAR(45),
    City VARCHAR(45),
    State VARCHAR(2),
    Zip VARCHAR(10),
    IsMain Boolean,
    Email VARCHAR(45),
    Phone VARCHAR(12)
);
```

## Question 2: Create Employee Table

```sql
CREATE TABLE Employee(
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(45),
    LastName VARCHAR(45),
    Salary Decimal(10,2),
    HireDate Date,
    JobTitle VARCHAR(25),
    Email VARCHAR(45),
    Phone VARCHAR(12)
);
```

## Question 3: Create ContactEmployee Table

```sql
CREATE TABLE ContactEmployee ( 
    ContactEmployeeID INT PRIMARY KEY AUTO_INCREMENT, 
    ContactID INT, 
    EmployeeID INT, 
    ContactDate Date, 
    Description VARCHAR(100) 
);
```

## Question 4: Update Employee Phone Number

Update Lesley Bland's phone number to 2155558800.

```sql
UPDATE Employee 
SET phone = '2155558800' 
WHERE FirstName = 'Lesley' AND LastName = 'Bland';
```

## Question 5: Update Company Name

Update Company_tbl to change 'Urban Outfitters, Inc.' to 'Urban Outfitters'.

```sql
UPDATE Company_tbl 
SET CompanyName = 'Urban Outfitters' 
WHERE CompanyName = 'Urban Outfitters, Inc.';
```

## Question 6: Delete Contact Event

Remove Dianne Connor's contact event with Jack Lee from the ContactEmployee table.

```sql
DELETE FROM ContactEmployee 
WHERE ContactID = (SELECT ContactID FROM Contact WHERE FirstName = 'Dianne' AND LastName = 'Connor') 
AND EmployeeID = (SELECT EmployeeID FROM Employee WHERE FirstName = 'Jack' AND LastName = 'Lee');
```

## Question 7: Select Employee Names

Display the names of employees that have contacted Toll Brothers.

```sql
SELECT FirstName, LastName 
FROM Employee;
```

## Question 8: LIKE Operator with % and _

The `%` and `_` are wildcard operators used with the LIKE statement to search for patterns in text.

**Examples:**

### Find names starting with 'J'

```sql
SELECT * FROM Employee WHERE FirstName LIKE 'J%';
```

**Results:** Jack, Joanne, James, etc.

### Find names ending with 'e'

```sql
SELECT * FROM Contact WHERE LastName LIKE '%e';
```

**Results:** Dianne, Jake, James, etc.

### Find names containing 'a' anywhere

```sql
SELECT * FROM Employee WHERE FirstName LIKE '%a%';
```

**Results:** James, Frank, Sarah, Jack, etc.