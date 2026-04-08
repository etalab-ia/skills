# INSTRUCTIONS.md — La Suite numérique Projects

> **Ready to use.** Copy this file to the root of your project as `INSTRUCTIONS.md`.
> Claude Code and other AI coding assistants automatically load it as context.
>
> Source: [Suite numérique Dev Handbook](https://suitenumerique.gitbook.io/handbook)

---

# Project Instructions

## Context

Project part of La Suite numérique, the French government's digital workplace.
Follows the [Suite numérique Dev Handbook](https://suitenumerique.gitbook.io/handbook) conventions.

## Language

| Context | Language |
|---------|----------|
| Source code (variables, functions, types) | English |
| Code comments | English |
| Commit messages | **English** (La Suite convention) |
| Issues, MR/PR, discussions | **French** |
| User interface | French |

---

## Design System

Use the **La Suite UI Kit** and **Cunningham**:

- `@gouvfr-lasuite/ui-kit` — https://github.com/suitenumerique/ui-kit
- `@gouvfr-lasuite/cunningham-react` — the UI Kit foundation
- Online Storybook: https://suitenumerique.github.io/cunningham/storybook
- "French State Design System" theme (light + dark mode)

**Available components:**
MainLayout, Header, LeftPanel, RightPanel, Footer, Tabs, DropdownMenu, Input, Textarea, Select, Checkbox, Radio, Switch, Label, TreeView, Datagrid, QuickSearch, Badge, Icon, Loader, Tooltip, Modal, Separator, Hero, Filter, LanguageSelector, ShareModal, UserAvatar, UserMenu, UsersInvitation, LaGaufre, ProConnectButton

> For detailed component reference and code patterns, the `lasuite-ui-kit` skill from [etalab-ia/skills](https://github.com/etalab-ia/skills) covers both `@gouvfr-lasuite/ui-kit` and `@gouvfr-lasuite/cunningham-react`.

**Rules:**
- NEVER create a custom component if an equivalent UI Kit or Cunningham component exists
- Use Cunningham design tokens for theming (no hardcoded colors)
- Run `yarn storybook` for local interactive documentation

---

## Accessibility — RGAA

RGAA 4.2 compliance (WCAG 2.1 AA) is mandatory.
Ref: https://accessibilite.numerique.gouv.fr/ + [handbook/accessibility](https://suitenumerique.gitbook.io/handbook/accessibility)

> For a comprehensive audit, the `rgaa` skill from [etalab-ia/skills](https://github.com/etalab-ia/skills) provides a full 106-criteria audit tool that produces structured conformity reports.

**Test with a screen reader:**
- macOS: VoiceOver + Safari (built-in)
- Windows: NVDA + Firefox (free)
- Browser devtools accessibility tools are a first check, not a replacement

### Images and text alternatives

- Only give `alt` to images that carry information
- If the info is already in adjacent text → `alt=""` (no duplication for screen readers)
- Decorative images: `alt=""` mandatory (otherwise some screen readers read the file URL)
- Decorative SVGs: `aria-hidden="true"`
- Informative SVGs: `role="img"` + `aria-label` + `<title>` inside the SVG
- The alternative describes the **meaning**, not the appearance ("Share on Facebook", not "Blue Facebook logo")

### Contrasts

- Text: minimum 4.5:1 ratio (3:1 for large text)
- Interface components (input borders, progress bars...): minimum 3:1 ratio with their environment — RGAA criterion 3.3
- If a component conveys information only through color: either ensure contrast or add accessible text

### Headings (h1-h6)

- Strict hierarchy with no skipping (h2 → h3, never h2 → h4)
- A heading contextualizes a section — do not use it for bold text
- In a modal: restart from h1 (isolated context)
- Style with CSS if the visual rendering ≠ semantic level

### Links

- Link texts must be unique on the page (no multiple "Learn more")
- If differentiation is needed: add visually hidden text (offscreen class)
- Avoid `<a>` wrapping rich content (cards): put the link on the title, extend the clickable area with JS using `aria-hidden` and `tabindex="-1"` on duplicated elements

### Forms

- Each input has a `<label for="...">` or an `aria-label`
- `placeholder` is NOT a label
- Link errors/help to their input with `aria-describedby`
- Do NOT disable the submit button: let the user attempt to submit, then focus on the first error

### Keyboard navigation and SPA

- When content replaces other content (client navigation, form steps) → reposition focus with `tabindex="-1"` + programmatic focus
- Systematically test keyboard navigation after every content replacement
- `aria-live="polite"` for partial updates without full replacement
- In React: `useRef` + `useEffect` or `MutationObserver` to manage focus on mount/unmount

### DOM order

- DOM order = reading order (screen readers ignore CSS)
- If the visual layout differs: use `flexbox` + `order`, or duplicate with hidden content

---

## Security

Ref: [handbook/security](https://suitenumerique.gitbook.io/handbook/security) + ANSSI

> For a comprehensive review, the `securite-anssi` skill from [etalab-ia/skills](https://github.com/etalab-ia/skills) provides a full 12-rule ANSSI security checklist for government app development.

**Code:**
- No secrets, API keys, or passwords in code
- Environment variables not committed, different between local / staging / production
- Validate all user inputs (Zod recommended)
- SQL injection prevention (parameterized queries)
- XSS prevention (sanitized outputs)
- Error messages without internal details
- Dependencies up to date
- Develop in containerized environments (Docker)

**GitHub:**
- Signed commits mandatory (SSH or GPG, Yubikey recommended)
- 2FA enabled
- No automatic production deployment from the repo

---

## GDPR / CNIL

- Minimize collected data
- Explicit consent for non-essential cookies
- No third-party tracking without consent
- Legal notices and privacy policy required

---

## Stack

| Component | Default choice |
|-----------|---------------|
| Frontend | Next.js or Vite + React 19 |
| Backend | Django Rest Framework |
| Design System | `@gouvfr-lasuite/ui-kit` + `cunningham-react` |
| Validation | Zod |
| Tests | Vitest + Playwright |
| Package manager | **yarn** (never npm) |
| Hosting | Scalingo or sovereign PaaS |
| TypeScript | Strict mode |
| Formatting | Prettier |
| Linting | ESLint with TypeScript rules |

---

## Tests

- Any new feature must be accompanied by tests
- Before considering a task complete, run the tests and verify that they pass
- If you modify existing code, add tests if there aren't any already

```bash
yarn test              # Unit tests
yarn test:e2e          # E2E tests
yarn test:coverage     # Coverage
```

---

## Git Conventions

Ref: [handbook/git](https://suitenumerique.gitbook.io/handbook/git)

### Commits (gitmoji)

Format: `<emoji>(<scope>) <subject>` + mandatory body

```
✨(frontend) add user authentication logic

Implemented login and signup features, and integrated OAuth2
for social login.
```

- Emoji: unicode (✨ not :sparkles:) — https://gitmoji.dev/
- Scope: affected component (docker, frontend, backend, auth...)
- Subject: present imperative, lowercase, no trailing period
- Body: explain **WHY**, not what (the diff shows the what)

**Common emojis:**

| Emoji | Usage |
|-------|-------|
| ✨ | New feature |
| 🐛 | Bug fix |
| ♻️ | Refactoring |
| 📝 | Documentation |
| 🔧 | Configuration |
| 🔖 | Release / version |
| 🔥 | Code removal |
| ✅ | Tests |
| 🐳 | Docker |

### Granularity

- Few but coherent commits
- Green tests on each commit
- Multiple commits in a branch = multiple distinct sub-problems

### Workflow

- **Open source**: GitHub Flow (master stable, feature branches, PR)
- **Internal**: Git Flow (master + develop + feature/hotfix/release)
- Merge: **rebase and merge** (no merge commits)

### Pull Requests

- Open the PR early with `WIP:` in the title
- Max **500 lines** per PR (split otherwise)
- Before review: green tests, feature documented, branch rebased
- Changelog under `[Unreleased]` (keepachangelog format)
- Approval by at least 1 core member

### Releases

Format: `🔖(minor) bump release to X.Y.Z` with changelog in the commit body.

---

## Pre-commit Checklist

1. No secrets in code
2. Inputs validated
3. No `console.log` in production
4. UI Kit / Cunningham components used
5. Text alternatives on informative images
6. Keyboard navigation OK for dynamic content
7. Tests pass
8. Changelog up to date if applicable

---

## Open Source

- All code is public
- License: **MIT**
- Signed commits (SSH/GPG)
- Never commit personal data or tokens

---

## Relevant Skills

The [etalab-ia/skills](https://github.com/etalab-ia/skills) repository provides AI coding assistant skills tailored for French government projects:

- **lasuite-ui-kit** — Component reference for La Suite UI Kit (`@gouvfr-lasuite/ui-kit` and `@gouvfr-lasuite/cunningham-react`)
- **rgaa** — Full 106-criteria RGAA accessibility audit tool with structured conformity reports
- **securite-anssi** — Comprehensive 12-rule ANSSI security checklist
- **datagouv-apis** — data.gouv.fr APIs reference (catalog, metrics, tabular data)
