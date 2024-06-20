#!/usr/bin/env bash

export GIT_REPO_DIR=${PWD}
echo "Set git email and name"
git config user.email "kk.gmail.com"
git config user.name "coco"
git config advice.addIgnoredFile false
echo "Checkout pages"
git checkout gh-pages
echo "Remove devel"
rm -rf devel
echo "Make a new devel"
mkdir devel
echo "Checking for tag"
if [[ -n "${GIT_TAG}" ]]; then
  echo "Tag ${GIT_TAG} is defined"
  echo "Copy docs to root"
  echo cp -r ${PWD}/docs/_build/html/* ${PWD}/
  cp -r ${PWD}/docs/_build/html/* ${PWD}
else
  echo "Tag is ${GIT_TAG}. Not updating main documents"
fi
echo "Copy docs to devel"
echo cp -r ${PWD}/docs/_build/html/* ${PWD}/devel/
cp -r ${PWD}/docs/_build/html/* ${PWD}/devel/
echo "Clean up docs"
cd ${GIT_REPO_DIR}/docs
make clean && git clean -xfd
echo "Add files"
cd ${GIT_REPO_DIR}
git add .
git add --all .
git add -u .
# Ensure key files are added
git add devel/**/* || true
git add **/*.html || true
git add **/*.ipynb || true
git add **/*.txt || true
git add _images/* || true
git add _sources/**/* || true
git add _modules/**/* || true
git add _static/**/* || true
echo "Github Actions docs build after commit ${GITHUB_SHA::8}"
git commit -a -m "Github Actions docs build after commit ${GITHUB_SHA::8}"