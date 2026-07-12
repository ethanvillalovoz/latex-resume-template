# Why These Layouts Work

This repository separates two documents that are often forced into one format.

## Technical Resume

The resume is a one-page decision surface for technical recruiting. Its hierarchy makes four questions easy to answer quickly:

1. What has this person worked on?
2. What did they personally own?
3. How technically deep was the work?
4. What evidence shows that it mattered?

The layout supports that scan with compact section rules, aligned organizations and dates, short role lines, and bullets that preserve enough width for technical detail. Selective bolding identifies systems, methods, and measured outcomes; it should not turn every noun into emphasis.

The starter includes education, experience, publications, projects, and skills because that combination works for early-career software, AI/ML, robotics, and research-engineering candidates. Remove a section when it is weak rather than keeping it for symmetry.

## Academic CV

The CV is a scholarly record, not an expanded resume. It introduces research direction first, then separates preprints and peer-reviewed publications before experience. Advisor names, teaching, awards, and outreach remain visible because they provide useful context for labs, fellowships, and graduate applications.

The left-margin section labels create a stable navigation column while the wider body column carries citations and research descriptions. Healthy page-two whitespace is preferable to padding the document with low-signal entries.

## PDF And Extraction Choices

- Both templates use ordinary text rather than image-based content.
- XeLaTeX produces selectable Unicode text without requiring custom fonts.
- Contact links are visible in a muted blue and remain clickable.
- PDF title, author, subject, and keyword metadata are explicit.
- CI checks US Letter geometry, expected page counts, section markers, and extracted text.

The resume does use alignment tables internally. What matters for downstream systems is the resulting PDF text order, which the verification script checks. ATS products still vary, so test the exact PDF you submit.

## Writing Strong Content

A useful bullet usually identifies an action, a technical mechanism, and an outcome. Quantification helps when it describes a real scale, latency, accuracy, cost, adoption, or reliability change. It should not be invented to satisfy a formula.

Prefer:

> Built five C++/SQL analytics jobs and scaled metric computation from 1% to full dataset coverage within four hours, reducing runtime by 66%.

Avoid responsibility-only lines that could describe anyone on the team.

## Evidence From Use

The example format has accompanied interview opportunities across research labs, large technology companies, and robotics organizations. That observation does not establish that layout caused the outcomes; content, experience, timing, referrals, and role fit matter more. The record is documented in [Observed Interview Outcomes](COMPANIES.md) for transparency rather than as a guarantee.
