# 🎓 Digital Nurture 5.0 - Full Stack & QA Engineering

<div align="center">

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

</div>

---

## 📌 Project Overview

Welcome to my portfolio repository showcasing the work completed during the **Cognizant Digital Nurture 5.0** program. The core of this repository is a fully functional **Student Course Registration & Management System**, developed progressively through four key phases:

1. **Frontend Development (10 Hands-On)**
2. **Database Integration (10 Hands-On)**
3. **Python Backend Frameworks (10 Hands-On)**
4. **QA Concepts & Selenium Basics (7 Hands-On)**

This repository serves as a practical demonstration of end-to-end software engineering, covering user interface design, data modeling, API creation, distributed services, and automated software testing.

---

## 🚀 Technologies Used

| Category | Technologies |
|----------|-------------|
| **Frontend** | HTML5, CSS3, JavaScript (ES6+), React.js |
| **Databases** | PostgreSQL, MySQL, MongoDB |
| **Backend Frameworks** | FastAPI, Django, Flask |
| **ORM & Migrations** | SQLAlchemy, Alembic |
| **Security** | JWT, passlib (Bcrypt), OAuth2 |
| **QA Automation** | Selenium WebDriver, Pytest, pytest-html, webdriver-manager |

---

## 🗂️ Module 1: Frontend Development (10 Hands-On)

This section emphasizes the creation of intuitive, device-friendly user interfaces.

### 🔹 Hands-On 1 to 4: Structuring the Web & Vanilla JS
- Crafted adaptable web layouts utilizing modern HTML5 and CSS3 methodologies like Grid and Flexbox.
- Applied vanilla JavaScript for direct DOM interactions, event listening, and ES6+ asynchronous programming.

### 🔹 Hands-On 5 to 7: React Engineering & State Architecture
- Developed isolated, reusable UI components utilizing React.js.
- Controlled application behavior and lifecycles via React Hooks (such as `useState` and `useEffect`).
- Set up seamless page navigation using React Router for a Single Page Application (SPA) feel.

### 🔹 Hands-On 8 to 10: Backend Integration & UI Polish
- Connected the client side to RESTful backend services leveraging Fetch and Axios APIs.
- Handled secure authentication processes (using JWTs) and intricate form validations.
- Fine-tuned the final dashboard rendering for an optimal and fluid user experience.

---

## 🗂️ Module 2: Database Integration (10 Hands-On)

This module dives deep into data architecture, query efficiency, NoSQL implementations, and schema versioning.

### 🔹 Hands-On 1 to 4: Relational Modeling & Query Tuning
- Structured the core relational database (Students, Courses, Enrollments) adhering to strict normalization rules (1NF up to 3NF).
- Executed sophisticated SQL commands encompassing multi-table JOINs, nested subqueries, and stored procedures.
- Addressed performance bottlenecks like the N+1 query issue by interpreting `EXPLAIN` outputs and building composite indexes.

### 🔹 Hands-On 5 to 7: Bridging NoSQL & ORM Ecosystems
- Designed BSON data structures and executed complex queries via the MongoDB Aggregation Pipeline.
- Established database connections and entity relationships using the SQLAlchemy ORM framework.
- Implemented **Alembic** for systematic database migrations and version control (handling seamless schema upgrades and downgrades).

### 🔹 Hands-On 8 to 10: ACID Properties & Caching Strategies
- Ensured ACID compliance and data safety using SQL Transactions (`COMMIT`, `ROLLBACK`, `SAVEPOINT`).
- Integrated caching mechanisms to boost retrieval speeds for the final database capstone project.

---

## 🗂️ Module 3: Python Backend Frameworks (10 Hands-On)

This phase explores server-side logic, RESTful API design, and the shift from monolithic structures to microservices.

### 🔹 Hands-On 1 to 4: Framework Philosophies & API Genesis
- Configured and compared the foundational architectures of **Django**, **Flask**, and **FastAPI**.
- Programmed core API endpoints handling CRUD operations, query string parsing, and payload validation via Pydantic.

### 🔹 Hands-On 5 to 7: Advanced FastAPI & Asynchronous Tasks
- Applied **FastAPI Dependency Injection** to elegantly manage database sessions and lifecycles.
- Embedded SQLAlchemy ORM operations directly within the API routing layer.
- Delegated heavy computational tasks to asynchronous **Background Tasks** to maintain API responsiveness.

### 🔹 Hands-On 8 & 9: Shielding APIs & REST Standards
- Enforced strict REST constraints, standard HTTP status codes, and URI versioning.
- Protected endpoints utilizing **OAuth2** flows and **JWT** issuance.
- Fortified the application against OWASP vulnerabilities by configuring CORS and hashing passwords with **Bcrypt**.

### 🔹 Hands-On 10: Transitioning to Microservices
- Segmented the monolithic backend into an **API Gateway**, a **Course Service** (Port 5001), and a **Student Service** (Port 5002).
- Orchestrated inter-service API calls and engineered network fault tolerance (handling 503 Service Unavailable errors).

---

## 🗂️ Module 4: QA Concepts & Selenium Basics (7 Hands-On)

This final module establishes a robust testing culture and constructs an automated UI testing framework.

### 🔹 Hands-On 1 to 3: Quality Engineering & Shift-Left Tactics
- Studied Software Testing Life Cycles (STLC), the V-Model, and the philosophy of Shift-Left testing.
- Formulated a comprehensive automation strategy, assessing ROI across Modular, Data-Driven, and Hybrid frameworks.

### 🔹 Hands-On 4 & 5: WebDriver Automation & Synchronization
- Initialized Selenium WebDriver to operate Headless Chrome browsers.
- Deployed reliable DOM locators (XPath, CSS Selectors, ID).
- Replaced brittle `time.sleep()` calls with dynamic **Explicit Waits** (`WebDriverWait`) to guarantee test stability.

### 🔹 Hands-On 6: Pytest Mechanics & Report Generation
- Upgraded standard Python scripts into a structured **pytest** framework, utilizing `conftest.py` for global fixtures.
- Created automated hooks to snap screenshots whenever a test case fails.
- Exported comprehensive execution logs via `pytest-html`.

### 🔹 Hands-On 7: The Page Object Model (POM) Paradigm
- Engineered a resilient testing architecture by adopting the **Page Object Model (POM)**.
- Designed a universal `BasePage` alongside specialized page objects (`SimpleFormPage`, `CheckboxPage`), effectively abstracting all raw `find_element` interactions away from the actual test scripts.

---

## 🎯 Gaining Knowledge & Technical Expertise

By completing this comprehensive curriculum, I have acquired practical expertise in:
- Engineering highly interactive and responsive web interfaces with contemporary frontend libraries.
- Architecting normalized relational schemas and tuning SQL queries for massive data loads.
- Executing programmatic database migrations and managing schema evolution through code.
- Designing, securing, and deploying distributed REST APIs and scalable microservice architectures.
- Constructing resilient, flake-free test automation frameworks utilizing Pytest and the Page Object Model.

---

## 👨‍💻 Author
**Rathish R**  
*Digital Nurture 5.0 – Full Stack Engineering Track*
