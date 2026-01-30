1. CREATE TABLE Contact(
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

2. CREATE TABLE Employee(
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(45),
    LastName VARCHAR(45),
    Salary Decimal(10,2),
    HireDate Date,
    JobTitle VARCHAR(25),
    Email VARCHAR(45),
    Phone VARCHAR(12)
    );

3. CREATE TABLE ContactEmployee ( 
    ContactEmployeeID INT PRIMARY KEY AUTO_INCREMENT, 
    ContactID INT, 
    EmployeeID INT, 
    ContactDate Date, 
    Description VARCHAR(100) 
    );

4. UPDATE Employee SET phone = '2155558800' WHERE FirstName = 'Lesley' and LastName = 'Bland';

5. UPDATE Company_tbl SET CompanyName = 'Urban Outfitters' WHERE CompanyName = 'Urban Outfitters, Inc.';

6. DELETE FROM ContactEmployee WHERE ContactID = (SELECT ContactID FROM Contact WHERE FirstName = 'Dianne' AND LastName = 'Connor') 
AND EmployeeID = (SELECT EmployeeID FROM Employee WHERE FirstName = 'Jack' AND LastName = 'Lee');

7. SELECT FirstName, LastName FROM Employee

8. The % and _ are  operators used with the LIKE statement to search for patterns in text:
    examples: 
    -- Find names starting with 'J'
SELECT * FROM Employee WHERE FirstName LIKE 'J%';
-- Results: Jack, Joanne, James, etc.

-- Find names ending with 'e'
SELECT * FROM Contact WHERE LastName LIKE '%e';
-- Results: Dianne, Jake, James, etc.

-- Find names containing 'a' anywhere
SELECT * FROM Employee WHERE FirstName LIKE '%a%';
-- Results: James, Frank, Sarah, Jack, etc.