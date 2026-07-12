LATEXMK ?= latexmk
LATEX_FLAGS := -xelatex -file-line-error -halt-on-error -interaction=nonstopmode

.PHONY: install build build-resume build-cv verify previews check clean

install:
	python3 -m pip install -r requirements-dev.txt

build: build-resume build-cv

build-resume:
	cd src && $(LATEXMK) $(LATEX_FLAGS) resume.tex starter-resume.tex

build-cv:
	cd src/cv && $(LATEXMK) $(LATEX_FLAGS) cv.tex starter-cv.tex

verify: build
	python3 scripts/verify_pdfs.py

previews: verify
	cp src/resume.pdf docs/resume.pdf
	cp src/cv/cv.pdf docs/cv.pdf
	pdftoppm -f 1 -singlefile -png -r 144 src/resume.pdf docs/preview
	pdftoppm -f 1 -singlefile -png -r 144 src/cv/cv.pdf docs/cv-preview

check: verify

clean:
	cd src && $(LATEXMK) -C resume.tex starter-resume.tex
	cd src/cv && $(LATEXMK) -C cv.tex starter-cv.tex
