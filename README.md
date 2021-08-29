Basic script for handling data associated with a list of cards

The `card_list.txt` file should be populated with the cards you'd like to process, or `card_file` should be changed to some other file.

Running the code:
```sh
python main.py card_list.txt
```

By default the code lists out the card names and converted mana cost separated by a tab character. This is so you can open it with excel. You can either copy the output directly from the command line or pipe it out to a file.
```sh
python main.py card_list.txt > data.tsv
``` 