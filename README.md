# Personal Expense Tracker

## 1. Project Overview

The **Personal Expense Tracker** is a command-line-based application developed using Python to record, manage, analyze, and visualize daily expenses.

The application helps users maintain expense records, organize spending by categories, generate financial reports, and understand their spending patterns through graphical visualizations.

Expense records are stored in CSV format, allowing data to be saved and retrieved whenever the application is executed.

## 2. Features

- **Add Expenses:** Record daily expenses with amount, category, date, and description.
- **View Expenses:** Display all previously recorded expenses.
- **Expense Categorization:** Organize expenses into different categories.
- **Input Validation:** Validate expense amounts, categories, dates, and descriptions.
- **CSV File Handling:** Save and retrieve expense records using CSV files.
- **Expense Reports:**
  - Total amount spent
  - Average expense
  - Category-wise spending
  - Weekly spending
  - Monthly spending
  - Highest expense
- **Data Visualization using Matplotlib:**
  - Category-wise bar chart
  - Category-wise pie chart
  - Weekly expense analysis
  - Monthly expense analysis
- **Error Handling:** Handle invalid user inputs and invalid CSV records.
- **Data Protection:** Use temporary-file replacement for safer CSV saving.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| CSV | Expense data storage |
| Datetime | Date validation and time-based analysis |
| Matplotlib | Data visualization |

## 4. Project Structure

```text
EXPENSE-TRACKER/
│
├── main.py
├── README.md
├── requirements.txt
│
├── data/
│   └── expenses.csv
│
└── screenshots/
    └── Application screenshots
```

**Note:** Backup and test CSV files used during development are not required to run the final application.

## 5. Installation and Setup

### Prerequisites

- Python installed on your system.
- Visual Studio Code or any Python-supported IDE.

### Step 1: Clone or Download the Project

Download the project and open the project folder in Visual Studio Code.

### Step 2: Install Dependencies

Open the terminal in the project directory and execute:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

Execute the following command:

```bash
python main.py
```

## 6. Application Menu

After executing the application, the following menu is displayed:

```text
========== PERSONAL EXPENSE TRACKER ==========

1. Add Expense
2. View All Expenses
3. Generate Reports
4. Visualize Expenses
5. Exit
```

Select the required option by entering its corresponding number.

## 7. Data Storage

The application stores expense records in:

```text
data/expenses.csv
```

Each expense record contains the following fields:

- Amount
- Category
- Date
- Description

Previously saved records are automatically loaded when the application starts. New and existing records are saved when the user exits the application.

## 8. Reports and Visualizations

The application generates financial reports and graphical representations to help users understand their spending patterns.

The available visualizations include:

1. Category-wise Expense Analysis – Bar Chart
2. Category-wise Expense Distribution – Pie Chart
3. Weekly Expense Analysis – Bar Chart
4. Monthly Expense Analysis – Bar Chart

## 9. Error Handling and Validation

The application includes validation and error-handling mechanisms to improve reliability.

- Prevents non-numeric and non-positive expense amounts.
- Validates dates using the `YYYY-MM-DD` format.
- Prevents empty categories and descriptions.
- Handles invalid menu selections.
- Handles invalid CSV records.
- Handles missing or invalid CSV files.

## 10. Learning Outcomes

This project demonstrates practical implementation of:

- Python functions and modular programming
- Lists and dictionaries
- Loops and conditional statements
- Exception handling using `try-except`
- CSV file handling
- Date validation using the `datetime` module
- Data analysis and aggregation
- Data visualization using Matplotlib

## 11. Project Information

**Project Name:** Personal Expense Tracker

**Project Type:** Major Internship Project

**Internship Domain:** Data Science and Artificial Intelligence

**Programming Language:** Python

