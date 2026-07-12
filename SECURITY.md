# Security And Privacy

## Report A Problem

Use GitHub's private vulnerability reporting when available. Do not publish another person's resume, contact details, application history, or PDF metadata in a public issue.

## Document Privacy

Resume source and rendered PDFs can contain phone numbers, email addresses, locations, citizenship or work authorization, education history, and links to personal profiles. Before publishing a fork or attaching a reproduction:

- start from a neutral starter file
- remove contact details and sensitive history
- inspect PDF title, author, subject, and keywords
- inspect committed preview images and PDFs
- remember that deleting a file does not remove it from Git history

## LaTeX Safety

Compile untrusted TeX in an isolated environment. LaTeX can read local files and, when shell escape is enabled, execute commands. This repository does not require shell escape. CI uses a containerized action and does not accept arbitrary user-submitted source at runtime.

Avoid adding packages or build flags that enable network access, shell execution, or writes outside the project unless the security impact is documented and reviewed.

## Dependencies

The build uses TeX Live, `latexmk`, XeLaTeX, a containerized GitHub Action, and `pypdf` for verification. Dependabot monitors Python and GitHub Actions dependencies. Third-party behavior and vulnerabilities remain outside this repository's direct control.
