"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    # Display user preferences
    print("\n" + "="*70)
    print("🎵  MUSIC RECOMMENDER SYSTEM")
    print("="*70)
    print("\n📋 Your Taste Profile:")
    print(f"   Genre: {user_prefs.get('genre', 'Any')}")
    print(f"   Mood: {user_prefs.get('mood', 'Any')}")
    print(f"   Energy Level: {user_prefs.get('energy', 'N/A')}")
    if 'likes_acoustic' in user_prefs:
        acoustic_pref = "Acoustic" if user_prefs['likes_acoustic'] else "Electronic"
        print(f"   Style: {acoustic_pref}")
    
    print("\n" + "="*70)
    print(f"🎧  TOP {len(recommendations)} RECOMMENDATIONS")
    print("="*70 + "\n")
    
    # Display each recommendation with clean formatting
    for idx, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        
        # Header for each song
        print(f"#{idx}  {song['title']}")
        print(f"    by {song['artist']}")
        print(f"    💯 Score: {score:.2f}/9.0")
        print(f"    🎸 Genre: {song['genre']} | 🎭 Mood: {song['mood']} | ⚡ Energy: {song['energy']:.2f}")
        
        # Split explanation into individual reasons
        reasons = explanation.split("; ")
        print(f"    ✨ Why this matches:")
        for reason in reasons:
            print(f"       • {reason}")
        
        print()  # Blank line between songs
    
    print("="*70)


if __name__ == "__main__":
    main()
