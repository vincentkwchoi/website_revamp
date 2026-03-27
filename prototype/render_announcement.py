#!/usr/bin/env python3.11
"""
NYCBC AI-Assisted Announcement Renderer Prototype

Takes a single announcement from the CMS and uses Claude CLI (via Max subscription)
to render it optimally for three channels: Bulletin, Website, App.
Outputs a side-by-side HTML preview.
"""

import html
import json
import subprocess
import webbrowser
from pathlib import Path

# --- Sample CMS Data ---
ANNOUNCEMENT = {
    "title": "受難節崇拜及同守主餐",
    "scope": "church-wide",
    "date_start": "2026-03-29",
    "date_end": "2026-04-03",
    "pinned": True,
    "body": """1. 4 月 3 日受難節崇拜及同守主餐：
•上午 10:00，粵語堂受難節崇拜，在 685 禮堂，提供 YouTube 直播。
•上午 10:00，國語堂受難節崇拜，在 675 禮堂，提供 YouTube 直播。
*請留意當日早上不設兒童節目。但會開放嬰兒房和幼兒房，及安排直播，有需要的家長可帶同其嬰幼兒子女內進一起參與崇拜。
•晚上 7:30，英語堂受難節崇拜，在 685 禮堂，提供 YouTube 直播。""",
    "image_url": None,
}

# --- Channel Prompts ---

BULLETIN_PROMPT = """You are formatting a church announcement for a weekly printed bulletin PDF.

Guidelines:
- Output clean HTML suitable for PDF rendering
- Use compact, print-friendly layout
- Use Chinese typography: font-family should prefer "Noto Serif TC", serif
- Numbered items and bullet points (use • character)
- Bold key info: dates, times, locations
- Include a subtle note styling for asterisk (*) notes
- Keep it compact — space is precious on a printed page
- Do NOT add any images
- Wrap everything in a single <div class="bulletin-announcement">

Output ONLY the HTML, no explanation."""

WEBSITE_PROMPT = """You are formatting a church announcement as a rich card for the church website.

Guidelines:
- Output clean HTML for a web card component
- Use modern, clean card design with subtle shadow
- Color scheme: primary #1A7A9B (deep teal), accent #4DA18B, background #F5F9F7
- Font: "Noto Sans TC", sans-serif
- Include a decorative header/banner area with a cross icon (use ✝ or unicode)
- Clear visual hierarchy: title prominent, times easy to scan
- Each service time should be its own visual row/block for easy scanning
- Style the special note (*) differently — as a warm, highlighted callout
- Make it responsive-friendly
- Wrap everything in a single <div class="web-announcement-card">

Output ONLY the HTML and inline styles, no explanation."""

APP_PROMPT = """You are formatting a church announcement for a mobile app screen.

Guidelines:
- Output clean HTML that simulates a mobile app card (max-width: 375px)
- Mobile-first: large tap targets, good spacing, scannable
- Use a condensed/summary view at the top, with details below
- Color scheme: primary #1A7A9B, light background
- Font: "Noto Sans TC", system-ui, sans-serif
- Include a small icon or emoji for the event type (🕊️ for Good Friday)
- Each service should be a clearly separated item (like a list in a native app)
- The special note should be a collapsible-style callout (just style it, no JS needed)
- Add a subtle "Add to Calendar" button placeholder at the bottom
- Wrap everything in a single <div class="app-announcement-card">

Output ONLY the HTML and inline styles, no explanation."""


def render_channel(announcement: dict, channel_prompt: str, channel_name: str) -> str:
    """Call Claude CLI to render an announcement for a specific channel."""
    print(f"  Rendering for {channel_name}...")

    prompt = f"""{channel_prompt}

Here is the announcement data from the CMS:

Title: {announcement['title']}
Scope: {announcement['scope']}
Date range: {announcement['date_start']} to {announcement['date_end']}
Pinned: {announcement['pinned']}

Content:
{announcement['body']}"""

    result = subprocess.run(
        ["claude", "-p", prompt, "--model", "sonnet"],
        capture_output=True,
        text=True,
        timeout=120,
    )

    if result.returncode != 0:
        print(f"  Error: {result.stderr}")
        return f"<p>Error rendering {channel_name}: {html.escape(result.stderr)}</p>"

    output = result.stdout.strip()
    # Strip markdown code fences that Claude CLI may wrap around HTML output
    if output.startswith("```"):
        lines = output.split("\n")
        # Remove first line (```html) and last line (```)
        lines = [l for l in lines[1:] if l.strip() != "```"]
        output = "\n".join(lines)
    return output


