# Charts

**Numbers on a documentation page are drawn as charts, from the data the page already holds, and the table stays beside them as the table view. A page that reports measurements, a comparison or a trend has at least one chart.** Decided 2026-11-03.

## Why

A table of figures makes the reader find the shape themselves: where two rates cross, which group is firm and which is a hint, how a number moved. A chart shows that at a glance. A chart typed or exported by hand goes stale the next time the numbers change, and a stale chart is worse than none, so the chart is generated from the same numbers as the table and moves with them.

## How

- **Draw from the data.** A small MkDocs hook (`docs_hooks/charts.py`) reads the page's results table or a history file and replaces a marker such as `<!-- chart:sweep -->` with inline SVG. No chart is typed by hand, and a test checks that every marker is drawn.
- **Pick the form by the job:**

    | To show … | Use |
    |---|---|
    | How a set of items divides into outcomes | a segmented bar, never a pie |
    | A value as a setting moves (a threshold, time) | a line, with the default marked |
    | Rates with their uncertainty | a dot with a whisker for the interval |
    | A few items compared on one measure | horizontal bars, labelled with the value |

- **One axis.** Two measures of different scale are two charts, never a dual axis.
- **Colour:** at most three categorical colours, in a fixed order, validated for colour-blind separation in light and dark mode (the `dataviz` skill ships a validator and a reference palette). Text stays in the text colour, never in a series colour. Colours are CSS variables, so the dark theme follows.
- **Marks:** thin lines (2px), markers of at least 8px with a 2px ring in the page colour, a 2px gap between stacked segments, a recessive grid, labels at the ends of lines instead of a legend where there are few series.
- **Tooltips and the table view:** every mark has its value as a tooltip (`<title>`), the figure has an `aria-label`, and the table it was drawn from stays on the page.
- **Motion:** none, or ambient only, and off under `prefers-reduced-motion`.
- **Check every chart in a screenshot, light and dark.**

## Rules out

- A table of figures with no chart where the shape is the point.
- A chart typed by hand, or exported as an image, that can drift from its table.
- Pie charts, dual axes, a rainbow of series colours, 3D.
- A chart whose colours were not checked for colour-blind separation.
- A chart without its table view.

## Reference

passageway (`docs_hooks/charts.py` and the measurement pages of its docs: outcomes, a threshold sweep, group intervals, a model comparison; Marceltov/passageway#117).
