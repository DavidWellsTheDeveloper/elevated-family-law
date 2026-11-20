# Legal disclaimer and privacy policy (2026-11-19)

**DRAFT. Must be checked with the client (Michelle) before launch, and the Spanish text reviewed by the Spanish reviewer.**

## What was added

1. **Footer disclaimer** (English and Spanish, language-aware) below the "Built by FoCo Websites" line on every page: general-information / no attorney-client relationship / testimonials / attorney advertising, plus the firm name and address, and a link to the policy page. File: `elevated-family-law-child/template-parts/footer/site-info.php`; styling `.efl-footer-disclaimer` in `style.css` (theme version 1.0.5).
2. **Privacy Policy and Legal Disclaimer page**, English (ID 3, `/privacy-policy/`, now published) and Spanish (ID 217, `/es/politica-de-privacidad/`). The footer privacy link now appears because the page is published.
3. **Contact form notice** above the Submit button (English page 15, Spanish page 168): no attorney-client relationship, don't include confidential details, link to the privacy policy.

## Facts used in the drafts (confirm with the client)

- Address: 2625 Redwing Road, Suite 205, Fort Collins, Colorado 80526 (taken from the old site's contact page content).
- Phone (970) 797-4757, email info@elevatedfamilylaw.com.
- Services named: Web3Forms (form), AWS (hosting), Google Analytics, Jetpack stats, Google Fonts, Polylang language cookie.
- "Attorney advertising" wording is optional in Colorado; included as a conservative choice.

## Things to verify on the site that affect the policy text

- Active plugins that may collect data and are not mentioned in the policy: **OptinMonster**, **WPForms Lite** (the form now uses Web3Forms), WP Mail SMTP. Remove unused ones, or add them to the policy.
- The WordPress admin email is still `user@example.com`; set a real one.
- Google Analytics via Site Kit / MonsterInsights: confirm what is actually enabled.

## Files

- `build.py`: generates `new/` (privacy pages and contact pages with the notice).
- `backup-original/`: original content of page 3 (default WordPress text), 15, and 168.
- The footer file change is in git history (see the previous commit for the original).

## How to undo

- **Footer disclaimer:** restore `site-info.php` from git (`git checkout 83ac301 -- elevated-family-law-child/template-parts/footer/site-info.php`) and remove the `Footer legal disclaimer` block from `style.css`, then redeploy.
- **Contact form notice:** push `backup-original/15.html` and `168.html` with `wp post update <id> <file>`.
- **Privacy page:** set pages 3 and 217 back to draft (`wp post update 3 --post_status=draft`).
