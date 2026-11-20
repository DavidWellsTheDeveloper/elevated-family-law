# Product Requirements Document (PRD)

## Project Overview

- **Project type:** Small business website (WordPress)
- **Company:** Elevated Family Law, LLC
- **Website domain:** `https://elevatedfamilylaw.focowebsites.com`
- **Hosting:** AWS Lightsail WordPress instance
- **Status:** SSL certificate installed and domain configured. Content, Spanish translations, and testimonials are built on the development site. Remaining work is review, SEO setup, and the domain cutover (waiting on the client for domain access).
- **Development site:** `https://elevatedfamilylaw.focowebsites.com/` — live updates will be visible here. Placeholder content is present and will be replaced as the project progresses.

---

## Client Information

| Field | Value |
|-------|-------|
| **Name** | Michelle Andrews |
| **Email** | michelle@elevatedfamilylaw.com |
| **Phone** | 9707974757 |
| **Company** | Elevated Family Law, LLC |

---

## Target Audience

- **Primary audience:** Customers / potential clients seeking family law services

---

## Brand & Design Direction

### Brand Assets
- **Status:** Partially available.
- **Confirmed on file:**
  - `Logo.webp`
  - `Post.webp` (sample social-media post from several years ago)
- **Logo requirement:** Obtain or create a vector/transparent version of the logo for web use. The current `.webp` has a solid background and white text, which limits where it can be used on the site.
  - **Preferred:** SVG file with transparent background.
  - **Acceptable:** High-resolution PNG with transparent background (and sufficient contrast for light backgrounds).
  - **Fallback:** Recreate the logo in a design tool if original source files are unavailable.
- **Additional inspiration:** The client’s mother is looking for a law-firm website she liked as a reference; that will be sent over when available.

### Color Palette
- Primary colors: **light blue**, **white**
- Overall feel: **very light and calm**

### Aesthetic Preference
- **Style:** Bright / light
- **Feel:** Light, soft, ethereal, airy, and comforting
- **Goal:** Create a welcoming, calming experience for users who may be going through a difficult time.

---

## Branding Guide (Draft)

> **Note:** This guide is a starting point based on the existing `Logo.webp` and `Post.webp`. Exact hex colors and fonts should be finalized once a high-resolution or vector version of the logo is available.

### Logo Usage
- Use the vector/transparent logo version (once obtained) for headers, footers, and favicons.
- Maintain clear space around the logo equal to at least the height of the wordmark.
- Avoid stretching, rotating, or placing the logo on busy backgrounds.
- Provide a dark/contrast variant for use on light backgrounds.

### Color Palette (Derived from Logo)

Colors sampled from `Logo.webp`. These are placeholders and should be refined once a vector/high-resolution logo is available.

| Role | Hex | RGB | Usage |
|------|-----|-----|-------|
| **Background** | `#F6F8F8` | `246, 248, 248` | Page / section backgrounds |
| **Primary Accent** | `#A9D6D6` | `169, 214, 214` | Buttons, links, icons, key accents |
| **Secondary Accent** | `#BDCEDB` | `189, 207, 219` | Subtle highlights, cards, borders |
| **Tertiary Accent** | `#B7D7CA` | `183, 215, 202` | Soft accent variation (analogous teal) |
| **Deep Accent** | `#5EBABA` | `94, 186, 186` | Button hover, emphasis |
| **Body Text** | `#323E3E` | `50, 62, 62` | Paragraphs, default text |
| **Heading Text** | `#283333` | `40, 51, 51` | Headings |

**Palette type:** Analogous, built around the soft cyan-blue-gray of the logo background.

### Typography

**Recommended font pairing for Twenty Seventeen:**

- **Headings:** `Cormorant Garamond` (Google Fonts) — an elegant, soft serif that feels approachable and professional.
- **Body:** Keep `Libre Franklin` (already loaded by the theme) or switch to `Inter` for a slightly more modern, readable sans-serif.

**Why this pairing:** The serif headings add warmth and elegance, while the clean sans-serif body keeps the site readable and calm.

**Implementation note:** Load the heading font via Google Fonts and apply it through **Appearance → Customize → Additional CSS**. Keep body text at a comfortable size (16–18px) with generous line height.

