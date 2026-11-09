"""Build the public page from the editable Markdown files. Run from any folder."""

from datetime import date
from html import escape
import json
from pathlib import Path
import shutil
from string import Template

import markdown


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist"


def render_content(name: str) -> str:
    source = (ROOT / "content" / f"{name}.md").read_text(encoding="utf-8")
    return markdown.markdown(source, extensions=["extra", "sane_lists"])


def main() -> None:
    config = json.loads((ROOT / "site.json").read_text(encoding="utf-8"))
    updated = date.fromisoformat(config["updated"])
    values = {key: escape(value, quote=True) for key, value in config.items()}
    values["updated_display"] = f"{updated.day} {updated:%b %Y}"
    for name in ("introduction", "week-1", "week-3", "week-5", "reflections"):
        values[name.replace("-", "_")] = render_content(name)

    template = Template((ROOT / "templates" / "index.html").read_text(encoding="utf-8"))
    OUTPUT.mkdir(exist_ok=True)
    (OUTPUT / "index.html").write_text(template.substitute(values), encoding="utf-8")
    shutil.copytree(ROOT / "assets", OUTPUT / "assets", dirs_exist_ok=True)
    (OUTPUT / ".nojekyll").touch()
    (OUTPUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {config['url']}sitemap.xml\n",
        encoding="utf-8",
    )
    (OUTPUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f'<url><loc>{escape(config["url"])}</loc><lastmod>{updated}</lastmod></url>'
        '</urlset>\n',
        encoding="utf-8",
    )
    print(f"Built {OUTPUT / 'index.html'}")


if __name__ == "__main__":
    main()
