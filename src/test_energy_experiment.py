"""
Test script to compare recommendations with energy-focused profiles
Shows how the weight adjustment (genre 3→1.5, energy 2→4) affects results
"""

from src.recommender import load_songs, recommend_songs

def display_recommendations(profile_name, profile_dict, songs, top_n=5):
    """Display recommendations in a simple format"""
    print(f"\n{'='*70}")
    print(f"Profile: {profile_name}")
    print(f"  Genre: {profile_dict.get('genre', 'Any')}, Mood: {profile_dict.get('mood', 'Any')}, Energy: {profile_dict.get('energy', 'N/A')}")
    print(f"{'='*70}")
    
    recommendations = recommend_songs(profile_dict, songs, top_n)
    
    for i, (song, score, reasons) in enumerate(recommendations, 1):
        print(f"\n#{i} {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f} | Genre: {song['genre']} | Mood: {song['mood']} | Energy: {song['energy']:.2f}")
        print(f"   Reasons: {reasons}")  # reasons is already a joined string

if __name__ == "__main__":
    songs = load_songs('data/songs.csv')
    print(f"Loaded {len(songs)} songs")
    print("="*70)
    print("TESTING ENERGY-DOMINANT WEIGHTING (Genre: 1.5, Energy: 4.0)")
    print("="*70)
    
    # Test 1: Low energy (study/relax)
    low_energy_profile = {
        'genre': 'lofi',
        'mood': 'chill',
        'energy': 0.3,  # Low energy - should now be heavily weighted
    }
    display_recommendations("Low Energy Study Session", low_energy_profile, songs)
    
    # Test 2: High energy (workout/party)
    high_energy_profile = {
        'genre': 'edm',
        'mood': 'energetic',
        'energy': 0.9,  # High energy - should now be heavily weighted
    }
    display_recommendations("High Energy Workout", high_energy_profile, songs)
    
    # Test 3: Genre mismatch but energy match (real test of weight impact)
    energy_over_genre = {
        'genre': 'classical',  # Ask for classical
        'energy': 0.9,  # But want high energy (most classical is low energy)
    }
    display_recommendations("Classical Lover with High Energy Need", energy_over_genre, songs)
    
    # Test 4: No genre preference, pure energy sorting
    pure_energy_low = {
        'energy': 0.2,  # Very low energy
    }
    display_recommendations("Pure Energy Match (Low)", pure_energy_low, songs)
