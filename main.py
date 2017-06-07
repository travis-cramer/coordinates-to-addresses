import pandas as pd
import googlemaps
import pprint


#create a pretty printer for displaying gmaps request results (for debugging/altering the code dealing with gmaps result)
pp = pprint.PrettyPrinter(indent=4)




#THE FOLLOWING CODE IMPORTS YOUR GEO COORDINATES INTO A PANDAS DATAFRAME

#get column names into header variable (first row in csv file)
header = pd.read_csv('properties_head_2016.csv', nrows=0)

#import first <nrows> rows of properties dataset, use header for header names (this is needed if we want to increase paramter skiprows)
df = pd.read_csv("properties_head_2016.csv", names=header, skiprows=1, nrows = 10 )

#make separate df with just lat and lng values
my_df = df[['latitude', 'longitude']]



#get gmaps client key from text file
gmaps_key = open("passwords.txt", 'r').read()
#instantiate the gmaps api/client
gmaps = googlemaps.Client(key = gmaps_key)





#make lists for appending city names and state abbreviations (corrwsponds to commented out code in for loop below)
#cities = [] 
#states = []
#index_errors = 0


for i in range(len(my_df)):
	result = gmaps.reverse_geocode((float(my_df.iloc[i]['latitude'])/1000000, float(my_df.iloc[i]['longitude'])/1000000)) 


	#pretty print for examining gmaps result (for debugging/altering the code)
	#pp.pprint(result)

	result = result[0]['address_components']

	address = ''
	for j in range(len(result)):
		address = address + result[j]['long_name'] + ' '

	print address[:-1]  #remove unnecessary space at the end of string
	print "-" * 20		#prettify




	#THE FOLLOWING CODE IS IF WE/YOU ONLY WANT TO PRINT THE "CITY, STATE" OF THE GEO COORDINATES

	#find and get 'locality' (city) and 'administratvie_area_level_1' (state) and append them to their respective list
	"""
	j = 0
	city_found = False
	state_found = False
	while (not city_found) or (not state_found):
		try:
			if 'locality' in result[j]['types']:
				cities.append(result[j]['long_name'])
				city_found = True
				j = j + 1
			elif 'administrative_area_level_1' in result[j]['types']:
				states.append(result[j]['short_name'])
				state_found = True
				j = j + 1
			else:
				j = j + 1
		except IndexError:
			state_found = True
			city_found = True
			print "IndexError"
			index_errors += 1

	#print cities accounting for index errors
	print cities[i - index_errors] + ', ' + states[i - index_errors]
	"""