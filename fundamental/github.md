# GitHub — Lecture Notes

## Overview
- **What is GitHub?** A web-based platform for hosting Git repositories that enables version control, collaboration, and project management for software and documentation.
- **Core purpose:** Store code, track changes, collaborate with others, and automate workflows (CI/CD).

## Git vs GitHub
- **Git:** A distributed version control system that runs locally; manages commits, branches, merges, and history.
- **GitHub:** A hosted service built around Git that adds collaboration features (pull requests, issues), web UI, access control, and integrations.

## Key Concepts
- **Repository (repo):** A project container holding files, history, and metadata.
- **Commit:** A snapshot of changes with a message and author metadata.
- **Branch:** A movable pointer to a commit; used to develop features in isolation.
- **Merge:** Integrate changes from one branch into another.
- **Pull Request (PR):** A request to merge changes; facilitates code review and discussion.
- **Issue:** A tracker for bugs, tasks, or feature requests.
- **Fork:** A personal copy of someone else's repository to propose changes independently.

## Collaboration Workflows
- **Centralized (branch on main):** Developers create branches in the main repo, open PRs, then merge.
- **Fork & PR:** Common in open-source: contributors fork the repo, push feature branches to their fork, then open PRs to the upstream repo.
- **Feature branches:** Use short-lived branches per feature/bugfix and delete after merging.

## Pull Requests & Code Review
- PRs include diffs, discussion threads, and checks (CI results).
- Reviewers request changes, comment on lines, and approve before merge.
- Use protected branches and required checks to enforce quality.

## GitHub Actions (CI/CD)
- Automate builds, tests, and deployments using workflow YAML files in `.github/workflows/`.
- Triggers: push, pull_request, schedule, and more.
- Example: run tests on every PR and deploy on merge to `main`.

## Issues & Project Management
- Use **Issues** for tracking work, labels for categorization, and milestones for grouping.
- **Projects (boards)** provide Kanban-style planning and automation.

## Security & Access
- **Permissions:** Organization-level teams and repo-level roles (read, triage, write, maintain, admin).
- **Secrets:** Store credentials for workflows safely (encrypted secrets).
- **Dependabot:** Automated dependency updates and security alerts.

## Best Practices
- Write clear commit messages and small commits.
- Use descriptive branch names (e.g., `feature/login-form`, `fix/typo-readme`).
- Protect `main`/`master` with branch protection rules.
- Require PR reviews and CI checks before merging.
- Keep PRs focused and small for easier review.

## Useful Git Commands (quick reference)
```bash
# clone a repo
git clone https://github.com/user/repo.git

# create and switch to a branch
git checkout -b feature/my-feature

# stage and commit
git add .
git commit -m "Add feature"

# push branch to origin
git push -u origin feature/my-feature

# update local main and rebase feature branch
git checkout main
git pull
git checkout feature/my-feature
git rebase main

# merge via PR (preferred) or locally
git checkout main
git merge feature/my-feature
git push
```

## Example Minimal Workflow
1. Create a branch: `git checkout -b feature/x`
2. Implement changes, commit locally.
3. Push branch: `git push -u origin feature/x`
4. Open a Pull Request on GitHub, request review.
5. Fix review comments, push additional commits.
6. Merge PR after passing checks and reviews.

## Resources
- Official GitHub Docs: https://docs.github.com
- Pro Git book: https://git-scm.com/book/en/v2

---

Prepared as concise lecture notes for classroom or self-study.