### Imagery & Photography
- Prefer soft, natural light photography.
- Warm, candid family moments that feel supportive rather than staged.
- Avoid harsh shadows, overly corporate stock photos, or dark/moody imagery.

### Voice & Tone
- **Calm** and **reassuring**
- **Professional** but **approachable**
- **Empathetic** to people going through difficult family situations
- Avoid legal jargon where possible; explain processes in plain language.

---

## Content Strategy / Site Phases

### Phase 1 — Foundation
The priority is to get the basics live:

1. **Landing page** with general contact information and initial styling/content.
2. **About Me page** for Michelle Andrews.
3. **Consultation Request page/form** — a simple list of questions with fillable fields (no conditional logic or special features for now).

### Phase 2 — Content & SEO Expansion (Partially Complete)
Scope was expanded (see Budget) to include migrating content from the old site's hidden/unlinked pages. Completed on the development site:

- Services overview page and five service sub-pages: Divorce (DOM), Parenting Time & Decision Making (APR), Relocation, Settlement Options, Requesting Supervised Parenting Time.
- Dependency & Neglect: **intentionally left as a draft placeholder** at the client's specific request.
- Testimonials carousel with six real client reviews.
- Spanish versions of all pages (see Spanish Language Support).

Possible future pages (not currently planned): additional case-type pages, resources page.

---

## Sitemap (Initial)

- **Home** — welcoming landing page, contact info, key CTA to consultation form
- **About** — Michelle Andrews bio
- **Consultation Request** — simple list of questions with fillable fields
- (Phase 2) Divorce
- (Phase 2) Child Custody
- (Phase 2) Resources

---

## Project Workflow / Process

### 1. Discovery
- **Status:** In progress.
- **Goal:** Identify what the client needs from the site and what the site can do to make things easier for the law firm.
- **Approach:** Ask clarifying questions as the project moves forward to ensure effort is focused on useful features and not wasted on unnecessary work.

### 2. Proposal
- **Status:** Completed and accepted.

### 3. Design & Deliverables
Deliverables are released in phases, with opportunities for revisions, changes, and brainstorming at each step.

#### Phase A — Sitemap & One Styled Page
- Build the sitemap and one page with initial styling and content.
- The landing page is the best candidate for this first deliverable.
- **Purpose:** Finalize big-picture design decisions before building out the rest of the site.

#### Phase B — Remaining Pages with Placeholder Content & Features
- Build the rest of the pages with placeholder content.
- Some features may not have full functionality at this stage.
- **Purpose:** Make detailed changes and finalize functionality.
- **Note:** Pages can be left unpublished so the client can edit them before deploying. This lets Phase 2 content roll out at a pace that works for the client.

### 4. Deployment
- Connect the site to the domain (currently `elevatedfamilylaw.focowebsites.com`; the client may switch to `elevatedfamilylaw.com`).
- Review content editing and design tools the client will have access to.

### 5. Support
- After launch, the client may want changes or additional features.
- Ongoing support and feature additions are available as needed.

---

## Core Functionality

### Initial Consultation Request Form

The website must include a simple consultation request form. For now, the form will be a straightforward list of questions with fillable fields and a submit button. No conditional logic, disqualifying rules, or special features are required at this stage.

#### Key Behaviors

1. Users fill out the list of questions.
2. The form is submitted to the firm via email notification.
3. The client can edit the questions and recipient email(s) after launch.

#### Fields (based on the current Contact Us form)

| Field | Type | Required |
|-------|------|----------|
| Name (First, Last) | Text | Yes |
| Phone | Text (masked) | Yes |
| Email Address | Email | Yes |
| County / Jurisdiction | Text | No |
| Best time to contact me | Checkboxes (Morning, Afternoon, Evening) | No |
| Days availability | Checkboxes (Monday–Sunday) | No |
| Brief Description of Your Family Law Matter | Textarea | Yes |
| Type of Family Law Consultation | Select | No |

#### Notes

- The current form uses WPForms. We will rebuild it with Web3Forms using the same fields.
- Conditional logic / screening features can be revisited in the future if needed.

---

## Nice-to-Have Features

### Reviews / Testimonials Section

