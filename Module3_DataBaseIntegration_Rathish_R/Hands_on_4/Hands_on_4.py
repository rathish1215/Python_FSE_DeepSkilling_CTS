import psycopg2
import time

# Database connection
conn = psycopg2.connect(
    dbname="college_db",
    user="postgres",
    password="your_password",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# -------------------------------
# BAD APPROACH : N+1 QUERY
# -------------------------------

start_time = time.time()

cur.execute(
    "SELECT student_id, course_id FROM enrollments"
)

enrollments = cur.fetchall()
query_count = 1
results = []

for student_id, course_id in enrollments:
    cur.execute(
        """
        SELECT
            s.first_name,
            s.last_name,
            c.course_name
        FROM students s
        JOIN courses c
            ON c.course_id = %s
        WHERE s.student_id = %s
        """,
        (course_id, student_id)
    )

    results.append(cur.fetchone())
    query_count += 1

end_time = time.time()

print("N+1 Approach")
print("----------------")
print("Results:", results)
print("Total Queries:", query_count)
print("Time Taken:", end_time - start_time)

# -------------------------------
# GOOD APPROACH : JOIN QUERY
# -------------------------------

start_time = time.time()

cur.execute(
    """
    SELECT
        s.first_name,
        s.last_name,
        c.course_name
    FROM enrollments e
    JOIN students s
        ON e.student_id = s.student_id
    JOIN courses c
        ON e.course_id = c.course_id;
    """
)

results = cur.fetchall()

end_time = time.time()

print("\nJOIN Approach")
print("----------------")
print("Results:", results)
print("Total Queries: 1")
print("Time Taken:", end_time - start_time)

cur.close()
conn.close()
