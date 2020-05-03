#!/bin/bash
while inotifywait -q -e attrib $1;do
		clear;
		python3 $1;
done
