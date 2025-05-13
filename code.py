import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob
import random
from tkinter import font

# Predefined songs by mood and language
SONGS = {
    'happy': {
        'en': [
            'Happy - Pharrell Williams',
            'Uptown Funk - Mark Ronson ft. Bruno Mars',
            'Can’t Stop The Feeling - Justin Timberlake',
            'Best Day Of My Life - American Authors',
            'Walking On Sunshine - Katrina & The Waves',
            'I Gotta Feeling - Black Eyed Peas',
            'Good as Hell – Lizzo',
            'Shut Up and Dance – Walk the Moon'
        ],
        'es': [
            'Vivir Mi Vida - Marc Anthony',
            'Bailando - Enrique Iglesias',
            'La Bicicleta - Carlos Vives & Shakira',
            'Echa Pa’lla - Pitbull',
            'Rayando el sol - Maná',
            'Mi Gente - J Balvin',
            'Limón y sal - Julieta Venegas'
        ],
        'fr': [
            'Alors on danse - Stromae',
            'Dernière danse - Indila',
            'Moi Lolita - Alizée',
            'Papaoutai - Stromae',
            'Je veux - Zaz',
            'Formidable - Stromae',
            'Elle me dit - MIKA'
        ],
        'ta': [
            'Surviva - Anirudh',
            'Selfie Pulla - Anirudh',
            'Aaluma Doluma - Anirudh',
            'Sodakku - Anirudh',
            'Vaathi Coming - Anirudh',
            'Why This Kolaveri Di - Dhanush',
            'Petta Paraak - Anirudh',
            'Danga Maari Oodhari - Anirudh',
            'Chill Bro - Anirudh'
        ],
        'hi': [
            'Gallan Goodiyan - Dil Dhadakne Do',
            'London Thumakda - Queen',
            'Kar Gayi Chull - Kapoor & Sons',
            'Cutiepie - Ae Dil Hai Mushkil',
            'Badtameez Dil - Yeh Jawaani Hai Deewani',
            'Bom Diggy Diggy - Sonu Ke Titu Ki Sweety',
            'Nashe Si Chadh Gayi - Befikre',
            'Kala Chashma - Baar Baar Dekho',
            'Tamma Tamma Again - Badrinath Ki Dulhania'
        ],
        'ml': [
            'Jimikki Kammal - Vineeth Sreenivasan',
            'Entammede Jimikki Kammal',
            'Malare - Premam',
            'Thudakkam Maangalyam - Bangalore Days',
            'Njanum Neeyum - Vikramadithyan',
            'Vennilave - Sagar Alias Jacky',
            'Oru Vadakkan Selfie Title Song',
            'Pistah - Neram',
            'Muthuchippi Poloru - Thattathin Marayathu'
        ]
    },
    'sad': {
        'en': [
            'Someone Like You - Adele',
            'Fix You - Coldplay',
            'Let Her Go - Passenger'
        ],
        'es': [
            'Corre - Jesse & Joy',
            'El Sol No Regresa - La Quinta Estación'
        ],
        'fr': [
            'Ne Me Quitte Pas - Jacques Brel',
            'Je suis malade - Serge Lama'
        ],
        'ta': [
            'Ennodu Nee Irundhaal - I',
            'Munbe Vaa - Sillunu Oru Kaadhal'
        ],
        'hi': [
            'Tum Hi Ho - Aashiqui 2',
            'Channa Mereya - Ae Dil Hai Mushkil'
        ],
        'ml': [
            'Mazha Paadum - Poomaram',
            'Nilaavinte Neela Bhasmam - Ennu Ninte Moideen'
        ]
    },

    'angry': {
        'en': [
            'Smells Like Teen Spirit - Nirvana',
            'Killing In The Name - Rage Against The Machine'
        ],
        'es': [
            'La Raza - Kid Frost',
            'Puto - Molotov'
        ],
        'fr': [
            'La Rage - Keny Arkana',
            'Si c’était à refaire - Kery James'
        ],
        'ta': [
            'Kathi Theme - Anirudh',
            'Naan Ready - Vikram'
        ],
        'hi': [
            'Zinda - Bhaag Milkha Bhaag',
            'Apna Time Aayega - Gully Boy'
        ],
        'ml': [
            'Kalippu - Premam',
            'Thaniye - Guppy'
        ]
    },

    'relaxed': {
        'en': [
            'Weightless - Marconi Union',
            'Banana Pancakes - Jack Johnson'
        ],
        'es': [
            'Contigo Aprendí - Armando Manzanero',
            'Amor Eterno - Rocío Dúrcal'
        ],
        'fr': [
            'La Vie en Rose - Édith Piaf',
            'Sous le vent - Garou & Céline Dion'
        ],
        'ta': [
            'Enna Solla Pogirai - Kandukondain Kandukondain',
            'Anbil Avan - Pariyerum Perumal'
        ],
        'hi': [
            'Raabta - Agent Vinod',
            'Khaabon Ke Parinday - ZNMD'
        ],
        'ml': [
            'Aaro Nenjil - Notebook',
            'Manathe Chandanakkeeru - Thattathin Marayathu'
        ]
    },

    'love': {
        'en': [
            'All of Me - John Legend',
            'Perfect - Ed Sheeran'
        ],
        'es': [
            'Te Amo - Franco de Vita',
            'Bailando - Enrique Iglesias'
        ],
        'fr': [
            'Je t’aime - Lara Fabian',
            'Le Temps des Fleurs - Dalida'
        ],
        'ta': [
            'Puthu Maalai - Maan Karate',
            'Suttrum Vizhi - Ghajini'
        ],
        'hi': [
            'Raabta - Agent Vinod',
            'Tum Hi Ho - Aashiqui 2'
        ],
        'ml': [
            'Premam Premam - Premam',
            'Mazhavil Kavadi - Kalyanaraman'
        ]
    },

    'workout': {
        'en': [
            'Eye of the Tiger - Survivor',
            'Stronger - Kanye West'
        ],
        'es': [
            'Danza Kuduro - Don Omar',
            'Bailando - Enrique Iglesias'
        ],
        'fr': [
            'On va tout déchirer - Soprano',
            'La Fuerza - Dance Remix'
        ],
        'ta': [
            'Thalaivaa - Anirudh',
            'Vettaikaran Theme - Vijay'
        ]
    }
}



