#!/bin/bash
IFS=$'\n'

old=$(ps -eo command)
while true; do
  new=$(ps -eo command)
  diff <( echo "$old" ) <( echo "$new" )
  sleep 1
  old=$new
done
