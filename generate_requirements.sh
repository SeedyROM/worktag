#!/bin/bash

pipenv lock -r > requirements.txt
pipenv lock -r --dev > dev_requirements.txt 