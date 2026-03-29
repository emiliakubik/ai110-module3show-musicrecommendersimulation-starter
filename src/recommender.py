from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and return as list of dictionaries."""
    print(f"Loading songs from {csv_path}...")
    songs = []
    
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert numeric fields to appropriate types
            song = {
                'id': int(row['id']),
                'title': row['title'],
                'artist': row['artist'],
                'genre': row['genre'],
                'mood': row['mood'],
                'energy': float(row['energy']),
                'tempo_bpm': float(row['tempo_bpm']),
                'valence': float(row['valence']),
                'danceability': float(row['danceability']),
                'acousticness': float(row['acousticness'])
            }
            songs.append(song)
    
    print(f"Loaded {len(songs)} songs.")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculate similarity score and reasons for a single song based on user preferences."""
    score = 0.0
    reasons = []
    
    # Genre match (+3 points)
    if 'genre' in user_prefs and song['genre'] == user_prefs['genre']:
        score += 3.0
        reasons.append(f"Genre match: {song['genre']}")
    
    # Mood match (+2 points)
    if 'mood' in user_prefs and song['mood'] == user_prefs['mood']:
        score += 2.0
        reasons.append(f"Mood match: {song['mood']}")
    
    # Energy similarity (up to +2 points)
    if 'energy' in user_prefs:
        energy_diff = abs(song['energy'] - user_prefs['energy'])
        energy_score = (1.0 - energy_diff) * 2.0
        energy_score = max(0.0, energy_score)  # Ensure non-negative
        score += energy_score
        reasons.append(f"Energy similarity: {energy_score:.2f}/2.00 (song: {song['energy']:.2f}, target: {user_prefs['energy']:.2f})")
    
    # Acoustic preference (+1 point)
    if 'likes_acoustic' in user_prefs:
        if user_prefs['likes_acoustic'] and song['acousticness'] > 0.7:
            score += 1.0
            reasons.append(f"Acoustic music match (acousticness: {song['acousticness']:.2f})")
        elif not user_prefs['likes_acoustic'] and song['acousticness'] < 0.3:
            score += 1.0
            reasons.append(f"Electronic music match (acousticness: {song['acousticness']:.2f})")
    
    # Valence bonus (up to +1 point) - assumes users prefer moderate-to-happy songs
    valence_target = user_prefs.get('valence', 0.65)  # Default to moderate happiness
    valence_diff = abs(song['valence'] - valence_target)
    valence_score = (1.0 - valence_diff) * 1.0
    valence_score = max(0.0, valence_score)
    score += valence_score
    reasons.append(f"Valence match: {valence_score:.2f}/1.00 (song: {song['valence']:.2f})")
    
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs, sort by match quality, and return top k recommendations with explanations."""
    # Score all songs using list comprehension
    scored_songs = [
        (song, score, "; ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]
    
    # Sort by score (highest first) and return top k
    return sorted(scored_songs, key=lambda x: x[1], reverse=True)[:k]
