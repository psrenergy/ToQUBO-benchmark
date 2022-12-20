PYTHON        := python3
PYTHON-PIP    := pip3
SYSIMAGE      := sysimage
VENV-SCRIPT   := bin/activate
VENV-CMD      := source
SHELL         := /bin/bash
TOQUBO_BRANCH := master

.PHONY: run perf plot

all: install setup run

install: install-toqubo install-venv setup
	
install-toqubo:
	julia --proj -e 'import Pkg; Pkg.add(Pkg.PackageSpec(url="https://github.com/psrenergy/ToQUBO.jl.git", rev="$(TOQUBO_BRANCH)")); Pkg.instantiate()'
	julia --proj ./benchmark/ToQUBO/create_sysimage.jl

install-venv:
	$(PYTHON-PIP) install virtualenv

install-latex:
	sudo apt install texlive texlive-latex-extra cm-super dvipng

install-plot: install-venv install-latex setup-plot

setup: setup-venv

setup-venv: setup-pyqubo-venv setup-pyqubo-040-venv setup-qubovert-venv

setup-pyqubo-venv:
	virtualenv ./benchmark/pyqubo
	$(VENV-CMD) ./benchmark/pyqubo/$(VENV-SCRIPT)
	$(PYTHON-PIP) install -r ./benchmark/pyqubo/requirements.txt

setup-pyqubo-040-venv:
	virtualenv ./benchmark/pyqubo_040
	$(VENV-CMD) ./benchmark/pyqubo_040/$(VENV-SCRIPT)
	$(PYTHON-PIP) install -r ./benchmark/pyqubo_040/requirements.txt

setup-qubovert-venv:
	virtualenv ./benchmark/qubovert
	$(VENV-CMD) ./benchmark/qubovert/$(VENV-SCRIPT)
	$(PYTHON-PIP) install -r ./benchmark/qubovert/requirements.txt

setup-plot-venv:
	virtualenv ./benchmark/plots
	$(VENV-CMD) ./benchmark/plots/$(VENV-SCRIPT)
	$(PYTHON-PIP) install -r ./benchmark/plots/requirements.txt

setup-plot: setup-plot-venv

run: run-pyqubo run-pyqubo-040 run-qubovert run-toqubo

run-toqubo:
	julia --project=. --sysimage ./benchmark/ToQUBO/$(SYSIMAGE) ./benchmark/ToQUBO/tsp.jl --run

run-pyqubo:
	$(VENV-CMD) ./benchmark/pyqubo/$(VENV-SCRIPT)
	$(PYTHON) ./benchmark/pyqubo/tsp.py

run-pyqubo-040:
	$(VENV-CMD) ./benchmark/pyqubo_040/$(VENV-SCRIPT)
	$(PYTHON) ./benchmark/pyqubo_040/tsp.py

run-qubovert:
	$(VENV-CMD) ./benchmark/qubovert/$(VENV-SCRIPT)
	$(PYTHON) ./benchmark/qubovert/tsp.py

plot:
	$(VENV-CMD) ./benchmark/plots/$(VENV-SCRIPT)
	$(PYTHON) ./benchmark/plots/plot.py

perf:
	julia --project=perf --sysimage ./benchmark/ToQUBO/$(SYSIMAGE) ./perf/tsp.jl --run
