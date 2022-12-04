from flask import Flask, render_template
import random
import os
from PIL import Image


#Add a lot of text within the function, import py file use send from directory
#Add buttons
#Redirect to pokemon pictures
#Use random to get a random pokemon picture and output it

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')
    

def chosen_pokemon():
    region_names = ['Kanto', 'Johto', 'Hoenn', 'Sinnoh']

    pick_the_region = random.choice(region_names)

    if pick_the_region == 'Kanto':
        pokemon_entry = random.randint(1, 151)
    elif pick_the_region == 'Johto':
        pokemon_entry = random.randint(152, 251)
    elif pick_the_region == 'Hoenn':
        pokemon_entry = random.randint(252, 386)
    elif pick_the_region == 'Sinnoh':
        pokemon_entry = random.randint(387, 493)
    else:
        print("An error has occurred. Run the program again")
        
    str_pokemon_entry = str(pokemon_entry)
        
    if pokemon_entry <= 9:
        str_pokemon_entry = "00" + str_pokemon_entry
    elif pokemon_entry >= 10 and pokemon_entry <= 99:
        str_pokemon_entry = "0" + str_pokemon_entry

    path = r".\static\Pokemon_Images\{}\{}.png".format(pick_the_region, str_pokemon_entry)
    img = Image.open(path)
    img.show()


if __name__== '__main__':
    app.run()
    
