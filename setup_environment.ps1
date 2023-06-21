# Create virtualenv
python -m venv env

# Activate virtualenv
env\Scripts\Activate.ps1

# install module in virtualenv in dev mode
python -m pip install -e .

# Deactivate virtualenv
deactivate