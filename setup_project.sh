#!/bin/bash

echo "========================================="
echo "Creating Adaptive RL Project Structure..."
echo "========================================="

# ==========================
# Top-Level Directories
# ==========================
mkdir -p \
datasets/{raw,processed,external} \
notebooks \
configs \
outputs/{figures,metrics,predictions,reports} \
logs \
checkpoints/{isolation_forest,lof,ocsvm,autoencoder,rl} \
tests \
docs \
src/{config,preprocessing,feature_engineering,models,ensemble,rl,evaluation,visualization,utils,pipelines}

# ==========================
# Python Packages
# ==========================
touch \
src/__init__.py \
src/config/__init__.py \
src/preprocessing/__init__.py \
src/feature_engineering/__init__.py \
src/models/__init__.py \
src/ensemble/__init__.py \
src/rl/__init__.py \
src/evaluation/__init__.py \
src/visualization/__init__.py \
src/utils/__init__.py \
src/pipelines/__init__.py

# ==========================
# Root Files
# ==========================
touch README.md
touch requirements.txt
touch .gitignore

echo ""
echo "Project structure created successfully!"
echo ""

if command -v tree >/dev/null 2>&1; then
    tree -L 2
else
    echo "Install 'tree' to view the structure:"
    echo "sudo apt install tree"
fi
