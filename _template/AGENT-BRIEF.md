# Building a GMM playbook page

You are turning ONE existing GMM "Done-For-You Marketing Calendar" play into a web page that matches `bring-your-boo/index.html` in this repo. That page is the finished reference. Open it first and read it top to bottom before writing anything.

## What "good" is

Reference: `bring-your-boo/index.html` (the whole file), `_template/head.html`, `_template/style.html`, `_template/script.html`, `_template/body-byb.html`.

Reuse the CSS and JS verbatim (copy `_template/style.html` and `_template/script.html` into your page). Reuse the same section pattern: hero → "What's in here" contents → numbered sections (`<section class="pb" id="...">` with `<div class="kicker">NN</div><h2>`) → setup checklist (localStorage, same JS) → printable staff cheat sheet. Only include sections the play actually needs. A 7-day play does not need 16 sections.

The reader is a gym owner at a front desk at 5:45am. Everything on the page has to be something they can DO. Bullets over prose. Scripts in quotes. Every email/text is a `.msg` card w/ `.msg-head` (type + when) and `.msg-body`, copy-ready.

## Voice (non-negotiable)

Read `_template/VOICE-RULES.md`. The short version:

- Instructional sections = G.R. talking to a gym owner: "w/", "e.g.", "folks", first-person opinion stated flat ("I'd do it," "I wouldn't"), parentheticals. Plain. Rough edges left in.
- Copy TO MEMBERS/PROSPECTS (emails, texts, posts) = warm, exclamation-y, "super fun," ":)", "Let me know!" See the Member Madness copy in the source material.
- NO em dashes anywhere. Use commas, parens, or a period.
- NO paragraphs that end on a quotable button. NO "X, not Y." NO three-beat lists in narration. NO "That's the whole thing." NO invented first-person anecdotes.
- Keep G.R.'s existing wording from the source material wherever it exists. Restructure, don't rewrite. Where the source is thin and you draft something new, wrap the whole section or card in `<div class="draft">` (CSS: add `.draft{outline:2px dashed #ff7a1a;outline-offset:6px;position:relative} .draft::before{content:"DRAFT";position:absolute;top:-10px;left:8px;background:#ff7a1a;color:#111;font:700 11px/1 Inter,sans-serif;padding:3px 6px;border-radius:3px}` to the style block) so G.R. sees exactly what's new vs. his.

## Placeholders

Two kinds, same as BYB:
- GHL merge tags for anything an automation sends: `<span class="mt">{{contact.first_name}}</span>`, `{{location.name}}`, `{{user.first_name}}`, and campaign custom values `{{custom_values.<play>_<thing>}}`. Prefix every custom value w/ the play's short slug (e.g. `mm_` for Member Madness, `pz_` for Project Zero). List every custom value ONCE in the setup checklist as a table: display name → merge tag → example value.
- Manual fills in `<span class="blank">[BRACKETS]</span>` for posts, scripts, and print pieces.

Rule learned the hard way on BYB: if a custom value lands in messages to two different audiences (member vs. prospect), it holds a number or a noun phrase, never a sentence fragment w/ a pronoun. "$100" or "$100 off month one," never "$100 off your first month." The sentence around the tag carries the pronoun.

## Simplicity rules (G.R. will reject anything that adds admin)

- No spreadsheets, no trackers to maintain, no new systems. Use what the gym already has: their booking/billing software, a sign-up sheet on the whiteboard, a jar, a whiteboard count.
- No sizing gates, no insurance notes, no Day-30/Day-90 follow-ups. One post-campaign call ("call everybody who didn't join") is fine.
- Decisions up top ("Decide First"), then copy, then a checklist in order. The owner should be able to read Decide First + the checklist and run the play.
- If the source play already has a tracker/Canva/video link, keep the link. Don't rebuild assets.

## Deliverables (in your worktree)

1. `<slug>/index.html` (complete page, self-contained, same head meta pattern as BYB w/ the slug in og:url). Update `<title>`, og tags, description.
2. `<slug>/oembed.json` copied from BYB's w/ the title/URLs changed.
3. `<slug>/NOTES.md`: (a) which Circle lesson(s) + Drive docs you used, (b) a list of every DRAFT block and why the source was thin there, (c) open questions for G.R., (d) anything in the source you think is wrong or outdated.
4. Commit on your branch w/ message `"<Play name>: playbook page (draft)"`. Do not push. Do not touch `bring-your-boo/` or `_template/`.

Skip the PDF. Skip cover.png (reference `../bring-your-boo/cover.png` as a placeholder og:image for now).

## Process

1. Read the reference page and the voice rules.
2. Read your source material (the Circle lesson text in `_sources/`, plus any Drive doc IDs listed in your task; read Drive docs w/ the Drive connector `read_file_content`).
3. Write a 10-line outline of your sections before writing HTML. Keep it in NOTES.md.
4. Build the page. Then lint: `grep -c '—' <slug>/index.html` must be 0; every `{{custom_values.*}}` you use must appear in the checklist table; no `[TO BUILD]` for things the source already links.
5. Open it in a browser once (the `run`/preview tool or `python3 -m http.server`) and screenshot the hero + one msg card to confirm the CSS applied.
