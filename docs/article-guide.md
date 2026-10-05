# Article Draft Guide

**Title**: Scanning Vulnerabilities in a Flask Web Application Using Semgrep, GitHub Actions and Render

**Structure:**

- **Introduction**: Introduce DevSecOps and the need to shift-left in security.
- **Objective**: Explain the creation of Secure Notes to demonstrate the flow.
- **What is SAST?**: Define SAST.
- **Why Semgrep?**: Mention its speed and customizability.
- **Application architecture**: Describe the Flask/SQLite stack.
- **Building Secure Notes**: Overview of the coding process.
- **Introducing an insecure pattern**: Show the string concatenation vulnerability.
- **Running Semgrep**: Detail the command and configuration.
- **Vulnerability analysis**: Explain the Semgrep finding output.
- **Fixing the issue**: Show the change to parameterized queries.
- **Running the scanner again**: Show the clean scan.
- **Automating the scan with GitHub Actions**: Explain the `security.yml` file.
- **Deploying automatically**: Explain Render's CI/CD connection.
- **Publishing the application on Render**: Describe the public deployment.
- **Results**: Summarize what was achieved.
- **Lessons learned**: What the project taught about automated security.
- **Conclusions**: Final thoughts on DevSecOps in academia.
- **Repository**: [ADD GITHUB URL]
- **Live application**: [ADD RENDER URL]
- **Video**: [ADD VIDEO URL]
- **References**: Mention Flask docs, Semgrep docs, OWASP.
