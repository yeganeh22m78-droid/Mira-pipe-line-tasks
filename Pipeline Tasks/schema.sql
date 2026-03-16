-- Create Student table
CREATE TABLE IF NOT EXISTS Student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    birthday DATE,
    major TEXT
);

-- Create Course table
CREATE TABLE IF NOT EXISTS Course (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

-- Insert sample students
INSERT INTO Student (name, birthday, major) VALUES
('Alex Student', '2000-05-15', 'Computer Science'),
('Blake Student', '2001-08-22', 'Computer Science'),
('Casey Learner', '1999-11-03', 'Information Tech');