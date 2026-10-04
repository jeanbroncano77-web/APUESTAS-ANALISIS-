$ProgressPreference = 'SilentlyContinue'
$url = 'https://api.github.com/repos/jeanbroncano77-web/APUESTAS-ANALISIS-/actions/runs'
try {
    $resp = Invoke-RestMethod -Uri $url -Headers @{ 'User-Agent' = 'PowerShell' }
    Write-Host "Total workflow runs: $($resp.total_count)"
    foreach ($r in ($resp.workflow_runs | Select-Object -First 10)) {
        Write-Host "Run #$($r.run_number): $($r.name) | Event: $($r.event) | Status: $($r.status) | Conclusion: $($r.conclusion) | CreatedAt: $($r.created_at)"
    }
} catch {
    Write-Host "Error: $($_.Exception.Message)"
}
