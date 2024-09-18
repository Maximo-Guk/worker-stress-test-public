#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage $0 <number_of_commits>"
    exit 1
fi

NUM_COMMITS=$1

create_and_push_commit() {
    local index=$1
    git commit --allow-empty -m "Blank Commit $i"
    git push origin $(git rev-parse --abbrev-ref HEAD)
    echo "Pushed commit $i"
}

for ((i = 1; i <= NUM_COMMITS; i++))
do
    create_and_push_commit $i
done