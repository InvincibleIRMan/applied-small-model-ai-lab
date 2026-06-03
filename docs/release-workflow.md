# Release Workflow

This document describes the weekly release process for Applied Small Models AI Lab.

---

## Weekly Release Checklist

Run this checklist every Monday morning on release day.

### Content

- [ ] YouTube video is published and unlisted link is ready
- [ ] Substack article is published (or scheduled)
- [ ] Notebook is tested end-to-end on a clean environment
- [ ] `requirements.txt` in the week's `code/` folder is up to date
- [ ] Datasets are committed or download instructions are in the README

### Repository

- [ ] Week folder README is complete (links, objectives, instructions)
- [ ] Main `README.md` roadmap table updated:
  - Status column: `Coming Soon` → `Released MMM D, YYYY`
  - YouTube column: placeholder → actual link
  - Substack column: placeholder → actual link
  - Notebook column: placeholder → relative path link
- [ ] All placeholder `.gitkeep` files removed from the week's folder
- [ ] Git tag created: `git tag week-XX-release`

### GitHub

- [ ] Push tag: `git push origin week-XX-release`
- [ ] Create a GitHub Release from the tag with a short description
- [ ] Pin the discussion post for the week (optional)

---

## Branch Strategy

```
main          ← always clean; only released content
dev           ← working branch; prep next week here
week-XX-prep  ← optional short-lived branch per week
```

Work on `dev` or a `week-XX-prep` branch.
Merge to `main` on release day only.

---

## URL Placeholder Convention

In weekly README files, use these placeholders until content goes live:

```
YouTube:  https://youtube.com/@applied-slm-lab (channel link)
Substack: https://appliedslmlab.substack.com   (publication link)
Notebook: Coming Soon
```

Replace with direct links on release day.

---

## Git Tag Convention

```bash
git tag week-01-release -m "Week 01: Welcome to Applied Small Models AI Lab"
git tag week-02-release -m "Week 02: Hello Small Language Models"
git push origin --tags
```

---

## GitHub Release Description Template

```
## Week XX – [Title]

Released: [Date]

### What's inside
- Notebook: [brief description]
- Key concepts: [bullet list]

### Links
- YouTube: [URL]
- Substack: [URL]
```
