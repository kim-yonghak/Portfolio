# Smilegate 16:9 Slide Design System (Apple-Grammar Adaptation)

**Version: v7** — updated to confirm real Pretendard `.otf` files supplied and registered, confirm the Smilegate logo asset supplied, and add the numbered-circle row-centering rule (see "Resolved during sixth-round review" for the full changelog of this revision).

> **Purpose of this document:** This is a design-system prompt for generating a Smilegate-branded PowerPoint deck. It is adapted from an Apple web-design token analysis, but every brand-specific element has been swapped: **font is Pretendard only** (real `.otf` files supplied in project knowledge and registered in the generation environment — see Typography), **logo is Smilegate** (asset supplied in project knowledge as a black-on-transparent wordmark, with a light-on-dark counterpart derived from it — see Logo), and the **canvas is a fixed 16:9 slide**, not a scrolling webpage. Where the source system described infinite-scroll web behavior (breakpoints, hover, sticky nav), this version replaces it with the fixed-slide equivalent: one canvas size, one master layout grid, and a per-slide header system that repeats in identical position on every slide.

## Overview

The visual grammar being adapted is **reverent, photography-first, quiet UI**: full-bleed tiles, alternating light/dark canvases, a single accent color, minimal chrome, and typography that is confident but never loud. That grammar is preserved. What changes is the delivery format and brand skin:

- **One fixed canvas**: 16:9 only. No responsive breakpoints — a slide deck has exactly one viewport.
- **One font family**: Pretendard, in the weights supplied and confirmed present in project knowledge as real `.otf` files (Thin, ExtraLight, Light, Regular, Medium, SemiBold, Bold, ExtraBold, Black). No system-font fallback, no Inter substitution, no SF Pro, no Noto Sans CJK KR or other Korean-support stand-in — the supplied Pretendard files are registered directly in the generation environment before any slide is produced, and every text element in the deck references the "Pretendard" family (or its named static-weight variants) by name.
- **One logo system**: Smilegate wordmark/symbol replaces every instance where the source system referenced an Apple logo. The logo asset is supplied in project knowledge (see Logo (Smilegate)) — use it directly rather than guessing at a substitute mark.
- **One repeating header grid**: chapter label, title, and subtitle sit at the same x/y coordinates on every content slide, regardless of slide type (light tile, dark tile, utility grid). This is the single most important structural rule in this document.
- **No empty bottom**: the lower third of the content area is never left as bare canvas. It is filled with density-appropriate supporting content (footnotes, source tags, page/section index, secondary stat chips, thin data rules) that reinforces the slide without competing with the hero content.

