# FAQ

## Which file should I edit?

Use `src/starter-resume.tex` for technical recruiting and `src/cv/starter-cv.tex` for research, fellowship, lab, or graduate-school contexts. The other two TeX files are complete examples.

## Which compiler should I use?

Use XeLaTeX. CI pins TeX Live 2026 and compiles through `latexmk` with XeLaTeX. The sources can also compile under pdfLaTeX, but the automated path is the supported reference.

## Can I use Overleaf?

Yes. Upload the repository ZIP, choose the relevant starter as the main document, and select XeLaTeX. Keep `res.cls` in the same directory as the academic CV source.

## Is the output ATS-friendly?

The output is text-based and extraction-tested. CI checks that each page contains readable text and expected section markers. ATS implementations differ, so paste text extracted from your final PDF into a plain-text editor and inspect its order before submitting.

## Why are links blue?

Muted blue makes interactive text discoverable in a PDF without turning the document into a web page. Change `cvblue` in the preamble if you need a different accessible color. Verify the result in color and grayscale.

## How do I keep the resume to one page?

Trim weak bullets, older projects, generic coursework, and redundant tools first. Do not shrink below readable type or compress spacing until entries touch. A strong one-page resume should feel selected, not squeezed.

## Should I keep Publications?

Keep peer-reviewed work, meaningful preprints, or research artifacts when they support the role. Remove the section when it contains class reports or unrelated writing.

## How should I identify myself in an author list?

The example resume uses bold and the CV uses underline. Pick one convention per document and explain equal contribution or corresponding authorship only when the publication does.

## Why does the CV include more categories?

Academic readers need publication status, advisors, teaching, awards, and service context. These categories often matter more than squeezing every entry into a one-page recruiting format.

## How do I update PDF metadata?

Edit the `\hypersetup` block near the top of the chosen source. Replace title, author, subject, and keywords before publishing your customized PDF.

## What does `make check` require?

Install TeX Live with XeLaTeX and `latexmk`, then install `requirements-dev.txt`. The check compiles all examples and starters before running `scripts/verify_pdfs.py`.

## Can I delete the example personal information?

Yes. You should use a starter file for your own document. If you fork the repository publicly, review source files, rendered PDFs, preview PNGs, commit history, and PDF metadata for information you do not intend to publish.
