# MyPortfolio

Personal site of Lorenzo Bonetti, AI Product Owner · Senior Product Engineer.

**Live:** https://ilbonez.github.io/MyPortfolio/

## How it works

- `content/portfolio.yaml` holds every text on the site, in Italian and English.
- `tools/build_content.py` (run with [uv](https://docs.astral.sh/uv/)) validates the YAML with Pydantic
  and writes `site/src/data/portfolio.json`. A typo fails the build with the field path.
- `site/` is a static Vue 3 + Vite app. Visitors switch between IT and EN; the first visit follows the browser language.
- `.github/workflows/pages.yml` builds on every push to `main` and publishes `site/dist` to GitHub Pages.

## Update the content

Edit `content/portfolio.yaml`, commit, push to `main`. The site updates in about a minute.
To replace the CV, overwrite `site/public/CV_Lorenzo_Bonetti.pdf`.

## Run locally

Requires uv and Node 22.

```bash
cd site
npm install
npm run dev
```

`npm run dev` and `npm run build` regenerate the JSON from the YAML first.

## One-time GitHub setup

Settings → Pages → Build and deployment → Source: **GitHub Actions**.
