import media
import fresh_tomatoes

# List of some of my favourite movies to be generated on the Fresh Tomatoes webpage
movies = [
  media.Movie(
    'Inception',
    'Cobb steals information from his targets by entering their dreams. He is wanted for his \
     alleged role in his wifes murder and his only chance at redemption is to perform the \
     impossible, an inception.',
    'https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg',
    'https://www.youtube.com/watch?v=8hP9D6kZseM'
    ),
  media.Movie(
    'The Shawshank Redemption',
    'Andy Dufresne, a successful banker, is arrested for the murders of his wife and \
     her lover, and is sentenced to life imprisonment at the Shawshank prison. He \
     becomes the most unconventional prisoner.',
    'https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg',
    'https://www.youtube.com/watch?v=6hB3S9bIaco'
    ),
  media.Movie(
    'Batman v Superman',
    'Fearing the actions of Superman are left unchecked, Batman takes on \
    Superman, while the world wrestles with what kind of a hero it really needs.',
    'https://upload.wikimedia.org/wikipedia/en/2/20/Batman_v_Superman_poster.jpg',
    'https://www.youtube.com/watch?v=Cle_rKBpZ28'
    ),
  media.Movie(
    'Kung Fu Panda',
    'Po finds himself selected as the Dragon Warrior. The Furious Five, residing \
     in the barracks, and he take on the responsibility to battle against the inimical \
     forces in the Valley of Peace.',
    'https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg',
    'https://www.youtube.com/watch?v=PXi3Mv6KMzY'
    ),
  media.Movie(
    'The Internship',
    'Salesmen Billy and Nick find themselves unemployed in the digital world. In a bid \
     to prove their competence, they try to bag an internship at Google, where \
     they must beat some tech-savvy geniuses.',
    'https://upload.wikimedia.org/wikipedia/en/e/ed/The-internship-poster.jpg',
    'https://www.youtube.com/watch?v=cdnoqCViqUo'
    ),
  media.Movie(
    'Fight Club',
    'An ordinary employee is tired of his drudged existence. His life \
     changes when he meets Tyler, a soap salesman, and the two develop \
     a unique bond after they decide to fight each other.',
    'https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg',
    'https://www.youtube.com/watch?v=SUXWAEX2jlg'
    )
  ]

fresh_tomatoes.open_movies_page(movies)
