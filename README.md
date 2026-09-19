# AI Requirements Documentation Copilot

An AI-powered Business Requirements & Documentation Copilot that converts natural-language business requirements into structured business analysis documentation using Large Language Models (LLMs).

> **Project Status:** 🚧 Under Development

## 📌 Project Overview

Business Analysts often spend significant time converting unstructured business requirements into formal documentation such as Business Requirements Documents (BRDs), Functional Requirements, User Stories, Acceptance Criteria, Business Rules, Risks, and Assumptions.

The **AI Requirements Documentation Copilot** aims to automate and accelerate this process.

The application accepts a business requirement written in natural language and uses an LLM to generate structured, reviewable business analysis outputs.

### Example Input

> "We need an employee reimbursement system where employees can submit claims, managers can approve claims, and the finance team can process approved reimbursements."

### Expected Output

The application will generate:

* Business Objective
* Stakeholders
* Functional Requirements
* Non-Functional Requirements
* User Stories
* Acceptance Criteria
* Business Rules
* Risks
* Assumptions
* Clarification Questions

---

## 🎯 Project Objectives

The main objectives of this project are to:

1. Automate repetitive Business Analysis documentation activities.
2. Convert unstructured requirements into structured outputs.
3. Demonstrate practical use of LLM APIs in a business application.
4. Implement structured AI responses using Python and Pydantic.
5. Build a user-friendly interface using Streamlit.
6. Demonstrate secure API-key management.
7. Apply software engineering and Git/GitHub best practices.
8. Create a practical GenAI application suitable for real-world business scenarios.

---

## 🧠 AI Engineering Concepts

This project is designed to provide hands-on experience with:

* Large Language Models (LLMs)
* Prompt Engineering
* Structured Outputs
* JSON-based AI responses
* Pydantic validation
* API integration
* Input validation
* Error handling
* Environment variables
* LLM application architecture
* AI application testing
* Git
* GitHub
* Streamlit application development

Future versions may include:

* Retrieval-Augmented Generation (RAG)
* Vector databases
* Document retrieval
* AI agents
* Tool/function calling
* Automated document generation
* LLM evaluation

---

## 🏗️ Planned Architecture

```text
                 USER
                   │
                   ▼
          ┌─────────────────┐
          │   Streamlit UI  │
          └────────┬────────┘
                   │
                   ▼
          Business Requirement
                   │
                   ▼
          ┌─────────────────┐
          │ Prompt Builder  │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │    LLM API      │
          └────────┬────────┘
                   │
                   ▼
          Structured JSON
                   │
                   ▼
          ┌─────────────────┐
          │ Pydantic Model  │
          │   Validation    │
          └────────┬────────┘
                   │
                   ▼
          Business Analysis
             Documentation
```

---

## 🛠️ Technology Stack

### Programming

* Python

### Generative AI

* Large Language Model API
* Prompt Engineering
* Structured LLM Responses

### Application

* Streamlit

### Data Validation

* Pydantic

### Version Control

* Git
* GitHub

### Configuration

* Environment Variables
* `.env`

---

## ✨ Planned Features

### 1. Requirement Input

Users can enter a business requirement in natural language.

### 2. AI Requirement Analysis

The LLM analyzes the submitted requirement and identifies relevant business information.

### 3. Structured Documentation

The system generates structured outputs including:

```text
Business Objective
Stakeholders
Functional Requirements
Non-Functional Requirements
User Stories
Acceptance Criteria
Business Rules
Risks
Assumptions
Clarification Questions
```

### 4. Structured JSON Output

The LLM response will be converted into a structured schema to improve consistency and validation.

### 5. Validation

Pydantic will be used to validate the generated response before it is displayed to the user.

### 6. Error Handling

The application will handle:

* Invalid input
* Missing configuration
* API failures
* Invalid model responses
* Network errors
* Validation errors

### 7. Export

Future versions will support exporting generated documentation into formats such as:

* PDF
* DOCX
* JSON

---

## 📂 Planned Project Structure

```text
ai-requirements-documentation-copilot/
│
├── app.py
├── llm_service.py
├── schemas.py
├── prompts.py
├── config.py
│
├── requirements.txt
├── README.md
├── .gitignore
│
├── screenshots/
│
├── sample_outputs/
│
└── tests/
```

### File Description

