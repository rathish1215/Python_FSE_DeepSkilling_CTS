-- HANDS-ON 3


-- TASK 1: SUBQUERIES


-- Students having more courses than average

SELECT 
e.student_id,
s.first_name || ' ' || s.last_name AS student_name,
COUNT(e.course_id) AS total_courses
FROM enrollments e
JOIN students s
ON e.student_id=s.student_id
GROUP BY 
e.student_id,
s.first_name,
s.last_name
HAVING COUNT(e.course_id) >
(
SELECT AVG(course_count)
FROM
(
SELECT student_id,
COUNT(course_id) AS course_count
FROM enrollments
GROUP BY student_id
) x
);



-- Courses where all grades are A

SELECT 
c.course_id,
c.course_name
FROM courses c
WHERE EXISTS
(
SELECT 1
FROM enrollments e
WHERE e.course_id=c.course_id
)
AND NOT EXISTS
(
SELECT 1
FROM enrollments e
WHERE e.course_id=c.course_id
AND e.grade <> 'A'
);



-- Highest salary professor in every department

SELECT *
FROM professors p
WHERE salary=
(
SELECT MAX(salary)
FROM professors p2
WHERE p2.department_id=p.department_id
);



-- Departments average salary above 85000

SELECT *
FROM
(
SELECT 
department_id,
AVG(salary) average_salary
FROM professors
GROUP BY department_id
) a
WHERE average_salary > 85000;




-- TASK 2: VIEWS


DROP VIEW IF EXISTS vw_student_summary CASCADE;


CREATE VIEW vw_student_summary AS
SELECT
s.student_id,
s.first_name || ' ' || s.last_name AS student_name,
d.dept_name,
COUNT(e.course_id) total_courses
FROM students s
JOIN departments d
ON s.department_id=d.department_id
LEFT JOIN enrollments e
ON s.student_id=e.student_id
GROUP BY
s.student_id,
s.first_name,
s.last_name,
d.dept_name;


SELECT *
FROM vw_student_summary;



DROP VIEW IF EXISTS vw_course_summary CASCADE;


CREATE VIEW vw_course_summary AS
SELECT
c.course_id,
c.course_name,
COUNT(e.enrollment_id) total_students
FROM courses c
LEFT JOIN enrollments e
ON c.course_id=e.course_id
GROUP BY
c.course_id,
c.course_name;


SELECT *
FROM vw_course_summary;





-- TASK 3: FUNCTIONS



DROP FUNCTION IF EXISTS fn_add_enrollment(INT,INT,DATE);


CREATE OR REPLACE FUNCTION fn_add_enrollment
(
p_student INT,
p_course INT,
p_date DATE
)
RETURNS TEXT
LANGUAGE plpgsql
AS $$

BEGIN

IF EXISTS
(
SELECT 1
FROM enrollments
WHERE student_id=p_student
AND course_id=p_course
)

THEN

RETURN 'Already enrolled';

END IF;


INSERT INTO enrollments
(
student_id,
course_id,
enrollment_date
)

VALUES
(
p_student,
p_course,
p_date
);


RETURN 'Enrollment Added';


END;

$$;



-- Function test

SELECT fn_add_enrollment
(
(SELECT MIN(student_id) FROM students),
(SELECT MIN(course_id) FROM courses),
CURRENT_DATE
);





-- Transfer log table


DROP TABLE IF EXISTS student_transfer_log;


CREATE TABLE student_transfer_log
(
log_id SERIAL PRIMARY KEY,
student_id INT,
old_department INT,
new_department INT,
transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



DROP FUNCTION IF EXISTS fn_transfer_student(INT,INT);


CREATE OR REPLACE FUNCTION fn_transfer_student
(
p_student INT,
p_new_dept INT
)

RETURNS TEXT
LANGUAGE plpgsql
AS $$

DECLARE
old_dept INT;

BEGIN

SELECT department_id
INTO old_dept
FROM students
WHERE student_id=p_student;


UPDATE students
SET department_id=p_new_dept
WHERE student_id=p_student;


INSERT INTO student_transfer_log
(
student_id,
old_department,
new_department
)

VALUES
(
p_student,
old_dept,
p_new_dept
);


RETURN 'Transfer Completed';


END;

$$;



-- Function test

SELECT fn_transfer_student
(
(SELECT MIN(student_id) FROM students),
(SELECT MIN(department_id) FROM departments)
);





-- TASK 4: TRANSACTIONS



BEGIN;


UPDATE students
SET department_id=
(
SELECT MIN(department_id)
FROM departments
)
WHERE student_id=
(
SELECT MIN(student_id)
FROM students
);


COMMIT;





-- SAVEPOINT TRANSACTION


BEGIN;


INSERT INTO enrollments
(
student_id,
course_id,
enrollment_date
)

VALUES
(
(SELECT MIN(student_id) FROM students),
(SELECT MIN(course_id) FROM courses),
CURRENT_DATE
);


SAVEPOINT save1;


ROLLBACK TO SAVEPOINT save1;


COMMIT;
