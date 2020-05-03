#!/bin/bash
while inotifywait -q -e ATTRIB $1;do
		python3 $1;
done
