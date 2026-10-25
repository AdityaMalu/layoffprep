#!/usr/bin/env bash
# Cloudflare Pages build: clone and build the tools, then assemble them beside the hub into site/.
# Build command: bash scripts/cf_build.sh   Output directory: site   Env: NODE_VERSION=22
set -euo pipefail
mkdir -p .src
for r in algoscope java-visualizer DBVisualizer OSVisualizer backpressure; do
  rm -rf ".src/$r"
  git clone --depth 1 -q "https://github.com/AdityaMalu/$r.git" ".src/$r"
done

(cd .src/algoscope && python3 tools/make_site.py --out _site)
for d in java-visualizer DBVisualizer OSVisualizer; do
  (cd ".src/$d" && npm ci --silent && npm run build)
done

python3 scripts/assemble.py --out site \
  --algoscope .src/algoscope/_site \
  --java .src/java-visualizer/dist \
  --db .src/DBVisualizer/dist \
  --os .src/OSVisualizer/dist \
  --backpressure .src/backpressure
