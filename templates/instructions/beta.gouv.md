# INSTRUCTIONS.md — beta.gouv / French Government Projects

> **Ready to use.** Copy this file to the root of your project as `INSTRUCTIONS.md`.
> Claude Code and other AI coding assistants automatically load it as context.
>
> Source: [beta.gouv standards](https://doc.incubateur.net/communaute/gerer-son-produit/readme-doc-incubateur-net)

---

# Project Instructions

## Context

> **Adapt this section to your project.** Describe what the product does, who it serves, and its current stage (investigation, construction, acceleration, transfer). This helps the AI assistant understand the domain and make better decisions.

French government project, part of the [beta.gouv.fr](https://beta.gouv.fr/) ecosystem.
Compliant with [beta.gouv standards](https://doc.incubateur.net/).

<!-- Example:
**[Product name]** is a [brief description of the product and its purpose].
It serves [target users] and is currently in [phase] stage.
Key domain concepts: [list 3-5 domain terms the AI should know].
-->

## Language

> **Adapt if needed.** These are the beta.gouv defaults. Adjust if your team uses different conventions (e.g., English commit messages for international contributors).

| Context | Language |
|---------|----------|
| Source code (variables, functions, types) | English |
| Code comments | English |
| Commit messages | **French** |
| Pull/Merge Requests (title, description) | **French** |
| Issues and discussions | **French** |
| Code review | **French** |
| User interface | French |

---

## Expected Behavior

### Plan Mode

For any non-trivial task (3+ steps or architectural decision):

1. Write the plan in `tasks/todo.md` with checkable items
2. Validate the plan before implementing
3. Mark items as completed along the way
4. Add a "result" section at the end of `tasks/todo.md`

If something goes off track: **STOP** and re-plan before continuing.

### Task Management (`tasks/`)

```
tasks/
├── todo.md      # Current plan: checkable items, final result
└── lessons.md   # Error patterns encountered on this project
```

`tasks/todo.md` is reset for each new task. `tasks/lessons.md` is cumulative.

### Self-Improvement Loop

After any user correction:
- Update `tasks/lessons.md` with the error pattern and the rule to remember
- Re-read `tasks/lessons.md` at the start of each session to avoid repeating the same mistakes

### Bug Fixing

When facing a bug: fix it directly. Point to logs, errors, and failing tests — then resolve without asking for step-by-step guidance.

### Code Quality

For any non-trivial change, ask yourself: **"Is there a more elegant solution?"**

If a fix feels hacky: *"Knowing everything I know now, implement the elegant solution."*

Do not apply to simple, obvious fixes — no over-engineering.

---

## Architecture

> **Adapt this section to your project.** Document the directory structure and key files so the AI assistant understands the codebase layout.

```
src/
├── app/                # Pages and routes
├── components/         # Reusable UI components
├── lib/                # Business logic, utilities, types
└── __tests__/          # Unit and E2E tests
```

---

## Design System — DSFR

> **Keep the framework row matching your stack** and remove the others from the table below. If your project has no UI, you can remove this entire section.

The [DSFR](https://www.systeme-de-design.gouv.fr/) (Design System de l'État) is **mandatory** for French government services.
Component docs: https://www.systeme-de-design.gouv.fr/version-courante/fr/composants

**Framework implementations:**

| Framework | Package | Repo |
|-----------|---------|------|
| React | `@codegouvfr/react-dsfr` | https://github.com/codegouvfr/react-dsfr |
| Vue.js | `vue-dsfr` | https://github.com/dnum-mi/vue-dsfr |
| Angular | `@edugouvfr/ngx-dsfr` | https://gitlab.mim-libre.fr/men/transverse/dsmen/ngx-dsfr-components |
| Django | `django-dsfr` | https://github.com/entrepreneur-interet-general/django-dsfr |
| Rails | `dsfr-view-components` | https://github.com/betagouv/dsfr-view-components |
| Keycloak | `keycloak-theme-dsfr` | https://github.com/codegouvfr/keycloak-theme-dsfr |

> Use the DSFR implementation matching your project's stack. RGAA 4.2 accessibility compliance is built in.

> For React projects, the `react-dsfr` skill from [skills-etat](https://github.com/numerique-gouv/skills-etat) provides detailed component reference and code patterns.

**Plain HTML:**
- Use `fr-*` CSS classes
- Follow the examples from the official documentation

**Rules:**
- NEVER create a custom component if an equivalent DSFR component exists
- Always check the DSFR docs before implementing
- Use DSFR colors and spacing (no hardcoded values)
- Map Figma components to existing DSFR components

---

## Accessibility — RGAA

RGAA 4.2 compliance (WCAG 2.1 AA) is mandatory.
Ref: https://accessibilite.numerique.gouv.fr/

> For a comprehensive audit, the `rgaa` skill from [skills-etat](https://github.com/numerique-gouv/skills-etat) provides a full 106-criteria audit tool that produces structured conformity reports.

### Images

- `alt` only on images that carry information
- Decorative images: `alt=""` (mandatory, otherwise screen readers read the URL)
- The alternative describes the **meaning**, not the appearance

### Contrasts

- Text: minimum 4.5:1 ratio (3:1 for large text)
- Interface components: minimum 3:1 ratio with their environment
- Use DSFR colors (compliant by default)

### Structure

- Headings h1-h6: strict hierarchy with no level skipping
- Functional keyboard navigation
- Semantic structure (headings, landmarks, lists)

### Forms

- Each input has a `<label for="...">` or `aria-label`
- `placeholder` is NOT a label
- Link errors/help via `aria-describedby`
- Do not disable the submit button

### SPA Navigation

- Reposition focus after content replacement (`tabindex="-1"` + programmatic focus)
- Test keyboard navigation after every view change
- `aria-live="polite"` for partial updates

---

## Security — ANSSI

Ref: https://cyber.gouv.fr/les-regles-de-securite

- [ ] No secrets, API keys, or passwords in code
- [ ] Environment variables not committed, different per environment
- [ ] All inputs validated (Zod recommended)
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (sanitized outputs)
- [ ] Error messages without internal details
- [ ] Dependencies up to date (no known vulnerabilities)
- [ ] No `console.log` in production

> For a comprehensive review, the `securite-anssi` skill from [skills-etat](https://github.com/numerique-gouv/skills-etat) provides a full 12-rule security checklist for government app development.

---

## GDPR / CNIL

- Minimize collected data
- Explicit consent for non-essential cookies
- No third-party tracking without consent
- Legal notices and privacy policy required

---

## Recommended Stack

> **Adapt to your project.** Replace the defaults below with your actual stack. Remove rows that don't apply (e.g., no frontend for an API-only project). The AI assistant uses this table to choose the right tools and patterns.

| Component | Default choice |
|-----------|---------------|
| Frontend | Next.js or Vite + React |
| Design System | `@codegouvfr/react-dsfr` |
| Validation | Zod |
| Unit tests | Vitest |
| E2E tests | Playwright |
| Package manager | **pnpm** (never npm or yarn) |
| Hosting | Scalingo or sovereign PaaS |
| TypeScript | Strict mode |
| Formatting | Prettier (single quotes) |
| Linting | ESLint with TypeScript rules |

<!-- Add or remove rows as needed. Examples:
| Backend | Django / FastAPI / Express |
| Database | PostgreSQL |
| ORM | Prisma / Drizzle |
| Auth | ProConnect / Keycloak |
-->

**Code conventions:**
- `type` over `interface`
- Unused variables prefixed with `_`
- No `any` type
- Arrow functions for React components

---

## Tests & Definition of Done

### Definition of Done

A task is only complete when all 3 steps are validated, in order:

1. **Automated tests**: `pnpm validate` passes (lint + type-check + unit tests)
2. **Visual verification**: open the relevant page in the browser, verify rendering, navigation, and interactions
3. **Fix loop**: if any issue is found (test or visual), fix and restart from step 1

Never consider a task done based solely on code — the browser rendering is the source of truth.

### Commands

> **Adapt to your project.** The key principle is having a single `validate` command that runs all checks.

```bash
pnpm dev               # Dev server
pnpm test              # Unit tests (Vitest)
pnpm test:e2e          # E2E tests (Playwright)
pnpm test:coverage     # Coverage
pnpm validate          # lint + type-check + tests (single entry point)
```

The `validate` script should be defined in `package.json`:
```json
{
  "scripts": {
    "validate": "pnpm lint && pnpm type-check && pnpm test"
  }
}
```

**Coverage targets:** 70% minimum for new code, 90%+ for critical paths.

---

## CI — GitHub Actions

> **Adapt to your project.** At minimum, CI should run lint, type-check, tests, and build on every push and PR.

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'pnpm'
      - run: pnpm install --frozen-lockfile
      - run: pnpm lint
      - run: pnpm type-check
      - run: pnpm test
      - run: pnpm build
```

---

## Pre-commit (Husky)

`pnpm validate` runs on every commit via Husky. **Never bypass with `--no-verify`** — if the hook fails, fix the underlying issue.

```bash
# Setup (once)
pnpm add -D husky
pnpm exec husky init
echo "pnpm validate" > .husky/pre-commit
```

---

## Dependencies

**Never add a dependency without explicit approval.** Before installing a new package:
- Check if the functionality already exists in the current stack or in DSFR
- Prefer standard library or built-in browser APIs when possible
- Ask for validation before running `pnpm add`

This prevents dependency bloat, supply chain risks, and ensures the team reviews every addition.

---

## Git Conventions

### Commits

Format: `type: Description en français`

```bash
feat: Ajouter l'export PDF des fiches projet
fix: Corriger le calcul du budget prévisionnel
docs: Mettre à jour le guide d'installation
refactor: Simplifier la logique de validation
test: Ajouter les tests du composant Filtre

# With issue reference
feat: Implémenter le filtre par région (#456)
```

**Common types:**

| Type | Usage |
|------|-------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation |
| `refactor` | Refactoring without functional change |
| `test` | Adding or modifying tests |
| `chore` | Maintenance, config, CI |
| `style` | Formatting, no logic change |
| `data` | Adding or modifying data files |

### Branches

> **Add branch patterns specific to your project** (e.g., `data/source-name` for data projects, `hotfix/...` for production fixes).

```
feat/description-courte
fix/description-courte
```

---

## Pre-commit Checklist

1. No secrets in code
2. Inputs validated
3. No `console.log` in production
4. DSFR components used (no custom components if a DSFR equivalent exists)
5. `alt` on informative images
6. Keyboard navigation OK for dynamic content
7. `pnpm validate` passes
8. Tests pass

---

## Open Source

> **Specify your license.** beta.gouv projects are open source by default. Choose MIT or Apache 2.0 and update below.

- All code is public (beta.gouv requirement)
- License: MIT or Apache 2.0
- Never commit personal data or tokens
- Ref: [Open source contribution policy](https://disic.github.io/politique-de-contribution-open-source/)

---

## Relevant Skills

The [skills-etat](https://github.com/numerique-gouv/skills-etat) repository provides AI coding assistant skills tailored for French government projects:

- **react-dsfr** — React component reference for the DSFR design system (`@codegouvfr/react-dsfr`)
- **rgaa** — Full 106-criteria RGAA accessibility audit tool with structured conformity reports
- **securite-anssi** — Comprehensive 12-rule ANSSI security checklist
- **datagouv** — data.gouv.fr APIs reference (catalog, metrics, tabular data)

---

## Resources

**Standards & documentation:**
- [beta.gouv standards](https://doc.incubateur.net/communaute/gerer-son-produit/readme-doc-incubateur-net)
- [Sillon — beta.gouv technical guide](https://sillon.incubateur.net)
- [Dashlord — Quality dashboard](https://dashlord.incubateur.net)
- [beta.gouv project templates](https://github.com/betagouv/?q=template&type=all)
- [Awesome beta.gouv — Open source tools catalog](https://github.com/betagouv/awesome-betagouv)

**DSFR & accessibility:**
- [DSFR — Components](https://www.systeme-de-design.gouv.fr/)
- [react-dsfr](https://github.com/codegouvfr/react-dsfr)
- [RGAA 4.2](https://accessibilite.numerique.gouv.fr/)

**Security & compliance:**
- [ANSSI — Security rules](https://cyber.gouv.fr/les-regles-de-securite)
- [Open source contribution policy](https://disic.github.io/politique-de-contribution-open-source/)
