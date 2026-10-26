"""Assemble the deployable site: the hub at the root, each tool in its own folder beside it.

Usage:
  python scripts/assemble.py --out site --algoscope A --java J --db D --os O --backpressure B
Each tool argument is the folder holding that tool's built, ready-to-serve files.
"""
import argparse, os, shutil, sys

HUB_FILES = ["index.html", "data.json", "sw.js", "og.png", "robots.txt", "sitemap.xml", "google732466c2c1f96fdd.html", "_headers"]
HUB_DIRS = ["leetcode"]
TOOLS = {"algoscope": "algoscope", "java": "java-visualizer", "db": "DBVisualizer", "os": "OSVisualizer", "backpressure": "backpressure"}
SKIP = shutil.ignore_patterns(".git", ".github", "node_modules", "__pycache__", "serve.py", "tools", "*.md")

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ap = argparse.ArgumentParser()
ap.add_argument("--out", default="site")
for arg in TOOLS:
    ap.add_argument("--" + arg, required=True)
args = ap.parse_args()

if os.path.isdir(args.out):
    shutil.rmtree(args.out)
os.makedirs(args.out)
for f in HUB_FILES:
    shutil.copy(os.path.join(root, f), args.out)
for d in HUB_DIRS:
    shutil.copytree(os.path.join(root, d), os.path.join(args.out, d))
for arg, folder in TOOLS.items():
    src = getattr(args, arg)
    if not os.path.isfile(os.path.join(src, "index.html")):
        sys.exit(f"{src} has no index.html: build {folder} first")
    shutil.copytree(src, os.path.join(args.out, folder), ignore=SKIP)
open(os.path.join(args.out, ".nojekyll"), "w").close()
print("assembled", args.out)
