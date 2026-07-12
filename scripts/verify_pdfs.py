"""Verify page geometry, metadata, and text extraction for compiled templates."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
LETTER_WIDTH = 612.0
LETTER_HEIGHT = 792.0


@dataclass(frozen=True)
class ExpectedPdf:
    path: Path
    pages: int
    title: str
    author: str
    markers: tuple[str, ...]


TARGETS = (
    ExpectedPdf(
        ROOT / "src" / "resume.pdf",
        pages=1,
        title="Ethan Villalovoz - Technical Resume",
        author="Ethan Villalovoz",
        markers=("ETHAN VILLALOVOZ", "EDUCATION", "TECHNICAL SKILLS"),
    ),
    ExpectedPdf(
        ROOT / "src" / "starter-resume.pdf",
        pages=1,
        title="First Last - Technical Resume",
        author="First Last",
        markers=("FIRST LAST", "EXPERIENCE", "PROJECTS"),
    ),
    ExpectedPdf(
        ROOT / "src" / "cv" / "cv.pdf",
        pages=2,
        title="Ethan Villalovoz - Academic CV",
        author="Ethan Villalovoz",
        markers=("Ethan Villalovoz", "Research Interests", "Conference Publications"),
    ),
    ExpectedPdf(
        ROOT / "src" / "cv" / "starter-cv.pdf",
        pages=1,
        title="First Last - Academic CV",
        author="First Last",
        markers=("First Last", "Research Interests", "Conference Publications"),
    ),
)


def _metadata_value(reader: PdfReader, key: str) -> str:
    metadata = reader.metadata or {}
    return str(metadata.get(key, "")).strip()


def verify(target: ExpectedPdf) -> None:
    if not target.path.is_file():
        raise RuntimeError(f"missing compiled PDF: {target.path.relative_to(ROOT)}")

    reader = PdfReader(target.path)
    if len(reader.pages) != target.pages:
        raise RuntimeError(
            f"{target.path.name}: expected {target.pages} pages, found {len(reader.pages)}"
        )

    if _metadata_value(reader, "/Title") != target.title:
        raise RuntimeError(
            f"{target.path.name}: missing or incorrect PDF title metadata"
        )
    if _metadata_value(reader, "/Author") != target.author:
        raise RuntimeError(
            f"{target.path.name}: missing or incorrect PDF author metadata"
        )

    page_text: list[str] = []
    for index, page in enumerate(reader.pages, start=1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        if abs(width - LETTER_WIDTH) > 1 or abs(height - LETTER_HEIGHT) > 1:
            raise RuntimeError(f"{target.path.name}: page {index} is not US Letter")
        text = (page.extract_text() or "").strip()
        if len(text) < 80:
            raise RuntimeError(
                f"{target.path.name}: page {index} has insufficient extractable text"
            )
        page_text.append(text)

    combined = "\n".join(page_text)
    normalized = " ".join(combined.split()).casefold()
    for marker in target.markers:
        if " ".join(marker.split()).casefold() not in normalized:
            raise RuntimeError(
                f"{target.path.name}: extracted text is missing {marker!r}"
            )
    if "\ufffd" in combined:
        raise RuntimeError(
            f"{target.path.name}: extracted text contains replacement characters"
        )

    relative = target.path.relative_to(ROOT)
    print(
        f"verified {relative}: {target.pages} page(s), metadata and text extraction intact"
    )


def main() -> None:
    for target in TARGETS:
        verify(target)


if __name__ == "__main__":
    main()
