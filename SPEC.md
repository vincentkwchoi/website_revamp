# NYCBC Website Restyling Spec

## 1. Scope

**Layout and style changes only.**

> **CRITICAL: No text changes whatsoever.** All existing text — headings, body copy, labels, captions, scripture verses, contact info, announcements, descriptions — must remain byte-for-byte identical. Do not rewrite, rephrase, translate, abbreviate, reorder, or omit any text. The only changes are to how content is visually arranged and styled.

Reuse all existing images, colors, and fonts from the current Squarespace site. This spec covers all pages listed in [nycbc_pages.txt](nycbc_pages.txt).

### Pages in scope

| Group | Page | URL |
|-------|------|-----|
| Home | Home | /csc/home |
| About Us | About Us | /csc/about-us |
| | Our Faith | /csc/our-faith |
| | Our History | /csc/our-history |
| | Staffs | /csc/staffs |
| Ministries | Ministries Hub | /csc/ministries1 |
| | Children's Ministry | /children-ministry |
| | Local Outreach (LOM) | /csc/lom |
| | Youth Ministry | /csc/youth-ministry |
| | Community Service | /csc/community-service |
| | Worship | /csc/worship |
| | Teaching | /csc/teaching |
| | Servant Development (SDM) | /sdm |
| | Body Life | /csc/body-life |
| Giving | Giving | /csc/giving |

---

## 2. Current state assessment

The existing site is built on Squarespace with a default template. Key issues:

- **Navigation is cluttered** — three congregation menus (Cantonese/English/Mandarin) stacked vertically with mobile hamburger-style "Back" buttons, shopping cart icon, search icon
- **No visual hierarchy** — sections run together with inconsistent spacing, no clear section breaks
- **Inconsistent layouts** — each page uses a different ad-hoc arrangement; some pages are very sparse (Worship, LOM), others are extremely long (Teaching, Home)
- **No responsive grid system** — content widths and spacing vary across pages
- **Footer is minimal** — plain text links (Home, Contact, Office Hours, Parking, Privacy), no visual design
- **No shared component language** — cards, headings, image treatments differ page to page

---

## 3. Design system (existing assets to reuse)

### 3.1 Colors

Extracted from current site — no new colors introduced:

| Token | Value | Usage |
|-------|-------|-------|
| `--brand` | Current Squarespace theme primary | Nav, headings, CTAs |
| `--bg` | Current page background | Page background |
| `--bg-alt` | Slightly darker/tinted variant | Alternating sections |
| `--text` | Current body text color | Body copy |
| `--text-muted` | Lighter variant | Captions, metadata |
| `--border` | Current border/divider color | Cards, tables |

> Implementation note: extract exact hex values from the live Squarespace CSS custom properties or computed styles.

### 3.2 Fonts

Keep the current font stack as-is (likely Noto Sans TC for Chinese, system/Google font for English). No font changes.

### 3.3 Images

All existing images are retained at their current URLs (Squarespace CDN). No new images. Image treatment (sizing, aspect ratio, border radius) is defined per layout pattern below.

---

## 4. Shared components

### 4.1 Navigation bar

**Current:** Three stacked congregation menus with mobile "Back" buttons, shopping cart, search icon. Visually heavy.

**Restyled:**

```
┌─────────────────────────────────────────────────────────┐
│ [Logo]   粵語堂 | English | 国语堂    [Search]          │
├─────────────────────────────────────────────────────────┤
│ Home   About Us ▾   Ministries ▾   Giving   Resources  │
└─────────────────────────────────────────────────────────┘
```

- **Top bar:** Logo left, congregation toggle (tab-style, not dropdown), search icon right
- **Menu bar:** Horizontal nav for the selected congregation's pages; dropdowns for About Us (sub-pages) and Ministries (sub-pages)
- **Sticky on scroll:** Nav bar sticks to top with subtle shadow
- **Mobile (< 768px):** Hamburger menu, congregation toggle remains visible, full-screen slide-out menu
- Remove shopping cart icon (not used for a church site)

### 4.2 Footer

**Current:** Single line of plain text links.

