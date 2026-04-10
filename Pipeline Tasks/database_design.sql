-- Scenario 1: Books and Authors

CREATE TABLE Authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

CREATE TABLE Books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    publication_year INTEGER,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

INSERT INTO Authors (first_name, last_name) VALUES
    ('Stephen', 'King'),
    ('J.K.', 'Rowling'),
    ('George', 'Orwell');

INSERT INTO Books (title, author_id, publication_year) VALUES
    ('The Shining', 1, 1977),
    ('Harry Potter and the Sorcerer''s Stone', 2, 1997),
    ('1984', 3, 1949),
    ('It', 1, 1986);

SELECT
    B.title AS BookTitle,
    A.first_name || ' ' || A.last_name AS AuthorName,
    B.publication_year
FROM Books B
JOIN Authors A ON B.author_id = A.author_id
WHERE A.last_name = 'King';


-- Scenario 2: Departments and Employees

CREATE TABLE Departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    department_name TEXT NOT NULL
);

CREATE TABLE Employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    department_id INTEGER,
    hire_date DATE,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

INSERT INTO Departments (department_name) VALUES
    ('Sales'),
    ('Marketing'),
    ('Engineering');

INSERT INTO Employees (first_name, last_name, department_id, hire_date) VALUES
    ('John', 'Doe', 1, '2020-01-15'),
    ('Jane', 'Smith', 2, '2019-03-20'),
    ('Peter', 'Jones', 1, '2021-06-01'),
    ('Alice', 'Williams', 3, '2018-11-10');

SELECT
    E.first_name || ' ' || E.last_name AS EmployeeName,
    D.department_name
FROM Employees E
JOIN Departments D ON E.department_id = D.department_id
WHERE D.department_name = 'Sales';


-- Scenario 3: Customers and Orders

CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE
);

CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date DATE,
    total_amount REAL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

INSERT INTO Customers (first_name, last_name, email) VALUES
    ('Michael', 'Brown', 'michael.brown@example.com'),
    ('Emily', 'Davis', 'emily.davis@example.com'),
    ('David', 'Wilson', 'david.wilson@example.com');

INSERT INTO Orders (customer_id, order_date, total_amount) VALUES
    (1, '2023-01-10', 150.75),
    (2, '2023-01-12', 200.00),
    (1, '2023-02-01', 50.25),
    (3, '2023-02-05', 300.50);

SELECT
    C.first_name || ' ' || C.last_name AS CustomerName,
    O.order_id,
    O.order_date,
    O.total_amount
FROM Customers C
JOIN Orders O ON C.customer_id = O.customer_id
WHERE C.email = 'michael.brown@example.com';


-- Scenario 4: Consultants and Meetings

CREATE TABLE Consultants (
    consultant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    specialty TEXT
);

CREATE TABLE Meetings (
    meeting_id INTEGER PRIMARY KEY AUTOINCREMENT,
    consultant_id INTEGER NOT NULL,
    meeting_date DATETIME,
    topic TEXT,
    FOREIGN KEY (consultant_id) REFERENCES Consultants(consultant_id)
);

INSERT INTO Consultants (first_name, last_name, specialty) VALUES
    ('Sarah', 'Miller', 'Marketing Strategy'),
    ('Robert', 'Taylor', 'Financial Planning'),
    ('Laura', 'Moore', 'IT Consulting');

INSERT INTO Meetings (consultant_id, meeting_date, topic) VALUES
    (1, '2023-03-01 10:00:00', 'Q1 Marketing Review'),
    (2, '2023-03-05 14:30:00', 'Investment Portfolio Discussion'),
    (1, '2023-03-10 11:00:00', 'Social Media Campaign Planning');

SELECT
    C.first_name || ' ' || C.last_name AS ConsultantName,
    M.meeting_date,
    M.topic
FROM Consultants C
JOIN Meetings M ON C.consultant_id = M.consultant_id
WHERE C.specialty = 'Marketing Strategy';


-- Scenario 5: Directors and Movies

CREATE TABLE Directors (
    director_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

CREATE TABLE Movies (
    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    director_id INTEGER NOT NULL,
    release_year INTEGER,
    FOREIGN KEY (director_id) REFERENCES Directors(director_id)
);

INSERT INTO Directors (first_name, last_name) VALUES
    ('Christopher', 'Nolan'),
    ('Quentin', 'Tarantino'),
    ('Steven', 'Spielberg');

INSERT INTO Movies (title, director_id, release_year) VALUES
    ('Inception', 1, 2010),
    ('Pulp Fiction', 2, 1994),
    ('Interstellar', 1, 2014),
    ('Jaws', 3, 1975);

SELECT
    M.title AS MovieTitle,
    D.first_name || ' ' || D.last_name AS DirectorName,
    M.release_year
FROM Movies M
JOIN Directors D ON M.director_id = D.director_id
WHERE D.last_name = 'Nolan';