- Display Michelle’s reviews on the site.
- **Status: Done.** Six real client reviews are displayed in the footer carousel (Easy Testimonial Rotator plugin; manage under **Testimonial Slider → Manage Testimonials** in the admin). The carousel appears on all pages in both languages.

---

## Form Plugin

Because the initial consultation form is simple (a list of questions with fillable fields), any reliable WordPress form plugin will work. The selected plugin should support email notifications and be easy for the client to edit.

### Recommendation: Fluent Forms (Free)

- **Cost:** Free
- **Why:** Modern drag-and-drop builder, stores entries in WordPress, supports multiple email recipients, and allows for future expansion (conditional logic, multi-step forms, etc.) if needed later.

### Alternatives

- **WPForms Lite** — very user-friendly, but the free version may limit multiple email recipients.
- **Formidable Forms** — flexible, good for data views.
- **Contact Form 7** — completely free and flexible, but less beginner-friendly.
- **Web3Forms** — form backend service. Form submissions are sent via Web3Forms’ infrastructure, so **no SMTP plugin or mail server setup is needed**. Can be embedded as a simple HTML form in WordPress.
  - **Pros:** No SMTP headaches, built-in spam protection, supports multiple recipients, easy to set up.
  - **Cons:** Form data is handled by a third-party service; free plan has submission limits; less visual drag-and-drop editing than Fluent Forms/WPForms.

**Decision:** Use **Web3Forms** for the consultation form. This avoids SMTP configuration, DNS authentication issues, and the need to manage a sending email account. The form will include a field for the prospective client’s email address.

**Form recipients:** `info@elevatedfamilylaw.com`, `kaia@elevatedfamilylaw.com`

---

## Technical Environment

- **CMS:** WordPress
- **Hosting:** AWS Lightsail
- **Domain:** `elevatedfamilylaw.focowebsites.com`
- **SSL:** Let’s Encrypt certificate installed and auto-renewal enabled
- **Static IP:** `32.185.210.182` attached to the Lightsail instance
- **Admin access:** SSH via `make ssh` using `LightsailDefaultKey-us-west-2.pem`

### Search Engine Indexing (Currently Blocked)

While the site lives on the development domain, it is intentionally hidden from Google and other search engines:

- `X-Robots-Tag: noindex, nofollow` HTTP header on every response
- `<meta name="robots" content="noindex, nofollow">` in every page `<head>`
- Implemented in the child theme: `elevated-family-law-child/functions.php` (block guarded by the `EFL_BLOCK_INDEXING` constant)

**When moving to the permanent domain (e.g., `elevatedfamilylaw.com`):** remove this block from `functions.php` (or set `EFL_BLOCK_INDEXING` to `false`), then bump the theme `Version` in `style.css` and deploy. Afterwards:

1. Confirm **Settings → Reading → "Discourage search engines from indexing this site"** is unchecked.
2. Verify the header and meta tag are gone (`curl -sI <site> | grep -i x-robots`).
3. Submit the sitemap in Google Search Console (Yoast SEO and Site Kit are already installed).

### SEO & Digital Footprint Checklist (Before Launch / Cutover)

Adapted from an earlier assessment. Not applicable here: WooCommerce/e-commerce SEO (the site does no commerce).

#### A. Decisions to make now

- [x] **SEO plugin: Rank Math** (decided). Migration from Yoast is deferred and not needed immediately. When ready: use Rank Math's built-in Yoast importer (titles, descriptions, canonicals), then deactivate and delete Yoast. **Never run two SEO plugins at once** (duplicate meta tags). Until then, keep only Yoast active.
- [ ] **Final domain** (`elevatedfamilylaw.com` vs. the temp domain). **Waiting on the client for domain access.**
- [ ] **Permalink structure:** set it now and do not change it later.
- [ ] **Avoid plugin overlap** (decide at cutover with the Rank Math migration): Site Kit and Rank Math both connect Search Console. Pick one for that integration. Site Kit is still useful for GA4 and PageSpeed.

#### B. Keep the temp domain safe and the site portable