| File               | Purpose                                  |
| ------------------ | ---------------------------------------- |
| `app.py`           | Streamlit application and user interface |
| `llm_service.py`   | LLM API communication                    |
| `schemas.py`       | Pydantic response models                 |
| `prompts.py`       | Prompt templates                         |
| `config.py`        | Configuration and environment variables  |
| `requirements.txt` | Python dependencies                      |
| `tests/`           | Application tests                        |
| `screenshots/`     | Project screenshots                      |
| `sample_outputs/`  | Example generated outputs                |

---

## 🔐 Security

API credentials must never be hard-coded into the application.

Sensitive information will be stored using environment variables.

Example:

```text
OPENAI_API_KEY=your_api_key_here
```

The `.env` file must not be committed to GitHub.

The repository uses `.gitignore` to prevent sensitive and unnecessary files from being uploaded.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/NippunWahi1997/ai-requirements-documentation-copilot.git
```

### 2. Navigate into the project

```bash
cd ai-requirements-documentation-copilot
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows Command Prompt:

```bash
.venv\Scripts\activate
```

Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

### 7. Run the application

```bash
streamlit run app.py
```

---

## 🧪 Example Use Case

### Input

```text
Build a student attendance management system where faculty
can mark attendance, students can view their attendance,
and program leaders can generate attendance reports.
```

### Expected AI Analysis

**Business Objective**

Centralize attendance management and improve attendance reporting.

**Stakeholders**

* Students
* Faculty
* Program Leaders
* Administration

**Functional Requirements**

* Faculty can mark attendance.
* Students can view attendance.
* Program leaders can generate reports.

**User Story**

> As a faculty member, I want to record student attendance so that attendance records remain accurate and accessible.

**Acceptance Criteria**

> Given a registered student, when the faculty records attendance, the student's attendance record should be updated.

---

## 📊 AI Engineering Learning Outcomes

This project is being developed as a practical learning project to understand how to build an LLM-powered application.

By completing the project, the developer will gain practical experience in:

* Connecting Python applications to LLM APIs
* Designing effective prompts
* Working with structured AI responses
* Validating AI-generated data
* Building an interactive AI application
* Managing API credentials securely
* Handling API and application errors
* Using Git and GitHub
* Documenting an AI application
* Preparing an LLM application for future RAG and agentic capabilities

---

## 🔮 Future Enhancements

### Phase 1 — LLM Application

* Basic LLM integration
* Prompt engineering
* Structured responses
* Pydantic validation
* Streamlit UI

### Phase 2 — Document Generation

* BRD generation
* FRD generation
* DOCX export
* PDF export

### Phase 3 — RAG

* Upload requirement documents
* Document chunking
* Embeddings
* Vector database
* Retrieval
* Context-aware generation

### Phase 4 — Agentic AI

* Tool calling
* Automated requirement validation
* Requirement completeness checking
* Requirement conflict detection
* AI-driven clarification questions

### Phase 5 — Production Improvements

* Automated tests
* Logging
* Monitoring
* Evaluation
* Authentication
* API backend
* Deployment

---

## 📈 Project Roadmap

```text
✅ GitHub Repository
      ↓
🔄 Python Project Setup
      ↓
🔄 LLM API Integration
      ↓
🔄 Structured Output
      ↓
🔄 Pydantic Validation
      ↓
🔄 Streamlit UI
      ↓
🔄 Error Handling
      ↓
🔄 Document Export
      ↓
🔜 RAG
      ↓
🔜 Vector Database
      ↓
🔜 AI Agents
      ↓
🔜 Deployment
```

---

## 👨‍💻 Author

### Nippun Wahi

**Business Analytics | Business Analysis | Generative AI | LLM Applications**

**GitHub:**
https://github.com/NippunWahi1997

**Project Repository:**
https://github.com/NippunWahi1997/ai-requirements-documentation-copilot

**LinkedIn:**
https://linkedin.com/in/nippunwahi

---

## ⚠️ Disclaimer

This project is created for educational, portfolio, and experimentation purposes.

AI-generated requirements should be reviewed and validated by a qualified Business Analyst or relevant business stakeholder before being used in production systems.

---

## ⭐ Project Vision

The long-term goal of this project is to evolve from a simple LLM-powered documentation assistant into an **AI Engineering platform for requirements analysis, retrieval, validation, and intelligent business analysis automation**.