**Restyled:**

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  [Logo]              Quick Links        Connect         │
│  北約華人浸信會       Home               Address         │
│  NYCBC               About Us           Phone           │
│                      Ministries         Email           │
│  Social icons:       Giving             Office Hours    │
│  IG FB YT Spotify    Resources          Parking         │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  © 2025 NYCBC  |  Privacy Policy  |  Privacy Disclaimer│
└─────────────────────────────────────────────────────────┘
```

- 3-column layout: branding + social, quick links, contact info
- Bottom bar: copyright + legal links
- Mobile: stacks to single column

### 4.3 Section container

All page content uses a shared container:

- `max-width: 1120px`, centered
- `padding: 0 1.5rem` (horizontal gutter)
- Sections separated by `padding: 4rem 0`
- Alternating sections can use `--bg-alt` background for visual rhythm

### 4.4 Component library

| Component | Description |
|-----------|-------------|
| **Hero banner** | Full-width background (color or image), centered title + optional subtitle + optional verse, max 400px height |
| **Card** | White background, subtle border or shadow, border-radius 8px, padding 1.5rem. Variants: image-top, icon-top, horizontal (image-left) |
| **Person card** | Circular headshot (120px), name, title, contact below. Used in grid. |
| **Data table** | Styled `<table>` with header row, alternating row colors, responsive horizontal scroll on mobile |
| **Section heading** | H2 with optional subtitle, left-aligned, bottom border accent |
| **Image gallery** | CSS grid, 2-3 columns, gap 1rem, images with border-radius 4px |
| **CTA button** | Primary (filled) and secondary (outlined) variants |
| **Icon card** | Square icon image (80px) + title + short text, used in grids |
| **Resource link** | Download/external link with icon prefix, used in lists |
| **Verse block** | Centered scripture quote in italic/serif, muted color, with reference |

---

## 5. Layout patterns

Each page selects one layout pattern. Patterns are composable from the shared components above.

### Pattern A: Dashboard

**Used by:** Home

A multi-section landing page with varied content blocks.

```
┌──────────────────────────────────┐
│          Hero Banner             │
├──────────────────────────────────┤
│  2026 Theme / Featured Content   │
├──────────────────────────────────┤
│  Sunday Worship Info    │ Giving │  ← 2-column (2:1 ratio)
├──────────────────────────────────┤
│  Card  │  Card  │  Card │  Card │  ← Event cards grid (4 cols → 2 on tablet → 1 on mobile)
├──────────────────────────────────┤
│  Announcements / Blog            │  ← Full-width or 2-column
├──────────────────────────────────┤
│  Sunday School Schedule          │  ← Data table
├──────────────────────────────────┤
│  Prayer Meeting / Zoom CTA       │
└──────────────────────────────────┘
```

- Sections use alternating `--bg` / `--bg-alt` backgrounds
- Each section is independently scrollable content block
- Cards use consistent card component

### Pattern B: Hub

**Used by:** About Us, Ministries Hub

A page that primarily links to sub-pages via a card grid.

```
┌──────────────────────────────────┐
│          Hero Banner             │
│   Title + optional intro text    │
├──────────────────────────────────┤
│  Card  │  Card  │  Card          │  ← 3-column grid of linked cards
│  Card  │  Card  │  Card          │     (icon-top or image-top variant)
├──────────────────────────────────┤
│  Optional: welcome text / pastor │
│  message (About Us only)         │
└──────────────────────────────────┘
```

- About Us: 3 cards (Our Faith, Our History, Our Team) + pastor's welcome message below
- Ministries Hub: 8 icon cards (2 rows of 4, or 3-col with wrap) linking to ministry pages

### Pattern C: Long-form content

**Used by:** Our Faith, Our History

Text-heavy pages with optional images.

```
┌──────────────────────────────────┐
│          Hero Banner             │
│      Title + verse/quote         │
├──────────────────────────────────┤
│  Sub-nav links (inline):         │
│  Welcome | Our Faith | Our Team  │
├──────────────────────────────────┤
│                                  │
│  Long-form body text             │
│  with H3 sub-sections            │
│                                  │
│  [Image gallery if applicable]   │
│                                  │
│  Continued body text...          │
│                                  │
└──────────────────────────────────┘
```

- Body text max-width: 720px for readability
- Sub-sections use `<h3>` with consistent spacing
- Our Faith: 9 doctrinal sub-sections, no images
- Our History: narrative + 5 historical photos (gallery component) + 2 building photos

### Pattern D: People

**Used by:** Staffs

A grid of person cards.

```
┌──────────────────────────────────┐
│          Hero Banner             │
│          "Our Team"              │
├──────────────────────────────────┤
│  Section: Pastoral Staff         │
├──────────────────────────────────┤
│  [Person] [Person] [Person]      │  ← 3-column grid
│  [Person] [Person] [Person]      │     (2-col on tablet, 1-col on mobile)
│  [Person] [Person] [Person]      │
├──────────────────────────────────┤
│  Section: Administrative Staff   │
├──────────────────────────────────┤
│  [Person] [Person] [Person]      │
│  [Person] [Person] [Person]      │
└──────────────────────────────────┘
```

- Person card: circular photo, name, title, phone ext, email
- Grouped by section heading (Pastoral / Administrative)

### Pattern E: Program

**Used by:** Children's Ministry, Youth Ministry, Community Service

Pages with multiple program/event blocks, each with image + details.

```
┌──────────────────────────────────┐
│          Hero Banner             │
│     Title + verse/mission        │
├──────────────────────────────────┤
│  Program Block 1                 │
│  [Image left/right] + Details    │  ← Horizontal card, alternating image side
├──────────────────────────────────┤
│  Program Block 2                 │
│  [Details] + [Image left/right]  │
├──────────────────────────────────┤
│  Program Block 3                 │
│  [Image left/right] + Details    │
├──────────────────────────────────┤
│  Optional: linked card grid      │
│  (e.g. Community Service's       │
│   Programs / Sharing / Photos)   │
└──────────────────────────────────┘
```

- Program blocks alternate image placement (left, right, left...) for visual rhythm
- Each block: image (40% width) + content area (title, description, time/location, CTA button)
- Mobile: stacks vertically (image on top)

### Pattern F: Resource

**Used by:** Teaching, Giving

Content-rich pages with tables, downloadable resources, and structured information.

```
┌──────────────────────────────────┐
│          Hero Banner             │
│        Title + verse             │
├──────────────────────────────────┤
│  Vision / intro text             │
│  Contact info                    │
├──────────────────────────────────┤
│  Data Table                      │  ← Course schedule or giving options
│  (responsive, scrollable)        │
├──────────────────────────────────┤
│  Resource cards / download links │
│  [Resource] [Resource] [Resource]│
├──────────────────────────────────┤
│  Optional: image gallery         │
├──────────────────────────────────┤
│  Optional: additional resource   │
│  sections (study materials etc.) │
└──────────────────────────────────┘
```

- Teaching: course schedule table + resource download links + photo gallery + study material sections
- Giving: giving options as icon cards (PAD, e-Transfer, Cheque, Cash, Investment) + forms + tax receipt section

### Pattern G: Minimal

**Used by:** Worship, LOM (Local Outreach), SDM (Servant Development)

Simple pages with hero + 1-2 content blocks.

```
┌──────────────────────────────────┐
│          Hero Banner             │
│        Title + verse             │
├──────────────────────────────────┤
│                                  │
│  [Featured image]                │
│                                  │
│  Description text                │
│  Contact info                    │
│                                  │
├──────────────────────────────────┤
│  Optional: second content block  │
│  (SDM has 2 sections)            │
└──────────────────────────────────┘
```

- Centered content, max-width 720px
- Simple and clean — no grids or complex layout

---

## 6. Page-to-pattern mapping

| Page | Pattern | Notes |
|------|---------|-------|
| Home | A: Dashboard | Most complex page; hero + worship info + event cards + announcements + schedule + prayer |
| About Us | B: Hub | 3 sub-page cards + pastor welcome message |
| Our Faith | C: Long-form | 9 doctrinal sections, text only |
| Our History | C: Long-form | Narrative + photo gallery (5 historical + 2 building photos) |
| Staffs | D: People | 9 pastoral + 8 admin staff cards |
| Ministries Hub | B: Hub | 8 icon cards linking to ministry sub-pages |
| Children's Ministry | E: Program | APT announcement + VBS + Sunday School + volunteer recruitment |
| LOM | G: Minimal | Hero image + contact |
| Youth Ministry | E: Program | 3 programs: Teens, Youth Sunday School, Daniel Fellowship |
| Community Service | E: Program | Events + activity schedule + 3 linked cards at bottom |
| Worship | G: Minimal | Verse + single image + contact |
| Teaching | F: Resource | Course schedule table + downloadable study materials + photo gallery |
| SDM | G: Minimal | 2 content blocks (FaithlifeTV + Discipleship groups) |
| Body Life | F: Resource | Photo gallery + fellowship groups table + contact |
| Giving | F: Resource | 5 giving options + forms + tax receipt info |

---

## 7. Responsive breakpoints

| Breakpoint | Label | Behavior |
|------------|-------|----------|
| >= 1120px | Desktop | Full layout as designed |
| 768px - 1119px | Tablet | 2-column grids, smaller hero |
| < 768px | Mobile | Single column, hamburger nav, stacked cards |

### Grid behavior per breakpoint

| Component | Desktop | Tablet | Mobile |
|-----------|---------|--------|--------|
| Hub cards (Pattern B) | 3-col | 2-col | 1-col |
| Event cards (Pattern A) | 4-col | 2-col | 1-col |
| Person cards (Pattern D) | 3-col | 2-col | 1-col |
| Program blocks (Pattern E) | Side-by-side | Side-by-side | Stacked |
| Image gallery | 3-col | 2-col | 1-col |
| Data table | Full width | Horizontal scroll | Horizontal scroll |

---

## 8. Constraints

- **No text changes whatsoever** — all text (headings, body, labels, captions, verses, contact info) remains byte-for-byte identical; do not rewrite, rephrase, translate, abbreviate, reorder, or omit any text
- **No content changes** — all links, URLs, and information remain identical
- **No new images** — reuse all existing Squarespace CDN images
- **No new colors** — extract and reuse current site colors
- **No new fonts** — keep current font stack
- **Accessibility** — maintain or improve: semantic headings (H1 > H2 > H3), image alt text, sufficient color contrast, keyboard navigable
- **Performance** — no heavy JS frameworks; CSS-only animations where possible (scroll reveal optional via lightweight library or Intersection Observer)

---

## 9. Implementation approach

1. Build the shared component CSS (nav, footer, section container, card variants, table, gallery, buttons)
2. Build the 7 layout pattern templates (A through G)
3. For each page, select the pattern and populate with existing content
4. Test at all 3 breakpoints
5. Verify content parity with current live pages (same text, same images, same links)
