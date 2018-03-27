env:
	rm -R venv
	virtualenv -p python3 venv
	. venv/bin/activate && pip install -r requirements.txt && deactivate

flake8:
	. venv/bin/activate && flake8 --exclude=venv,settings.py . && deactivate

curl:
	curl -d '{"text":"$(text)", "token": "$(token)"}' -H "Content-Type: application/json" -X POST $(host)/$(endpoint)
