# Security Analysis

## What is SAST?
Static Application Security Testing (SAST) analyzes source code to find security vulnerabilities without executing the program.

## What is Semgrep?
Semgrep is a fast, open-source SAST tool that uses simple patterns to find bugs and security issues in code.

## Demonstrated Vulnerability
**SQL Injection (SQLi) CWE-89**
We demonstrate how an attacker can manipulate database queries if user input is not properly sanitized.

### Vulnerable Example
```python
# DO NOT USE
query = "SELECT * FROM notes WHERE title LIKE '%" + search_term + "%'"
cursor.execute(query)
```
*Risk*: An attacker providing `' OR '1'='1` can bypass the intended query logic.

### Corrected Code
```python
# SECURE IMPLEMENTATION
cursor.execute("SELECT * FROM notes WHERE title LIKE ?", (f'%{search_term}%',))
```
*Why it works*: Parameterized queries separate the SQL logic from the data. The database engine treats the input strictly as a parameter, not as executable SQL code.

## How to run Semgrep
```bash
semgrep --config auto --config .semgrep.yml .
```

## Results
- **Before**: [Screenshot: Semgrep finding]
- **After**: [Screenshot: Secure code passing scan]

## Suggested Git Commits for Video
- Commit 1: Introduce educational vulnerable search example
- Commit 2: Demonstrate Semgrep detection
- Commit 3: Fix SQL query using parameterized query
- Commit 4: Confirm successful security scan
