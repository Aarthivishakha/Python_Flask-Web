# Flask Web / REST API (Python 3.4)

Legacy Flask REST API with an application factory, blueprints, validation,
service-layer storage, tests, and version-aware analysis-tool metadata.

```bash
virtualenv .venv
. .venv/bin/activate
pip install -r requirements-dev.txt
python run.py
```

Endpoints: `GET /health` and CRUD at `/api/v1/items`.

Python 3.4 is end-of-life. Dependencies are deliberately pinned to their last
compatible legacy lines. Only tools explicitly marked `supported: true` in
`tool-triggers/` can execute on this interpreter; the other manifests document
why that analysis is unavailable rather than pretending it can run.
