# Uber Price Prediction Repo for CE 262 Transportation Analysis Project 

**Goal**
To predict future uberX and uberPool prices between two locations to determine best time to take an Uber and what type to take

## PriceEstimate.py
Utilizes Uber's API to generate a dataset of uberPool and uberX prices between two locations in the span of approximately one week

Data collected include:
- Date and Time in UTC
- Price
- Duration [Seconds]
- Distance [Miles]
- Wait Time [Minutes]

## TestFile.ipynb
File for testing processes for analysis

Cleans and plots data from UberX and UberPool
Performs regression analysis on trip prices on both datasets for weekdays 

