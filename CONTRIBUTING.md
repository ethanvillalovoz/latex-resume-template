# Contributing

Contributions should preserve readable typography, clean text extraction, and a low-friction Overleaf workflow.

## Setup

Install TeX Live with XeLaTeX and `latexmk`, then:

```sh
git clone https://github.com/ethanvillalovoz/latex-resume-template.git
cd latex-resume-template
python3 -m pip install -r requirements-dev.txt
make check
```

## Before A Pull Request

1. Compile all four TeX entry points with `make check`.
2. Inspect every changed page at normal zoom and in grayscale.
3. Confirm section labels, dates, links, and long lines do not collide or clip.
4. Regenerate `docs/*.pdf` and preview PNGs with `make previews` when output changes.
5. Review extracted text for reading order and uncommon-character failures.
6. Update documentation and `CHANGELOG.md` when behavior changes.

## Scope

- Keep template changes focused and generally useful.
- Preserve the one-page contract for both resume files.
- Preserve the two-page example CV unless a pull request explicitly justifies a structural change.
- Avoid optional fonts, shell escape, or platform-specific packages without a strong reason.
- Do not include customized resumes with private contact details in issues or fixtures.
- Retain third-party attribution and embedded class notices.

## Generated Files

The example PDFs and first-page PNGs are committed so visitors can inspect the templates without compiling LaTeX. They must correspond to the current example sources. Starter PDFs are CI artifacts and are not committed.

## Reporting Problems

Use the structured issue form and include the affected document, compiler, TeX distribution, minimal reproduction, and sanitized log. Remove personal information from screenshots and customized source.

Please follow the [Code of Conduct](CODE_OF_CONDUCT.md).
