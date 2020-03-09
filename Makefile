.PHONY: usage, start, stop, build, start-build

OK_COLOR=\033[32;01m
NO_COLOR=\033[0m
ERROR_COLOR=\033[31;01m

DOCKER_COMPOSE := docker-compose


## usage: show available actions
usage: Makefile
	@echo "to use make call:"
	@echo "make <action>"
	@echo ""
	@echo "list of available actions:"
	@sed -n 's/^##//p' $< | column -t -s ':' | sed -e 's/^/ /'

## start: start compose
start:
	@echo "$(OK_COLOR)==> Starting docker compose...$(NO_COLOR)"
	$(DOCKER_COMPOSE) up

## stop: stop composer
stop:
	@echo "$(OK_COLOR)==> Stopping docker compose...$(NO_COLOR)"
	$(DOCKER_COMPOSE) down --remove-orphan -t 10

## build: build dockerfile
build:
	@echo "$(OK_COLOR)==> Build Dockerfile...$(NO_COLOR)"
	$(DOCKER_COMPOSE) build --no-cache

##start-build: docker-compose up --build
start-build:
	@echo "$(OK_COLOR)==> Starting docker compose up build...$(NO_COLOR)"
	$(DOCKER_COMPOSE) up --build
