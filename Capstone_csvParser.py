#!/usr/bin/python3

# -------------------------------------------------------------------------------------------
# Define:
#     This program parses a csv file of a tweet database based on the column names.
#     Then it appends all the tweet text to a list.
# -------------------------------------------------------------------------------------------

import sys
import csv

allTweets = []

def readFile(fn):
    f = open(fn,"r")
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        tweetID = row["tweetid"]    # may need to change this based on column name
        tweetTxt = row["tweet_text"] # may need to change this based on column name
        allTweets.append(tweetTxt)

def main():
    if (len(sys.argv) != 2):
        print(f"USAGE: {sys.argv[0]} csv_filename")
        exit(1)

    filename = sys.argv[1]
    readFile(filename)
    print(allTweets)

main()
