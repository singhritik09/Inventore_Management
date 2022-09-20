CREATE TABLE department(
	pid int PRIMARY KEY,
    pname varchar(25),
    location varchar(25)
);

INSERT INTO department VALUES('10','Marketing','Bangalore');
INSERT INTO department VALUES('11','Sales','Bangalore');
INSERT INTO department VALUES('12','Operation','Bangalore');
INSERT INTO department VALUES('13','Product','Bangalore');
INSERT INTO department VALUES('14','Admin','Bangalore');


CREATE TABLE managers(
  id int,
  name varchar(25),
  phone int,
  FOREIGN KEY(id) REFERENCES Employee(id)
);


INSERT INTO managers VALUES('10','Rohan','9782134532')
INSERT INTO managers VALUES('1','Shivam','9782134551');
INSERT INTO managers VALUES('2','Saiyam','9843245331');

CREATE TABLE Inventory(
  inid int PRIMARY KEY,
  name varchar(100),
  cost int,
  quantity int,
  quantity_sold int,
  sales int,
  stock_date date,
  last_sale date
);


INSERT INTO Inventory VALUES('1','Shoes','100','10','5','500','2022-04-02');
INSERT INTO Inventory VALUES('2','Glasses','300','10','4','600','2022-04-02');
INSERT INTO Inventory VALUES('3','Watch','150','10','5','750','2022-04-02');
INSERT INTO Inventory VALUES('4','Wallet','100','10','5','500','2022-04-02');
INSERT INTO Inventory VALUES('5','Shirt','200','10','4','800','2022-04-02');

--EMPLOYEE TABLE WILL HAVE TWO FOREIGN KEYS ONE FROM DEPARTMENT AND ONE FROM MANAGERS
 
CREATE TABLE employee(
  id int PRIMARY KEY,
  name varchar(25),
  aadhar int,
  email varchar(25),
  phone int,
  address varchar(50),
  mid int,
  did int,
  FOREIGN KEY(mid) REFERENCES managers(mid) ON DELETE CASCADE,
  FOREIGN KEY(did) REFERENCES department(pid) ON DELETE CASCADE
	
);



INSERT INTO employee VALUES('1','Rohan Singh','144412','rohan@gmail.com','9943433221','Ranchi','10','10');
INSERT INTO employee VALUES('2','Saiyam','141412','sj@gmail.com','9743433221','Banglaore','12','11');
INSERT INTO employee VALUES('3','Raghav','144412','ri@gmail.com','9942434121','Raipur','12','12');
INSERT INTO employee VALUES('4','Nishant','144412','ni@gmail.com','9943475221','Dehradun','13','13');
INSERT INTO employee VALUES('5','Navin','144412','navin@gmail.com','991431221','Bangalore','14','11');

SELECT * FROM Employee

SELECT * FROM Managers

SELECT * from Department


--DELETE OPERATIONS FROM INVENTORY

delete from inventory where id='4';
delete from inventory where id='3';
delete from inventory where id='2';


--JOIN OPERATION TO SHOW EMPLOYEE NAME ADDRESS AND DEPARTMENT HE IS WORKING IN

SELECT e.name, e.address,d.pname from employee as e
LEFT JOIN department as d ON
e.did=d.pid;

-- SUBQUERIES TO DISPLAY MAXIMUM AND SECOND MAX SALARY FOR EMPLOYEES

SELECT * FROM Inventory where sales IN(SELECT MAX(sales) from Inventory)
SELECT * FROM Inventory where sales IN(SELECT MAX(sales) from Inventory where sales <>(SELECT MAX(sales) from Inventory))