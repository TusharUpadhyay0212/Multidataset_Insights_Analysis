import pandas as pd
import matplotlib.pyplot as plt
import textwrap

df = pd.read_csv("C:\\Users\\TUSHAR UPADHYAY\\Desktop\\Internship\\eng.1.csv")


df[["Home Team Score", "Opponent Team Score"]] = df["FT"].str.split("-", expand=True)


df["Winning Team"] = df.apply(
    lambda row: row["Team 1"]
    if row["Home Team Score"] > row["Opponent Team Score"]
    else row["Team 2"],
    axis=1,
)


df.loc[df["Winning Team"] == df["Team 1"], "Winning Team Score"] = df["Home Team Score"]
df.loc[df["Winning Team"] == df["Team 2"], "Winning Team Score"] = df["Opponent Team Score"]


new_df = df[["Date", "Team 1", "Team 2", "Home Team Score","Winning Team", "Winning Team Score"]]

new_df.columns = ["Date", "Home Team", "Opponent Team", "Home Team Score","Winning Team", "Winning Team Score"]

#new_df.to_csv("output1.csv", index=False)

#Draw Graphs 

plt.style.use('bmh')

df = pd.read_csv("output1.csv")

x = df["Home Team"]
y = df["Home Team Score"]

x_labels = [ '\n'.join(textwrap.wrap(label, 10)) for label in x ]

# Bar Graph

plt.xlabel("Home Team", fontsize=18)
plt.ylabel("Home Team Score", fontsize=16)
plt.bar(x_labels, y)

plt.xticks(rotation=90)
plt.xticks(size=7)

plt.show()

#pie Chart

home_wins = df[df["Winning Team"] == df["Home Team"]]["Winning Team"].count()
opponent_wins = df[df["Winning Team"] == df["Opponent Team"]]["Winning Team"].count()

labels = ["Home Team", "Opponent Team"]
winning_times = [home_wins, opponent_wins]
plt.pie(winning_times, labels=labels)
plt.show()