- [ ] **Make noindex environment-driven, not a DB setting.** The current `EFL_BLOCK_INDEXING` constant in the child theme already does this. Option: move it to `wp-config.php` or an mu-plugin (`wp-content/mu-plugins/staging-noindex.php`) keyed off an environment constant, so it is not tied to a theme deploy. Keep "Discourage search engines" unchecked and do not rely on it, because a DB clone to production can carry it over and deindex the live site.
- [ ] Optional: HTTP basic auth on the temp domain (the only approach that fully keeps crawlers out). Note this would also block the client from previewing unless they get credentials.
- [ ] Define `WP_HOME` and `WP_SITEURL` in `wp-config.php` instead of relying on DB values.
- [ ] Do not hardcode the temp domain in page content, menus, widgets, or theme files (use relative URLs or `home_url()`).
- [ ] Migrate the domain with WP-CLI (handles serialized data): `wp search-replace 'https://elevatedfamilylaw.focowebsites.com' 'https://elevatedfamilylaw.com' --all-tables --dry-run`, then re-run without `--dry-run`.

#### C. On-page SEO and content

- [ ] Unique title tag and meta description for every page. Home (EN and ES) done; remaining pages to do.
- [ ] One H1 per page, logical heading hierarchy, descriptive image alt text.
- [ ] Open Graph / social share image set (use the logo or a branded image).
- [ ] Schema markup: `LegalService`/`Attorney` + `Organization` with name, address, phone, hours, and `sameAs` profile links.
- [ ] Confirm NAP (name, address, phone) is identical on the site, Google Business Profile, and all directory listings.
- [ ] Review the existing site's URLs (see `content-from-existing-site.md` and `wordpress-export.xml`) and **set up 301 redirects** from any old URL that will change or disappear (Yoast Premium/Rank Math redirects or the free **Redirection** plugin).
- [ ] Custom 404 page and no broken internal links.
- [x] Hidden/unlinked content from the old site: decided and migrated (see Client Discussion Items). Dependency & Neglect remains a client-requested placeholder; it is a draft and not public.

#### D. Performance, security, and reliability

- [ ] Caching: LiteSpeed Cache only if the server runs LiteSpeed; otherwise W3 Total Cache or similar. Lightsail typically runs Apache or Nginx, so check first.
- [ ] Image compression and WebP/AVIF (Imagify, ShortPixel, or EWWW free tiers). Compress the large source images in the project root before uploading. (Videos are not committed to git.)
- [ ] Run PageSpeed Insights (mobile and desktop) and fix Core Web Vitals issues.
- [ ] Security: Wordfence or Solid Security; limit login attempts; remove unused plugins and themes.
- [ ] Backups: UpdraftPlus (or Lightsail snapshots) with remote storage and a tested restore.
- [ ] HTTPS everywhere: confirm the Let's Encrypt cert covers the final domain and auto-renews, and that HTTP redirects to HTTPS and www/non-www to one canonical host.

#### E. Email deliverability

- [ ] The consultation form is sent through Web3Forms, so no site mail, SMTP plugin, or Brevo is needed, and the "from" address is not a concern. Brevo is only a fallback if Web3Forms is dropped.
- [ ] Check that the form notifications to info@ and kaia@ land in the inbox (not spam) during testing. If they are filtered, add a mail filter/allowlist for Web3Forms.
- [ ] Optional: SPF/DKIM/DMARC on `elevatedfamilylaw.com` matter only for mail the firm sends from its own domain (regular staff email). Confirm they are set with the client's email provider. This is not part of the website.
- [ ] WordPress's own emails (password resets, admin notices) use the server mail function and may not arrive. Low priority; add WP Mail SMTP only if this becomes a problem.

#### F. Digital footprint / off-site

- [ ] Claim and complete **Google Business Profile** (categories, services, hours, service area, photos).
- [ ] Verify the site in **Google Search Console** (required) and **Bing Webmaster Tools**. **Blocked until the permanent domain is live**; do this at cutover, not before.
- [ ] Set up **GA4** (via Site Kit) with a conversion event for consultation form submissions. Add a cookie/privacy notice if required.
- [ ] Create or claim listings: Avvo, Justia, FindLaw, Martindale, Yelp, state/local bar profile, and relevant local directories. Link each to the site.
- [ ] Link the social profiles from the site and in schema `sameAs` (need the profile list from the client).
- [x] Privacy Policy and attorney advertising disclaimer drafted and published (EN + ES). **Still to do: client approval.** See Attorney Advertising Disclaimer section.
- [x] Reviews: real reviews are on the site. Optional: set up a process for collecting future Google reviews.

