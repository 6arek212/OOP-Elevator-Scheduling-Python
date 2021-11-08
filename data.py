import json
import csv
import call as Call

def get_building():
    files = []

    with open('./data/Ex1_input/Ex1_Buildings/B1.json', 'r') as f:
        files.append(json.load(f))

    return files


def get_calls():
    rows = []
    obgs = []

    with open('./data/Ex1_input/Ex1_Calls/Calls_a.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)
    return rows


get_calls()
