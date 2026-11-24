# TRMNL Farm Almanac for Frame

A landscape almanac screen for the [TRMNL Frame](https://trmnl.com/blog/introducing-frame) (31.5 in, full-color e-paper). A full-height farm photo on the left; on the right: days to frost, tonight's frost risk, the moon's phase and sign with traditional planting ratings, what to plant now, and what's coming up.

## What it shows
- **Photo:** one of three, rotating by day of year, with a credit line. Blank `photo_base_url` shows a plain panel.
- **Frost Reckoning:** days to last/first frost, frost-tonight alert, low and soil temperature, sunrise/sunset.
- **The Moon:** phase, zodiac sign and element, ratings for leafy crops, root crops and pruning, next full/new moon (approximate).
- **Plant Now / Coming Up:** crop tasks timed from your frost dates, with sowing depth and a soil-temperature check.
- **This Month:** one chore.

## Setup
1. Publish the frost data site from the [trmnl-farmers-almanac](https://github.com/YOUR_GITHUB_USER/trmnl-farmers-almanac) repo (its "Build and publish frost data" workflow). This plugin reuses that data and does not rebuild it.
2. In TRMNL, create a Private Plugin (Polling strategy). Paste the two URLs from `src/settings.yml`, one per line.
3. Paste `src/full.liquid` into the Full layout and `src/shared.liquid` into Shared.
4. Add the custom fields from `src/settings.yml`. Set `data_base_url` to the data site and, for photos, `photo_base_url` to a folder serving `frame-1.jpg` to `frame-3.jpg` (for example the raw GitHub URL of this repo's `photos/` folder).

## Custom fields
| Field | Purpose | Default |
|---|---|---|
| `data_base_url` | Frost data site root, no trailing slash | placeholder |
| `zip` | ZIP for the frost lookup | 65101 |
| `latitude`, `longitude` | Weather, soil temp, sun times | 38.58, -92.17 |
| `region_label` | Panel title text | nearest station |
| `photo_base_url` | Folder with `frame-N.jpg`; blank hides photos | blank |
| `last_frost_override` / `first_frost_override` | Manual MM-DD | blank |

## Limits and caveats
- **Untested on a Frame.** Frame is pre-order and TRMNL's Framework docs do not list it. Sizes use `vh` units, designed for the reported 2560x1440 (16:9) landscape panel, and scale to any size. Portrait is not supported.
- Colors stay near the six Spectra 6 inks (black, white, red, yellow, blue, green); the Frame's own conversion produces the final look. Photos are left in full color for that reason.
- Refresh: once a day. Frost data is NOAA 1991-2020 averages from the nearest station. Check your local forecast.
- Moon sign is approximate. Moon ratings are **traditional folklore, not science**. Crop timings are typical planning values, not agronomic advice.
- Open-Meteo may rate-limit shared IPs. If its call fails, the weather lines are hidden.
- To change photos: `python3 photos/prep_photos.py A.jpg B.jpg C.jpg` (needs Pillow).

## Data and attribution
- NOAA NCEI 1991-2020 U.S. Climate Normals and Census ZCTA centroids (via the almanac data site).
- Weather data by [Open-Meteo.com](https://open-meteo.com/) (CC BY 4.0).
- Photos by Raphael Rychetsky, Dan Meyers and B S via [Unsplash](https://unsplash.com), under the [Unsplash License](https://unsplash.com/license). They are not covered by this repo's MIT license.
- Not affiliated with NOAA, TRMNL, Open-Meteo or The Old Farmer's Almanac.

## License
MIT (code only)
