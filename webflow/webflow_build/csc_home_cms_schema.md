# Webflow CMS Collection: "CSC Home Sections"

## How to create in Webflow
1. Go to CMS panel (database icon in left sidebar)
2. Click "+ Create New Collection"
3. Name it: `CSC Home Sections`
4. Add these fields:

## Collection Fields

| Field Name | Slug | Type | Required | Notes |
|---|---|---|---|---|
| Name | name | Plain Text | Yes | Internal identifier (auto-created) |
| Order | order | Number | Yes | Sort order (1-8) |
| Section Type | section-type | Option | Yes | Options: `banner`, `quick-links`, `content-block`, `event`, `blog-teaser`, `media-promo`, `info-block` |
| Heading | heading | Plain Text | No | Section heading (Chinese) |
| Subheading | subheading | Plain Text | No | Secondary heading or tagline |
| Body Content | body-content | Rich Text | No | Main rich text body |
| Hero Image | hero-image | Image | No | Main section image |
| Button Text | button-text | Plain Text | No | CTA button label |
| Button URL | button-url | Link | No | CTA button destination |
| Secondary Image | secondary-image | Image | No | For sections with 2 images |
| Secondary Button Text | secondary-button-text | Plain Text | No | 2nd CTA label |
| Secondary Button URL | secondary-button-url | Link | No | 2nd CTA destination |
| Extra Rich Text | extra-rich-text | Rich Text | No | For sub-blocks, additional info |
| Visible | visible | Switch | Yes | Toggle section on/off without deleting |

## After creating the collection
- Import the CSV: `csc_home_sections.csv`
- Or manually create 8 items (see below)
