"""
Adversarial and Edge Case User Profiles

These profiles are designed to test the limits and expose potential weaknesses
in the recommendation system. They represent unusual, conflicting, or extreme
preferences that might produce unexpected results.
"""

# ============================================================================
# Edge Case 1: Conflicting Energy-Mood Combination
# ============================================================================

CONFLICTING_ENERGY_MOOD = {
    "genre": "lofi",
    "mood": "melancholic",  # Sad/low mood
    "energy": 0.95,  # But wants HIGH energy?!
    "likes_acoustic": True
}
# Expected issue: This combination doesn't exist naturally
# Most melancholic songs have low energy
# Will the system recommend high-energy songs (ignoring mood) or 
# melancholic songs (ignoring energy)?


# ============================================================================
# Edge Case 2: Genre That Doesn't Exist
# ============================================================================

NONEXISTENT_GENRE = {
    "genre": "death metal",  # Not in our dataset
    "mood": "aggressive",
    "energy": 1.0,
    "likes_acoustic": False
}
# Expected issue: No genre match means -3 points for all songs
# System falls back to mood and energy only
# Might recommend rock/metal but will never get full score


# ============================================================================
# Edge Case 3: Empty/Minimal Profile
# ============================================================================

MINIMAL_PROFILE = {}
# Expected issue: With no preferences, all songs score equally based only on valence
# System has no way to differentiate user taste
# Should expose default valence assumption (0.65)


# ============================================================================
# Edge Case 4: Extreme Acoustic + Electronic Genre
# ============================================================================

ACOUSTIC_ELECTRONIC_CONFLICT = {
    "genre": "edm",  # Electronic Dance Music
    "mood": "energetic",
    "energy": 0.90,
    "likes_acoustic": True  # But wants acoustic?!
}
# Expected issue: EDM is inherently electronic (low acousticness)
# System will match genre/mood/energy but fail on acoustic preference
# Will it prioritize genre or acoustic style?


# ============================================================================
# Edge Case 5: Impossible Low Energy + Intense Mood
# ============================================================================

LOW_ENERGY_INTENSE = {
    "genre": "rock",
    "mood": "intense",  # Typically high energy
    "energy": 0.15,  # But wants very low energy?!
    "likes_acoustic": True
}
# Expected issue: Intense rock is never low energy
# System must choose: match genre+mood or match energy?


# ============================================================================
# Edge Case 6: Perfect Energy Match, Wrong Everything Else
# ============================================================================

ENERGY_ONLY_MATCH = {
    "genre": "kpop",  # Doesn't exist in dataset
    "mood": "dramatic",  # Doesn't exist in dataset
    "energy": 0.40,  # Matches lofi songs perfectly
    "likes_acoustic": False  # But lofi is typically acoustic
}
# Expected issue: Tests if energy similarity can compensate for 
# complete genre/mood mismatch


# ============================================================================
# Edge Case 7: Extreme Valence Manipulation
# ============================================================================

EXTREMELY_SAD = {
    "genre": "classical",
    "mood": "peaceful",
    "energy": 0.25,
    "likes_acoustic": True,
    "valence": 0.05  # EXTREMELY low happiness/positivity
}
# Expected issue: Tests if extreme valence preference overrides 
# good genre/mood/energy matches
# Most songs have valence 0.4-0.8, so all will score low on valence


# ============================================================================
# Edge Case 8: Maximum Score Fishing
# ============================================================================

SCORE_MAXIMIZER = {
    "genre": "pop",
    "mood": "happy",
    "energy": 0.82,  # Exactly matches "Sunrise City"
    "likes_acoustic": False,
    "valence": 0.84  # Exactly matches "Sunrise City"
}
# Expected result: Should get near-perfect score (9.0) for one song
# Tests if system rewards "gaming" the algorithm


# ============================================================================
# Edge Case 9: No Genre or Mood Specified
# ============================================================================

NO_CATEGORICAL = {
    "energy": 0.50,
    "likes_acoustic": True
}
# Expected issue: Loses -5 points (no genre/mood match possible)
# All songs compete only on energy + acoustic + valence
# Could expose bias toward songs with specific energy levels


# ============================================================================
# Edge Case 10: Everything Contradicts
# ============================================================================

TOTAL_CONTRADICTION = {
    "genre": "country",
    "mood": "nostalgic",
    "energy": 0.05,  # Country in dataset has 0.55 energy
    "likes_acoustic": False,  # Country is typically acoustic
    "valence": 0.95  # Very happy, but nostalgic is typically moderate
}
# Expected issue: Every preference conflicts with natural properties
# System will struggle to find ANY good match


# ============================================================================
# Collection for Testing
# ============================================================================

ADVERSARIAL_PROFILES = {
    "Conflicting Energy-Mood": CONFLICTING_ENERGY_MOOD,
    "Nonexistent Genre": NONEXISTENT_GENRE,
    "Empty Profile": MINIMAL_PROFILE,
    "Acoustic EDM Paradox": ACOUSTIC_ELECTRONIC_CONFLICT,
    "Low Energy Intense": LOW_ENERGY_INTENSE,
    "Energy-Only Match": ENERGY_ONLY_MATCH,
    "Extremely Sad": EXTREMELY_SAD,
    "Score Maximizer": SCORE_MAXIMIZER,
    "No Categorical Prefs": NO_CATEGORICAL,
    "Total Contradiction": TOTAL_CONTRADICTION,
}


# ============================================================================
# Analysis Questions for Each Profile
# ============================================================================

EXPECTED_ISSUES = """
When testing these profiles, ask yourself:

1. **Conflicting Energy-Mood**: Does the system pick high-energy OR melancholic songs?
   Which feature wins? Is the result musically sensible?

2. **Nonexistent Genre**: What does the system fall back to? Do all songs score similarly low?

3. **Empty Profile**: Are all songs ranked purely by valence? Does this expose a bias?

4. **Acoustic EDM Paradox**: Does genre override acoustic preference? Should it?

5. **Low Energy Intense**: Is there ANY song that fits? What compromise does the system make?

6. **Energy-Only Match**: Can energy alone create a "good" recommendation despite wrong genre/mood?

7. **Extremely Sad**: Do all songs get penalized equally? Does this make sense?

8. **Score Maximizer**: Can users "game" the system by learning exact song attributes?

9. **No Categorical Prefs**: Does the system have a built-in preference for certain genres?

10. **Total Contradiction**: What gets recommended when NOTHING fits? Is it random?

💡 **Key Insight**: These edge cases reveal your algorithm's priorities and biases.
Real-world users may have strange taste—your system needs to handle it gracefully!
"""


if __name__ == "__main__":
    print("="*70)
    print("ADVERSARIAL USER PROFILES FOR TESTING")
    print("="*70)
    print(EXPECTED_ISSUES)
    
    print("\n" + "="*70)
    print("AVAILABLE TEST PROFILES:")
    print("="*70)
    for name, profile in ADVERSARIAL_PROFILES.items():
        print(f"\n{name}:")
        for key, value in profile.items():
            print(f"  {key}: {value}")
