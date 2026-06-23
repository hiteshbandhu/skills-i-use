#!/usr/bin/env node
/**
 * Sync `.claude-plugin/marketplace.json` skill lists from the filesystem.
 *
 * Each plugin's `skills` array is regenerated from the SKILL.md folders found
 * under that plugin's `source` directory — so adding a new skill folder is all
 * it takes; the manifest stays correct automatically.
 *
 * Usage:
 *   node scripts/sync-marketplace.mjs            # rewrite the manifest in place
 *   node scripts/sync-marketplace.mjs --check    # exit 1 if the manifest is stale
 */
import { existsSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const repo = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const manifestPath = join(repo, ".claude-plugin", "marketplace.json");
const check = process.argv.includes("--check");

const manifest = JSON.parse(readFileSync(manifestPath, "utf8"));

// A skill folder is one that contains SKILL.md. We must not register another
// plugin's source root as a skill of its parent (e.g. the ai-engineer-talks
// bundle dir living inside ./skills).
const pluginRoots = new Set(
  manifest.plugins.map((p) => resolve(repo, p.source)),
);

let stale = false;

for (const plugin of manifest.plugins) {
  const dir = resolve(repo, plugin.source);
  const discovered = readdirSync(dir, { withFileTypes: true })
    .filter((e) => e.isDirectory())
    .map((e) => e.name)
    .filter((name) => existsSync(join(dir, name, "SKILL.md")))
    .filter((name) => !pluginRoots.has(join(dir, name)))
    .sort()
    .map((name) => `./${name}`);

  const previous = plugin.skills ?? [];
  if (JSON.stringify(previous) !== JSON.stringify(discovered)) {
    stale = true;
    const added = discovered.filter((s) => !previous.includes(s));
    const removed = previous.filter((s) => !discovered.includes(s));
    const parts = [];
    if (added.length) parts.push(`+${added.join(", ")}`);
    if (removed.length) parts.push(`-${removed.join(", ")}`);
    console.log(`[${plugin.name}] ${parts.join("  ")}`);
    plugin.skills = discovered;
  }
}

if (!stale) {
  console.log("marketplace.json is in sync.");
  process.exit(0);
}

if (check) {
  console.error(
    "\nmarketplace.json is out of date with the skills/ folders.\n" +
      "Run: node scripts/sync-marketplace.mjs",
  );
  process.exit(1);
}

writeFileSync(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`);
console.log("Updated marketplace.json.");
