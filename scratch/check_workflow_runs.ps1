$ProgressPreference = 'SilentlyContinue'
$url = 'https://api.github.com/repos/jeanbroncano77-web/APUESTAS-ANALISIS-/actions/workflows/372708300/runs'
try {
    $resp = Invoke-RestMethod -Uri $url -Headers @{ 'User-Agent' = 'PowerShell' }
    Write-Host "Total runs for workflow 372708300: $($resp.total_count)"
    foreach ($r in $resp.workflow_runs) {
        Write-Host "Run #$($r.run_number): Event: $($r.event) | Status: $($r.status) | Conclusion: $($r.conclusion) | CreatedAt: $($r.created_at)"
    }
} catch {
    Write-Host "Error: $($_.Exception.Message)"
}
