# Chains Invent Insanity
A Markov Chain-based [Cards Against Humanity](https://cardsagainsthumanity.com) answer card generator.

## Usage:

### Basic Standalone Setup:
*All app files can be found within the ```./app``` directory.*

1. Create a virtualenv: ```virtualenv chains-invent-insanity```
2. Activate the new virtualenv: ```source $path_to_venv/bin/activate``` or with virtualenvwrapper: ```workon chains-invent-insanity```
3. Install Requirements: ```pip install -r requirements.txt```
4. Create .env file in ```./app``` directory based on the ```env.example``` file in the same directory. 
5. Run the app via the bundled gunicorn WSGI server: ```gunicorn -D -b 0.0.0.0:8000 -w 1 web:app```

### Setup via Docker Compose:
1. Create ```.env``` file in ```./app``` directory based on the ```env.example``` file in the same directory.
2. Build microservices: ```docker-compose build```
3. Bring up cluster: ```docker-compose up -d```

***NOTES:*** 
- URIs in the ```.env``` file **MUST NOT** contain quotes, as these will be parsed literally as part of the URI.
- If you decide to store the wordlists for the cards remotely on Amazon S3, ensure that the ```Content-Type``` metadata 
 (found under the *Properties* for the file in the AWS Web Console) for the file is set to ```text/plain; charset=utf-8```, otherwise special characters in the cards may not
render correctly.
