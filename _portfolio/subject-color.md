---
title: "School Subject Color Preferences"
layout: single
excerpt: "A quick and fun visualization of personal color preferences for school subjects."
header:
    teaser: /assets/images/subject-color-teaser.png
toc: true
published: true
---
<!-- markdownlint-disable MD033 -->

## Overview

This project was a fun side objective based on an opinion poll in my workplace. The question was simply "Which color notebook or folder do you use for each school subject?".

The color ratios are presented in a format similar to a school college-ruled notebook.

<iframe src="https://marimo.app/github/ktrex00/ktrex00.github.io/blob/main/assets/subject-color.py/wasm?embed=true&mode=read&include-code=false" sandbox="allow-scripts allow-same-origin allow-downloads allow-popups allow-forms" allow="microphone" allowfullscreen style="width: calc(100% + 500px); margin-left: -250px; margin-right: -250px; height: 525px;" frameborder="0"></iframe>

## Tools Used

Pandas was used for the initial import of the .csv file into a Marimo notebook, along with ensuring proper datatypes, setting and labeling an index, and grouping subject colors. Marimo was chosen specifically because of the feature allowing for cells to update in real time. The goal was to allow the visualization to update the rest of the 'notebooks' when a color is selected. For example, if Red is selected for Science, the other notebooks should show the range of colors for anyone who picked Red for Science.

Because a goal of this project was to filter multiple views, marimo, with its reactive execution, seemed like the right fit. Ultimately, the base cell reactivity did not work as hoped. The visual had to be split into two separate visuals, with the second depending on selections in the first. This was not the intended effect, so research continued to create a functional, cohesive visualization that would update itself. 
This problem was solved eventually by using the mo.state() function. This allowed the visualization to hold its state outside of the cell, rather than only being dependent on another cell. Now, when a color is selected, that state can hold a dictionary of the 'locked' subjects (ie: Math to Red and English to Blue) to a color to allow for proper filtering of the remaining colors.

Another benefit to a marimo notebook is the ability to run as an encapsulated notebook on its own, ideal for presenting in a portfolio such as this. The full notebook is presented at the bottom of the page.

Plotly was the visualization library used, due to its interactivity and flexibility. It allows for tree graphs, which is what was used instead of something like a pie chart, for stylistic reasons. The goal was to show a visual distinction between colors chosen more often and the area taken up by each color. Instead of a pie chart, the tree graph can be presented in a rectangle, allowing it to be designed to mimic a typical school notebook. Plotly also allows for tooltips when hovering over different areas of the visualization, providing more information about each choice.

## Deployment

To present the final visualization on this portfolio, an iframe was used on a markdown page to embed the visualization in an interactive way. The portfolio consists of multiple Markdown pages, built on a Jekyll base. Using an iframe allowed for adding the HTML output of the visualization.

## AI Use

Anthropic's Claude was used as a tool to assist with concepts and figuring out bugs. The initial idea came from myself, but Claude was used for small visual details, such as setting up the charts to look like notebooks. Code was not taken wholesale from the AI agent, but instead used as a jumping-off point.

## Full Code

<iframe src="https://marimo.app/github/ktrex00/ktrex00.github.io/blob/main/assets/subject-color.py?embed=true&mode=read" sandbox="allow-scripts allow-same-origin allow-downloads allow-popups allow-forms" allow="microphone" allowfullscreen width="100%" height="700" frameborder="0"></iframe>