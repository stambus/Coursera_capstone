# Vilnius_enterprises_and_apartments_data_analysis
This repository is meant for coursera capstone project called
 "Vilnius_enterprises_and_apartments_data_analysis"
 
## Data acquisition
### Apartment data

I have utilised my skills in web scraping and acquired all apartment listings available at the time from website: 

https://aruodas.lt/butai/vilniuje/

Getting this data was quite easy, it did not require much additional formating and cleaning up. 

### Enterprise data

Big chunk of this data was taken from publicly available data sheets in website:

https://www.sodra.lt/lt/paslaugos/informacijos-rinkmenos

Altough this data set required tons of cleaning and additional scraping to do. 
First of all I needed to acquire addresses for these companies, which made me create additional scraper for website : 

https://www.1551.lt/paieska/

This website contained addresses specific to companies names, which I utilised from initial data-set.
After I got all the addresses, I had to make another script in order to get latitutde and longitude coords based on adresses (because final goal was to visual data using maps).
In order to get coords, I used google's geocoder API.

## Exploratory data analysis

