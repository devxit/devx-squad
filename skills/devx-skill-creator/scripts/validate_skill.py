#!/usr/bin/env python3
"""Validate one Agent Skills directory against the DEVX packaging rules."""

from __future__ import annotations

import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
RESERVED = ("claude", "anthropic")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def split_frontmatter(text: str) -> tuple[str, str] | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    front = text[3:end].strip("\n")
    rest = text[end + 4 :]
    return front, rest


def field(front: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{key}:\s*(.*)$", front)
    if not match:
        return None
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        value = value[1:-1]
    return value


def main() -> int:
    if len(sys.argv) != 2:
        print("uso: python validate_skill.py <pasta-da-skill>", file=sys.stderr)
        return 2

    skill = Path(sys.argv[1]).resolve()
    errors: list[str] = []

    if not skill.is_dir():
        fail(errors, f"pasta inexistente: {skill}")
        return report(errors)

    names = [path.name for path in skill.iterdir()]
    if "SKILL.md" not in names:
        found = ", ".join(name for name in names if name.lower() == "skill.md") or "nenhum"
        fail(errors, f"falta SKILL.md com esse casing exato (encontrado: {found})")
        return report(errors)

    readmes = [path for path in skill.rglob("*") if path.is_file() and path.name.lower() == "readme.md"]
    for readme in readmes:
        fail(errors, f"README.md dentro da skill: {readme.relative_to(skill)}")

    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    parts = split_frontmatter(text)
    if parts is None:
        fail(errors, "frontmatter ausente: o arquivo deve abrir com --- e fechar com ---")
        return report(errors)

    front, _body = parts
    if "<" in front or ">" in front:
        fail(errors, "frontmatter contém < ou >")

    name = field(front, "name")
    description = field(front, "description")

    if not name:
        fail(errors, "campo name ausente")
    else:
        if not NAME_RE.fullmatch(name) or len(name) > 64:
            fail(errors, "name deve ser kebab-case, 1-64 caracteres, sem -- e sem hífen nas pontas")
        if name != skill.name:
            fail(errors, f"name ({name}) diferente da pasta ({skill.name})")
        lowered = name.lower()
        for token in RESERVED:
            if token in lowered:
                fail(errors, f"name não pode conter {token}")

    if description is None or not description.strip():
        fail(errors, "campo description ausente")
    elif not (1 <= len(description) <= 1024):
        fail(errors, f"description tem {len(description)} caracteres; o limite é 1024")

    line_count = len(text.splitlines())
    if line_count > 500:
        fail(errors, f"SKILL.md tem {line_count} linhas; o limite é 500")

    return report(errors)


def report(errors: list[str]) -> int:
    if errors:
        for error in errors:
            print(f"ERRO: {error}")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
