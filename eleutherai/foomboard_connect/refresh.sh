#!/bin/sh

notebookurl=https://raw.githubusercontent.com/kevinwatkins/deep-learning-sandbox/master/eleutherai/EleutherAI_training_overview.ipynb
notebook=in.ipynb
outdir=/out
scriptdir="$(pwd)"

set -e -x

cd "$outdir"
python "$scriptdir"/fetch_notebook.py "$notebookurl" "$notebook"
jupyter nbconvert --no-input --to notebook --output out --ExecutePreprocessor.timeout=240 --execute "$notebook"
python "$scriptdir"/extract_images.py "$scriptdir" .
