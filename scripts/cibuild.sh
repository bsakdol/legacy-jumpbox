#!/bin/bash

# If any checks fail, modify the exit code
EXIT=0

# Print a timestamp
info()
{
	echo "$(date +'%F %T') |"
}

# Track the time it takes to run the script
START=$(date +%s)
echo "$(info) starting build checks."

# Syntax check all python source files
SYNTAX=$(find . -name "*.py" -type f -exec python -m py_compile {} \; 2>&1)
if [[ ! -z $SYNTAX ]]; then
	echo -e "$SYNTAX"
	echo -e "\n$(info) detected one or more syntax errors, failing build."
	EXIT=1
fi

# Check all python source files for PEP 8 compliance, but explicitly
# ignore:
#  - E501: line greater than 80 characters in length
pep8 --ignore=E501 jumpbox/
RC=$?
if [[ $RC != 0 ]]; then
	echo -e "\n$(info) one or more PEP 8 errors detected, failing build."
	EXIT=$RC
fi

# Show time it took to run the script
END=$(date +%s)
echo "$(info) exiting with code $EXIT after $(($END - $START)) seconds."

exit $EXIT 
