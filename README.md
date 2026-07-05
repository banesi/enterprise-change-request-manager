# Enterprise Change Advisory Manager

## Overview

Enterprise Change Advisory Manager is a Python-based application that simulates an enterprise Change Advisory Board (CAB) workflow by processing change requests stored in JSON format. The application analyzes change requests, identifies high-risk changes, generates customer notifications, and produces structured reports for CAB review.

The project follows a clean, modular architecture and demonstrates software engineering best practices such as Object-Oriented Programming (OOP), JSON processing, file handling, error handling, and Git-based version control. It serves as a strong foundation for building future AI-powered enterprise support applications.

---

## Business Problem

Enterprise organizations receive numerous change requests for activities such as firmware upgrades, storage migrations, security patching, and infrastructure maintenance.

Manually reviewing every request is time-consuming and increases the risk of overlooking high-impact changes.

This application automates the analysis of change requests by:

* Organizing change request data
* Identifying high-risk changes
* Generating CAB-ready reports
* Producing professional customer notifications

---

## Features

* Load enterprise change requests from JSON files
* Convert JSON dictionaries into Python objects using OOP
* Identify high-risk change requests
* Generate concise change request summaries
* Produce customer-friendly notification messages
* Generate CAB reports with change statistics
* Save structured JSON reports
* Handle missing files and invalid JSON gracefully
* Follow a clean multi-file Python project architecture
* Track project history using Git and GitHub

---

## Tech Stack

* Python 3
* Object-Oriented Programming (OOP)
* JSON
* File Handling
* Exception Handling
* Git
* GitHub

---

## Project Structure

```text
enterprise_change_advisory_manager/
│
├── data/
│   └── change_requests.json
│
├── outputs/
│   ├── cab_report.json
│   ├── high_risk_changes.json
│   └── customer_notifications.json
│
├── models.py
├── managers.py
├── file_handler.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## How It Works

1. Load change request data from a JSON file.
2. Convert each change request into a `ChangeRequest` object.
3. Analyze the data to identify high-risk changes.
4. Generate CAB statistics.
5. Generate customer notification messages.
6. Save reports as JSON files inside the `outputs/` directory.

---

## Sample Input

```json
{
    "change_id": "CR1001",
    "customer": "ABC Bank",
    "risk": "High",
    "status": "Scheduled",
    "description": "Upgrade ONTAP firmware on production cluster",
    "planned_days": 3
}
```

---

## Generated Outputs

The application creates the following reports:

### CAB Report

* Total change requests
* Scheduled changes
* In-progress changes
* Completed changes
* Cancelled changes
* High-risk changes
* Medium-risk changes
* Low-risk changes

---

### High-Risk Change Report

Contains only change requests classified as **High Risk** for quick CAB review.

---

### Customer Notifications

Generates professional customer-facing messages containing:

* Customer name
* Change ID
* Change description
* Current status
* Planned implementation timeline
* Risk level

---

## Error Handling

The application safely handles:

* Missing input files (`FileNotFoundError`)
* Invalid JSON (`JSONDecodeError`)
* Unexpected runtime exceptions

This ensures the application fails gracefully instead of crashing.

---

## Skills Demonstrated

This project demonstrates:

* Python Programming
* Object-Oriented Design
* Clean Code Principles
* Multi-file Project Architecture
* JSON Data Processing
* File Input/Output
* Exception Handling
* Report Generation
* Git Version Control
* GitHub Project Management

---

## Future AI Enhancements

This project is designed as the foundation for an AI-powered Change Advisory Assistant.

Planned enhancements include:

* AI-generated change request summaries using the OpenAI API
* AI-generated customer notifications
* Risk assessment using Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG) for CAB knowledge search
* FastAPI backend for API integration
* AI-powered change impact analysis
* Agent-based CAB workflow automation
* Interactive web dashboard for change management

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/<your-github-username>/enterprise-change-advisory-manager.git
```

Navigate to the project directory:

```bash
cd enterprise-change-advisory-manager
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

macOS / Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

## Learning Objectives

This project was built to strengthen practical software engineering skills before integrating Artificial Intelligence into enterprise applications.

It focuses on building maintainable, modular, and production-oriented Python applications that can later be extended with AI capabilities.

---

## Author

**Sibaji Banerjee**

Aspiring AI Engineer | Enterprise Support Professional

Currently building enterprise-focused AI applications using Python, Git, OpenAI APIs, RAG, FastAPI, and AI Agents.
