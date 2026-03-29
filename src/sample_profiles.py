"""
Sample User Profiles for Testing the Music Recommender

These profiles represent different music taste preferences that you can use
to test your recommendation system. Each profile is provided as both a
dictionary and a UserProfile object.
"""

from recommender import UserProfile

# ============================================================================
# Profile Dictionaries (useful for testing and creating profiles dynamically)
# ============================================================================

STUDY_BUDDY = {
    "favorite_genre": "lofi",
    "favorite_mood": "chill",
    "target_energy": 0.40,
    "likes_acoustic": True
}

GYM_ENTHUSIAST = {
    "favorite_genre": "rock",
    "favorite_mood": "intense",
    "target_energy": 0.90,
    "likes_acoustic": False
}

COFFEE_SHOP_LOVER = {
    "favorite_genre": "jazz",
    "favorite_mood": "relaxed",
    "target_energy": 0.35,
    "likes_acoustic": True
}

PARTY_MODE = {
    "favorite_genre": "edm",
    "favorite_mood": "energetic",
    "target_energy": 0.85,
    "likes_acoustic": False
}

CHILL_EVENING = {
    "favorite_genre": "ambient",
    "favorite_mood": "peaceful",
    "target_energy": 0.25,
    "likes_acoustic": True
}

COUNTRY_FAN = {
    "favorite_genre": "country",
    "favorite_mood": "nostalgic",
    "target_energy": 0.55,
    "likes_acoustic": True
}

HIP_HOP_HEAD = {
    "favorite_genre": "hip hop",
    "favorite_mood": "confident",
    "target_energy": 0.75,
    "likes_acoustic": False
}

# ============================================================================
# UserProfile Objects (ready to use with your Recommender class)
# ============================================================================

def get_study_buddy() -> UserProfile:
    """Returns a profile for someone who needs focus/study music."""
    return UserProfile(**STUDY_BUDDY)

def get_gym_enthusiast() -> UserProfile:
    """Returns a profile for high-intensity workout music."""
    return UserProfile(**GYM_ENTHUSIAST)

def get_coffee_shop_lover() -> UserProfile:
    """Returns a profile for relaxed acoustic background music."""
    return UserProfile(**COFFEE_SHOP_LOVER)

def get_party_mode() -> UserProfile:
    """Returns a profile for upbeat electronic dance music."""
    return UserProfile(**PARTY_MODE)

def get_chill_evening() -> UserProfile:
    """Returns a profile for low-energy peaceful music."""
    return UserProfile(**CHILL_EVENING)

def get_country_fan() -> UserProfile:
    """Returns a profile for nostalgic country music."""
    return UserProfile(**COUNTRY_FAN)

def get_hip_hop_head() -> UserProfile:
    """Returns a profile for confident hip hop music."""
    return UserProfile(**HIP_HOP_HEAD)

# ============================================================================
# Collection of all profiles
# ============================================================================

ALL_PROFILE_DICTS = {
    "Study Buddy": STUDY_BUDDY,
    "Gym Enthusiast": GYM_ENTHUSIAST,
    "Coffee Shop Lover": COFFEE_SHOP_LOVER,
    "Party Mode": PARTY_MODE,
    "Chill Evening": CHILL_EVENING,
    "Country Fan": COUNTRY_FAN,
    "Hip Hop Head": HIP_HOP_HEAD,
}

def get_all_profiles() -> dict[str, UserProfile]:
    """Returns a dictionary of all sample profiles."""
    return {
        "Study Buddy": get_study_buddy(),
        "Gym Enthusiast": get_gym_enthusiast(),
        "Coffee Shop Lover": get_coffee_shop_lover(),
        "Party Mode": get_party_mode(),
        "Chill Evening": get_chill_evening(),
        "Country Fan": get_country_fan(),
        "Hip Hop Head": get_hip_hop_head(),
    }


# ============================================================================
# Usage Examples
# ============================================================================

if __name__ == "__main__":
    # Example 1: Create a profile from dictionary
    user1 = UserProfile(**STUDY_BUDDY)
    print(f"User 1: {user1}")
    
    # Example 2: Use helper function
    user2 = get_gym_enthusiast()
    print(f"User 2: {user2}")
    
    # Example 3: Iterate through all profiles
    print("\nAll Sample Profiles:")
    for name, profile in get_all_profiles().items():
        print(f"  {name}: genre={profile.favorite_genre}, mood={profile.favorite_mood}, energy={profile.target_energy}")
