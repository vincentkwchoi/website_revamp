# NYCBC Communication Platform Architecture

## Overview

A CMS-driven system where content is authored once and AI formats it optimally for each channel:

```
                    ┌─────────────┐
                    │     CMS     │
                    │ (single     │
                    │  source of  │
                    │  truth)     │
                    └──────┬──────┘
                           │
                    ┌──────┴──────┐
                    │  AI Renderer │
                    │  (Claude API)│
                    └──────┬──────┘
                           │
       ┌────────────┬──────────────┬──────────────┐
       ▼            ▼              ▼              ▼
┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐
│  Website   │ │  Bulletin  │ │ E-Bulletin │ │  Mobile /  │
│ (Webflow)  │ │  (Print)   │ │  (Email)   │ │  Web App   │
└────────────┘ └────────────┘ └────────────┘ └────────────┘
```

## Channels

### 1. CMS (Content Management)
- Single source of truth for all content
- Staff enter content once; it flows to all channels
- See [Content Types](#content-types) below

### 2. Website (Webflow)
- Public-facing site at nycbc.ca
- Pulls from CMS collections
- Pages: see [nycbc_pages.txt](nycbc_pages.txt)

### 3. Bulletin (Print)
- Weekly printed bulletin for Sunday services
- Generated from CMS content as PDF
- Sections: service info, announcements, attendance stats, financial report

### 4. E-Bulletin (Email)
- Weekly digital bulletin sent via email
- Modern, elegant HTML email format — optimized for screen reading
- Same content as print bulletin, but AI adapts layout for email:
  - Responsive design for desktop/mobile email clients
  - Clickable links (YouTube livestream, registration, giving)
  - Richer visuals — images, color, icons
  - Can include interactive elements (e.g. "Add to Calendar" links)
- Distributed via email service (e.g. Mailchimp, SendGrid)

### 5. Mobile / Web App
- Status: **in development**
- Will consume the same CMS content as website and bulletin

---

## Content Types

### Announcements (first priority)

Announcements are the primary content type that spans all three channels. They appear in the bulletin as text lists and on the website as rich cards with images.

#### Scope levels

| Level | Chinese | Example | Bulletin | E-Bulletin | Website | App |
|-------|---------|---------|----------|------------|---------|-----|
| Church-wide | 全教會家事報告 | Good Friday / Easter services schedule | Yes | Yes | Yes | Yes |
| Congregation-specific | e.g. 粵語堂報告 | Cantonese Sunday School classes, teaching ministry | Yes | Yes | Yes | Yes |

#### CMS fields for an Announcement

| Field | Type | Description |
|-------|------|-------------|
| title | Plain Text | Announcement title (Chinese + English) |
| scope | Option | `church-wide`, `cantonese`, `mandarin`, `english` |
| body | Rich Text | Full announcement content |
| image | Image | Hero image (used on website/app; omitted in bulletin) |
| date_start | Date | When to start showing |
| date_end | Date | When to stop showing |
| bulletin_order | Number | Sort order within bulletin section |
| pinned | Switch | Keep at top regardless of date |
| visible | Switch | Toggle on/off without deleting |

#### AI-Assisted Rendering Pipeline

Content is stored as **Rich Text** in the CMS (bold, bullets, headings, inline images). AI (Claude API) then formats it optimally for each channel — not rigid templates, but intelligent adaptation.

```
1. Staff enters announcement in CMS (rich text + images + metadata)
2. On publish, for each channel:
   a. AI receives: content + channel guidelines + constraints
   b. AI outputs: channel-optimized formatted content
   c. Staff reviews → approve / adjust → publish
```

##### What AI handles per channel

| Channel | AI Role | Output |
|---------|---------|--------|
| **Bulletin (Print)** | Lays out announcements to fit page budget. Decides spacing, whether to include images based on available space. Formats numbered lists, bullets, bold. | Styled HTML → PDF |
| **E-Bulletin (Email)** | Adapts print bulletin into modern, elegant email format. Adds clickable links, richer visuals, responsive layout for email clients. | HTML email |
| **Website** | Composes rich cards — picks image placement, heading hierarchy, responsive layout. | HTML/CSS for Webflow |
| **App** | Optimizes for mobile — concise, scannable sections. Can generate push notification summaries. | Structured JSON → native components |

##### AI capabilities beyond rigid templates

| Capability | Example |
|-----------|---------|
| **Adapt to space** | Bulletin page is full → AI tightens wording, adjusts layout |
| **Summarize** | App push notification: "受難節崇拜 4/3 10:00 685禮堂" from a 5-bullet announcement |
| **Image treatment** | Web: hero image. Bulletin: smaller inline or omitted if space is tight |
| **Reformat structure** | Same content → numbered list (bulletin), heading + paragraphs (web), expandable sections (app) |
| **Bilingual** | Generate English summary from Chinese content, or vice versa |

##### Staff review workflow

AI drafts, humans approve. Over time as trust builds, some channels could auto-publish.

```
CMS content updated
  → AI generates draft for each channel
    → Staff dashboard shows side-by-side preview (bulletin / e-bulletin / web / app)
      → Staff approves, adjusts, or regenerates
        → Publish to channel
```

#### How it renders per channel

**Bulletin (Print)**
- Rich format — can include images, styled text, tables
- Grouped by scope: 全教會家事報告 first, then congregation sections
- AI optimizes layout to fit page constraints (typically 2-4 pages)

**E-Bulletin (Email)**
- Modern, elegant HTML email version of the same content
- Clickable YouTube livestream links, registration URLs, giving links
- Responsive layout for desktop and mobile email clients
- Richer visuals than print: color banners, icons, styled cards
- Weekly send via email service to subscriber list

**Website**
- Rich cards with hero image, title, and body text
- Displayed on home page and relevant ministry pages
- Example: Good Friday Services card with cross imagery, Easter Sunday card

**App**
- Card-based layout optimized for mobile
- Push notification summaries generated by AI
- Expandable sections for detailed content

---

## Future Content Types

The following will be added to the CMS as the platform matures:

- **Service Info** — weekly sermon title, scripture, speaker, schedule
- **Attendance Stats** — 上週主日崇拜聚會人數 (weekly service attendance by congregation)
- **Financial Reports** — 奉獻報告 (giving summaries)
- **Events** — calendar events with registration
- **Sunday School** — class listings by congregation (粵語堂主日學, etc.)
- **Ministry Pages** — static content for each ministry
