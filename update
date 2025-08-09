#!/bin/bash

brew update

while true; do

  read -p "Do you want to proceed? (y/n) " yn

  case $yn in
  [yY])
    echo "Updating..."
    brew upgrade
    break
    ;;
  [nN])
    echo "Skipping..."
    break
    ;;
  *)
    echo "Invalid input. Please enter 'y' or 'n'."
    ;;
  esac

done

echo "==> Updating Mac App Store applications..."
mas outdated

while true; do

  read -p "Do you want to proceed? (y/n) " yn

  case $yn in
  [yY])
    mas upgrade
    break
    ;;
  [nN])
    echo "Skipping..."
    break
    ;;
  *)
    echo "Invalid input. Please enter 'y' or 'n'."
    ;;
  esac

done