**Key Characteristics (carried over from the source grammar):**
- Photography/graphic-first presentation; UI recedes so the content visual can speak.
- Alternating full-bleed tile "slides": white/parchment ↔ near-black, with the color change itself acting as the section divider between chapters.
- Single blue accent (`{colors.primary}` — #0066cc, placeholder pending final Smilegate brand color) carries every interactive/emphasis element. No second brand color, until Smilegate brand guidelines override this token.
- Two button/chip grammars: pill-shaped emphasis chips (`{rounded.pill}`) and compact utility rects (`{rounded.sm}`).
- **Pretendard only** — negative-tracking discipline at display sizes is retained conceptually but tuned to Pretendard's own metrics (see Typography).
- Whisper-soft elevation used only when a hero image/graphic needs to visually "sit" on the slide — one drop-shadow token in the entire system.
- Fixed two-row header: slim top identity bar (`{component.slide-topbar}`) + repeating chapter/title/subtitle block (`{component.slide-header}`), same position on every slide.
- Section rhythm across the deck: light title/divider slide → dark content slide → light utility/data slide → dark slide → parchment closing slide — a predictable chapter pulse.

## Canvas & Aspect Ratio

> **Non-negotiable: 16:9 only.** There is no phone/tablet/desktop variant. Every layout, spacing value, and font size below is authored for one canvas.

- **Canvas size:** 13.333in × 7.5in (1280 × 720pt equivalent) — the "wide" 16:9 preset, not the legacy 10in × 5.625in default some slide tools ship with. Always set the wide 16:9 layout explicitly before adding content; do not accept a tool's narrower default.
- **Safe margin:** 0.5in (≈ `{spacing.xl}`, 32px-equivalent) on all four edges as the absolute minimum content inset, except for intentional full-bleed photography/tile backgrounds, which may run edge-to-edge.
- **No breakpoints, no responsive collapse.** Anywhere the source system said "collapses to hamburger at 834px" or similar, that behavior simply does not exist here — there is one fixed arrangement per slide type.
- **Export target:** every slide in the deck is 16:9; mixed aspect ratios are not permitted within one deck.

## Typography

### Font Family — Pretendard only
- **All text on all slides, all weights, uses Pretendard.** No system-ui fallback stack, no SF Pro, no Inter substitution logic, no Noto Sans CJK KR or other placeholder Korean font. The real `.otf` files are supplied in project knowledge and must be registered in the generation environment (e.g. copied to a user font directory and `fc-cache`-refreshed, or equivalent) **before** any slide is built — font registration is a precondition of generation, not a post-hoc fix:
  - `Pretendard-Thin.otf` (100) → family `Pretendard Thin`
  - `Pretendard-ExtraLight.otf` (200) → family `Pretendard ExtraLight`
  - `Pretendard-Light.otf` (300) → family `Pretendard Light`
  - `Pretendard-Regular.otf` (400) → family `Pretendard`, style Regular
  - `Pretendard-Medium.otf` (500) → family `Pretendard Medium`
  - `Pretendard-SemiBold.otf` (600) → family `Pretendard SemiBold`
  - `Pretendard-Bold.otf` (700) → family `Pretendard`, style Bold
  - `Pretendard-ExtraBold.otf` (800) → family `Pretendard ExtraBold`
  - `Pretendard-Black.otf` (900) → family `Pretendard Black`
  - Each weight resolves to its own font family name once registered (only Regular/Bold share the base `Pretendard` family via style attribute); reference the exact family name for the weight needed in each text run — e.g. `fontFace: "Pretendard SemiBold"` for a headline, not `fontFace: "Pretendard", bold: true`, since the latter synthesizes a fake bold instead of using the real SemiBold/Bold outlines.
- **Weight ladder actually used in this system:** 300 (Light) / 400 (Regular) / 600 (SemiBold) / 700 (Bold), mirroring the source grammar's discipline of skipping weight 500 for body/headline use. Medium (500), ExtraLight, Thin, ExtraBold, and Black stay available for rare accent moments (large stat numbers, cover-slide wordmarks) but are not part of the default hierarchy.
- **Pretendard is confirmed supplied and must be used as-is — no substitution, ever.** Since Pretendard does not ship with every OS, the supplied files must be registered on the generating machine before slides are produced, and ideally embedded in the exported `.pptx` (font-embed on export) so the deck also renders correctly on a viewer's machine that doesn't have Pretendard installed. If font-embedding isn't supported by the export pipeline in use, that is a **known limitation to flag to the person**, not a reason to fall back to a different font family — the text still renders in true Pretendard wherever it's opened with the font installed (including this generation environment, now that it's registered), and the person should be told plainly if embedding wasn't possible so they know to check on other machines.
- **QA renders must use the real Pretendard, not a substitute.** Treat any auto-substituted preview font as a hard QA failure, not a cosmetic difference — re-verify font registration (`fc-list | grep -i pretendard` or equivalent) before trusting any rendered preview, since text width, line-wrap points, and the padding rules elsewhere in this document (card padding, footer clearance, header gaps) are only valid when measured against true Pretendard metrics.

### Hierarchy

| Token | Size | Pretendard Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.hero-display}` | 44pt | Bold (700) | 1.07 | -0.5% | Cover-slide / chapter-divider headline |
| `{typography.display-lg}` | 32pt | SemiBold (600) | 1.10 | -0.25% | Title slot in the repeating slide header |
| `{typography.display-md}` | 26pt | SemiBold (600) | 1.2 | -0.25% | Section/tile headlines inside content slides |
| `{typography.lead}` | 20pt | Regular (400) | 1.3 | 0 | Subtitle slot in the repeating slide header |
| `{typography.lead-airy}` | 18pt | Light (300) | 1.4 | 0 | Rare airy lead paragraph (quote slides, closing) |
| `{typography.tagline}` | 15pt | SemiBold (600) | 1.2 | 0 | Chapter-label slot; small tile tagline |
| `{typography.body-strong}` | 13pt | SemiBold (600) | 1.3 | 0 | Inline strong emphasis, callout labels |
| `{typography.body}` | 13pt | Regular (400) | 1.45 | 0 | Default body copy |
| `{typography.dense-link}` | 12pt | Regular (400) | 1.6 | 0 | Footer link lists, dense reference columns |
| `{typography.caption}` | 11pt | Regular (400) | 1.4 | 0 | Secondary captions, chip labels |
| `{typography.caption-strong}` | 11pt | SemiBold (600) | 1.3 | 0 | Emphasized captions, small data labels |
| `{typography.footer-fill}` | 10pt | Regular (400) | 1.4 | 0 | Bottom-of-slide density content (footnotes, source tags, running index) |
| `{typography.micro-legal}` | 8pt | Regular (400) | 1.3 | 0 | Legal/disclaimer line, page numbers |

### Principles
- **Pretendard tracking discipline**: display sizes (26pt+) carry a small negative tracking (-0.25% to -0.5%) to keep the "tight, confident" headline read the source grammar relies on. Never apply negative tracking below 11pt — Pretendard's Korean glyphs lose legibility if tightened at small sizes.
- **Body copy stays comfortable, not compressed**: 13pt body with 1.45 line-height is the deck's reading pace — do not drop below this for primary content.
- **Weight 300 is rare and intentional**: reserved for the airy lead/quote moments, matching the source grammar's use of a light weight only where a slide should feel spacious.
- **Weight 600, not 700, for most headlines**: 700 (Bold) is reserved for the cover/chapter-divider hero and for rare extra-assertive moments; everyday titles use SemiBold (600).
- **500 (Medium) is available but not part of the default ladder** — use only for isolated accent numerals or wordmark moments, consistent with the source system's "500 deliberately absent" rule.
- **No font substitution logic needed**: because Pretendard is supplied directly, skip any system-font-stack or Inter-equivalent guidance — always render in true Pretendard.
- **Control line breaks manually on short, multi-line card/label copy** — don't leave a two-to-three-word phrase to the auto-wrap engine and hope it breaks in a sensible place. Auto-wrap breaks purely on available width, and can split a natural two-word Korean phrase across two lines in a way that reads awkwardly (e.g. breaking "선행 수행" apart so "선행" ends one line and "수행" starts the next, when they read as one unit). For process-step or card body text under ~15 Korean characters spanning 2–3 lines, insert an explicit line break at the natural phrase boundary instead of trusting the wrap point the renderer picks.

## Slide Header System (repeats in identical position on every slide)

This is the section that answers "keep chapter/title/subtitle in the same place on every page."

**`slide-topbar`** — Fixed, ultra-thin identity bar pinned to the very top of every slide. Height 0.35in. Left: Smilegate logo mark (the supplied asset, in its dark-on-light or light-on-dark lockup per background — see Logo) at fixed size and position. Right: deck name or running chapter number in `{typography.micro-legal}`. This bar's position and size never change between light and dark slides — only its color mode inverts (dark logo lockup on light slides, light/white lockup on dark slides).

**`slide-header`** — The repeating chapter/title/subtitle block. Fixed top-left anchored zone, same coordinates on every content slide type (light tile, dark tile, utility/data slide):
- **Chapter label** (`{typography.tagline}`, 15pt SemiBold): positioned at a fixed offset (0.6in from left, **0.6in from top**). Always present, even if visually quiet — this is what lets a viewer track "which chapter am I in" without reading the title.
- **Title** (`{typography.display-lg}`, 32pt SemiBold): fixed offset directly below the chapter label (**+0.45in**).
- **Subtitle** (`{typography.lead}`, 20pt Regular): fixed offset directly below the title (**+0.67in**).
- **Revision note:** earlier drafts used tighter deltas (+0.35in / +0.5in, chapter starting at 0.9in from top) and read as cramped in review — chapter/title/subtitle sat too close together. The wider deltas above are the corrected, tested values; do not tighten them back for the sake of saving vertical space.
- This three-line stack occupies a **locked header zone** — treat its height as reserved space on every slide, even on slides where the subtitle is omitted (leave the vertical gap rather than pulling content up to fill it). Locking the zone height, not just the starting position, is what keeps every slide's body content starting at the same y-coordinate.
- On divider/cover slides the same stack may center instead of left-align, but the vertical rhythm (chapter → title → subtitle spacing) stays identical.
- **Centered cover/divider variant — exact offsets:** chapter label at **y = 2.455in** (not 2.55in), with a **0.457in gap** to the title (not 0.4in) — this reads as slightly more lifted and more evenly spread than the flush-left header's deltas, and was a deliberate hand-tuned adjustment on review. The subtitle keeps its position unchanged relative to the title. Treat this as a distinct, slightly looser rhythm from the left-aligned in-content header, not a bug to reconcile back to the same numbers.
- **Header-to-body gap (mandatory):** leave a clear gap of **at least 0.45in** between the bottom of the subtitle line and the first body element below it (column headers, card grid, table, process flow). Body content starting immediately under the subtitle — even if technically inside the reserved header zone — reads as crowded and makes the subtitle look like a table caption rather than a section intro. This gap is separate from, and in addition to, the locked header zone height.

**`slide-footer-index`** — Fixed thin footer strip, same position on every slide (e.g., 0.3in from bottom edge). Contains: page number (`{typography.micro-legal}`), a running chapter/section indicator, and a small Smilegate wordmark lockup (secondary, smaller than the topbar logo). This strip is part of what fills the bottom of the slide — see next section — rather than leaving it blank.
- **Footer clearance (mandatory):** the last body content element (final card, table row, process-flow box) must end with **at least 0.2in of clear space** above the footer rule line — never flush against it, never overlapping it. When laying out a repeating list/table, compute row height and row count against this constraint up front (available height = footer-line y − 0.2in − body-start y) rather than fitting rows first and checking the footer afterward. A table or card grid that just barely reaches the footer line on paper often clips it once real content wraps to an extra line — always verify against a render, not just the arithmetic.

## Content Density — Do Not Leave the Bottom Empty

The source grammar's whisper-quiet whitespace works on an infinite-scroll webpage, where the next tile is one scroll away. On a fixed 16:9 slide, an empty lower third reads as an unfinished slide rather than restraint. This system keeps the minimalist tone but requires every slide's lower band to carry *something*:

- **Never leave more than ~15% of a slide's height as pure empty canvas below the last content element**, excluding the reserved footer strip.
- Fill options, chosen by slide type, that reinforce rather than clutter:
  - A thin horizontal data rule with 2–3 small stat chips (`{component.stat-chip}`) below the main content.
  - A one-line source/footnote (`{typography.footer-fill}`) — always present on any slide citing data.
  - A secondary supporting visual (small icon row, mini-diagram, or thumbnail strip) under the primary hero graphic.
  - On text-heavy slides: a short "key takeaway" strip in `{colors.canvas-parchment}` spanning the bottom of the content zone.
- **The fix is density, not decoration**: added elements must sit on the existing grid (same margins, same type ramp) — do not introduce new colors, shadows, or shapes to fill space. If a slide genuinely has nothing more to say, shrink the hero content's own footprint and re-center it rather than stretching it to fake fullness, then use the freed band for the footer/index strip at slightly larger scale.

## Layout

### Spacing System
- **Base unit:** 4px-equivalent (0.04in). Structural layout snaps to 0.08in / 0.12in / 0.16in / 0.24in / 0.32in / 0.48in / 0.8in.
- **Tokens:** `{spacing.xxs}` 0.04in · `{spacing.xs}` 0.08in · `{spacing.sm}` 0.12in · `{spacing.md}` 0.17in · `{spacing.lg}` 0.24in · `{spacing.xl}` 0.32in · `{spacing.xxl}` 0.48in · `{spacing.section}` 0.8in.
- **Reserved header zone height:** ~1.55in from the top of the slide for the chapter/title/subtitle stack itself (topbar sits above it). Add the mandatory 0.45in header-to-body gap (see Slide Header System) on top of this — in practice, body content on a typical content slide starts around **y ≈ 2.6–3.0in** from the top of the slide, not immediately at the edge of the header zone.
- **Reserved footer zone height:** ~0.4in from the bottom of the slide, plus the mandatory 0.2in footer-clearance gap above the rule line (see `slide-footer-index`) — body content must not extend past **y ≈ 6.85in** on the 7.5in-tall canvas.
- **Body content zone:** everything between the two reserved zones — roughly **3.85–4.25in of usable height**, depending on exactly where a given slide's header stack ends (subtitle present vs. omitted).
- **Card padding:** `{spacing.lg}` (0.24in) inside utility grid cards.

### Grid & Container
- **Canvas:** fixed 13.333in × 7.5in for every slide — no exceptions.
- **Column patterns:** 3–5 column utility card grid for data/comparison slides; 2-column side-by-side for content+visual slides; single-column centered stack for cover/divider slides.
- **Gutters:** 0.2–0.24in between cards in a utility grid.
- **Margin alignment (mandatory):** a card grid's left edge must equal the header's left margin (0.6in) exactly, and the right edge must sit the same 0.6in from the slide's right edge — left and right margins are symmetric. **Do not center a grid by splitting the leftover width evenly** (`gridX = (canvasWidth − gridWidth) / 2`); that computation only equals 0.6in by coincidence and normally drifts wider (e.g. ~0.87in was observed in review), producing a card grid whose left edge doesn't line up with the title above it — an easy-to-miss misalignment that reads as sloppy once pointed out. Instead fix the margin first (0.6in each side), and **derive card width from the remaining space**: `cardWidth = (13.333 − 1.2 − (cols − 1) × gutter) / cols`. This keeps every grid's edges flush with the title/subtitle above it, on every slide type.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, no border | Full-bleed tiles, topbar, footer strip |
| Soft hairline | 1px `rgba(0,0,0,0.08)` border | Utility cards, stat chips |
| Hero shadow | `rgba(0,0,0,0.22) 3px 5px 30px 0` | The single shadow token — hero product/graphic imagery only |

**Shadow philosophy is unchanged from the source grammar:** exactly one drop-shadow, reserved for hero imagery, never applied to cards, chips, buttons, or text.

## Shapes

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0 | Full-bleed tile backgrounds |
| `{rounded.sm}` | 6px | Utility buttons, inline card imagery |
| `{rounded.md}` | 8px | Secondary capsule buttons |
| `{rounded.lg}` | 14px | Utility/data cards |
| `{rounded.pill}` | 9999px | Primary CTAs, chapter chips, stat chips |
| `{rounded.full}` | 50% | Circular icon chips |

## Colors

Palette is carried over as a functional placeholder — **swap `{colors.primary}` and any logo-adjacent color the moment final Smilegate brand colors are provided.** Until then:

- **Accent** (`{colors.primary}` — #0066cc): every interactive/emphasis element, chips, links, primary CTA fills, and **solid-fill shapes** (icon circle backgrounds, chip backgrounds) — anywhere the color is a background that a white/light glyph or label sits on top of.
- **Accent, on-dark text variant** (`{colors.primary-on-dark}` — #4da3ff): use this lighter tint instead of `{colors.primary}` whenever the accent color is applied **as text** directly on a dark tile background (`{colors.surface-tile-1/2/3}`) — chapter labels, section/column eyebrows, small inline links on dark tiles. Reason: `{colors.primary}` at #0066cc is tuned for contrast against white/parchment; at body-label weight and size it reads too dark/muddy against the near-black tile colors and fails a readability check on review. Do not use `{colors.primary-on-dark}` for solid fills — it's a text-only substitution, the base accent stays canonical for shapes and light-background text.
- **Canvas** — Pure White `{colors.canvas}` #ffffff, Parchment `{colors.canvas-parchment}` #f5f5f7.
- **Dark tiles** — `{colors.surface-tile-1}` #272729, `{colors.surface-tile-2}` #2a2a2c, `{colors.surface-tile-3}` #252527.
- **Text** — Ink `{colors.ink}` #1d1d1f on light, White `{colors.body-on-dark}` #ffffff on dark, Muted `{colors.body-muted}` #cccccc for secondary copy on dark tiles.
- **No decorative gradients** — atmosphere comes from photography/graphics, not CSS/vector gradients, matching the source system exactly.

## Charts & Data Visualization

**Any visual that represents actual data — proportions, comparisons, distributions, trends over time — must be a native chart object bound to real data, not a hand-built approximation made of rectangles, lines, or other shapes.** This applies even to a simple one-row proportion bar (e.g. success/fail/timeout share of a test run): build it as a native stacked bar/column chart with the real counts or percentages as its data series, not as manually positioned colored rectangles sized to *look* like the right proportions.

- **Why this matters, beyond "correctness":** a shape-built fake chart has no data behind it — the proportions were eyeballed or hand-calculated once and baked into fixed coordinates. If a number changes later, someone has to manually recompute and reposition every rectangle; a native chart just re-renders from its updated data. It's also the direct cause of the seam/z-order problem documented below — a real chart engine handles adjoining segment boundaries correctly by construction, so that whole workaround becomes unnecessary once the chart is native.
- **Build with the platform's native chart API**, not an image export of a chart made elsewhere and not a manually drawn approximation. For a pptxgenjs-based pipeline: use `addChart()` for every chart type PowerPoint can render natively (bar, column, stacked bar/column, line, pie, doughnut, scatter, combo — pass an array of `{type, data, options}` for combo charts). Only fall back to an image for chart types PowerPoint has no native form for at all (Sankey, network/node graphs, chord diagrams) — a plain proportion bar, comparison bar, or trend line is never in that category.
- **Style the native chart to match this system's quiet-UI grammar** rather than accepting its default look: set an explicit title (or suppress it if the slide header already states what the chart shows), turn on data labels positioned `ctr`/`inEnd`/`inBase` (never `outEnd` on a stacked chart — some chart libraries corrupt the file), pull chart colors from `{colors.primary}` / the same green-success / red-fail / amber-timeout palette used elsewhere in the deck, hide default gridlines and axis chrome down to the minimum the data needs to be read, and suppress the legend for a single-series chart where the labels already say what's what.
- **The underlying data belongs in the chart's own data table**, not just in a caption below it — this is what makes it a real chart rather than a styled image. If the source numbers live in an Excel file, pull the actual values from that file into the chart's series rather than retyping rounded figures from memory.
- **Verify with the platform's own validator after generating** (e.g. `validate.py` for a pptxgenjs/python-pptx pipeline) — chart XML is one of the more common ways a generated deck silently corrupts, and the validator catches the specific faults (bad `dataLabelPosition` on a stacked chart, missing axis declarations on a combo chart) before they reach the person opening the file.

## Icons



The icon-in-colored-circle motif (see Overview) has two easy-to-miss failure modes found during review — both are now hard rules:

- **Solid fill, not outline.** An icon circle is a **solid `{colors.primary}` fill with a white (or, on light tiles, `{colors.ink}`) glyph on top** — not a dark/near-black circle with a thin accent-colored outline and an accent-colored glyph. The outline treatment reads low-contrast and washed out, especially on dark tiles; the solid-fill treatment is the corrected, tested version.
- **True centering means mass-centroid centering, not bounding-box centering.** An earlier fix trimmed each glyph to its visual bounding box and centered *that box* in the circle — an improvement, but still not enough for icons whose "ink" is unevenly distributed within their own bounding box. A funnel/filter icon is wide at the top and narrows to a point at the bottom: its bounding box can be perfectly centered while the visual mass still reads as sitting high in the circle. A warning triangle is the mirror case — wide base at the bottom — and reads as sitting low even when its box is centered. Both showed up in review on the same slide, shifted in opposite directions, which is what made the pattern visible. **Compute each icon's alpha-weighted pixel centroid** (mean x/y position weighted by the alpha channel, not just the trimmed box's midpoint) and align *that point* to the circle's center: `iconX = circleCenterX − renderedWidth × centroidXFraction`, same for Y. This is the rule that actually produces a "centered-looking" icon for asymmetric glyphs; box-centering is necessary but not sufficient.
- **Pick icons for what the row actually says**, not generic sequence markers — a filter/criteria icon for a "differing standards" row, a person-plus icon for "onboarding," a refresh icon for "repeated manual testing," reads as considered; a generic list/clock/layers rotation picked without regard to content reads as filler.
- **Build note (if rasterizing icons from SVG via a headless renderer, e.g. sharp/resvg/librsvg):** popular icon libraries (e.g. react-icons/Feather) emit `stroke="currentColor"` and rely on an inherited `style="color:#hex"` for the browser to resolve the actual color. Headless SVG rasterizers commonly do **not** resolve that CSS inheritance and will silently rasterize the icon as pure black regardless of the color you requested — with no error. Replace `currentColor` with the literal hex value directly in the SVG before rasterizing, and spot-check the actual rendered pixel color (not just the code) on at least one icon before batch-generating the full set.
- **Small marker glyphs (checkboxes, bullet squares) next to a line of text benefit from a small manual optical nudge** (~0.03–0.06in right and down from a pure grid-aligned position) to sit centered against the text's cap-height rather than its full line-box — mathematically grid-aligned placement can read as very slightly high/left of where the eye expects it next to the text baseline. This is a small hand-tuned adjustment, not a formula to derive up front; check it against a render.
- **Numbered circle bullets in a list row (agenda/table-of-contents rows, step-number lists) must be centered on the row's own vertical center, not a small fixed inset from the row's top edge.** Compute `circleY = rowY + rowH / 2 − circleDiameter / 2` so the circle's center lands exactly on the row's center — the same center-to-the-row-height, not the row-top logic used for checkbox nudging above, just solved from the row geometry directly instead of hand-nudged, since the row height (and therefore its center) is already known at layout time.

## Utility Card Internals

A 3–5 column utility card (see Grid & Container) has its own internal rhythm, separate from the outer grid margins. Three failure modes found in review, now hard rules — note the first and third pull in opposite directions on the same padding value, so both need to be checked, not just one:

- **Don't reserve more vertical space than the text needs.** An earlier draft gave the body-copy line a fixed-height box sized for its longest possible wrap, so a short one-line answer left visible dead air below it before the next element. Size text boxes (or the gap after them) to the content's actual line count at the chosen font size, not to a worst-case allowance — and when in doubt, increase the font size a point or two before adding more box height, since larger text reads as "considered" while empty space reads as "unfinished."
- **A card's footer line (the short justification/point line under the main body copy) gets a hairline divider directly above it, not italics, for separation.** Italics on a small (9–11pt) Pretendard footer line reads as blurry and low-legibility rather than "secondary emphasis" — remove the italic, set the line non-italic and bold in `{colors.primary}` instead, and use a 1px hairline rule (see Elevation & Depth → Soft hairline) directly above it to do the job italics was trying to do. Keep the gap between that hairline and the text under it tight (~0.04in) — a wider gap (~0.1in) reads as an unrelated floating line rather than a caption directly tied to the text below it.
- **Internal padding is a floor, not a target — it must hold even when the text is long, not just when it's short.** `{spacing.lg}` (0.24in), or `{spacing.md}`-ish (~0.18in) for smaller cards in a 4+ column grid, is the *minimum* clearance between text and the card's edge on all four sides, at all times. The failure mode this guards against is the mirror image of the first bullet: when a card's text runs longer than expected, the padding is the thing that silently gives way first — text ends up flush against, or clipped by, the card border, because the box height was fixed without checking the longest real copy that would go in it. **When text length varies (e.g. cards populated from a data source, or copy that gets edited after layout is built), size the card height — or the grid's row height — to the longest actual content plus the full padding, not to an average or a first-draft guess.** Verify this on an actual render, the same way footer clearance is verified (see `slide-footer-index`) — the arithmetic can look fine while the rendered text still touches the edge once real line-wrapping is accounted for.
- **Internal padding stays a single consistent value** (`{spacing.lg}` 0.24in, or tighter at ~0.18in for smaller cards in a 4+ column grid) on all four sides of the card — the icon, label, body copy, divider, and footer line all indent from the same edge.

## Logo (Smilegate)

- Logo asset is supplied via project knowledge (`logo_black.png`, a black wordmark on a white/transparent background) — **do not substitute a placeholder mark, wordmark reconstruction, or the Apple mark from the source grammar.**
- The single supplied asset is a black-on-transparent lockup, so the **light-on-dark counterpart must be derived from it directly** (e.g. re-mapping the black glyph's alpha channel to a white fill), not redrawn or approximated — this keeps both lockups pixel-identical in shape, weight, and kerning. Once derived, the deck needs both: a **dark-on-light** version (for light/parchment slides) and a **light-on-dark** version (for dark tiles) — swapped automatically per slide background, same position and size in both cases.
- If a future logo asset arrives as a different file (updated mark, new lockup, vector source, etc.), regenerate both derived lockups from that new source rather than reusing the previously derived white version — treat the derived lockup as disposable output of the source file, not as its own source of truth.

## Iteration Guide

1. Lock the canvas size and the header/footer reserved zones **first**, before designing any individual slide — every other decision inherits from those two fixed bands.
2. Reference tokens directly (`{component.slide-header}`, `{typography.display-lg}`) rather than inlining pixel/point values.
3. Never leave the lower band of a content slide as bare canvas — check every slide against the density rule above before calling it done.
4. Display headlines stay Pretendard SemiBold/Bold with the tight tracking; body stays Pretendard Regular at 13pt. This boundary is unbreakable.
5. The single hero drop-shadow is reserved for hero imagery only — never for cards, chips, or text.
6. When in doubt about emphasis: alternate the tile surface (light → dark) before adding any new chrome, shadow, or color.
7. **Give the header stack room to breathe** — use the tested chapter/title/subtitle deltas (0.6in → +0.45in → +0.67in) and the mandatory 0.45in header-to-body gap. Tighter spacing consistently reads as cramped in review.
8. **Always verify the footer clearance on an actual render**, not just the layout math — compute available body height against the footer-line y minus the 0.2in clearance, and re-check after any copy or row-count change.
9. **Icon circles are solid-fill + white glyph**, glyphs are centered on their **alpha-weighted mass centroid** (not just their trimmed bounding box — asymmetric shapes like funnels or triangles need this to actually look centered), and icon choice should match what each row/card actually says. If rasterizing from SVG, verify actual rendered pixel colors — `currentColor`-based color pipelines silently fail black on many headless renderers.
10. **Use `{colors.primary-on-dark}` for any accent-colored text sitting on a dark tile** (chapter labels, column eyebrows) — the base `{colors.primary}` is a fill color first, a light-background text color second, and an on-dark text color never.
11. **Derive card-grid margins from the header's 0.6in, never from splitting leftover canvas width evenly** — center-balancing a grid independently of the header routinely drifts the grid's left edge wider than the title's, breaking the shared left margin that ties a slide together.
12. **Size card text to its actual content, not a worst-case box** — a short line of body copy in an oversized fixed box is the single most common cause of a card grid "feeling empty." Increase font size before increasing box height.
13. **On centered cover/divider slides, use the slightly looser 2.455in / +0.457in chapter-to-title rhythm**, distinct from the left-aligned in-content header's 0.6in / +0.45in — don't force these two header variants to share identical numbers.
14. **Any bar/proportion/trend visual that represents real data is a native chart bound to real data, never hand-drawn shapes** — this also eliminates the segment-seam problem a shape-built bar is prone to, since a real chart engine handles adjoining segments correctly by construction.
15. **Don't trust auto-wrap for short Korean card copy** — insert explicit line breaks at natural phrase boundaries so a two-word phrase doesn't fragment across lines.
16. **Card padding is a floor that must hold at the longest realistic content length, not just at the length used while designing** — check padding against the longest real copy on a render, the same way footer clearance is checked, since a fixed box height silently lets padding collapse to zero (text touching the edge) once content runs longer than the first draft.
17. **Register the supplied Pretendard `.otf` files before generating anything, and confirm the registration rather than assuming it worked** — a deck built against a silently-substituted font is a QA failure even if every layout rule above was followed correctly, since padding, wrap points, and header/footer clearances are all measured against Pretendard's specific metrics.
18. **Center numbered circle bullets on their row's vertical center** (`rowY + rowH/2 − circleDiameter/2`), not a fixed top-inset — check this on any agenda, table-of-contents, or step-number list against a render, the same way icon centering is checked.

## Known Gaps (to resolve before final production)

- Final Smilegate brand color(s) not yet supplied — `{colors.primary}` (and its `{colors.primary-on-dark}` tint) are functional placeholders inherited from the source grammar.
- Font-embedding support depends on the export pipeline in use — confirm on each new pipeline whether the `.pptx` export step actually embeds Pretendard, or only references it by name (see Typography → Font Family). If embedding isn't supported, flag this to the person explicitly rather than silently shipping a font-referenced-but-not-embedded file.

**Resolved during first-round review** (kept here as a changelog, not open items):
- Header stack spacing (chapter/title/subtitle felt cramped) → fixed via wider deltas + mandatory header-to-body gap, see Slide Header System.
- Table/card content overlapping the footer rule line → fixed via mandatory 0.2in footer clearance, see `slide-footer-index`.
- Icon circles low-contrast (dark circle + accent outline + accent glyph) and glyphs visually off-center for asymmetric icons → fixed via solid-fill + white-glyph treatment and bounding-box centering, see Icons.
- Accent-colored text on dark tiles hard to read → fixed via `{colors.primary-on-dark}`, see Colors.

**Resolved during second-round review** (kept here as a changelog, not open items):
- Card grid's left margin didn't match the header's left margin (grid was center-balanced independently and drifted ~0.27in wider) → fixed via mandatory margin alignment, see Grid & Container.
- Utility cards read as having too much empty space, and the small italic footer line inside them was hard to read → fixed via content-sized text boxes, a hairline divider tight against the footer line, and removing italic in favor of bold + `{colors.primary}`, see Utility Card Internals.
- Bounding-box icon centering (the first-round fix) still left visually asymmetric icons — a funnel, a warning triangle — looking off-center in opposite directions from each other → fixed via alpha-weighted mass-centroid centering, see Icons.

**Resolved during third-round review** (kept here as a changelog, not open items):
- Centered cover-slide header stack read as slightly cramped/low compared to the corrected in-content header rhythm → fixed via a distinct, slightly looser centered-variant spacing, see Slide Header System.
- A segmented proportion bar (success/fail/timeout) showed a hairline seam at a segment boundary despite mathematically exact adjoining coordinates → patched at the time via an overlap + z-order technique (fourth-round note: this patch is now obsolete, see below).
- Auto-wrapped card body copy split a two-word Korean phrase ("선행 수행") across two lines in a way that read awkwardly → fixed via explicit manual line breaks at phrase boundaries instead of relying on auto-wrap, see Typography → Principles.
- Checkbox marker glyphs sat very slightly off from their adjacent text's optical baseline → fixed via a small manual nudge (~0.03–0.06in), see Icons.

**Resolved during fourth-round review** (kept here as a changelog, not open items):
- Data visuals (a success/fail/timeout proportion bar) were being built as hand-drawn rectangles sized to approximate the right proportions, rather than as real charts bound to actual data — this was the root cause of the segment-seam issue from the third round, and meant the visual had no live connection to its source numbers. Fixed by mandating native chart objects for any data visualization, see Charts & Data Visualization. The overlap + z-order seam fix from the third round is now obsolete for this case — a native chart doesn't have the problem in the first place — and is kept above only as a historical note, not current guidance.

**Resolved during fifth-round review** (kept here as a changelog, not open items):
- On a separate deck built from an earlier version of this system, several utility cards had text running flush against the card's border — the opposite failure from the second-round "too much empty space" fix. The card height had been fixed without checking it against the longest real copy that would fill it, so padding silently collapsed to zero once the actual text ran longer than the layout's first draft. Fixed by treating internal padding as a floor that must hold at the longest realistic content length, not just the length used while designing — see Utility Card Internals.

**Resolved during sixth-round review** (kept here as a changelog, not open items):
- Pretendard was referenced by name in earlier decks but the actual `.otf` files were not yet available in the generation environment, so text silently rendered in a substituted Korean-support font instead. The real files are now supplied and registered — see Typography → Font Family. Any deck generated before this point should be treated as a font-substitution QA risk and re-rendered, not assumed correct.
- The Smilegate logo lockup was treated as a placeholder gap; the black-on-transparent asset is in fact supplied, and a light-on-dark counterpart has been derived from it directly (alpha-channel remap, not redrawn) — see Logo (Smilegate).
- **Numbered circle bullets in a vertical list row (e.g. a table-of-contents/agenda slide) were vertically offset from their row's text** — the circle was positioned at a small fixed inset from the row's top edge (`rowY + 0.04in`) rather than centered against the row itself, so at the row's line height the circle's optical center sat measurably above the text's vertical center (roughly 0.06in in the case found on review — small enough to miss on a quick glance, obvious once the row is compared side-by-side with the text next to it). Fixed by centering the circle on the row's own vertical center rather than eyeballing a fixed top offset: `circleY = rowY + rowH / 2 − circleDiameter / 2` (for the reviewed case: 0.6in row height, 0.4in circle → offset of rowY + 0.1in, not rowY + 0.04in). This is a general rule, not a one-slide fix — **any bullet/number glyph placed beside a line or block of text must be centered against that text's own row height**, the same "align to the thing it labels, not to an arbitrary inset" principle the Icons section already applies to icon-in-circle glyphs.