#### G. Final cutover verification (blocked until the permanent domain is available)

- [ ] Remove or disable the noindex block (see steps above).
- [ ] Flush permalinks and regenerate the XML sitemap.
- [ ] Confirm canonicals, Open Graph URLs, and sitemap URLs show the **new** domain.
- [ ] Check page source and response headers: no `noindex` meta or `X-Robots-Tag`.
- [ ] Check `robots.txt` references the sitemap and does not disallow the site.
- [ ] (Required, post-cutover) Add/verify the Search Console property for the new domain and submit the sitemap. If it is a domain change, use Search Console's Change of Address tool (only if the old domain had been indexed; it is currently noindexed).
- [ ] Test the consultation form end to end on the live domain.
- [ ] Verify the 301 redirects from old URLs.

---

## Spanish Language Support

- **Plugin:** Polylang (free). Languages: English (default) and Spanish. English at `/`, Spanish at `/es/`.
- **Pages:** every public page has a linked Spanish translation (home, about, contact, services and the five service sub-pages). Not translated: Dependency & Neglect (placeholder draft, per the client). The Privacy Policy and Legal Disclaimer are also translated (draft).
- **Navigation:** separate menu per language, assigned to the Top Menu location in Polylang. A pill-styled language switcher is a menu item in each menu. Menus do not auto-add new pages; add new pages to the right menu manually.
- **Contact form:** Spanish version with Spanish labels; field values and email subject stay English so staff can read notifications. It sends a hidden `preferred_language=Spanish` field and a subject marked "(SPANISH-speaking client)".
- **Process:** Spanish text is drafted in `spanish-translations.md` (glossary and review notes), then applied to WordPress. A Spanish speaker reviews on the live site; **review is still pending**.
- **Rule:** Spanish pages are not auto-synced. If an English page changes, update its Spanish version too.

## Service Page Visual Improvements

Applied to the five service sub-pages (English and Spanish): a key-fact callout at the top, section cards, one pull quote per page, and spacing improvements. Relocation, Settlement Options, and Supervised Parenting Time gained new section headings. Everything is tracked in `changes/service-pages-visuals/` (`CHANGELOG.md`, original-content backups, `apply.sh`, `revert.sh`). Styling lives in a marked block in the child theme `style.css` (theme version 1.0.4).

---

## Budget & Estimate

- **Original approved estimate:** $500–$600 (cap $1,000)
- **Updated scope and estimate:** expanded to approximately **$1,000** after the content from the old site's hidden pages was migrated and a Spanish version of the site was added.
- **Scope included:**
  - Landing page, About Me page, consultation form, styling/content
  - Services overview and migrated service sub-pages
  - Testimonials section (six real reviews)
  - Full Spanish translation of all pages (Polylang), language switcher, Spanish menu and contact form
  - Visual improvements to text-heavy service pages
  - SEO setup (Rank Math) and deployment to the permanent domain
- **Not included / out of scope:**
  - Payment processing
  - Outlook/calendar integration
  - Conditional logic or special features on the consultation form
  - Dependency & Neglect content (placeholder only, per the client)
  - Certified/professional translation of legal content (Spanish is drafted by AI and reviewed by a Spanish speaker)
  - Additional content migration beyond what has already been done

---

## Assumptions

- The expanded scope and a total of about $1,000 have been agreed.
- The client will provide finalized copy, imagery, and brand assets in pieces.
- The consultation form questions and exact wording will be provided by the client.
- No payment processing, calendar integration, or conditional form logic is required for Phase 1.
- The site will be built on the existing WordPress instance already configured.
- Phase 2 content has already been migrated into the development site (see Content Strategy).
- The client likes the current visual direction; no further inspiration examples are needed.

---

## Questions for Client

1. Do you have any connected socials? (e.g., Facebook, X, Instagram, etc.)
2. Do you have access to the login credentials for `https://elevatedfamilylaw.com/admin`?

> **Status:** Question 2 (domain/admin access) is outstanding and blocks the domain cutover items.

---

## Client Discussion Items

