# CSC Home Page — Webflow Setup Instructions

## Files in this folder
| File | Purpose |
|------|---------|
| `csc_home_cms_schema.md` | CMS Collection field definitions |
| `csc_home_sections.csv` | CMS data to import (8 sections) |
| `csc_home_page.html` | Full page HTML (paste into Webflow Embed) |
| `csc_home_styles.css` | Matching CSS (paste into Project Settings) |

---

## Quick Start (15 min)

### Step 1: Create Blank Site
- Select "Blank site" from the Webflow welcome screen
- Name it: `NYCBC`

### Step 2: Add Fonts + CSS
1. Go to **Project Settings** (gear icon) > **Custom Code** > **Head Code**
2. Paste:
```html
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Noto+Sans+TC:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  /* Paste entire contents of csc_home_styles.css here */
</style>
```

### Step 3: Create the CMS Collection
1. In Webflow Designer, click the **CMS icon** (database) in the left panel
2. Click **"+ Create New Collection"**
3. Name: `CSC Home Sections`
4. Add fields per `csc_home_cms_schema.md`
5. After creating, click **Import** and upload `csc_home_sections.csv`

### Step 4: Build the Page

#### Option A — Full Custom Code Embed (Fastest)
1. Open the **Home** page (or create a new page called `CSC Home`)
2. Add a **Section** element
3. Inside it, add an **Embed** element (Components > Embed)
4. Paste the entire contents of `csc_home_page.html`
5. Replace all `src=""` with your uploaded image URLs from Webflow Assets

#### Option B — CMS Collection List (Recommended for ongoing updates)
1. On the page, add a **Collection List** element
2. Bind it to `CSC Home Sections`
3. Set filter: `Visible = Yes`
4. Set sort: `Order` ascending
5. Inside each Collection List Item, use Webflow's visual builder to create layouts:
   - Use **Conditional Visibility** on elements based on `Section Type`
   - Bind text elements to CMS fields (Heading, Body Content, etc.)
   - Bind images to the `Hero Image` field
   - Bind buttons to `Button Text` + `Button URL`

### Step 5: Upload Images
1. Go to **Assets** panel (folder icon in left sidebar)
2. Upload images from `webflow_assets/` folders
3. In the HTML Embed, replace `src=""` attributes with the Webflow asset URLs
4. For CMS approach: add images directly to each CMS item's image fields

### Step 6: Preview & Publish
1. Click **Preview** (eye icon) to test responsive behavior
2. Check mobile/tablet/desktop views
3. When ready, click **Publish**

---

## CMS Workflow (for weekly updates)

The main advantage of CMS is that non-technical staff can update content:

### Updating Sunday Sermon (weekly)
1. Go to CMS > CSC Home Sections > "Sunday Worship"
2. Edit `Body Content` with new date, topic, scripture, speaker
3. Upload new hero image if needed
4. Publish

### Adding/Removing Events
1. Go to CMS > CSC Home Sections > "Event Announcement"
2. Update heading, body, and image
3. Or toggle `Visible` to hide expired events
4. To add a new event: duplicate the item, update content, adjust `Order`

### Updating Sunday School Courses (quarterly)
1. Go to CMS > CSC Home Sections > "Sunday School"
2. Edit `Subheading` (quarter dates) and `Body Content` (course list)
3. Publish

---

## Notes
- The page is fully responsive (desktop, tablet, mobile)
- Colors and fonts match the NYCBC Style Guide
- External links (YouTube, Zoom, Breeze, Mailchimp) remain as outbound links
- All sections can be toggled on/off via the `Visible` switch in CMS
- Section order can be changed by updating the `Order` number field
