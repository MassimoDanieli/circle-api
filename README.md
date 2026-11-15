# Circle API (FastAPI)

Simple API that calculates area and circumference of a circle from a radius.

```bash
curl "http://localhost:8000/circle?radius=2&units=cm"
# {"radius":2.0,"area":12.566…,"circumference":12.566…,"units":"cm","pi":"math.pi"}
```

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
python -m pytest -q
```

`requirements.txt` holds the runtime dependencies (what goes in the image);
`requirements-dev.txt` adds the test tools.

## Container

```bash
docker build -t circle-api .
docker run -p 8000:8000 circle-api
```

Runs as an unprivileged user (uid 10001) and has a Docker `HEALTHCHECK` on `/healthz`.

## CI/CD

On every push and PR: tests and `pip-audit`, then the image is built, started
and smoke-tested. Pushes to `main` publish `ghcr.io/massimodanieli/circle-api:main`
and `:sha-<commit>`; same-repo PRs publish `:sha-<commit>`. The image is
deployed by [gitops-workloads](https://github.com/MassimoDanieli/gitops-workloads)
through Argo CD.
