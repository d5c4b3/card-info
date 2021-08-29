import json
import os
import requests
import sys


def get_card_list(filename):
	with open(filename) as file:
		list = []
		# read in each line of the file, making sure to remove newline characters
		for line in file:
			list.append(line.rstrip())
		return list

def get_mtg_card_data():
	# If we haven't downloaded the cards file download it
	if (not os.path.exists('AtomicCards.json')):
		print('Downloading card data...')
		url = 'https://mtgjson.com/api/v5/AtomicCards.json'
		file_object = requests.get(url)
		# Write it out to file so we can reuse it later
		with open('AtomicCards.json', 'wb', encoding='utf8') as json_file:
			json_file.write(file_object.content)

	# Open the cards file and convert it from json to python lists/dicts
	with open('AtomicCards.json', 'r', encoding='utf8') as json_file:
		# File contains a 'meta' and 'data' key, we only care about the 'data' key
		card_data = json.load(json_file)
		if 'data' in card_data:
			return card_data['data']
		else:
			print("Error: json was not in expected format", file=sys.stderr)
			sys.exit(1)


# Make sure the user provided a card list file
if len(sys.argv) != 2:
	print('Card list not provided', file=sys.stderr)
	print('usage: python main.py card_list.txt', file=sys.stderr)
	sys.exit(0)

card_file = sys.argv[1]

# Get the list of cards and the json data
cards = get_card_list(card_file)
card_data = get_mtg_card_data()

# If we can't find a card put it in this list so we can tell the user later
errors = []

for card in cards:
	# Check if card is in the data list
	if card not in card_data:
		errors.append(card)
		continue

	# Print the card out in "Name<tab>cmc" format
	print('{0}\t{1}'.format(card, card_data[card][0]['convertedManaCost']))

# print out the errors if there were any
if (len(errors) > 0):
	# print to sys.stderr so the user can run this command as 
	# python main.py card_list.txt > data.csv
	# and the errors will display to them and not be written to file
	print('\nCould not find these cards:', file=sys.stderr)
	for card in errors:
		print(card, file=sys.stderr)
