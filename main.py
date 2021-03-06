import pandas as pd

# import the csv file and printing the first ten rows of the file
ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head(10))
print(ad_clicks.groupby('utm_source')\
		.user_id.count()\
		.reset_index())

ad_clicks['is_click'] = ~ad_clicks\
   .ad_click_timestamp.isnull()

#Counting the number of clicks for each source
clicks_by_source = ad_clicks\
   .groupby(['utm_source',
             'is_click'])\
   .user_id.count()\
   .reset_index()

clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id').reset_index()

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])

print(clicks_pivot)

#Counting of number of clicks for each banner
group_count = ad_clicks\
  	.groupby('experimental_group').user_id\
       .count()\
       .reset_index()

print(group_count)

greater_percentage = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index().pivot(
		index = 'experimental_group',
		columns = 'is_click',
		values = 'user_id'
).reset_index()

print(greater_percentage)

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

print(a_precentage)

b_clicks_pivot = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(
		index = 'day',
		columns = 'is_click',
		values = 'user_id'
).reset_index()

b_precentage = b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False])

print(b_precentage)









