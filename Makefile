.PHONY: play

.EXPORT_ALL_VARIABLES:
PIPENV_CLEAR=1
PIPENV_SKIP_LOCK=1
PIPENV_VERBOSITY=-1
PIPENV_VENV_IN_PROJECT=1
PIPENV_PYPI_MIRROR=https://mirrors.cloud.tencent.com/pypi/simple

play: .venv
	pipenv run python pymine.py

.venv:
	sudo pacman -S sdl sdl_image sdl_mixer sdl_ttf portmidi python-pygame
	pipenv install --dev
