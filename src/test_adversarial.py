"""
Test Adversarial Profiles

Run this to see how the recommendation system handles edge cases
and adversarial user profiles.
"""

from .recommender import load_songs, recommend_songs
from .adversarial_profiles import ADVERSARIAL_PROFILES


def test_adversarial_profile(name: str, profile: dict, songs: list, k: int = 3) -> None:
    """Test a single adversarial profile and display results."""
    print("\n" + "="*70)
    print(f"🔬 TESTING: {name}")
    print("="*70)
    print(f"\n📋 Profile Details:")
    for key, value in profile.items():
        print(f"   {key}: {value}")
    
    if not profile:
        print("   (Empty profile - no preferences specified)")
    
    # Get recommendations
    recommendations = recommend_songs(profile, songs, k=k)
    
    print(f"\n🎧 Top {k} Recommendations:")
    print("-" * 70)
    
    if not recommendations:
        print("   ❌ No recommendations found!")
        return
    
    for idx, (song, score, explanation) in enumerate(recommendations, 1):
        print(f"\n#{idx}  {song['title']} by {song['artist']}")
        print(f"    💯 Score: {score:.2f}/9.0")
        print(f"    🎸 {song['genre']} | 🎭 {song['mood']} | ⚡ {song['energy']:.2f} | 🎹 {song['acousticness']:.2f}")
        print(f"    Reasons:")
        for reason in explanation.split("; "):
            print(f"      • {reason}")
    
    # Analysis
    print(f"\n💭 Analysis:")
    scores = [score for _, score, _ in recommendations]
    print(f"   Score range: {min(scores):.2f} - {max(scores):.2f}")
    print(f"   Average score: {sum(scores)/len(scores):.2f}")
    
    # Check for issues
    if max(scores) < 3.0:
        print("   ⚠️  LOW SCORES: No songs scored well. System struggling to match preferences.")
    if max(scores) - min(scores) < 0.5:
        print("   ⚠️  SIMILAR SCORES: System can't differentiate well between songs.")
    if max(scores) > 8.5:
        print("   ⚠️  NEAR-PERFECT: User may be 'gaming' the system with exact song values.")


def main():
    """Run all adversarial tests."""
    print("\n" + "="*70)
    print("🎯 ADVERSARIAL PROFILE TESTING")
    print("="*70)
    print("\nTesting edge cases to find weaknesses in the recommendation system...")
    
    songs = load_songs("data/songs.csv")
    
    # Test each adversarial profile
    for name, profile in ADVERSARIAL_PROFILES.items():
        test_adversarial_profile(name, profile, songs, k=3)
        print()
    
    # Summary
    print("\n" + "="*70)
    print("📊 TESTING COMPLETE")
    print("="*70)
    print("""
Key Questions to Consider:
1. Which profiles exposed the biggest weaknesses?
2. Did any profiles produce nonsensical recommendations?
3. How does the system prioritize when preferences conflict?
4. Could a user manipulate the system to get specific songs?
5. What happens when the dataset doesn't contain matching songs?

Next Steps:
- Document these findings in your README.md
- Discuss these limitations in your model_card.md
- Consider how you might improve the system to handle edge cases
    """)


if __name__ == "__main__":
    main()
