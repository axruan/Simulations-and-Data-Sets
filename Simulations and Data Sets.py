# Alex Ruan
# 17 January 2019
# Sources: matplotlib documentation and various StackOverflow threads

# Description: I graphed Tom Brady's record against the 31 other NFL teams. I split the data into
#              three graphs, one for a winning, tying, and losing record for ease of readability.  Initially, I
#              was going to create a 3D graph but I decided against it because the data was too hard to read.
#              I wanted to plot two bars next to each other for each team but to conserve space I decided to overlay
#              them. I think it turned out better because the data is still pretty clear, and I think it looks
#              better. Nothing was too hard about this project, most of it was just researching how to do
#              various things in matplotlib (like labeling axes and creating a legend).

# On my honor, I have neither received nor given unauthorized aid

import matplotlib.pyplot as plt


# Creates the labels for each graph
def label():
    plt.xlabel("Team", fontsize=10, fontweight='bold')
    plt.ylabel("Win/Loss", fontsize=10, fontweight='bold')


# Creates the actual pictures
fig = plt.figure(figsize=(12, 16), dpi=65)
ax = fig.add_subplot()
plt.ylim(top=50)
fig.suptitle("Tom Brady's Record Against Each NFL Team (Career Record: 225 - 65, most wins ever)", fontsize=16,
             fontweight='bold')


# Data set for winning records
wxpos = ["ATL", "BAL", "BUF", "CHI", "CIN", "CLE", "DAL", "DET", "GB", "HOU", "IND", "JAX", "KC", "LAC", "LAR", "MIA",
         "MIN", "NO", "NYJ", "OAK", "PHI", "PIT", "SF", "TB", "TEN", "WAS"]
wwin = [6, 8, 28, 4, 6, 6, 4, 4, 3, 9, 14, 8, 5, 8, 4, 21, 4, 4, 26, 5, 4, 11, 2, 4, 7, 3]
wloss = [0, 3, 3, 0, 1, 1, 0, 0, 2, 1, 4, 0, 3, 2, 1, 10, 0, 1, 7, 1, 2, 2, 1, 0, 1, 1]


# Data set for tying records
txpos = ["ARI", "CAR", "NYG", "SEA"]
twin = [1, 3, 3, 2]


# Data set for losing records
lxpos = ["DEN"]
lwin = [8]
lloss = [9]


# First graph
plt.subplot(3, 1, 1)
plt.bar(wxpos, wwin, color="blue")
plt.bar(wxpos, wloss, color="red")
plt.legend(["Win", "Loss"])
plt.title("Winning Records")
label()

# Second graph
plt.subplot(3, 1, 2)
plt.bar(txpos, twin, color="blue")
plt.legend(["Win", "Loss"])
plt.title("Tying Records")
label()

# Third graph
plt.subplot(3, 1, 3)
plt.bar(lxpos, lloss, color="red")
plt.bar(lxpos, lwin, color="blue")
plt.legend(["Loss", "Win"])
plt.title("Losing Records")
label()

# Saves the graph to your desktop
plt.savefig("Tom Brady.png")

plt.show()
