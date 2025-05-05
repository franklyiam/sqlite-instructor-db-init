# SQLite Instructor DB Init

This Python script demonstrates how to initialize a SQLite database, load data from a CSV file into a table, perform basic SQL queries using `pandas`, and append new records. It's ideal for beginners working with SQLite and Python-based data manipulation.

## 🧩 Features

- Creates a SQLite database named `STAFF.db`
- Loads instructor data from a CSV file into a table named `INSTRUCTOR`
- Executes basic SQL queries:
  - View all records
  - Select specific columns
  - Count total entries
- Appends new data to the existing table
- Closes the database connection properly after execution

## 📂 Project Structure

```
sqlite-instructor-db-init/
│
├── INSTRUCTOR.csv          # CSV file containing instructor data
├── script.py               # Main Python script
└── README.md               # This file
```

## 🛠️ Requirements

- Python 3.x
- pandas
- sqlite3 (comes with Python by default)

Install dependencies (if `pandas` is not already installed):

```bash
pip install pandas
```

## 🚀 How to Run

1. Place your `INSTRUCTOR.csv` file in the project directory.
2. Run the script:

```bash
python script.py
```

## 📋 Sample CSV Format (`INSTRUCTOR.csv`)

Ensure the file follows this structure (no header row, just values):

```
1,Jane,Doe,New York,US
2,Bob,Smith,London,UK
```

## 🧹 Notes

- The script uses `if_exists='replace'` to recreate the table each time it runs.
- Make sure `INSTRUCTOR.csv` is formatted correctly and exists in the working directory.

## 📜 License

This project is licensed under the MIT License.
