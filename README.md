# Magdalena Fuentes — academic website

Static HTML, CSS, and JavaScript recreation of [magdalenafuentes.com](https://magdalenafuentes.com/), ready for GitHub Pages.

This folder is a copy of `website` with the Join and Research pages removed, including nav and in-page links to them.


## Local preview

```bash
python3 -m http.server 8080
```

Then open [http://localhost:8080](http://localhost:8080).

## Publish on GitHub Pages

1. Create a GitHub repository (for example `magdalenafuentes.github.io` for `https://magdalenafuentes.github.io/`, or any repo name).
2. Push this folder to the `main` branch.
3. In the repo: **Settings → Pages → Build and deployment**.
4. Set **Source** to **GitHub Actions** or **Deploy from a branch**, branch `main`, folder `/ (root)`.

### Custom domain

To keep using `magdalenafuentes.com`:

1. Add a `CNAME` file in the repo root containing `magdalenafuentes.com`.
2. At your domain registrar, point an A/ALIAS/CNAME record to GitHub Pages ([docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)).
3. Enable HTTPS in the Pages settings once DNS has propagated.

## Site map

| Page | File |
| --- | --- |
| Home | `index.html` |
| Publications | `publications/index.html` |
| People | `people/index.html` |
| Activities | `activities/index.html` |
| Resources | `resources/index.html` |
| Deep Learning for Media | `teaching/deep-learning-for-media/index.html` |
| Music Information Retrieval | `teaching/music-information-retrieval/index.html` |

Shared styles live in `assets/css/style.css`. The mobile menu and sticky header are in `assets/js/main.js`. Photos, logos, and paper figures are in `assets/images/`.

To regenerate the HTML after editing `scripts/build_pages.py`:

```bash
python3 scripts/build_pages.py
```
