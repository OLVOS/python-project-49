

#Hexlet сказал:
#
install:
	poetry install

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

#
test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml

lint:
	poetry run flake8 brain_games

selfcheck:
	poetry check

check: selfcheck test lint

#
.PHONY: install test lint selfcheck check build

#my make:
#
brain-games:
	poetry run brain-games
