---
layout: single
title: "ZIMS Program Conversion Tool"
excerpt: "A hand-coded program to clean data and present it in a useable, familiar Excel format."
hide_masthead: true
header:
    teaser: /assets/images/ZIMStool-crop.png
---
## Project Overview
This is a project I created and designed myself, over many iterations, to allow less tech-savvy coworkers to access the data they need easily.

## History
Our facility moved to using [ZIMS](https://zims.species360.org/) as a data-management system in early 2022. Before ZIMS, my team primarily used Excel workbooks to track and manage our animals. ZIMS provided us the opportunity to use one location for all of our animal data. While it provides its own reports and graphs, we found that it was not providing the level of visualization we were hoping for.

The team uses a few key metrics to provide a snapshot of an animal's current behavior and potential motivation. These had historically been tracked as boolean values in Excel, and now were tracked under the Care and Welfare module in ZIMS. Diet records are also visualized only as bar graphs by ZIMS, whereas we found line graphs and the ability to track percent eaten to be most useful.

As I found that the excel outputs from ZIMS were consistent, but did not fit our needs, I created a pipeline to clean the data into a format that was more familiar and easier to manipulate than the raw output. 
This allowed my team to quickly convert data from ZIMS into a form that they were familiar with, saving hours of work per person spent on sorting through data by hand.
{: .notice--primary}

![1786805018023](</assets\images\ZIMStool.png>)

## Unique Challenges
This project tested my limits in quite a few ways beyond typical data processing. 

The actual data-cleaning pipeline was straightforward, and I had run multiple notebooks with similar code to extract data from different animals. Most of the data was already clean, and the biggest change was transposing rows and columns.

Historically, we had worked on spreadsheets with one row per day, and multiple columns for things we tracked. ZIMS tended to output multiple lines per day, resulting in the need to pivot the table and combine rows.
{: .notice--primary}