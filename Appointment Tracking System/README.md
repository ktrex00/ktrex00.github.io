# Appointment Tracking System Project

## Project Overview

This project was designed and implemented by myself in response to a business need. Specific details are not available due to company propriety. 

Our business sector needed an updated method of recording completed events, and ensuring that they were scheduled to happen in the future. This required the coordination of a few different teams and was previously kept in an Excel sheet that served more as a note sheet than a database of information. Dates were confused, notes were not present, and projects that were no longer relevant remained on the sheet. Going forward, there needed to be a clear system of retrieving the most recent appointments for each project, in case records needed to be pulled for an outside party. 

## Proposed Solution

In conversations with the teams that would be using the system the most, I was able to determine the primary and secondary goals of the task force. Previous appointments needed to be recorded for each project, and in a way that they could be retrieved easily. There were many appointment details, which impacted when the next appointment was due. Because these appointments were on a recurring schedule, having an automation take over the scheduling would be ideal for all parties.

After more discussions, Smartsheets was presented as the preferred option, due to its many integrations and similarity to Excel. In order to update the system to be more dynamic and clear, I transformed the current data into a database, involving a few sheets.

- Primary Project Listing
  - All potential projects were listed here, along with the teams involved, locations, and other relevant information.
  - This allowed for easier management of removing projects once they were no longer necessary, a problem in the previous solution.
- Appointment Records
  - A sheet containing the details of each appointment, with each row identifying the date, project, and other relevant information.
  - This sheet used the Primary Listing sheet to auto-populate fields, such as team contact information.
- Appointment Schedules
  - One sheet served as a library to help determine when the next appointment would be needed, based on the various aspects of the recorded appointment. This sheet took into account multiple appointment schedules based on the type of project and involved redundancies for situations not expressly described.

To ensure that the system would be easy to use for anyone not familiar with Smartsheets, automatic forms were created for the Primary Listing and Appointment Records sheets.

## Automation

A large draw of using Smartsheets was the automation and interface with Microsoft Outlook. A secondary goal of the team was to know when the next appointments were due, and to properly notify involved teams when those due dates approached. An automation scheme was set up in the Appointment Records sheet, where an email triggers to send to the necessary parties with their upcoming due date and information about the project.

## Implementation

The new system was deployed and has worked efficiently. Bugs were limited primarily to users adding projects outside of the workflow automation. The system has been incorporated into the operating guidelines of the team, and is used on a regular basis by the primary team and used for reference for secondary teams.
