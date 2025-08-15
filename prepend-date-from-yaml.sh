#!/bin/bash

# Loop through all markdown files in the current directory
for file in *.md; do
  # Skip if not a regular file
  [ -f "$file" ] || continue

  # Extract the date from YAML frontmatter
  date=$(grep -m 1 '^date:' "$file" | sed -E 's/^date:[[:space:]]*"?([0-9]{4}-[0-9]{2}-[0-9]{2})"?/\1/')

  # Skip if no date found
  [ -n "$date" ] || continue

  # New filename with date prepended
  newfile="${date} ${file}"

  # Only rename if the date is not already in the filename
  if [[ "$file" != "$date "* ]]; then
    mv "$file" "$newfile"
    echo "Renamed: $file → $newfile"
  else
    echo "Skipped (already has date): $file"
  fi
done