# Mood detection function
def detect_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.3:
        return 'happy'
    elif polarity < -0.3:
        return 'sad'
    elif -0.3 <= polarity <= 0.3:
        return 'relaxed'

# GUI setup
root = tk.Tk()
root.title("Mood-Based Playlist Recommender")

# Set background color to pastel
root.configure(bg="#f5e0b7")

# Set a custom font (Lobster)
custom_font = font.Font(family="Lobster", size=18)

# Language choice
language_label = tk.Label(root, text="Select Language:", font=custom_font, bg="#f5e0b7", fg="black")
language_label.pack(pady=10)

language_var = tk.StringVar(value='en')  # Default language is English
language_menu = tk.OptionMenu(root, language_var, 'en', 'es', 'fr', 'ta', 'hi', 'ml')
language_menu.config(font=custom_font, width=15, bg="#d1e8e2")
language_menu.pack(pady=10)

# Mood choice
mood_label = tk.Label(root, text="Enter your mood:", font=custom_font, bg="#f5e0b7", fg="black")
mood_label.pack(pady=10)

mood_entry = tk.Entry(root, width=50, font=custom_font)
mood_entry.pack(pady=10)

# Function to generate playlist
def generate_playlist():
    mood_input = mood_entry.get().lower()
    mood = detect_mood(mood_input)

    selected_language = language_var.get()
    songs = SONGS.get(mood, {}).get(selected_language, [])

    if not songs:
        messagebox.showinfo("No Songs Found", "Sorry, no songs found for this mood and language.")
        return

    random.shuffle(songs)
    selected_song = songs[0]  # Recommend one song

    messagebox.showinfo(f"Recommended Song", f"🎶 {selected_song}")

# Generate button
generate_button = tk.Button(root, text="Generate Playlist", command=generate_playlist, font=custom_font, bg="#8ecae6", fg="black")
generate_button.pack(pady=20)

# Run the GUI
root.mainloop()
