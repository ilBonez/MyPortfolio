"""Validate content/portfolio.yaml and compile it to site/src/data/portfolio.json.

Run with `uv run build-content` (or `uv run python tools/build_content.py`).
A typo in the YAML fails here, with the field path, instead of rendering an empty section.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, HttpUrl, ValidationError, field_validator

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "content" / "portfolio.yaml"
TARGET = ROOT / "site" / "src" / "data" / "portfolio.json"
PUBLIC = ROOT / "site" / "public"

MONTH = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")


class Model(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)


class Text(Model):
    it: str
    en: str


class Profile(Model):
    name: str
    title: Text
    location: Text
    summary: Text
    email: str
    linkedin: HttpUrl
    github: HttpUrl
    cv: str

    @field_validator("cv")
    @classmethod
    def cv_exists(cls, value: str) -> str:
        if not (PUBLIC / value).is_file():
            raise ValueError(f"{value} not found in site/public")
        return value


class Highlight(Model):
    value: str
    label: Text


class Experience(Model):
    company: str
    role: Text
    location: str
    start: str
    end: str | None
    bullets: list[Text]

    @field_validator("start", "end")
    @classmethod
    def year_month(cls, value: str | None) -> str | None:
        if value is not None and not MONTH.match(value):
            raise ValueError("expected YYYY-MM")
        return value


class Project(Model):
    title: str
    tag: Text
    description: Text
    tech: list[str]
    url: HttpUrl | None = None


class Academic(Model):
    year: int
    it: str
    en: str


class SkillGroup(Model):
    group: Text
    items: list[str]


class Publication(Model):
    venue: str
    title: str
    authors: str
    url: HttpUrl


class Education(Model):
    degree: Text
    school: Text
    years: str
    grade: Text


class Language(Model):
    name: Text
    level: Text


class Portfolio(Model):
    profile: Profile
    highlights: list[Highlight]
    experience: list[Experience]
    projects: list[Project]
    academic: list[Academic]
    skills: list[SkillGroup]
    publications: list[Publication]
    education: list[Education]
    languages: list[Language]


def main() -> int:
    raw = yaml.safe_load(SOURCE.read_text(encoding="utf-8"))
    try:
        portfolio = Portfolio.model_validate(raw)
    except ValidationError as error:
        print(f"{SOURCE.relative_to(ROOT)} is invalid:\n{error}", file=sys.stderr)
        return 1

    TARGET.parent.mkdir(parents=True, exist_ok=True)
    payload = portfolio.model_dump(mode="json")
    TARGET.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {TARGET.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
