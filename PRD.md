# Product Requirements Document (PRD)

## Project Overview

- **Project type:** Small business website (WordPress)
- **Company:** Elevated Family Law, LLC
- **Website domain:** `https://elevatedfamilylaw.focowebsites.com`
- **Hosting:** AWS Lightsail WordPress instance
- **Status:** SSL certificate installed and domain configured
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

### Phase 2 — Content & SEO Expansion (Future)
Add additional pages as the client writes the content:

- Divorce cases information page
- Child custody information page
- Additional family-law case-type pages as needed
- Potential resources page

> **Note:** Phase 2 pages are not part of the initial scope. They can be added later as content is ready.

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

- Display Michelle’s reviews on one of the main pages (likely the Home page or About page).
- The client will provide the review content or source (e.g., Google, Yelp, Avvo, or written testimonials).
- **Status:** Nice-to-have for Phase 1. Can be added after the core pages are complete.

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

---

## Budget & Estimate

- **Approved estimate:** $500–$600
- **Cap:** $1,000
- **Scope included:** Simple landing page, About Me page, consultation form, styling/content, deployment to the configured domain.
- **Not included / out of scope:**
  - Payment processing
  - Outlook/calendar integration
  - Conditional logic or special features on the consultation form
  - Phase 2 content pages (Divorce, Child Custody, Resources)
  - Reviews / testimonials section (nice-to-have)
- **Potential additional scope:** Significant pre-existing content was discovered on `elevatedfamilylaw.com` that is not in the current navigation or sitemap. Adding/migrating this content would require an updated quote.

---

## Assumptions

- The client has approved the $500–$600 estimate with a $1,000 cap.
- The client will provide finalized copy, imagery, and brand assets in pieces.
- The consultation form questions and exact wording will be provided by the client.
- No payment processing, calendar integration, or conditional form logic is required for Phase 1.
- The site will be built on the existing WordPress instance already configured.
- Phase 2 pages will be added after Phase 1 is approved and live.

---

## Questions for Client

1. Do you have any connected socials? (e.g., Facebook, X, Instagram, etc.)
2. Do you have access to the login credentials for `https://elevatedfamilylaw.com/admin`?

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

**Recommended next step:**

Discuss with the client whether they want to migrate/repurpose this content into the new site. If so, provide an updated quote for the additional content work.

---

## Open Questions / Next Steps

1. Where should the reviews be displayed (Home page or About page)?
2. What is the source for reviews — Google, Yelp, Avvo, or written testimonials?
3. Does the client have a preferred headshot and bio text for the About page?
4. Please send the additional law-firm inspiration link/example when available.
5. Are there any privacy, compliance, or data-retention requirements for form submissions?


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

