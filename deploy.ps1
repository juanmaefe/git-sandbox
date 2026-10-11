# deploy.ps1 — run INSIDE the prod clone: .\deploy.ps1 v0.2.0
param([Parameter(Mandatory=$true)][string]$Tag)

git fetch --tags origin
if ($LASTEXITCODE -ne 0) { throw "fetch failed" }

git checkout $Tag
if ($LASTEXITCODE -ne 0) { throw "tag $Tag not found" }

pip install -r requirements.txt --quiet

# --- FO-Auto will add here: python -m fo_auto.init_db, then
# --- Restart-Service fo-auto-api, fo-auto-worker-internal, ... and a GET /health/cachestatus

python -c "import engine.calc; print('import ok')"
Write-Host "[DEPLOY OK] now running $(git describe --tags)"