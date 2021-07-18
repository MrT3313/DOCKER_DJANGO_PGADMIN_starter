###################
##-- VARIABLES --##
###################
WORKDIR :=$(CURDIR)

########
# TEST #
########
.PHONY: test
test:
	@echo $(WORKDIR)
	@echo THIS IS A TEST....

########################
# MAIN DOCKER COMMANDS #
########################

.PHONY: docker-dev
docker-dev:
	@echo $(WORKDIR)
	docker-compose -f docker-compose.dev.yml up --build

.PHONY: build-image
build-image:
	@echo $(WORKDIR)
	docker-compose build

.PHONY: decompose-dev
decompose-dev:
	@echo $(WORKDIR)
	docker-compose -f docker-compose.dev.yml down

###############################
# DOCKER TERMINAL INTERACTION #
###############################
.PHONY: pgTerminal, djTerminal

pgTerminal:
	@echo $(WORKDIR)
	docker exec -it pg_container bash

djTerminal:
	@echo $(WORKDIR)
	docker exec -it dj_container bash