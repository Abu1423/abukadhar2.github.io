import pandas as pd

# Load bike dataset with extra details
data = pd.DataFrame([
    {"Bike": "Royal Enfield Classic 350", "Category": "Cruiser", "Engine": "349cc", "Feature": "Retro styling, great for long rides"},
    {"Bike": "Jawa 42", "Category": "Cruiser", "Engine": "293cc", "Feature": "Modern-retro design, smooth performance"},
    {"Bike": "KTM Duke 390", "Category": "Sports", "Engine": "373cc", "Feature": "Aggressive styling, excellent acceleration"},
    {"Bike": "Yamaha R15", "Category": "Sports", "Engine": "155cc", "Feature": "Aerodynamic design, beginner-friendly racing bike"},
    {"Bike": "TVS Apache RTR 160", "Category": "Sports", "Engine": "159cc", "Feature": "Sporty commuter, sharp handling"},
    {"Bike": "Bajaj Avenger", "Category": "Cruiser", "Engine": "220cc", "Feature": "Laid-back posture, budget-friendly cruiser"},
    {"Bike": "Hero Splendor", "Category": "Commuter", "Engine": "97cc", "Feature": "Fuel-efficient, India’s most popular daily bike"},
    {"Bike": "Honda Shine", "Category": "Commuter", "Engine": "125cc", "Feature": "Reliable, smooth city performance"},
    {"Bike": "Pulsar NS200", "Category": "Sports", "Engine": "199cc", "Feature": "Muscular design, strong mid-range performance"}
])

print("🏍️ Bike Recommendation System")
print("=" * 40)

# User input
favorite = input("Enter your favorite bike: ").strip().lower()

# Find bike
bike_row = data[data["Bike"].str.lower() == favorite]

if bike_row.empty:
    print("❌ Bike not found")

else:
    category = bike_row.iloc[0]["Category"]
    print(f"\n🔥 Because you like {bike_row.iloc[0]['Bike']} ({category})...")
    print("👉 Recommended bikes:\n")

    recommendations = data[
        (data["Category"] == category) &
        (data["Bike"].str.lower() != favorite)
    ]

    if recommendations.empty:
        print("No similar bikes found.")
    else:
        for _, row in recommendations.iterrows():
            print(f"- {row['Bike']} ({row['Engine']}) → {row['Feature']}")
