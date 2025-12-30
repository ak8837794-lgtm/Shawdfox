import pandas as pd

# Define weights for performance metrics
WEIGHTS = {
    "Clean Pick": 1,
    "Good Throw": 2,
    "Catch": 5,
    "Drop Catch": -3,
    "Stumping": 4,
    "Run Out": 6,
    "Missed Run Out": -2,
    "Direct Hit": 3
}

# Sample data (replace or load from CSV)
data = [
    {"Match No.": 101, "Innings": "1st", "Team": "IND", "Player Name": "Ravindra Jadeja", "Ballcount": "3.2", "Overcount": 4, "Position": "Point", "Short Description": "Dived to stop cut shot", "Pick": "Clean Pick", "Throw": "", "Runs": 2, "Venue": "Wankhede"},
    {"Match No.": 101, "Innings": "1st", "Team": "IND", "Player Name": "Ravindra Jadeja", "Ballcount": "5.1", "Overcount": 6, "Position": "Point", "Short Description": "Direct hit at striker's end", "Pick": "Direct Hit", "Throw": "Run Out", "Runs": 0, "Venue": "Wankhede"},
    {"Match No.": 101, "Innings": "1st", "Team": "IND", "Player Name": "Virat Kohli", "Ballcount": "5.4", "Overcount": 6, "Position": "Mid-off", "Short Description": "Misfielded a drive", "Pick": "Fumble", "Throw": "Missed Run Out", "Runs": -1, "Venue": "Wankhede"},
    {"Match No.": 101, "Innings": "1st", "Team": "IND", "Player Name": "Suryakumar Yadav", "Ballcount": "7.1", "Overcount": 8, "Position": "Deep Midwicket", "Short Description": "Quick throw to keeper", "Pick": "Good Throw", "Throw": "Run Out", "Runs": 3, "Venue": "Wankhede"},
    {"Match No.": 101, "Innings": "1st", "Team": "IND", "Player Name": "Suryakumar Yadav", "Ballcount": "9.3", "Overcount": 10, "Position": "Deep Midwicket", "Short Description": "Caught at boundary", "Pick": "Catch", "Throw": "", "Runs": 0, "Venue": "Wankhede"},
]

# Load into DataFrame
df = pd.DataFrame(data)

# Normalize column names
df["Pick"] = df["Pick"].str.strip()
df["Throw"] = df["Throw"].str.strip()

# Initialize summary
summary = {}

# Analyze each player's performance
for player in df["Player Name"].unique():
    player_data = df[df["Player Name"] == player]
    metrics = {
        "CP": (player_data["Pick"] == "Clean Pick").sum(),
        "GT": (player_data["Pick"] == "Good Throw").sum(),
        "C": (player_data["Pick"] == "Catch").sum(),
        "DC": (player_data["Pick"] == "Drop Catch").sum(),
        "ST": (player_data["Throw"] == "Stumping").sum(),
        "RO": (player_data["Throw"] == "Run Out").sum(),
        "MRO": (player_data["Throw"] == "Missed Run Out").sum(),
        "DH": (player_data["Pick"] == "Direct Hit").sum(),
        "RS": player_data["Runs"].sum()
    }

    # Calculate performance score
    PS = (
        metrics["CP"] * WEIGHTS["Clean Pick"] +
        metrics["GT"] * WEIGHTS["Good Throw"] +
        metrics["C"] * WEIGHTS["Catch"] +
        metrics["DC"] * WEIGHTS["Drop Catch"] +
        metrics["ST"] * WEIGHTS["Stumping"] +
        metrics["RO"] * WEIGHTS["Run Out"] +
        metrics["MRO"] * WEIGHTS["Missed Run Out"] +
        metrics["DH"] * WEIGHTS["Direct Hit"] +
        metrics["RS"]
    )

    summary[player] = {**metrics, "PS": PS}

# Display summary
summary_df = pd.DataFrame.from_dict(summary, orient="index")
print("\n🏏 Fielding Performance Summary:\n")
print(summary_df)

# result
🏏 Fielding Performance Summary:

#                     CP  GT  C  DC  ST  RO  MRO  DH  RS  PS
# Ravindra Jadeja      1   0  0   0   0   1    0   1   2  11
# Virat Kohli          0   0  0   0   0   0    1   0  -1  -3
# Suryakumar Yadav     0   1  1   0   0   1    0   0   3  16