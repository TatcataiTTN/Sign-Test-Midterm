#!/bin/bash
xelatex -interaction=nonstopmode main_NO_IMAGES && xelatex -interaction=nonstopmode main_NO_IMAGES && open main_NO_IMAGES.pdf