### Hidden / Unlinked Content on Existing Site

During research, a significant amount of real content was discovered on `https://elevatedfamilylaw.com/` that is **published but not linked** from the site navigation or sitemap. This content was found by querying the WordPress REST API (`/wp-json/wp/v2/pages`), not by browsing the visible menu.

**Pages found include:**

- Child Support in Colorado
- Allocation of Parental Responsibilities
- Enforcing Child Support Orders
- Asset & Debt Division
- Settlement Options
- Relocation
- Maintenance / Spousal Support
- Divorce
- Fort Collins and Greeley Child Custody / Custody Evaluations
- Child Support
- Requesting Supervised Parenting Time / Emergency Issues
- Contact Us content

**Why this matters:**

- The content appears to have been uploaded/published but was never added to the site’s navigation, so site visitors could not easily find it.
- This content is highly relevant to the new site and could be repurposed for Phase 2 information pages.
- Adding or migrating this content was not part of the original $500–$600 scope, which only covered a landing page, About page, and consultation form.

**Outcome:** Resolved. The client chose to migrate the content they wanted, and it has been added as the Services pages. The scope and cost were expanded to about $1,000. Dependency & Neglect remains a draft placeholder at the client's request. Content not migrated is out of scope unless the client asks.

---

## Open Questions / Next Steps

**Resolved**
- Reviews: resolved. Real reviews are live on the site.
- Inspiration links: no longer needed; the client likes the direction.
- Hidden content from the old site: migrated, and scope/cost expanded to about $1,000.
- Dependency & Neglect: stays a placeholder (client request).
- SEO plugin: Rank Math chosen (migration from Yoast deferred until the domain cutover work).

**Open: not blocked by the domain**
1. **Spanish review:** a Spanish speaker needs to review all Spanish pages (see `spanish-translations.md` for the glossary and open choices, such as "tiempo de crianza" vs. "tiempo con los hijos" and the Spanish brand label "Elevated Derecho Familiar").
2. **Privacy Policy and attorney advertising disclaimer:** drafted in English and Spanish and published on the development site (footer disclaimer, `/privacy-policy/`, `/es/politica-de-privacidad/`, and a notice on the contact form). **TODO: check with the client (Michelle) that she approves the wording and facts before launch** (address, the "attorney advertising" label, testimonial language, services listed in the policy). Spanish text also needs the Spanish reviewer. See `changes/legal-disclaimer/CHANGELOG.md`.
3. **Plugin cleanup affecting the privacy policy:** OptinMonster and WPForms Lite are active but may be unused (the form uses Web3Forms); remove them or add them to the policy. The WordPress admin email is still `user@example.com`.
4. **SEO titles and meta descriptions** for all pages except Home (English and Spanish).
5. **About page headshot and bio:** confirm with the client whether the placeholder photo area and text are final.
6. **Form privacy and compliance:** confirm retention and confidentiality language for form submissions (Web3Forms stores submissions on a third-party service).
7. **Social profiles to link** (Questions for Client).
8. **Performance and security setup** from the pre-launch checklist (caching, image compression, security plugin, backups).

**Blocked until the permanent domain is available (waiting on the client)**
- Final domain decision and admin access to the old site/domain.
- Search Console, Bing Webmaster Tools, and sitemap submission.
- `WP_HOME`/`WP_SITEURL` setup, `wp search-replace` migration, 301 redirects from old URLs.
- Removing the noindex block and the final cutover checklist (section G).
- Rank Math migration from Yoast (do together with cutover).
- Google Business Profile and directory listings (need final URL).

### Attorney Advertising Disclaimer: What Is Needed

Colorado treats a law firm's website as attorney advertising / communication about the lawyer's services, governed by the **Colorado Rules of Professional Conduct, Rules 7.1 to 7.5**. The attorney (Michelle) is responsible for compliance. This is a summary for planning, not legal advice; the client should confirm the exact wording against the current rules and the Colorado Supreme Court Office of Attorney Regulation Counsel.

Typical items to include or check:

