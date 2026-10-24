# layoffprep

The interview prep hub (AlgoScope, Java, DB and OS steppers, Backpressure system design, MachineCodingLab), served from its own site.

The hub (`index.html`, `data.json`, `sw.js`) lives here. The tools stay in their own repos; `.github/workflows/deploy.yml` checks each one out, builds it, and `scripts/assemble.py` puts them beside the hub, so `/algoscope/`, `/java-visualizer/`, `/DBVisualizer/`, `/OSVisualizer/` and `/backpressure/` are same-origin iframes. The Machine Coding lab runs on Render and is embedded from there.

It redeploys on every push, on demand, and daily at 03:17 UTC to pick up changes in the tool repos.

`data.json` is built by `tools/build_prep_data.py` in the portfolio repo (`AdityaMalu.github.io`); copy the result here after stepper content changes.
