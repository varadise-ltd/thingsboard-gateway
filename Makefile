# Variables
IMAGE_NAME := local-gateway
CONTAINER_NAME := varadise-gateway
DOCKER_VOLUME_LOGS := ./thingsboard_gateway/logs:/thingsboard_gateway/logs
DOCKER_VOLUME_EXTENSIONS := ./thingsboard_gateway/extensions:/thingsboard_gateway/extensions
DOCKER_VOLUME_CONFIG := ./thingsboard_gateway/config:/thingsboard_gateway/config

.PHONY: build run stop clean

# Default target
default: build

# Build Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run Docker container
run:
	docker run -d -v $(DOCKER_VOLUME_LOGS) -v $(DOCKER_VOLUME_EXTENSIONS) -v $(DOCKER_VOLUME_CONFIG) --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Stop Docker container
stop:
	docker stop $(CONTAINER_NAME)

# Remove Docker container
clean:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true
