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

<iframe src="/apps/school-colors/index.html"
width="100%" 
height="600px" 
style="border: none;"></iframe>

## Tools Used

Pandas was used for the initial import of the .csv file into a Marimo notebook, along with ensuring proper datatypes, setting and labeling an index, and grouping subject colors. Marimo was chosen specifically because of the feature allowing for cells to update in real time. The goal was to allow the visualization to update the rest of the 'notebooks' when a color is selected. For example, if Red is selected for Science, the other notebooks should show the range of colors for anyone who picked Red for Science.

Ultimately, it appeared that Marimo was not necessary for this feature. Marimo focuses on updating other cells in the notebook in real time, not elements in the same cell as where a selection has been made. Marimo was simply not the right tool for this project, but it was kept in the project because it functions similarly to a Jupyter Notebook, and provided the intended results, even without the cell reactivity feature.

Plotly was the visualization library used, due to its interactivity and flexibility. It allows for tree graphs, which is what was used instead of something like a pie chart, for stylistic reasons. The goal was to show a visual distinction between colors chosen more often and the area taken up by each color. Instead of a pie chart, the tree graph can be presented in a rectangle, allowing it to be designed to mimic a typical school notebook. Plotly also allows for tooltips when hovering over different areas of the visualization, providing more information about each choice.

## Deployment

To present the final visualization on this portfolio, an iframe was used on a markdown page to embed the visualization in an interactive way. The portfolio consists of multiple Markdown pages, built on a Jekyll base. Using an iframe allowed for adding the HTML output of the visualization.

## AI Use

Anthropic's Claude was used as a tool to assist with concepts and figuring out bugs. The initial idea came from myself, but Claude was used for small visual details, such as setting up the charts to look like notebooks. Code was not taken wholesale from the AI agent, but instead used as a jumping-off point.
