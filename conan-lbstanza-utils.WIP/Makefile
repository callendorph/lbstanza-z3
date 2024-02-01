
# execute all lines of a target in one shell
.ONESHELL:

.PHONY: all
all: build

.PHONY: build
build:
	export CONAN_HOME=$$PWD/.conan2
	[ ! -e .conan2/profiles/default ] && conan profile detect
	conan create .
	conan list \*

.PHONY: clean
clean:
	rm -rf .conan2 build
