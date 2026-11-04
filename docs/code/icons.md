# Icons

**A web UI takes its icons from one library, [lucide](https://lucide.dev) (`lucide-react`), through one icons module, and an icon only ever repeats a word that stands next to it. Docs sites use the icons that ship with Material for MkDocs. The app's own mark and its pictures are drawn for the project. In a row of text and icons, the texts share one baseline and each icon is centred on the capitals of its text.** Decided 2026-10-31; alignment added 2026-11-04.

## Why

Plain cards under text labels read as dull, and icons make a page easier to scan: what a card is (a weapon, a boss, an open quest) shows before its name is read. Mixing sets (a few from one library, an emoji here, a hand-drawn one there) gives mismatched line weights, and an icon without a word leaves every reader guessing, and a screen reader with nothing to say.

On 2026-11-04 Gamepanion's header took six rounds to look aligned: centred in the row, texts of different sizes stood at different heights; on the baseline, icons stood too high; centred on the x-height, they sat too low. What the eye reads as aligned is one baseline for every text, and each icon's middle on the middle of the capitals beside it. Flexbox offers neither out of the box (`vertical-align: middle` doesn't apply to flex items), so it has to be one deliberate rule.

## How

- **One library:** `lucide-react`, imported per icon (tree-shaken). Not a second set next to it.
- **One module** (`components/icons.tsx`) maps the app's things to icons: a part of a page, a kind of row, a status. A thing the map doesn't know gets a neutral fallback (`Package`), so new data never breaks a page. Components import icons from there, not ad hoc, so one thing keeps one icon everywhere.
- **Next to a word, hidden from screen readers:** `aria-hidden="true"` on the icon; the word says it. An icon-only control (a close button) gets an `aria-label` instead (see [Accessibility](accessibility.md)).
- **Colour from the place, not the icon:** an icon takes the colour of the section it is in (a CSS custom property such as `--c`), or the accent outside one; quieter (muted) for what is done or gone. Colour adds to the word, it never replaces it.
- **Sizes from the type:** about the cap height in running text (`1rem` next to `0.875rem` text), larger only in a tile that marks a card.
- **Aligned with its text:** in a row of controls (a header, a toolbar), the row aligns its items by baseline (`align-items: baseline`) so every text stands on one line, and every icon beside text gets one class that stands it on the baseline and moves it down by half its height less half a cap height, so its middle sits on the middle of the capitals. Only the drawing moves, not the layout. An icon that contains text (initials in a tile) must not give the row a baseline of its own: draw the text over it (`position: absolute`), and keep its own font size on that text, since `cap` is measured on the icon. A control alone in its own framed row is simply centred in it.

  ```css
  .icon-middle {
    align-self: baseline;
    transform: translateY(calc(50% - 0.5cap));
  }
  ```

  Check it by measuring, not by eye alone: in the browser, every text's baseline and every icon's centre against `baseline − 0.5cap` (Playwright, a zero-height inline marker for the baseline, a `1cap` box for the cap height).
- **Docs sites** (Material for MkDocs) use Material's bundled sets (`material/…`, the roadmap's Material Design icon names), which the theme and the roadmap hook already resolve.
- **The project's own mark** (app icon, favicon, docs logo) and its scene (a backdrop, an illustration) are drawn for the project, not taken from the library; see [Documentation site](../repo-setup/docs-site.md).

```tsx
// components/icons.tsx
import { Package, Skull, Sword, type LucideIcon } from "lucide-react";

const ITEM_ICONS: Record<string, LucideIcon> = { weapon: Sword };
export const itemIcon = (kind: string | null): LucideIcon => (kind && ITEM_ICONS[kind]) || Package;

// in a card: the icon, then the word
const Icon = itemIcon(item.kind);
<Icon aria-hidden="true" className="h-4 w-4" /> {item.name}
```

## Rules out

- A second icon library, emoji as icons, or icons pasted in as one-off SVGs where the library has one.
- An icon that carries meaning without a word next to it or an accessible name.
- An icon picked inline in a component for a thing the icons module already maps.
- Taking the project's own mark from the icon library.
- A row of mixed text sizes aligned by centring, icons centred on the row or on the x-height, or a per-icon nudge (`translate-y-[2px]`) instead of the one rule.

## Reference

questlog (Marceltov/questlog#33, ADR 0012: `components/icons.tsx` with the register tabs, section headings, card tiles and the start page's cards). Alignment: Gamepanion's header (gamepanion/gamepanion#130, `.icon-middle` in `app/globals.css`).
