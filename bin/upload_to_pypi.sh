#!/bin/bash

pandoc -f markdown -t plain --wrap=none README.md -o README.txt
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
