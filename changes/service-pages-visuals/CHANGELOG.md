# Service page visual changes (2026-11-19)

Goal: break up text-heavy service pages. Applied to 5 English pages and their 5 Spanish translations.

| Page | English ID | Spanish ID |
|------|-----------|-----------|
| Divorce (DOM) | 110 | 174 |
| Parenting time & Decision Making (APR) | 117 | 175 |
| Relocation | 122 | 176 |
| Settlement Options | 128 | 177 |
| Requesting supervised parenting time | 132 | 178 |

Not changed: the Services overview page (66/172), Home, About, Contact.

## What changed

1. **Key-fact callout** (`.efl-keyfact`): a one-sentence summary at the top of each page (new text, EN + ES).
2. **Section cards** (`.efl-section-card`, alternating `.efl-left` / `.efl-right`): each H2 section is wrapped in a white card with an accent border, matching the home page.
3. **Pull quotes** (`.efl-pullquote`): one sentence per page, repeated from the body text in large italic type.
4. **Spacing**: more line height and paragraph spacing inside cards.
5. **New H2 headings** on Relocation, Settlement Options, and Supervised Parenting Time (they had none), so the cards have titles:
   - Relocation: Two Legal Standards / Who Can Petition to Relocate / A Two-Step Process
   - Settlement Options: Alternatives to Trial / Why Settlement Matters / Keeping Control of Your Outcome
   - Supervised Parenting Time: the opening line became an H2; What Counts as Imminent Danger / What Happens After Filing / Protecting Yourself From False Claims
6. Removed an empty paragraph (APR page) and a stray "." paragraph (supervised parenting time page).
7. Theme `style.css` bumped to 1.0.4 with a block marked `SERVICE PAGE VISUALS (start/end)`.

Body wording was otherwise not edited.

## Revisions after first apply

- Relocation (122/176): key-fact line changed to "Planning to move with your children? Colorado law requires a specific legal process, and the standard the Court applies depends on whether parenting orders already exist." (the old line duplicated the pull quote).
- Supervised Parenting Time (132/178): pull quote changed from "A Motion to restrict Parenting Time is self executing." to "Imminent danger is not about harm from six months or a year ago. It must be a danger that is sure to occur right now." (light edit of body text); moved into the "What Counts as Imminent Danger" card. Spanish equivalents updated.

## Files

- `backup-original/<id>.html`: page content exactly as it was before this change.
- `new/<id>.html`: the version applied.
- `build.py`: generates `new/` from `backup-original/` (edit text/structure here and re-run).
- `apply.sh [ids]`: push `new/` to the site.
- `revert.sh [ids]`: restore `backup-original/` to the site.

## How to undo

- **Everything:** `changes/service-pages-visuals/revert.sh`, then delete the `SERVICE PAGE VISUALS` block in `elevated-family-law-child/style.css` and redeploy it.
- **One page:** `revert.sh 110 174` (EN and ES IDs).
- **Only one feature** (e.g. pull quotes): ask, or remove that item in `build.py` and re-run `build.py` + `apply.sh`.
- WordPress revisions (page editor, Revisions) are a second undo path.
- If you edit a page in WordPress after this, `revert.sh`/`apply.sh` will overwrite those edits.

## Status

- [x] Applied to the live site (not yet committed to git).
