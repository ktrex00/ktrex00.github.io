---
layout: single
title: "ZIMS Program Conversion Tool"
excerpt: "A hand-coded program to clean data and present it in a useable, familiar Excel format."
hide_masthead: true
header:
    teaser: /assets/images/ZIMStool-crop.png
toc: true
---
## Project Overview
This is a project I created and designed myself, over many iterations, to allow less tech-savvy coworkers to access the data they need easily.

## History
Our facility moved to using [ZIMS](https://zims.species360.org/) as a data-management system in early 2022. Before ZIMS, my team primarily used Excel workbooks to track and manage our animals. ZIMS provided us the opportunity to use one location for all of our animal data. While it provides its own reports and graphs, we found that it was not providing the level of visualization we were hoping for.

The team uses a few key metrics to provide a snapshot of an animal's current behavior and potential motivation. These had historically been tracked as boolean values in Excel, and now were tracked under the Care and Welfare module in ZIMS. Diet records are also visualized only as bar graphs by ZIMS, whereas we found line graphs and the ability to track percent eaten to be most useful.

As I found that the excel outputs from ZIMS were consistent, but did not fit our needs, I created a pipeline to clean the data into a format that was more familiar and easier to manipulate than the raw output.This allowed my team to quickly convert data from ZIMS into a form that they were familiar with, saving hours of work per person spent on sorting through data by hand.

![1786805018023](</assets\images\ZIMStool.png>)

## Unique Challenges
This project tested my limits in quite a few ways beyond typical data processing. 

The actual data-cleaning pipeline was straightforward, and I had run multiple notebooks with similar code to extract data from different animals. Most of the data was already clean, and the biggest change was transposing rows and columns. Historically, we had worked on spreadsheets with one row per day, and multiple columns for things we tracked. ZIMS tended to output multiple lines per day, resulting in the need to pivot the table and combine rows.

My target userbase for this project was comfortable with computers, but not with coding. I needed to create a program that did not require installing Python or running a code through a CLI, as this would increase the friction of actual usage.

We also work with a collection of machines, not a typical office setup where everyone has their own setup. No one machine 'belongs' to one person. Every person does have access to a few shared drives, including Sharepoint. 

Due to company propriety, I did not host the application on any outside server. It was important to protect anything from being accessible outside the organization. The program would need to run on multiple machines easily, without being hosted externally, and not require any CLI interactions. 

## Solutions
The first step was to build the pipeline. There were two main exports from ZIMS that were useful to the team, so I focused on those. I included a portion of code to identify the two different exports and apply the proper techniques based on that. 

I then converted my Jupyter Notebook code into procedural code that runs in Python scripts. There was a lot of trial and error, but eventually I landed on a combination of Flet and PyInstaller to create and distribute my application. Flet has a very user-friendly UI and looks native, which would make its use simple to understand. PyInstaller has the ability to export a full .exe file, which is familiar to many users, and easy to initiate.

## Issues
PyInstaller was the first distribution system used for the application, but the biggest issue was the load time. PyInstaller needed to unzip files in order to run them, and in the meantime, the user had no information that the program was even running, even a splash page. I pared down as much as I could in the base code, using only the pandas imports that were necessary and when they were needed, but the lag time continued to be an issue. The eventual fix was to look beyond PyInstaller.

Flet was the eventual choice for the main application, but it cannot be packaged into a single .exe file without the same issues as PyInstaller.