#!/bin/bash

# Definieren Sie den Pfad
PFAD_DIFFICULT="/home/stefan/Rüdiger/Projects/C++/LeetCode/Easy"
PFAD_LEETCODE="/home/stefan/Rüdiger/Projects/C++/LeetCode"

# Verwenden Sie den Pfad
echo "Der angegebene Pfad ist: $PFAD_DIFFICULT"

# Der Dateiname, nach dem gesucht wird
TASK_JSON="tasks.json"
LAUNCH_JSON="launch.json"

# Durchsuche alle Unterverzeichnisse nach den Dateien
for ordner in "$PFAD_DIFFICULT"/*; do
    # Extrahieren Sie den Namen des letzten Ordners aus dem vollständigen Pfad
    ordnername=$(basename "$ordner")
    
    if [ ! -e "$ordner/$TASK_JSON" ]; then
        scp -r $PFAD_LEETCODE/tasks.json $PFAD_DIFFICULT/$ordnername/
        sed -i "s/Name.cpp/$ordnername.cpp/g" $PFAD_DIFFICULT/$ordnername/tasks.json
        sed -i "s/Name.exe/$ordnername.exe/g" $PFAD_DIFFICULT/$ordnername/tasks.json
    else
        sed -i "s/Name.cpp/$ordnername.cpp/g" $PFAD_DIFFICULT/$ordnername/tasks.json
        sed -i "s/Name.exe/$ordnername.exe/g" $PFAD_DIFFICULT/$ordnername/tasks.json
    fi
    
    if [ ! -e "$ordner/$LAUNCH_JSON" ]; then
        scp -r $PFAD_LEETCODE/lauch.json $PFAD_DIFFICULT/$ordnername/
        sed -i "s/Name.exe/$ordnername.exe/g" $PFAD_DIFFICULT/$ordnername/launch.json
    else
        sed -i "s/Name.exe/$ordnername.exe/g" $PFAD_DIFFICULT/$ordnername/launch.json
    fi
done