1. **Responsible lawyer/firm and office address** shown on the site (footer or contact page). Michelle Andrews, Elevated Family Law, Fort Collins address.
2. **Nothing false or misleading** (Rule 7.1). This covers claims on the site such as "free consultation," experience, and outcomes. Avoid promising or implying results.
3. **Testimonial/results disclaimer** (important here, since six client reviews are displayed): for example, "Testimonials reflect individual experiences. Past results do not guarantee a similar outcome." Confirm the client has consent from each person quoted.
4. **No attorney-client relationship from the site or form**: a short notice near the consultation form, such as "Submitting this form does not create an attorney-client relationship. Do not include confidential details until you have been retained."
5. **Specialist/certification claims** (Rule 7.4): do not describe the attorney as a "specialist" or "certified" unless a recognized body has certified her. The "Dispute Resolution Institute" training mentioned on the Settlement Options page should be worded as training/certification and match what she actually holds.
6. **"Not legal advice" notice**: the site content is general information, not legal advice.
7. **Spanish versions**: the disclaimer must also appear in Spanish, with the same meaning (to be reviewed by the Spanish speaker, ideally also by the attorney).
8. **Optional label**: some states require the words "Attorney Advertising"; Colorado does not generally require this label, but the client may choose to include it.

**Implemented (draft):** a short footer disclaimer on every page (EN and ES, below the FoCo Websites credit) with a link to the Privacy Policy & Legal Disclaimer page, a "Legal Disclaimer" section on that page, and the no-attorney-client-relationship notice above the consultation form's Submit button. **Needs the client's approval of the wording before launch.**

---

## Revision History

| Date | Author | Notes |
|------|--------|-------|
| 2026-11-09 | OpenCode | Initial PRD created from client intake form. |
| 2026-11-09 | OpenCode | Updated with branding details, content phases, form plugin evaluation, and scheduling note. |
| 2026-11-09 | OpenCode | Added project workflow/process section. |
| 2026-11-09 | OpenCode | Confirmed proposal: simplified scope, added budget/estimate, reviews display, removed calendar and conditional form logic. |
| 2026-11-09 | OpenCode | Added development site URL note. |
| 2026-11-09 | OpenCode | Added "Questions for Client" section. |
| 2026-11-09 | OpenCode | Added logo vector/transparent background requirement. |
| 2026-11-09 | OpenCode | Added draft Branding Guide section with placeholder colors pending higher-resolution assets. |
| 2026-11-09 | OpenCode | Updated Branding Guide with an analogous color palette derived from the logo and font recommendations. |
| 2026-11-09 | OpenCode | Moved Reviews display from core Phase 1 scope to Nice-to-Have features. |
| 2026-11-09 | OpenCode | Added Client Discussion Items section about hidden/unlinked content on existing site and updated budget note. |
| 2026-11-11 | OpenCode | Added Web3Forms as an alternative form option to avoid SMTP configuration issues. |
| 2026-11-11 | OpenCode | Confirmed decision: use Web3Forms for the consultation form. |
| 2026-11-11 | OpenCode | Set consultation form recipients to info@elevatedfamilylaw.com and kaia@elevatedfamilylaw.com. |
| 2026-11-11 | OpenCode | Documented current consultation form fields based on the live Contact Us page. |
| 2026-11-19 | OpenCode | Blocked search engine indexing (noindex header + meta) via child theme; documented how to remove at domain cutover. |
| 2026-11-19 | OpenCode | Added SEO & Digital Footprint checklist (pre-launch and cutover) to Technical Environment. |
| 2026-11-19 | OpenCode | SEO checklist: chose Rank Math (migration deferred), simplified email deliverability, marked Search Console as post-cutover. |
| 2026-11-19 | OpenCode | Added Polylang/Spanish site: language switcher, Spanish menu, translated pages and contact form. |
| 2026-11-19 | OpenCode | Added six testimonials (three placeholders filled in by the client). |
| 2026-11-19 | OpenCode | Applied visual improvements to service pages (key-fact callout, cards, pull quotes), tracked in `changes/`. |
| 2026-11-19 | OpenCode | Updated scope/budget to about $1,000; marked reviews, inspiration links, and content migration resolved; added attorney advertising disclaimer guidance and domain-blocked items. |
| 2026-11-19 | OpenCode | Drafted and published privacy policy / legal disclaimer (EN + ES), footer disclaimer, and contact form notice. Pending client approval. |