def build_preview_html(bulletin_html: str, website_html: str, app_html: str) -> str:
    """Build a side-by-side preview page."""
    return f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NYCBC Announcement Renderer — Prototype</title>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&family=Noto+Serif+TC:wght@400;700&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: "Noto Sans TC", system-ui, sans-serif;
            background: #f0f2f5;
            padding: 2rem;
        }}
        h1 {{
            text-align: center;
            color: #1A7A9B;
            margin-bottom: 0.5rem;
            font-size: 1.5rem;
        }}
        .subtitle {{
            text-align: center;
            color: #666;
            margin-bottom: 2rem;
            font-size: 0.9rem;
        }}
        .pipeline {{
            text-align: center;
            background: #fff;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 2rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            font-size: 0.85rem;
            color: #555;
        }}
        .pipeline code {{
            background: #e8f4f8;
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            color: #1A7A9B;
        }}
        .pipeline .arrow {{ margin: 0 0.3rem; color: #aaa; }}
        .channels {{
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 1.5rem;
            align-items: start;
        }}
        .channel {{
            background: #fff;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }}
        .channel-header {{
            padding: 1rem 1.5rem;
            color: white;
            font-weight: 700;
            font-size: 1rem;
        }}
        .channel-header.bulletin {{ background: #5a5a5a; }}
        .channel-header.website {{ background: #1A7A9B; }}
        .channel-header.app {{ background: #4DA18B; }}
        .channel-body {{ padding: 1.5rem; }}
        .channel-body.app-container {{
            background: #f0f2f5;
            display: flex;
            justify-content: center;
            padding: 1.5rem;
        }}
        .cms-source {{
            background: #fff;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 2rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        .cms-source h2 {{
            font-size: 1rem;
            color: #1A7A9B;
            margin-bottom: 0.75rem;
        }}
        .cms-source pre {{
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 8px;
            font-size: 0.8rem;
            white-space: pre-wrap;
            line-height: 1.6;
            font-family: "Noto Sans TC", monospace;
        }}
        @media (max-width: 1200px) {{
            .channels {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <h1>NYCBC AI-Assisted Announcement Renderer</h1>
    <p class="subtitle">Prototype — same CMS content, AI-rendered for each channel via Claude CLI</p>

    <div class="pipeline">
        <code>CMS Rich Text</code>
        <span class="arrow">→</span>
        <code>Claude CLI (Max)</code>
        <span class="arrow">→</span>
        <code>Channel-optimized output</code>
        <span class="arrow">→</span>
        <code>Staff review</code>
        <span class="arrow">→</span>
        <code>Publish</code>
    </div>

    <div class="cms-source">
        <h2>CMS Source (Raw Announcement)</h2>
        <pre>{html.escape(ANNOUNCEMENT['body'])}</pre>
    </div>

    <div class="channels">
        <div class="channel">
            <div class="channel-header bulletin">Bulletin (PDF)</div>
            <div class="channel-body">
                {bulletin_html}
            </div>
        </div>
        <div class="channel">
            <div class="channel-header website">Website</div>
            <div class="channel-body">
                {website_html}
            </div>
        </div>
        <div class="channel">
            <div class="channel-header app">App</div>
            <div class="channel-body app-container">
                {app_html}
            </div>
        </div>
    </div>
</body>
</html>"""


def main():
    print("NYCBC Announcement Renderer Prototype")
    print("=" * 40)
    print(f"Announcement: {ANNOUNCEMENT['title']}")
    print(f"Using: Claude CLI (Max subscription)")
    print()

    # Render for all three channels
    bulletin_html = render_channel(ANNOUNCEMENT, BULLETIN_PROMPT, "Bulletin")
    website_html = render_channel(ANNOUNCEMENT, WEBSITE_PROMPT, "Website")
    app_html = render_channel(ANNOUNCEMENT, APP_PROMPT, "App")

    # Build preview
    preview = build_preview_html(bulletin_html, website_html, app_html)

    # Write output
    output_path = Path(__file__).parent / "preview.html"
    output_path.write_text(preview, encoding="utf-8")
    print(f"\nPreview saved to: {output_path}")

    # Open in browser
    webbrowser.open(f"file://{output_path}")
    print("Opened in browser.")


if __name__ == "__main__":
    main()
