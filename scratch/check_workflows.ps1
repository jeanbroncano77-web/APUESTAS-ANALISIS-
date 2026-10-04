$ProgressPreference = 'SilentlyContinue'
$url = 'https://api.github.com/repos/jeanbroncano77-web/APUESTAS-ANALISIS-/actions/workflows'
try {
    $resp = Invoke-RestMethod -Uri $url -Headers @{ 'User-Agent' = 'PowerShell' }
    foreach ($w in $resp.workflows) {
        Write-Host "Workflow: $($w.name) | State: $($w.state) | Path: $($w.path) | ID: $($w.id)"
    }
} catch {
    Write-Host "Error: $($_.Exception.Message)"
}
