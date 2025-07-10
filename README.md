# 💼 Ethan's LaTeX Resume Template

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License: MIT](https://img.shields.io/badge/license-MIT-blue)
![Overleaf Compatible](https://img.shields.io/badge/overleaf-supported-success)

---

## 🚀 Introduction

A clean, ATS-friendly, and professional LaTeX resume template designed for clarity, impact, and easy customization. Perfect for students, early-career professionals, and anyone who wants a modern, one-page resume.

---

## 📋 Description

This template emphasizes:
- **Minimalist, one-page layout** for maximum readability
- **Bold tech stacks** and modular bullet points for easy scanning
- **Machine-readable PDF output** for ATS compatibility
- **Easy customization** with clear LaTeX commands

---

## 🖼️ Visuals

![Resume Preview](./preview.png)

---

## 📦 Prerequisites

- **LaTeX distribution**: [TeX Live](https://www.tug.org/texlive/) (Linux/Windows) or [MacTeX](https://tug.org/mactex/) (macOS)
- (Optional) [Overleaf](https://overleaf.com/) account for online editing

---

## 🛠️ Technologies Used

- **LaTeX** (core typesetting)
- **Packages**: `fullpage`, `titlesec`, `marvosym`, `fontawesome5`, `tabularx`, `multicol`, `hyperref`, `fancyhdr`, `enumitem`, `geometry`
- **PDF output**: ATS-friendly, machine-readable

---

## ⚡ QuickStart Guide

1. **Clone the repo:**
   ```bash
   git clone https://github.com/ethanvillalovoz/latex-resume-template.git
   cd latex-resume-template
   ```

2. **Build the resume locally:**
   ```bash
   pdflatex resume.tex
   ```

3. **Or use Overleaf:**
   - Upload `resume.tex` to [Overleaf](https://overleaf.com/)
   - Edit and download your PDF

---

## 🔬 Advanced Usage

- **Customize sections**: Edit or add sections in `resume.tex` as needed.
- **Add new commands**: Define your own LaTeX commands for repeated patterns.
- **Change fonts or colors**: Modify the preamble to adjust style.
- **ATS optimization**: Avoid images or graphics in the main content.

---

## ⚙️ Configuration

- **Contact Info**: Update your name, email, phone, and links at the top of `resume.tex`.
- **Section Content**: Use `\resumeItem{}` for bullet points and `\resumeSubheading{}` for roles/education.
- **Bold Technologies**: Use `\textbf{}` for highlighting tools and languages.

---

## 🧪 Automated Test

To verify your LaTeX installation and template build:
```bash
pdflatex resume.tex
# Check for resume.pdf output and no errors in the log
```

---

## 🗂️ Folder Structure

```
latex-resume-template/
├── resume.tex        # Main LaTeX source file
├── resume.pdf        # Compiled sample (not versioned)
├── preview.png       # Screenshot preview
├── LICENSE           # MIT License
└── README.md         # This file
```

---

## 🛣️ Roadmap

- [ ] Add more resume section templates (e.g., Publications, Awards)
- [ ] Provide alternate color schemes
- [ ] Add CI for automated PDF builds
- [ ] Expand documentation (FAQ, troubleshooting)

---

## 🤝 Contribution

Contributions are welcome! To contribute:
- Fork the repo and create a new branch
- Make your changes (improve template, docs, or add features)
- Open a pull request with a clear description

For more details, see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 📜 License

MIT License — free to use, modify, and share. Attribution appreciated, but not required.

---

## 💬 Contact

If this template helps you land an interview or job, I’d love to hear about it!  
Feel free to reach out: ethan.villalovoz@gmail.com
