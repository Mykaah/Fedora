#!/usr/bin/python3
import os

import matplotlib as m
import matplotlib.pyplot as plt
import pandas

m.use("Agg")

m.rcParams["font.size"] = 12
m.rcParams["font.family"] = "Overpass"
m.rcParams["legend.frameon"] = True

try:
    os.makedirs("./images")
except OSError:
    pass

data = pandas.read_csv("data/contributor-count.csv", parse_dates=[0])
data.set_index("weekstart", inplace=True)


graph = (
    data[["oldactive", "midactive", "newactive"]]
    .rename(
        columns={
            "oldactive": "Old School",
            "midactive": "Intermediate",
            "newactive": "New Contributors",
        }
    )
    .plot.area(
        figsize=(16, 9),
        color=["#ff420e", "#ffd320", "#579d1c"],  # '#004586'
        grid=True,
        stacked=True,
        yticks=range(0, 451, 25),
    )
)
data[["rawcount"]].rename(
    columns={"rawcount": "All Contributors\nincluding less active"}
).plot(figsize=(16, 9), ax=graph, yticks=range(0, 426, 25))

graph.xaxis.grid(True, which="minor", linestyle="-", linewidth=0.25)
graph.yaxis.grid(True, which="major", linestyle="-", linewidth=0.25)

plt.suptitle("Fedora Contributors by Week", fontsize=24)
graph.set_title(
    "Stacked graph of contributors with measured activity each week — and at least 13 weeks total in the last year.\n"
    "“Old school” contributors have been active for longer than two years; new contributors, less than one.\n"
    "Blue line shows all contributors active this week regardless of amount of other activity.",
    fontsize=12,
)
graph.set_xlabel("")

fig = graph.get_figure()
fig.savefig("images/active-contributors-by-week.svg", dpi=300)


graph = (
    data[["oldcore", "midcore", "newcore"]]
    .rename(
        columns={
            "oldcore": "Old School",
            "midcore": "Intermediate",
            "newcore": "New Contributors",
        }
    )
    .plot.area(
        figsize=(16, 9),
        color=["#ff420e", "#ffd320", "#579d1c"],  # '#004586'
        grid=True,
        stacked=True,
        yticks=range(0, 101, 25),
    )
)

graph.xaxis.grid(True, which="minor", linestyle="-", linewidth=0.25)
graph.yaxis.grid(True, which="major", linestyle="-", linewidth=0.25)

plt.suptitle("Core Fedora Contributors by Week", fontsize=24)
graph.set_title(
    "Stacked graph of contributors with measured activity this week — and at least 13 weeks total in the last year.\n"
    "Old school contributors have been active for longer than two years; new contributors, less than one.\n"
    "“Core” means part of the set doing about ⅔s of all actions over the past year.",
    fontsize=12,
)
graph.set_xlabel("")
fig = graph.get_figure()
fig.savefig("images/active-core-contributors-by-week.svg", dpi=300)
