# Workflows — Build with Microsoft AI

## Workflow A — Mind the observability gap

**Source:** Boyd & Narasimhan [src-001]

### Steps

1. Requirements = platform; agent = train — measure fit continuously [src-001 @ 1:51].
2. Run evals from early lifecycle through production [src-001 @ 2:11].
3. Close gap between spec and wild behavior before launch [src-001 @ 2:20].
4. Accelerate observe → improve loop with traces [src-001 @ 3:43].

### Deliverables

- [ ] Eval matrix tied to product requirements

---

## Workflow B — Safety and monitoring

**Source:** Boyd & Narasimhan [src-001]

### Steps

1. Guardrails as user-facing “mind the gap” warnings [src-001 @ 2:25].
2. Monitor across fleet of agents, not one dashboard once [src-001 @ 2:56].
3. Track customer interaction patterns with agent [src-001 @ 2:51].

### Deliverables

- [ ] Safety + monitor dashboard spec

---

## Workflow C — Agent tier selection

**Source:** Hampton [src-002]

### Steps

1. **Local:** hands-on, human-in-the-loop pairing [src-002 @ 2:39].
2. **Background:** isolated worktree tasks, semi-async [src-002 @ 3:07].
3. **Cloud:** fire-and-forget heavy jobs [src-002 @ 4:48].
4. Reject one-shot “build entire app” expectations [src-002 @ 1:09].

### Deliverables

- [ ] Decision table for task types → agent tier

---

## Workflow D — Worktrees and parallelism

**Source:** Hampton [src-002]

### Steps

1. Map branch to isolated subdirectory (worktree) [src-002 @ 3:22].
2. Use background agent when local focus matters [src-002 @ 4:16].
3. Manage token spend explicitly [src-002 @ 1:46].

### Deliverables

- [ ] Copilot/VS Code setup guide for parallel background tasks
