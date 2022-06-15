#!/bin/bash
while IFS="" read -r p || [ -n "$p" ]
do
  printf '%s\n' "$p" | jq -r '.body' | sentiment
done <&0
