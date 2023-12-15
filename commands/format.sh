#!bin/bash
echo "Formatting python files ..."
black . --check
black .
echo "Done :)"