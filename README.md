An online shoe company has two different ad banners and want to know how they are performing on the four sources: Twitter, Facebook, Google and email.  The company wants to see how the ads are performing based on the number of clicks on each source.

I first look through the first ten rows of a csv file to get an idea of how the categories are broken down.  Then I want to see the number of views each source got.  So I used the 'groupby' function to count the number of times the ads were viewed by each source.  Next after seeing the number of views, I wanted to know after viewing the ad, if they clicked on it. Since their is a timestamp category where it determines the time the ad was clicked.  If was viewed but not clicked, it was be considered as 'null' or 'NaN' on the file. I used another 'groupby' and 'pivot' function to count the number of ads clicked and viewed by performing a boolean and printed out the number of clicks from each source.

To further determine the difference between the number of views and number of clicks of the two ad banners, I formulated a percentage rate to see the percent of users clicked on the ad from each source.

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])


Next, I wanted to break down how many times each ad banner was shown.  First ad banner is known as ad "A" and the second banner is ad "B".  So I did a 'groupby' function to count which ads were viewed and 'reset index' function:

group_count = ad_clicks\
  	.groupby('experimental_group').user_id\
       .count()\
       .reset_index()
       
After, I did another percentage formula to determine the difference between the number of views and number of clicks of each of the two ad banners.  I used all of the functions that I used throughout this project, "groupby", "count", "reset_index" and "pivot" to each of the two groups and how many times each ad was clicked.

greater_percentage = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index().pivot(
		index = 'experimental_group',
		columns = 'is_click',
		values = 'user_id'
).reset_index()

Lastly, to further compare the two ads, I calculated percentages for each ad clicked by the day.  To do that I provided code using the pivot function to determine the number of clicks for each day since their is a 'day' column in the data:

a_clicks = ad_clicks[
   ad_clicks.experimental_group
   == 'A']

b_clicks = ad_clicks[
   ad_clicks.experimental_group
   == 'B']

a_clicks_pivot = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(
		index = 'day',
		columns = 'is_click',
		values = 'user_id'
).reset_index()

a_precentage = a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False])


b_clicks_pivot = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(
		index = 'day',
		columns = 'is_click',
		values = 'user_id'
).reset_index()

b_precentage = b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False])







