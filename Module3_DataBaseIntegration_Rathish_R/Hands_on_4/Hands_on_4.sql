-- HANDS-ON 4

-- TASK 1 : BASELINE PERFORMANCE ANALYSIS

EXPLAIN
SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
    ON e.student_id = s.student_id
JOIN courses c
    ON e.course_id = c.course_id
WHERE s.enrollment_year = 2022;

/*
Observation:

Before indexing:

- PostgreSQL may use Sequential Scan
- Entire table rows are checked
- JOIN operations are slower for large data
*/


-- TASK 2 : ADD INDEXES AND COMPARE PERFORMANCE

CREATE INDEX IF NOT EXISTS idx_students_enrollment_year
ON students(enrollment_year);

CREATE INDEX IF NOT EXISTS idx_enrollments_student_course
ON enrollments(student_id, course_id);

CREATE INDEX IF NOT EXISTS idx_courses_course_id
ON courses(course_id);

-- Check execution plan after indexes

EXPLAIN
SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
    ON e.student_id = s.student_id
JOIN courses c
    ON e.course_id = c.course_id
WHERE s.enrollment_year = 2022;

/*
After adding indexes:

Improvements:

- Faster searching
- Faster JOIN operations
- Less table scanning
- Better performance for large datasets
*/


-- TASK 3 : QUERY OPTIMIZATION USING JOIN

-- N+1 problem example query

SELECT *
FROM enrollments;

-- Optimized single query

SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
    ON e.student_id = s.student_id
JOIN courses c
    ON e.course_id = c.course_id;

/*
N+1 Problem:

Bad approach:

1 query fetches enrollments

+
N queries fetch student and course details

Example:

1000 enrollments

Total queries = 1001

Problems:

- More database calls
- More execution time
- Poor scalability

Optimized approach:

JOIN executes only 1 query.

Benefits:

- Less network communication
- Faster response
- Better scalability
*/


-- TASK 4 : ANALYZE QUERY PERFORMANCE

ANALYZE students;
ANALYZE courses;
ANALYZE enrollments;

EXPLAIN ANALYZE
SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
    ON e.student_id = s.student_id
JOIN courses c
    ON e.course_id = c.course_id;

/*
EXPLAIN ANALYZE shows:

- Actual execution time
- Rows processed
- Query efficiency
*/
