# Task 4: Recommendation System
# CODSOFT AI Internship

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie dataset
data = {
    'movie': [
        'Avengers',
        'Iron Man',
        'Batman',
        'Superman',
        'Spider Man',
        'Doctor Strange'
    ],
    'genre': [
        'action superhero marvel',
        'action superhero marvel',
        'action superhero dc',
        'action superhero dc',
        'action superhero marvel',
        'action superhero marvel'
    ]
}

df = pd.DataFrame(data)

# Vectorize genres
cv = CountVectorizer()
genre_matrix = cv.fit_transform(df['genre'])

# Cosine similarity
similarity = cosine_similarity(genre_matrix)

def recommend(movie_name):
    if movie_name not in df['movie'].values:
        return "Movie not found in database."

    index = df[df['movie'] == movie_name].index[0]
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = []
    for i in scores[1:4]:
        recommendations.append(df.iloc[i[0]]['movie'])

    return recommendations

# Test
movie = input("Enter movie name: ")
print("Recommended movies:", recommend(movie))
