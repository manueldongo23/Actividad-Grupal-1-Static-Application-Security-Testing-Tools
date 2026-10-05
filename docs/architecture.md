# Architecture

This document explains the architecture of the DevSecOps process.

1. **Developer**: Writes code and tests locally. Commits code containing educational flaws to learn how the pipeline catches them.
2. **GitHub**: Stores the repository, providing version control and triggering webhooks.
3. **GitHub Actions**: Acts as the CI/CD orchestrator.
   - **CI Workflow**: Tests the application functionality.
   - **Security Workflow**: Runs Semgrep SAST to scan for vulnerabilities.
4. **Semgrep**: Identifies insecure code patterns (like SQL Injection).
5. **Render**: The cloud provider. Listens to branch changes. If CI and security scans pass, it automatically builds and deploys the new version.
6. **Public Web App**: End users access the fully secure, updated application.
