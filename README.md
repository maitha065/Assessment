# Data Exploration 

The aim of this project was to explore datasets that were released by Twiiter on state linked campaigns and write python scripts which include data summarization, time series construction, and topic modeling. The scripts can be found through the following link https://transparency.twitter.com/en/reports/information-operations.html.

## Description

Due to the size of the datasets, the script only works with one campaign, specifically, the Iran datasets from 2018 to 2021. The first task summarizes the data in terms of the total dataset size, it splits between the tweets and retweets, it shows the number of unique users involved, it portrays the number of likes with respect to the retweets, and it also the average interaction between the likes and tweets. The second task involves creating a time series plot, to do so, the tweet_time column was changed from an object to a date_time format, and upon doing that, the creation of an index with new columns that include the year, month, date and hour was done. The time series plot shows the number of likes that occured per hour in the iran campaign. The final task shows a plot that implements topic modeling on the data. It shows the most used words in the datasets. 

Note: iran_data.py includes code that can be run for each of the data exploration tasks. They are all combined into one script. 

### Libraries

Pandas, Numpy, Matplotlib, networkx 

### Installing

Install the iran_data.py script and save the datasets of the Iran campaign in a folder, whilst noting its path. 

### Executing program

Once the datasets have been saved, the paths after "pd.read_csv" should be set to the path where you have saved the datasets, in order to run the scripts and view the plots. 

## Authors

Maitha Alshaali




