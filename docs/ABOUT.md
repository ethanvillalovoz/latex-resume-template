# 🧠 Behind the Resume and CV: Why These Templates Work

This LaTeX template repository was created and refined by Ethan Villalovoz to support two public-facing career documents:

- a concise, ATS-friendly technical resume for software engineering, AI/ML, robotics, and research engineering roles
- an academic CV for research-oriented contexts where publications, advisors, teaching, and outreach matter

Both documents are intentionally conservative: readable typography, semantic text, visible links, and no visual tricks that make the PDF harder to parse.

---

## 🎯 Purpose & Audience

The resume template is designed for:
- Students and early-career professionals applying to **internships**, **fellowships**, **research roles**, and **new grad tech positions**
- Developers and researchers looking to showcase **projects**, **technical skills**, and **experience** concisely
- Anyone who wants a **LaTeX-powered**, fully customizable resume with clean formatting

The academic CV template is designed for:
- Research-oriented students and early-career researchers
- Academic websites, graduate applications, lab applications, and research programs
- Situations where publications, teaching, advisors, and outreach should not be compressed into a one-page resume

---

## ✅ Why the Resume Template Works

### 📌 1. **ATS-Compatible & PDF-Readable**
- Uses `\pdfgentounicode=1` to ensure machine-readable output
- Avoids tables and graphics that can break ATS parsing
- Prioritizes semantic structure (e.g., headings, bullet points, links)

### 🎨 2. **Minimalist & Scannable**
- Clear, single-page layout with tightly controlled spacing
- Bolded **technologies** and **key phrases** improve skimmability
- Focused on high-impact bullet points with quantifiable results

### ✍️ 3. **Bullets Emphasize Evidence**
Strong bullets usually follow the **XYZ formula** when it fits naturally:
> **"Accomplished X, by doing Y, as measured by Z"**

This ensures:
- Every line demonstrates **impact**, not just responsibility
- You communicate both **technical depth** and **business value**
- Recruiters and hiring managers immediately understand your contributions

Example:
> “Optimized data sampling strategies to scale job execution from **1% to 100%** within **4 hours**, achieving a **66% reduction in runtime**”

### 🛠 4. **Custom LaTeX Commands for Reusability**
- `\resumeItem{}` for clean bullet formatting
- `\resumeSubheading{}` and `\resumeProjectHeading{}` for layout consistency
- Easy to add sections or modify spacing using defined macros

### 💡 5. **Tailored for Technical Roles**
- Shows off technical depth with sections like:
  - **Technical Skills** (grouped by purpose)
  - **Projects** with tech stacks and outcomes
  - **Experience** with clear, outcome-driven bullet points

---

## 🎓 Why the Academic CV Template Works

The CV is not a stretched resume. It is a scholarly record, so it uses a different structure:

- **Research Interests** appear near the top to establish academic direction.
- **Publications** are placed before experience because peer-reviewed and preprint work carry research signal.
- **Experience** entries are concise and include advisors when relevant.
- **Teaching, awards, and outreach** are preserved as academic evidence rather than trimmed for one-page density.
- The template accepts healthy page-two whitespace instead of padding weak content.

---

## 🔍 Design Highlights

| Feature                     | Description |
|----------------------------|-------------|
| 🧩 Modular Commands         | Custom LaTeX macros for education, work, and projects |
| 📄 ATS-Friendly PDF         | Machine-readable format, no images or messy tables |
| ⚡ High Signal-to-Noise     | No fluff—only relevant experience and achievements |
| 🧠 Smart Emphasis           | Uses `\textbf{}` selectively to guide recruiter focus |
| 🌐 Linkable Metadata        | Contact info, GitHub, LinkedIn, and personal site at the top |

---

## 🧰 Tools & Packages Used

- Resume: `fullpage`, `titlesec`, `marvosym`, `tabularx`, `hyperref`, `fancyhdr`, `enumitem`, `xcolor`, and `glyphtounicode`
- CV: `res.cls`, `tabularx`, `hyperref`, and `xcolor`
- Preambles are tuned for readability, layout control, and PDF text extraction

---

## 🤝 Want to Use or Adapt It?

Feel free to:
- Fork the repo
- Start from `src/starter-resume.tex` for a blank resume
- Start from `src/cv/starter-cv.tex` for a blank academic CV
- Use `src/resume.tex` and `src/cv/cv.tex` as polished examples
- Tweak formatting using the LaTeX macros and class files
- Use Overleaf for no-install editing

---

## 💬 Creator Note

> "I made this because I never found a LaTeX resume that felt both modern and practical for tech applications. I believe resume templates should be free, accessible, and optimized for real success — not gatekept behind templates that lack substance or clarity."  
>
> — *Ethan Villalovoz*

---

## 📜 License

This resume template is open-source under the MIT License. Attribution is appreciated but not required.
