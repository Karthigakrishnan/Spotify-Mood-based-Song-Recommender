import tkinter as tk
import random

# Predefined songs by mood and language with consistent emojis
SONGS = {
    'Happy 😄': {
        'English 🍵📚': [
            'Happy - Pharrell Williams',
            'Uptown Funk - Mark Ronson ft. Bruno Mars',
            'Can’t Stop The Feeling - Justin Timberlake',
            'Best Day Of My Life - American Authors'
        ],
        'Spanish 🌮💃': [
            'Vivir Mi Vida - Marc Anthony',
            'Bailando - Enrique Iglesias',
            'La Bicicleta - Carlos Vives & Shakira'
        ],
        'French 🗼🥐': [
            'Alors on danse - Stromae',
            'Dernière danse - Indila',
            'Papaoutai - Stromae'
        ],
        'Tamil 🍚🍛': [
            'Selfie Pulla - Anirudh',
            'Vaathi Coming - Anirudh',
            'Aaluma Doluma - Anirudh'
        ],
        'Hindi 🕌🕉️': [
            'Gallan Goodiyan - Dil Dhadakne Do',
            'London Thumakda - Queen',
            'Badtameez Dil - Yeh Jawaani Hai Deewani'
        ],
        'Malayalam 🌴🌊': [
            'Jimikki Kammal - Vineeth Sreenivasan',
            'Malare - Premam',
            'Thudakkam Maangalyam - Bangalore Days'
        ]
    },

    'Sad 😢': {
        'English 🍵📚': [
            'Someone Like You - Adele',
            'Fix You - Coldplay',
            'Let Her Go - Passenger'
        ],
        'Spanish 🌮💃': [
            'Corre - Jesse & Joy',
            'Te Extraño - Xtreme',
            'Duele el Corazón - Enrique Iglesias'
        ],
        'French 🗼🥐': [
            'Ne Me Quitte Pas - Jacques Brel',
            'Je suis malade - Serge Lama'
        ],
        'Tamil 🍚🍛': [
            'Ennodu Nee Irundhaal - I',
            'Munbe Vaa - Sillunu Oru Kaadhal'
        ],
        'Hindi 🕌🕉️': [
            'Tum Hi Ho - Aashiqui 2',
            'Channa Mereya - Ae Dil Hai Mushkil'
        ],
        'Malayalam 🌴🌊': [
            'Mazha Paadum - Poomaram',
            'Ee Kaattu - Adam Joan'
        ]
    },

    'Angry 😡': {
        'English 🍵📚': [
            'Smells Like Teen Spirit - Nirvana',
            'Killing In The Name - Rage Against The Machine'
        ],
        'Spanish 🌮💃': [
            'La Raza - Kid Frost',
            'Puto - Molotov'
        ],
        'French 🗼🥐': [
            'La Rage - Keny Arkana',
            'Basique - Orelsan'
        ],
        'Tamil 🍚🍛': [
            'Kathi Theme - Anirudh',
            'Kaala Theme - Santhosh Narayanan'
        ],
        'Hindi 🕌🕉️': [
            'Zinda - Bhaag Milkha Bhaag',
            'Apna Time Aayega - Gully Boy'
        ],
        'Malayalam 🌴🌊': [
            'Kalippu - Premam',
            'Thaniye - Guppy'
        ]
    },

    'Relaxed 😌': {
        'English 🍵📚': [
            'Weightless - Marconi Union',
            'Banana Pancakes - Jack Johnson'
        ],
        'Spanish 🌮💃': [
            'Contigo Aprendí - Armando Manzanero'
        ],
        'French 🗼🥐': [
            'La Vie en Rose - Édith Piaf'
        ],
        'Tamil 🍚🍛': [
            'Enna Solla Pogirai - Kandukondain Kandukondain'
        ],
        'Hindi 🕌🕉️': [
            'Raabta - Agent Vinod'
        ],
        'Malayalam 🌴🌊': [
            'Aaro Nenjil - Notebook'
        ]
    },

    'Love ❤️': {
        'English 🍵📚': [
            'Perfect - Ed Sheeran',
            'All of Me - John Legend',
            'Thinking Out Loud - Ed Sheeran'
        ],
        'Spanish 🌮💃': [
            'Besame Mucho - Consuelo Velázquez',
            'Te Amo - Franco de Vita'
        ],
        'French 🗼🥐': [
            'Je t’aime - Lara Fabian',
            'Parle-moi - Isabelle Boulay'
        ],
        'Tamil 🍚🍛': [
            'Munbe Vaa - Sillunu Oru Kaadhal',
            'Enna Solla - Thangamagan'
        ],
        'Hindi 🕌🕉️': [
            'Pee Loon - Once Upon a Time in Mumbaai',
            'Tera Ban Jaunga - Kabir Singh'
        ],
        'Malayalam 🌴🌊': [
            'Malare - Premam',
            'Kanneer Poovinte - Kireedam'
        ]
    },

    'Workout 💪': {
        'English 🍵📚': [
            'Eye of the Tiger - Survivor',
            'Stronger - Kanye West'
        ],
        'Spanish 🌮💃': [
            'Danza Kuduro - Don Omar'
        ],
        'French 🗼🥐': [
            'Bella - Maître Gims'
        ],
        'Tamil 🍚🍛': [
            'Surviva - Vivegam',
            'Vaathi Coming - Master'
        ],
        'Hindi 🕌🕉️': [
            'Sultan Title Track - Sultan'
        ],
        'Malayalam 🌴🌊': [
            'Theerame - Malik'
        ]
    }
}

# GUI setup
root = tk.Tk()
root.title("🎵 Mood-Based Playlist Recommender")
root.geometry('520x520')
root.config(bg="#e0f7fa")

# Font styling
font_style = ("Arial", 14, "bold")

# Language selection
language_label = tk.Label(root, text="🌍 Select Language:", font=font_style, bg="#e0f7fa")
language_label.pack(pady=10)

language_var = tk.StringVar(value="🌐 Choose Language")
languages = ['English 🍵📚', 'Spanish 🌮💃', 'French 🗼🥐', 'Tamil 🍚🍛', 'Hindi 🕌🕉️', 'Malayalam 🌴🌊']
language_menu = tk.OptionMenu(root, language_var, *languages)
language_menu.pack(pady=10)

# Mood selection
mood_label = tk.Label(root, text="🧠 Select Mood:", font=font_style, bg="#e0f7fa")
mood_label.pack(pady=10)

mood_var = tk.StringVar(value="Happy 😄")
moods = ['Happy 😄', 'Sad 😢', 'Angry 😡', 'Relaxed 😌', 'Love ❤️', 'Workout 💪']
mood_menu = tk.OptionMenu(root, mood_var, *moods)
mood_menu.pack(pady=10)

# Recommendation logic
def recommend_song():
    mood = mood_var.get()
    language = language_var.get()
    try:
        recommended_song = random.choice(SONGS[mood][language])
        song_label.config(text=f"🎧 Recommended Song:\n{recommended_song}")
    except KeyError:
        song_label.config(text="⚠️ No songs found for this combination. Try a different one.")

# Button to get a recommendation
recommend_button = tk.Button(root, text="🎶 Get Song Recommendation", command=recommend_song,
                             font=font_style, bg="#4CAF50", fg="white")
recommend_button.pack(pady=20)

# Display label
song_label = tk.Label(root, text="🎧 Recommended Song: ", font=font_style, bg="#e0f7fa", wraplength=400)
song_label.pack(pady=20)

root.mainloop()
