# Chains Invent Insanity
A Markov Chain-based Cards Against Humanity answer card generator.

## Usage:

### Basic Setup:
1. Create a virtualenv: ```virtualenv chains-invent-insanity```
2. Activate the new virtualenv: ```source $path_to_venv/bin/activate``` or with virtualenvwrapper: ```workon chains-invent-insanity```
2. Install Requirements: ```pip install -r requirements.txt```
3. Run the app via the bundled gunicorn WSGI server: ```gunicorn -d -b 0.0.0.0:8000 -w 1 web:app```

### Setup via Docker:
1. Build the docker image: ```docker build -t chainsinventinsanity .```
2. Create and run the container: ```docker run -Pd chainsinventinsanity --name chainsinventinsanity```

