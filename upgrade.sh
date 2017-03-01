#!/bin/bash
#
# This script will prepare Jumpbox to run after a release upgrade.
#

# If not already root, use "sudo" and prompt for password
if [ "$(whoami)" = "root" ]; then
        # As "root", ask the user to confirm before continuing
        read -n1 -rsp $'Running Jumpbox as root, press any key to continue or ^C to cancel\n'
        PREFIX=""

fi

# Install new Python packages
COMMAND="${PREFIX}pip install -r requirements.txt --upgrade"
echo "Updating required Python packages ($COMMAND)..."
eval $COMMAND

