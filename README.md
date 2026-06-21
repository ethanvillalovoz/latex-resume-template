# 💼 Ethan's LaTeX Resume & Academic CV Template

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License: MIT](https://img.shields.io/badge/license-MIT-blue)
![Overleaf Compatible](https://img.shields.io/badge/overleaf-supported-success)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue)

---

## 🚀 Introduction

A clean, ATS-friendly LaTeX resume template and a companion academic CV template designed for clarity, credibility, and easy customization.

The repository includes:
- A modern one-page technical resume based on Jake's Resume
- A two-page academic CV based on a classic `res.cls` CV layout
- Source files that compile cleanly on Overleaf or with a local LaTeX installation

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
- **Platform**: Overleaf for online editing and compilation

---

## 📖 About the Template

Curious about the design philosophy, technical choices, and why this template works so well for technical roles?  

See [docs/ABOUT.md](docs/ABOUT.md) for a deep dive into the reasoning behind the layout, ATS compatibility, and customization features.

See [docs/COMPANIES.md](docs/COMPANIES.md) for a list of companies where this resume has earned me interview opportunities for both internships and full-time roles.

---

## ⚡ QuickStart Guide (Overleaf)

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
   - Modify your resume in `src/resume.tex`
   - Modify your academic CV in `src/cv/cv.tex`
   - Click **Recompile** to generate your PDF
   - Download the final PDF

For the CV, keep `src/cv/res.cls` in the same folder as `cv.tex`.

---

## 🔧 Customization

- **Contact Info**: Update your name, email, phone, and links at the top of `resume.tex`
- **Section Content**: Use `\resumeItem{}` for bullet points and `\resumeSubheading{}` for roles or education
- **Bold Technologies**: Use `\textbf{}` to highlight programming languages or tools
- **Style Adjustments**: Modify the preamble to change fonts, spacing, or colors
- **Academic CV**: Edit `src/cv/cv.tex`; keep the `res.cls` file alongside it for compilation

---

## 🗂️ Folder Structure

```
latex-resume-template/
├── .github/                 # GitHub templates and workflows
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/           # CI/CD workflows for automated PDF build & deploy
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/                    # Documentation and preview
│   ├── ABOUT.md
│   ├── preview.png
│   ├── resume.pdf
│   ├── cv-preview.png
│   └── cv.pdf
├── src/                     # LaTeX source files
│   ├── resume.tex
│   ├── cv/
│   │   ├── cv.tex
│   │   └── res.cls
│   └── prev_resume/
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

---

## 🛣️ Roadmap

- [x] Overleaf-only version for easier use  
- [x] Add academic CV source and preview
- [x] Add Publications section support
- [ ] Provide alternate color schemes  
- [ ] Expand documentation (FAQ, troubleshooting)

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
