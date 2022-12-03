from flask import Flask
import random
import os
import homepage


#Add a lot of text within the function, import py file use send from directory
#Add buttons
#Redirect to pokemon pictures
#Use random to get a random pokemon picture and output it

app = Flask(__name__)

@app.route('/')
def homepage():
    os.system('homepage.py')
    

def chosen_pokemon():
    region_names = ['Kanto', 'Johto', 'Hoenn', 'Sinnoh']

    pick_the_region = random.choice(region_names)

    if pick_the_region == 'Kanto':
        pokemon_entry = random.randint(1, 151)
    elif pick_the_region == 'Johto':
        pokemon_entry == random.randint(152, 251)
    elif pick_the_region == 'Hoenn':
        pokemon_entry == random.randint(252, 386)
    elif pick_the_region == 'Sinnoh':
        pokemon_entry == random.randint(387, 493)
    else:
        print("An error has occurred. Run the program again")
    
    str_pokemon_entry = str(pokemon_entry)
    
    if pokemon_entry <= 9:
        str_pokemon_entry = "00" + pokemon_entry
    elif pokemon_entry >= 10 and pokemon_entry <= 99:
        str_pokemon_entry = "0" + pokemon_entry


    retrieve_pokemon_image = os.path("./"+region_names+"/"+pokemon_entry+".png")



    
if __name__== '__main__':
    app.run()