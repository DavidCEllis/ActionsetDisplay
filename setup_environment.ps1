Write-Host "Creating virtual environment in folder: env"

# Create virtualenv
python -m venv env

# Activate virtualenv
env\Scripts\Activate.ps1

Write-Host "Environment Created"

Write-Host ""
Write-Host "Updating python dependency installer"
# Update pip
python -m pip install --upgrade pip

Write-Host ""
Write-Host "Installing project and dependencies"
# install module in virtualenv in dev mode
python -m pip install -e .

# Deactivate virtualenv
deactivate

Write-Host ""
Write-Host "Install Completed"

Write-Host -NoNewLine 'Press any key to close...'
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
