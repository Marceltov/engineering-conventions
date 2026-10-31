# Accessibility

**Every UI works for people who don't see colour the usual way, use a keyboard or a screen reader, or turn motion off: WCAG 2.2 AA as the floor, meaning never carried by colour alone, and colours that hold up with colour blindness.** Decided 2026-10-31.

## Why

A page that needs a mouse, perfect colour vision or a steady stomach for animation shuts people out, and fixing it late means reworking components that are already everywhere. Colour blindness alone affects about one man in twelve: a red–green status, a palette of near hues or a "the selected one is the coloured one" tab is unreadable for them.

## How

- **Colour is never the only signal.** A status, a category or a selection also has a word, a shape or a weight: questlog's open register tab is taller, its edge thicker and its name bold and underlined, besides its colour.
- **Categorical colours come from a colour-blind safe palette**, [Okabe-Ito](https://jfly.uni-koeln.de/color/) by default, ordered so neighbours also differ in lightness and stay apart in greyscale. A light colour on a light background gets a darker outline.
- **Contrast**: text 4.5:1, large text and the edges of controls 3:1, in light and dark mode.
- **Semantic HTML first, then the ARIA pattern** for what HTML lacks (tabs: `tablist`, `tab`, `tabpanel`, `aria-selected`, arrow keys, Home and End). A widget's keys don't reach handlers further up (a tab list's arrows don't turn the page).
- **Everything works by keyboard**, with a visible focus ring (`:focus-visible`) that contrasts with what is under it.
- **Every control has a name.** One without text gets an `aria-label`; a flag in a language switch is named by the language in its own words, with `lang` set, because a flag stands for a country, not a language. Decorative SVGs are `aria-hidden`.
- **Motion respects `prefers-reduced-motion`**: transitions and animations go, the change stays.
- **Phones count:** the layout works at 390 px wide, with touch targets of at least 24 px.
- **Checked by looking**: before a UI change ships, screenshots in light and dark, on a phone and a desktop, in each language; a colour change is also checked in greyscale or a colour-blindness simulation.

## Rules out

- A status, category or selection told only by colour, or a palette of hues that a colour-blind reader can't tell apart.
- Controls a keyboard can't reach, or focus outlines removed without a replacement.
- Icon-only buttons, flags or images without an accessible name.
- Motion that ignores `prefers-reduced-motion`.

## Reference

questlog (Marceltov/questlog#31: the register's tabs in Okabe-Ito colours, warm and cool in turn after a colour-blindness simulation showed three neighbours alike, with the ARIA tab pattern; the flags named by their language; its sign-in book and pull-to-refresh respect reduced motion).
