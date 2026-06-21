# 💼 Ethan's LaTeX Resume & Academic CV Template

[![CI](https://github.com/ethanvillalovoz/latex-resume-template/actions/workflows/ci.yml/badge.svg)](https://github.com/ethanvillalovoz/latex-resume-template/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
![Overleaf Compatible](https://img.shields.io/badge/overleaf-supported-success)

---

## 🚀 Introduction

A clean, ATS-friendly LaTeX resume template and a companion academic CV template designed for clarity, credibility, and easy customization.

The repository includes:
- A modern one-page technical resume based on Jake's Resume
- A two-page academic CV based on a classic `res.cls` layout
- Blank starter files for both the resume and academic CV
- Rendered PDF previews for both documents
- A GitHub Actions workflow that compiles every TeX entry point automatically

---

## 📋 Description

The resume template emphasizes:
- **Minimalist one-page layout** for technical recruiting
- **Machine-readable PDF output** for ATS compatibility
- **Compact sections** for education, experience, publications, projects, and skills
- **Visible but conservative link styling** using `#0a5994`

The CV template emphasizes:
- **Academic ordering** with research interests, education, publications, experience, awards, teaching, and outreach
- **Advisor and publication context** for research-oriented applications
- **Readable two-page structure** without forcing resume-style compression

---

## 🖼️ Visuals

### Resume

![Resume Preview](docs/preview.png)

### Academic CV

![Academic CV Preview](docs/cv-preview.png)

---

## 🛠️ Technologies Used

- **LaTeX** (core typesetting)
- **Resume packages**: `fullpage`, `titlesec`, `marvosym`, `tabularx`, `hyperref`, `fancyhdr`, `enumitem`, `xcolor`
- **CV class**: `res.cls` with `tabularx`, `hyperref`, and `xcolor`
- **PDF output**: ATS-friendly, machine-readable
- **Platforms**: Overleaf, local LaTeX workflows, and GitHub Actions

---

## 📖 About the Template

Curious about the design philosophy, technical choices, and why this template works so well for technical roles?  

See [docs/ABOUT.md](docs/ABOUT.md) for a deep dive into the reasoning behind the layout, ATS compatibility, and customization features.

See [docs/COMPANIES.md](docs/COMPANIES.md) for a list of companies where this resume has earned me interview opportunities for both internships and full-time roles.

See [docs/FAQ.md](docs/FAQ.md) for common Overleaf, compiler, and customization questions.

---

## ⚡ Quick Start (Overleaf)

1. **Download or clone the repository:**
   ```bash
   git clone https://github.com/ethanvillalovoz/latex-resume-template.git
   ```
   or simply click **“Download ZIP”** from GitHub.

2. **Upload to Overleaf:**
   - Go to [Overleaf](https://overleaf.com/)
   - Create a **New Project → Upload Project**
   - Upload the entire `src/` folder

3. **Edit and compile:**
   - Start from `src/starter-resume.tex` for a blank resume
   - Start from `src/cv/starter-cv.tex` for a blank academic CV
   - Use `src/resume.tex` and `src/cv/cv.tex` as polished examples
   - Click **Recompile** to generate your PDF
   - Download the final PDF

For the CV, keep `src/cv/res.cls` in the same folder as `cv.tex` or `starter-cv.tex`.

---

## 🔧 Customization

- **Contact Info**: Update your name, email, phone, and links at the top of `resume.tex`
- **Section Content**: Use `\resumeItem{}` for bullet points and `\resumeSubheading{}` for roles or education
- **Bold Technologies**: Use `\textbf{}` to highlight programming languages or tools
- **Style Adjustments**: Modify the preamble to change fonts, spacing, or colors
- **Starter Files**: Copy `src/starter-resume.tex` or `src/cv/starter-cv.tex` when building your own document
- **Academic CV**: Keep `src/cv/res.cls` alongside `cv.tex` or `starter-cv.tex` for compilation

---

## 🗂️ Repository Structure

```
latex-resume-template/
├── .github/                 # GitHub templates and workflows
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/           # CI workflow for PDF builds
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/                    # Documentation, previews, and rendered PDFs
│   ├── ABOUT.md
│   ├── COMPANIES.md
│   ├── FAQ.md
│   ├── preview.png
│   ├── resume.pdf
│   ├── cv-preview.png
│   └── cv.pdf
├── src/                     # LaTeX source files
│   ├── resume.tex
│   ├── starter-resume.tex
│   └── cv/
│       ├── cv.tex
│       ├── starter-cv.tex
│       └── res.cls
├── .gitattributes
├── .gitignore
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

---

## 🛣️ Roadmap

- [x] Overleaf-only version for easier use  
- [x] Add academic CV source and preview
- [x] Add Publications section support
- [x] Add blank starter files for public reuse
- [x] Expand documentation with FAQ and contribution standards
- [ ] Provide alternate color schemes

---

## 🤝 Contribution

Contributions are welcome!  
To contribute:
1. Fork the repo and create a new branch  
2. Make your improvements (e.g., design tweaks, doc edits)  
3. Open a pull request with a clear description  

For more details, see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 📜 License

MIT License — free to use, modify, and share. Attribution appreciated, but not required.

---

## 💬 Contact

If this template helps you land an interview or job, I’d love to hear about it!  

Reach out at **ethan.villalovoz@gmail.com**
