#!/bin/bash

./clean.sh

python setup.py build_ext --inplace

python setup.py bdist_wheel
