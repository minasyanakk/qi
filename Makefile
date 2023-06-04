REGISTRY := registry.hub.docker.com/minasyanakk
VERSION := $(shell git describe --tags --abbrev=0)-$(shell git rev-parse --short HEAD)
TARGETOS := linux
#linux darwin window
TARGETARCH := amd64
#amd64 arm64
CGO_ENABLED := 0
APP := $(shell basename $(shell git remote get-url origin))



image:
	docker build . -t ${REGISTRY}/${APP}:${VERSION}-${TARGETOS}-${TARGETARCH}
push:
	docker push ${REGISTRY}/${APP}:${VERSION}-${TARGETOS}-${TARGETARCH}
