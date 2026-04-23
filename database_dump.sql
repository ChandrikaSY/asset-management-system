-- Asset Management System Database Dump

-- =========================
-- TABLE: employees
-- =========================
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    department VARCHAR(100)
);

-- =========================
-- TABLE: assets
-- =========================
CREATE TABLE assets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    asset_code VARCHAR(50),
    type VARCHAR(50),
    is_assigned BOOLEAN
);

-- =========================
-- TABLE: assignments
-- =========================
CREATE TABLE assignments (
    id SERIAL PRIMARY KEY,
    employee_id INT,
    asset_id INT,
    assigned_date TIMESTAMP
);

-- =========================
-- SAMPLE DATA (EMPLOYEES)
-- =========================
INSERT INTO employees (name, email, department) VALUES
('Rahul Sharma', 'rahul@gmail.com', 'IT'),
('Anjali Verma', 'anjali@gmail.com', 'HR'),
('Ravi Kumar', 'ravi@gmail.com', 'Finance'),
('Sneha Reddy', 'sneha@gmail.com', 'Marketing'),
('Arjun Singh', 'arjun@gmail.com', 'IT');

-- =========================
-- SAMPLE DATA (ASSETS)
-- =========================
INSERT INTO assets (name, asset_code, type, is_assigned) VALUES
('Laptop Dell', 'A001', 'Electronics', TRUE),
('HP Laptop', 'A002', 'Electronics', TRUE),
('Office Chair', 'A003', 'Furniture', FALSE),
('Projector', 'A004', 'Electronics', TRUE),
('Desk Table', 'A005', 'Furniture', FALSE);

-- =========================
-- SAMPLE DATA (ASSIGNMENTS)
-- =========================
INSERT INTO assignments (employee_id, asset_id, assigned_date) VALUES
(1, 1, CURRENT_TIMESTAMP),
(2, 2, CURRENT_TIMESTAMP),
(3, 4, CURRENT_TIMESTAMP);