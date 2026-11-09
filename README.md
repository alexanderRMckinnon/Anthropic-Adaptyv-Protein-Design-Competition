# Anthropic × Adaptyv Protein Design Competition

A personal account of my submissions for weeks 1, 3 and 5 of the 2026 Anthropic × Adaptyv Protein Design Competition.

**Website:** [Read the notebook](https://alexanderrmckinnon.github.io/Anthropic-Adaptyv-Protein-Design-Competition/)

## Start writing

The page is built from five Markdown files. Edit the text directly on GitHub with the pencil button, then commit to `main`. The website updates automatically once the **Build and publish notebook** workflow finishes.

| What to write | File |
| --- | --- |
| The introduction and why I entered | [content/introduction.md](content/introduction.md) |
| Week 1: EGFR | [content/week-1.md](content/week-1.md) |
| Week 3: GLP-1R | [content/week-3.md](content/week-3.md) |
| Week 5: KRAS G12D pMHC | [content/week-5.md](content/week-5.md) |
| Reflections across the competition | [content/reflections.md](content/reflections.md) |

Each file has a short starting draft and invisible comments with writing prompts. Replace the wording freely. The starting draft summarises existing project records; it leaves the personal recollections for me to fill in.

Write in first person. Specific decisions, obstacles, failed attempts and changes of mind are useful material. Describe the help and tools I used alongside the judgements I made. Keep computational predictions, design hypotheses and experimental findings clearly identified in context.

## Add figures

Upload an image to `assets/images/`, then add this to a content file:

```markdown
![A description of what the reader should notice](assets/images/my-figure.png)

*Figure caption: what is shown, why it matters, and any limit on interpretation.*
```

Image paths are relative to the website root, including when writing inside a content file. The existing figure sources are recorded in [assets/images/SOURCES.md](assets/images/SOURCES.md). The figure blocks already in the page template can be moved or replaced later; standalone interactive structure viewers can also be linked or embedded when ready.

## Change page details

Edit [site.json](site.json) to change the author, search description, public URL or last-updated date. Dates use `YYYY-MM-DD`; update the date when making a meaningful writing change.

The page layout is in [templates/index.html](templates/index.html) and the styling is in [assets/style.css](assets/style.css). Ordinary writing changes only need the Markdown files. The page uses system fonts, has no tracking scripts, and remains readable without JavaScript.

## Preview locally

Python 3.12 or later is sufficient:

```console
python -m pip install -r requirements.txt
python scripts/build.py
python -m http.server 8000 --directory dist --bind 127.0.0.1
```

Open `http://127.0.0.1:8000`. After editing, run the build command again and refresh. Generated `dist/` files are ignored by Git.

## Publishing

GitHub Pages should use **Settings → Pages → Build and deployment → Source: GitHub Actions**. The workflow in [.github/workflows/pages.yml](.github/workflows/pages.yml) builds the page on pushes to `main` and deploys it to GitHub Pages. Pull requests build without deploying. The workflow can also be run manually from the Actions tab.

This repository contains the public write-up and selected figures. The individual challenge repositories remain the detailed scientific records.
