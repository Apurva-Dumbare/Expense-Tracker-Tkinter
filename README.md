# Expense Tracker Application

## Overview
The **Expense Tracker Application** is a simple and user-friendly tool designed to track daily expenses. It allows users to add, view, and analyze their expenses efficiently. This application saves data to a CSV file for persistent storage and avoids duplicate entries.

## Features

### 1. **Add Expenses**
- Users can add items with details such as:
  - Item name
  - Quantity
  - Unit cost
  
- The application calculates the total amount for each item automatically.

### 2. **View Expenses**
- Displays all added items in the application window.
- Shows details such as:
  - Item name
  - Quantity
  - Unit cost
  - Total cost

### 3. **Persistent Storage**
- All expense data is saved in a CSV file (`expense_tracker.csv`).
- Prevents duplicate entries by appending only new items to the CSV file.

### 4. **Analyze Expenses**
- Visualize expenses using a bar chart.
- Provides insights into spending patterns, such as total cost per item.

## Prerequisites
To run the Expense Tracker Application, ensure the following are installed on your system:

- Python 3.x
- Required Python libraries:
  - `tkinter`
  - `pandas`
  - `matplotlib`

## Installation
1. Clone the repository or download the project files.
2. Install the required libraries using pip:
   ```bash
   pip install pandas matplotlib
   ```
3. Save the script to a file named `expense_tracker.py`.

## Usage
1. Run the script:
   ```bash
   python expense_tracker.py
   ```
2. Enter details for an item (name, quantity, and cost).
3. Click "Add Item" to add the expense.
4. Click "Clear" to clear the input fields.
5. View the list of expenses in the application window.
6. Click "Analyze" to visualize the expense data as a bar chart.


## Acknowledgements
- Built using the Python `tkinter` library for the GUI.
- Used `pandas` for data handling and `matplotlib` for data visualization.

