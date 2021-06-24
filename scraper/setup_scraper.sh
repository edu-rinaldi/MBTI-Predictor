#!/bin/bash

# Simple script for creating your personal .env file

function print_usage {
	echo -e "Error, command expect:"
	echo -e "\tsetup_scraper CLIENT_ID CLIENT_SECRET USER_AGENT REDDIT_USERNAME PASSWORD";
}

# few arguments --> print_usage
if [ "$#" -le 4 ] ; then
	print_usage
fi

# if file already exist we can remove it
if [ -f ".env" ]; then
   rm ".env"
fi

touch .env
echo -e "# PRAW Credentials\n" >> .env
echo -e "# Personal use script (14 characters)" >> .env
echo -e "CLIENT_ID=\"$1\"\n" >> .env
echo -e "# Secret key (27 characters)" >> .env
echo -e "CLIENT_SECRET=\"$2\"\n" >> .env
echo -e "# App name" >> .env
echo -e "USER_AGENT=\"$3\"\n" >> .env
echo -e "# Reddit username" >> .env
echo -e "REDDIT_USERNAME=\"$4\"\n" >> .env
echo -e "# Reddit password" >> .env
echo -e "PASSWORD=\"$5\"\n" >> .env
