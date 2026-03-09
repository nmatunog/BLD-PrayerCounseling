# Source Audit — Prayer Counseling Seminar I Workbook

## Source files (in `Sources/`)

| Workbook section | Source file |
|-----------------|-------------|
| **Module 1** — Seminar Introduction, 7 Healing Ingredients | `MODULE 1. INTRO -PRAYER-COUNSELING-2023FEB11-noel.pptx` |
| **Module 2** — Repentance and Restitution | `MODULE 2-REPENTANCE-AND-RESTITUTION-2026-BY-AIMEE.pptx` |
| **Module 3** — Forgiveness, Forgiveness Prayer | `MODULE 3- ACCOMPLISHING_FORGIVENESS-FEB-2023.pptx` |
| **Module 4** — Bitter Roots (workbook Module 5) | `MODULE 4 2026-BITTER-ROOTS-FINAL.ppt` |
| **Modules 5–7** — Bitter Roots, Heart of Stone, Inner Vows / Foundations | `MODULE 5 -6-7 Bitter-Root-Hearts-of-Stone-and-Inner-Vows_LeeFeb2023-pdf.pdf` |
| **Module 8** — Honoring Father and Mother | `MOULE 8 - HONORING-FATHER-MOTHER-FINAL.ppt` |

*Note: Workbook “Module 4: Counselor Roles” may draw from seminar materials not in the above list; “Module 8: Mission” is closing content.*

## Fidelity rule
Content in this workbook must keep **100% integrity and fidelity** to the source material (seminar slides/PDFs). Only slight corrections for grammar and structure are allowed. **Do not summarize** source text.

## Bible & CCC
- **Bible:** All quotations use the **NABRE** (New American Bible, Revised Edition). Every citation is shown in an expansion card with a "Source: NABRE" tag.
- **CCC:** Catechism of the Catholic Church references are in expansion cards with full paragraph text and "Source: Catechism of the Catholic Church."

## Extraction
- Run `python3 scripts/extract_pptx_text.py "Sources/<filename>.pptx"` to extract slide text to stdout.
- Extracted Module 1 text saved as `Sources/extracted-module1.txt` for reference.

## Audit steps
1. Open the source file for the module (see table above).
2. Compare each slide/page to the matching section in `public/index.html`.
3. Restore any omitted or summarized text; add Bible/CCC refs as expansion cards via `bibleBtn()` and `cccBtn()`.

## Alignment status
- **Module 1** (INTRO): Aligned — intro (Welcome, Objectives, House Rules), 7 Ingredients (source wording + refs), Four Primary Laws, Small Groups.
- **Module 2** (Repentance and Restitution): Aligned — CCC 1442/1468, remorse vs repentance, restitution, Luke 19:8-9, 2 Chron 7:14, prayer of repentance.
- **Module 3** (Accomplishing Forgiveness): Aligned — definition, foundation verse, Forgiveness is NOT, obstacles, four levels of wounding, role of prayer partner, closing thoughts.
- **Module 8** (Honoring Father and Mother): Aligned — intro, fourth commandment (CCC), law absolute (Ex 20:12, Dt 5:16), sowing/reaping, dishonor, personhood vs performance, formation, process of healing, sample prayers, reflection questions, concluding thoughts. Reflective layout; journal per section; download already available.
- **Modules 4–7**: Pending alignment with MODULE 4 2026-BITTER-ROOTS-FINAL.ppt and MODULE 5 -6-7 … PDF.

## Journal & download
- Journal entries are saved automatically in this browser/device (localStorage).
- "Download full workbook" exports all section content (plain text) plus your journal notes.
- "Download journal only" exports only your notes.
