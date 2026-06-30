from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:rathish09@localhost/college_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Student(db.Model):
    __tablename__ = "students"

    student_id = db.Column(
        db.Integer,
        primary_key=True
    )

    first_name = db.Column(
        db.String(50)
    )

    last_name = db.Column(
        db.String(50)
    )

    email = db.Column(
        db.String(100)
    )

    enrollment_year = db.Column(
        db.Integer
    )


# TASK 1 : GET ALL STUDENTS

@app.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()

    result = []

    for s in students:
        result.append({
            "id": s.student_id,
            "name": s.first_name + " " + s.last_name,
            "email": s.email,
            "year": s.enrollment_year
        })

    return jsonify(result)


# TASK 2 : GET STUDENT BY ID

@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    student = Student.query.get(id)

    if student is None:
        return jsonify({
            "message": "Student not found"
        })

    return jsonify({
        "id": student.student_id,
        "name": student.first_name + " " + student.last_name,
        "email": student.email
    })


# TASK 3 : INSERT STUDENT

@app.route("/students", methods=["POST"])
def add_student():
    data = request.json

    student = Student(
        first_name=data["first_name"],
        last_name=data["last_name"],
        email=data["email"],
        enrollment_year=data["enrollment_year"]
    )

    db.session.add(student)
    db.session.commit()

    return jsonify({
        "message": "Student Added"
    })


# TASK 4 : UPDATE STUDENT

@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    student = Student.query.get(id)

    data = request.json

    student.enrollment_year = data["enrollment_year"]

    db.session.commit()

    return jsonify({
        "message": "Student Updated"
    })


# TASK 5 : DELETE STUDENT

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get(id)

    db.session.delete(student)

    db.session.commit()

    return jsonify({
        "message": "Student Deleted"
    })


if __name__ == "__main__":
    app.run(debug=True)
