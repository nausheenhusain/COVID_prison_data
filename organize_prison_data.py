## This scraper gets Marshall Project prison COVID data from here: https://github.com/themarshallproject/COVID_prison_data
## and creates a new spreadsheet with just Illinois data.

import csv
import os

def get_new_data():
	print('getting new data from github')
	bashCommand = "git pull origin master"
	os.system(bashCommand)

def get_illinois_data():

	get_new_data()

	IL_data = []

	with open('data/covid_prison_cases.csv', newline='') as C:
		reader = list(csv.reader(C, delimiter=','))
		print('Finding Illinois data:')
		for row in reader:
			if row[0] == "name" or row[0] == "Illinois" or row[1] == "IL":
				print(row)
				IL_data.append(row)

	with open('IL_prison_data.csv', 'w', newline='') as D:
		writer = csv.writer(D)
		writer.writerows(IL_data)

get_illinois_data()