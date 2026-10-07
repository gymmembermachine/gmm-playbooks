#!/usr/bin/env python3
"""Lint a playbook page: em dashes, custom values vs checklist, draft count, AI tics."""
import re, sys, html.parser, pathlib

def lint(path):
    p = pathlib.Path(path)
    s = p.read_text()
    out = {"file": str(p), "bytes": len(s.encode())}
    out["emdash"] = s.count("—")
    cvs = sorted(set(re.findall(r"\{\{custom_values\.([a-z0-9_]+)\}\}", s)))
    out["custom_values"] = cvs
    # checklist section = id="checklist" ... next <section
    m = re.search(r'<section[^>]*id="checklist".*?(?=<section|\Z)', s, re.S)
    chk = m.group(0) if m else ""
    out["cv_missing_from_checklist"] = [c for c in cvs if c not in chk]
    out["draft_blocks"] = len(re.findall(r'class="draft', s))
    out["sections"] = re.findall(r'<section[^>]*id="([^"]+)"', s)
    text = re.sub(r"<[^>]+>", " ", s)
    out["x_not_y"] = len(re.findall(r"\b\w+, not \w+", text))
    out["tbuild"] = text.count("[TO BUILD]")
    try:
        html.parser.HTMLParser().feed(s); out["parse"] = "ok"
    except Exception as e:
        out["parse"] = f"ERR {e}"
    return out

for f in sys.argv[1:]:
    r = lint(f)
    flag = "OK " if (r["emdash"]==0 and not r["cv_missing_from_checklist"] and r["parse"]=="ok") else "FIX"
    print(f"{flag} {r['file']}  {r['bytes']//1024}KB  emdash={r['emdash']} drafts={r['draft_blocks']} xnoty={r['x_not_y']} tobuild={r['tbuild']} parse={r['parse']}")
    print(f"     sections: {' '.join(r['sections'])}")
    print(f"     custom values ({len(r['custom_values'])}): {' '.join(r['custom_values'])}")
    if r["cv_missing_from_checklist"]:
        print(f"     MISSING FROM CHECKLIST: {' '.join(r['cv_missing_from_checklist'])}")
