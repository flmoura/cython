#!/bin/bash

rm -rf *.c
rm -rf *.egg-info
rm -rf *.so
rm -rf build/
rm -rf dist/
rm -rf mypkg/*.c
rm -rf mypkg/*.so

rm -rf mypkg/__pycache__/
rm -rf mypkg/module1/__pycache__/
rm -rf mypkg/module2/__pycache__/
rm -rf mypkg/module3/__pycache__/

rm -rf mypkg/module1/*.c
rm -rf mypkg/module2/*.c
rm -rf mypkg/module3/*.c

rm -rf mypkg/module1/*.so
rm -rf mypkg/module2/*.so
rm -rf mypkg/module3/*.so