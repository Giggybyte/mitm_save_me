#!/bin/bash

for FILE in *; do
    TYPE=$(file -b $FILE)
    if [ "$TYPE" == "MPEG transport stream data" ]; then
        echo "file '${FILE}'" >> list.txt
    fi
done
