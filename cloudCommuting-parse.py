import pickle
import csv

data = {}
system = {}

mh_dist1 = ('South St & Whitehall St', 'Bus Slip & State St', 'Water - Whitehall Plaza', 'Broad St & Bridge St', 'South St & Gouverneur Ln', 'Old Slip & Front St', 'Front St & Maiden Ln', 'Broadway & Battery Pl', 'Little West St & 1 Pl', 'Pearl St & Hanover Square', 'West Thames St', 'William St & Pine St', 'Maiden Ln & Pearl St', 'Liberty St & Broadway', 'John St & William St', 'Cliff St & Fulton St', 'Fulton St & William St', 'South End Ave & Liberty St', 'Barclay St & Church St', 'Park Pl & Church St', 'Vesey Pl & River Terrace', 'Murray St & West St', 'Greenwich St & Warren St', 'Warren St & Church St', 'Spruce St & Nassau St', 'Centre St & Chambers St', 'Reade St & Broadway', 'Centre St & Worth St', 'Leonard St & Church St', 'Hudson St & Reade St', 'Duane St & Greenwich St', 'West St & Chambers St', 'Harrison St & Hudson St', 'Greenwich St & N Moore St', 'Laight St & Hudson St', 'Watts St & Greenwich St', 'Lispenard St & Broadway')
mh_dist2 = ('Elizabeth St & Hester St', 'Howard St & Centre St', 'Grand St & Greene St', '6 Ave & Canal St', '6 Ave & Broome St', 'W Houston St & Hudson St', 'MacDougal St & Prince St', 'W Broadway & Spring St', 'Mercer St & Spring St', 'Cleveland Pl & Spring St', 'Mott St & Prince St', 'Lafayette St & Jersey St', 'Mercer St & Bleecker St', 'Great Jones St', 'Washington Pl & Broadway', 'Washington Square E', 'LaGuardia Pl & W 3 St', 'Sullivan St & Washington Sq', 'Carmine St & 6 Ave', 'Barrow St & Hudson St', 'Christopher St & Greenwich St', 'Washington Pl & 6 Ave', 'MacDougal St & Washington Sq', 'Lafayette St & E 8 St', 'E 11 St & Broadway', 'Broadway & E 14 St', 'University Pl & E 14 St', 'W 13 St & 6 Ave', 'Greenwich Ave & Charles St', 'W 13 St & 7 Ave', 'Greenwich Ave & 8 Ave', '9 Ave & W 14 St', 'W 14 St & The High Line', 'Washington St & Gansevoort St', 'W 4 St & 7 Ave S', 'Perry St & Bleecker St', 'Bank St & Hudson St', 'Bank St & Washington St', 'Bayard St & Baxter St')
mh_dist3 = ('St James Pl & Pearl St', 'Catherine St & Monroe St', 'Market St & Cherry St', 'Pike St & Monroe St', 'Madison St & Clinton St', 'Madison St & Montgomery St', 'Cherry St', 'Henry St & Grand St', 'Clinton St & Grand St', 'Canal St & Rutgers St', 'Pike St & E Broadway', 'St James Pl & Oliver St', 'Division St & Bowery', 'Forsyth St & Canal St', 'Allen St & Hester St', 'Bialystoker Pl & Delancey St', 'Norfolk St & Broome St', 'Columbia St & Rivington St', 'Stanton St & Mangin St', 'Pitt St & Stanton St', 'Suffolk St & Stanton St', 'Allen St & Rivington St', 'Rivington St & Chrystie St', 'Stanton St & Chrystie St', 'Allen St & E Houston St', 'Rivington St & Ridge St', 'E 2 St & 2 Ave', 'E 3 St & 1 Ave', 'E 2 St & Avenue B', 'E 2 St & Avenue C', 'Avenue D & E 3 St', 'E 6 St & Avenue D', 'E 5 St & Avenue C', 'E 6 St & Avenue B', 'E 7 St & Avenue A', 'E 4 St & 2 Ave', 'Shevchenko Pl & E 7 St', 'St Marks Pl & 2 Ave', 'St Marks Pl & 1 Ave', 'Avenue D & E 12 St', 'E 10 St & Avenue A', 'E 11 St & 2 Ave', 'E 11 St & 1 Ave', 'E 13 St & Avenue A', 'E 12 St & 3 Ave')
mh_dist4 = ('Broadway & W 60 St' ,'W 59 St & 10 Ave', 'W 56 St & 10 Ave', 'W 54 St & 9 Ave', 'W 53 St & 10 Ave', 'W 52 St & 11 Ave', 'W 52 St & 9 Ave', 'W 49 St & 8 Ave', 'W 47 St & 10 Ave', 'W 46 St & 11 Ave', 'W 45 St & 8 Ave', 'W 43 St & 10 Ave', 'W 42 St & 8 Ave', 'W 39 St & 9 Ave', 'W 37 St & 10 Ave', 'W 34 St & 11 Ave', 'W 29 St & 9 Ave', 'W 26 St & 10 Ave', 'W 26 St & 10 Ave', 'W 24 St & 7 Ave', 'W 22 St & 10 Ave', 'W 22 St & 8 Ave', 'W 21 St & 6 Ave', 'W 20 St & 11 Ave', 'W 20 St & 8 Ave', 'W 20 St & 7 Ave', 'W 17 St & 8 Ave', 'W 16 St & The High Line', 'W 15 St & 7 Ave', '12 Ave & W 40 St', '11 Ave & W 59 St', '11 Ave & W 41 St', '11 Ave & W 27 St', '10 Ave & W 28 St', '9 Ave & W 45 St', '9 Ave & W 22 St', '9 Ave & W 18 St', '9 Ave & W 16 St', '8 Ave & W 52 St', '8 Ave & W 33 St', '8 Ave & W 31 St')
mh_dist5 = ('E 56 St & Madison Ave', 'E 55 St & Lexington Ave', 'E 53 St & Madison Ave', 'E 51 St & Lexington Ave', 'E 47 St & Park Ave', 'E 43 St & Vanderbilt Ave', 'E 42 St & Vanderbilt Ave', 'E 41 St & Madison Ave', 'E 24 St & Park Ave S', 'E 20 St & Park Ave', 'E 16 St & 5 Ave', 'E 17 St & Broadway', 'Grand Army Plaza & Central Park S', 'Central Park S & 6 Ave', 'Broadway & W 58 St', 'Broadway & W 55 St', 'Broadway & W 53 St', 'Broadway & W 51 St', 'Broadway & W 49 St', 'Broadway & W 41 St', 'Broadway & W 39 St', 'Broadway & W 37 St', 'Broadway & W 36 St', 'Broadway & W 32 St', 'Broadway & W 29 St', 'W 56 St & 6 Ave', 'W 52 St & 5 Ave', 'W 51 St & 6 Ave', 'W 45 St & 6 Ave', 'W 44 St & 5 Ave', 'W 41 St & 8 Ave', 'W 37 St & 5 Ave', 'W 27 St & 7 Ave', 'W 25 St & 6 Ave', 'W 18 St & 6 Ave')
mh_dist6 = ('E 59 St & Sutton Pl', '2 Ave & E 58 St', 'E 58 St & 3 Ave', 'E 56 St & 3 Ave', 'E 55 St & 2 Ave', 'E 53 St & Lexington Ave', 'E 52 St & 2 Ave', 'E 51 St & 1 Ave', 'E 48 St & 3 Ave', 'E 47 St & 2 Ave', 'E 45 St & 3 Ave', 'E 47 St & 1 Ave', '1 Ave & E 44 St', 'E 43 St & 2 Ave', 'E 39 St & 2 Ave', 'E 39 St & 3 Ave', 'E 37 St & Lexington Ave', 'FDR Drive & E 35 St', '2 Ave & E 31 St', '1 Ave & E 30 St', 'E 31 St & 3 Ave', 'E 27 St & 1 Ave', 'E 25 St & 1 Ave', 'E 25 St & 2 Ave', 'Lexington Ave & E 26 St', 'Lexington Ave & E 24 St', 'E 23 St & 1 Ave', 'E 20 St & 2 Ave', '1 Ave & E 15 St', '1 Ave & E 18 St', 'E 14 St & Avenue B', 'E 19 St & 3 Ave', 'E 15 St & 3 Ave', 'E 16 St & Irving Pl')

bk_dist1 = ('Bedford Ave & S 9th St', 'Kent Ave & S 11 St', 'S 5 Pl & S 4 St', 'Broadway & Berry St', 'S 4 St & Wythe Ave', 'S 3 St & Bedford Ave', 'Grand St & Havemeyer St', 'Metropolitan Ave & Bedford Ave')
bk_dist6 = ('Old Fulton St', 'Columbia Heights & Cranberry St', 'Clark St & Henry St', 'Hicks St & Montague St', 'Atlantic Ave & Furman St', 'Henry St & Atlantic Ave', 'Clinton St & Joralemon St', 'Henry St & Poplar St', 'Front St & Washington St', 'Cadman Plaza E & Red Cross Pl', 'Cadman Plaza E & Tillary St', 'Cadman Plaza West & Montague St', 'Joralemon St & Adams St', 'State St & Smith St', 'Gallatin Pl & Livingston St', 'Lawrence St & Willoughby St', 'Jay St & Tech Pl', 'Concord St & Bridge St', 'York St & Jay St', 'Pearl St & Anchorage Pl', 'Front St & Washington St', 'Front St & Gold St', 'Sands St & Navy St', 'Nassau St & Navy St', 'DeKalb Ave & Hudson Ave', 'Duffield St & Willoughby St', 'Bond St & Schermerhorn St', 'Hanover Pl & Livingston St', 'Willoughby St & Fleet St', 'Park Ave & St Edwards St', 'Myrtle Ave & St Edwards St', 'Fulton St & Rockwell Pl', '3 Ave & Schermerhorn St', 'Lafayette Ave & Fort Greene Pl', 'Ashland Pl & Hanson Pl', 'Dean St & 4 Ave', 'Atlantic Ave & Fort Greene Pl', 'S Portland Ave & Hanson Pl', 'DeKalb Ave & S Portland Ave', 'Washington Park', 'Flushing Ave & Carlton Ave', 'Carlton Ave & Park Ave', 'Clermont Ave & Park Ave', 'Adelphi St & Myrtle Ave', 'Cumberland St & Lafayette Ave', 'S Portland Ave & Hanson Pl', 'Fulton St & Clermont Ave', 'Clermont Ave & Lafayette Ave', 'DeKalb Ave & Vanderbilt Ave', 'Clinton Ave & Myrtle Ave', 'Clermont Ave & Park Ave', 'Flushing Ave & Carlton Ave', 'Clinton Ave & Flushing Ave', 'Washington Ave & Park Ave', 'Willoughby Ave & Hall St', 'Lafayette Ave & St James Pl', 'Washington Ave & Greene Ave', 'Fulton St & Waverly Ave', 'Fulton St & Clermont Ave', 'Lafayette Ave & St James Pl', 'Emerson Pl & Myrtle Ave', 'Willoughby Ave & Hall St', 'Emerson Pl & Myrtle Ave', 'Franklin Ave & Myrtle Ave', 'Willoughby Ave & Walworth St', 'DeKalb Ave & Skillman St', 'Lafayette Ave & Classon Ave', 'Lexington Ave & Classon Ave', 'Lexington Ave & Classon Ave', 'Monroe St & Classon Ave', 'Fulton St & Grand Ave', 'Fulton St & Waverly Ave', 'Fulton St & Clermont Ave', 'S Portland Ave & Hanson Pl', 'Atlantic Ave & Fort Greene Pl', 'Dean St & 4 Ave', 'Ashland Pl & Hanson Pl', 'Lafayette Ave & Fort Greene Pl', 'Macon St & Nostrand Ave', 'Railroad Ave & Kay Ave')

with open('aug2014tripData.csv', 'rb') as csvfile:
    items = csv.reader(csvfile, delimiter=',', quotechar='"')
    items.next()
    for item in items:
		station = item[8]

		try:
			age = int(item[13])
		except:
			continue

		try:
			gender = int(item[14])
		except:
			continue

		if station not in data:
			data[station] = {'-30m': 0, '-30f': 0, '30-40m': 0, '30-40f': 0, '40-50m':0, '40-50f':0, '50+m':0, '50+f':0}

		genderKey = ''
		ageKey = ''

		if age > 1984:
			ageKey = str('-30')
		elif age <= 1984 and age > 1974:
			ageKey = str('30-40')
		elif age <= 1974 and age > 1964:
			ageKey = str('40-50')
		elif age <= 1964:
			ageKey = str('50+')
		else:
			continue

		if gender == 1:
			genderKey = 'm'
		elif gender == 2:
			genderKey = 'f'
		else:
			continue

		data[station][ageKey+genderKey] += 1

print data

m30Total = 0
f30Total = 0
m30to40Total = 0
f30to40Total = 0
m40to50Total = 0
f40to50Total = 0
mOver50Total = 0
fOver50Total = 0

# SYSTEM TOTALS

# for i in data:
# 	m30Total += data[i]['-30m']
# 	f30Total += data[i]['-30f']
# 	m30to40Total += data[i]['30-40m']
# 	f30to40Total += data[i]['30-40f']
# 	m40to50Total += data[i]['40-50m']
# 	f40to50Total += data[i]['40-50f']
# 	mOver50Total += data[i]['50+m']
# 	fOver50Total += data[i]['50+f']

# print "males under 30: " + str(m30Total)
# print "females under 30: " + str(f30Total)
# print "males 30 to 40: " + str(m30to40Total)
# print "females 30 to 40: " + str(f30to40Total)
# print "males 40 to 50: " + str(m40to50Total)
# print "females 40 to 50: " + str(f40to50Total)
# print "males over 50: " + str(mOver50Total)
# print "females over 50: " + str(fOver50Total)


# BK DISTRICT 6 SYSTEM TOTALS

# for i in bk_dist6:
# 	m30Total += data[i]['-30m']
# 	f30Total += data[i]['-30f']
# 	m30to40Total += data[i]['30-40m']
# 	f30to40Total += data[i]['30-40f']
# 	m40to50Total += data[i]['40-50m']
# 	f40to50Total += data[i]['40-50f']
# 	mOver50Total += data[i]['50+m']
# 	fOver50Total += data[i]['50+f']

# print "males under 30: " + str(m30Total)
# print "females under 30: " + str(f30Total)
# print "males 30 to 40: " + str(m30to40Total)
# print "females 30 to 40: " + str(f30to40Total)
# print "males 40 to 50: " + str(m40to50Total)
# print "females 40 to 50: " + str(f40to50Total)
# print "males over 50: " + str(mOver50Total)
# print "females over 50: " + str(fOver50Total)


# BK DISTRICT 1 SYSTEM TOTALS

# for i in bk_dist1:
# 	m30Total += data[i]['-30m']
# 	f30Total += data[i]['-30f']
# 	m30to40Total += data[i]['30-40m']
# 	f30to40Total += data[i]['30-40f']
# 	m40to50Total += data[i]['40-50m']
# 	f40to50Total += data[i]['40-50f']
# 	mOver50Total += data[i]['50+m']
# 	fOver50Total += data[i]['50+f']

# print "males under 30: " + str(m30Total)
# print "females under 30: " + str(f30Total)
# print "males 30 to 40: " + str(m30to40Total)
# print "females 30 to 40: " + str(f30to40Total)
# print "males 40 to 50: " + str(m40to50Total)
# print "females 40 to 50: " + str(f40to50Total)
# print "males over 50: " + str(mOver50Total)
# print "females over 50: " + str(fOver50Total)


# output = open('data.pkl', 'wb')
# pickle.dump(data, output)
# output.close()

# MANHATTAN DISTRICT 1 SYSTEM TOTALS

# for i in mh_dist1:
# 	m30Total += data[i]['-30m']
# 	f30Total += data[i]['-30f']
# 	m30to40Total += data[i]['30-40m']
# 	f30to40Total += data[i]['30-40f']
# 	m40to50Total += data[i]['40-50m']
# 	f40to50Total += data[i]['40-50f']
# 	mOver50Total += data[i]['50+m']
# 	fOver50Total += data[i]['50+f']

# print "males under 30: " + str(m30Total)
# print "females under 30: " + str(f30Total)
# print "males 30 to 40: " + str(m30to40Total)
# print "females 30 to 40: " + str(f30to40Total)
# print "males 40 to 50: " + str(m40to50Total)
# print "females 40 to 50: " + str(f40to50Total)
# print "males over 50: " + str(mOver50Total)
# print "females over 50: " + str(fOver50Total)


# output = open('data.pkl', 'wb')
# pickle.dump(data, output)
# output.close()

# MANHATTAN DISTRICT 2 SYSTEM TOTALS

# for i in mh_dist2:
# 	m30Total += data[i]['-30m']
# 	f30Total += data[i]['-30f']
# 	m30to40Total += data[i]['30-40m']
# 	f30to40Total += data[i]['30-40f']
# 	m40to50Total += data[i]['40-50m']
# 	f40to50Total += data[i]['40-50f']
# 	mOver50Total += data[i]['50+m']
# 	fOver50Total += data[i]['50+f']

# print "males under 30: " + str(m30Total)
# print "females under 30: " + str(f30Total)
# print "males 30 to 40: " + str(m30to40Total)
# print "females 30 to 40: " + str(f30to40Total)
# print "males 40 to 50: " + str(m40to50Total)
# print "females 40 to 50: " + str(f40to50Total)
# print "males over 50: " + str(mOver50Total)
# print "females over 50: " + str(fOver50Total)


# MANHATTAN DISTRICT 3 SYSTEM TOTALS

# for i in mh_dist3:
# 	m30Total += data[i]['-30m']
# 	f30Total += data[i]['-30f']
# 	m30to40Total += data[i]['30-40m']
# 	f30to40Total += data[i]['30-40f']
# 	m40to50Total += data[i]['40-50m']
# 	f40to50Total += data[i]['40-50f']
# 	mOver50Total += data[i]['50+m']
# 	fOver50Total += data[i]['50+f']

# print "males under 30: " + str(m30Total)
# print "females under 30: " + str(f30Total)
# print "males 30 to 40: " + str(m30to40Total)
# print "females 30 to 40: " + str(f30to40Total)
# print "males 40 to 50: " + str(m40to50Total)
# print "females 40 to 50: " + str(f40to50Total)
# print "males over 50: " + str(mOver50Total)
# print "females over 50: " + str(fOver50Total)


# MANHATTAN DISTRICT 4 SYSTEM TOTALS

# for i in mh_dist4:
# 	m30Total += data[i]['-30m']
# 	f30Total += data[i]['-30f']
# 	m30to40Total += data[i]['30-40m']
# 	f30to40Total += data[i]['30-40f']
# 	m40to50Total += data[i]['40-50m']
# 	f40to50Total += data[i]['40-50f']
# 	mOver50Total += data[i]['50+m']
# 	fOver50Total += data[i]['50+f']

# print "males under 30: " + str(m30Total)
# print "females under 30: " + str(f30Total)
# print "males 30 to 40: " + str(m30to40Total)
# print "females 30 to 40: " + str(f30to40Total)
# print "males 40 to 50: " + str(m40to50Total)
# print "females 40 to 50: " + str(f40to50Total)
# print "males over 50: " + str(mOver50Total)
# print "females over 50: " + str(fOver50Total)


# MANHATTAN DISTRICT 5 SYSTEM TOTALS

# for i in mh_dist5:
# 	m30Total += data[i]['-30m']
# 	f30Total += data[i]['-30f']
# 	m30to40Total += data[i]['30-40m']
# 	f30to40Total += data[i]['30-40f']
# 	m40to50Total += data[i]['40-50m']
# 	f40to50Total += data[i]['40-50f']
# 	mOver50Total += data[i]['50+m']
# 	fOver50Total += data[i]['50+f']

# print "males under 30: " + str(m30Total)
# print "females under 30: " + str(f30Total)
# print "males 30 to 40: " + str(m30to40Total)
# print "females 30 to 40: " + str(f30to40Total)
# print "males 40 to 50: " + str(m40to50Total)
# print "females 40 to 50: " + str(f40to50Total)
# print "males over 50: " + str(mOver50Total)
# print "females over 50: " + str(fOver50Total)


# MANHATTAN DISTRICT 6 SYSTEM TOTALS

for i in mh_dist6:
	m30Total += data[i]['-30m']
	f30Total += data[i]['-30f']
	m30to40Total += data[i]['30-40m']
	f30to40Total += data[i]['30-40f']
	m40to50Total += data[i]['40-50m']
	f40to50Total += data[i]['40-50f']
	mOver50Total += data[i]['50+m']
	fOver50Total += data[i]['50+f']

print "males under 30: " + str(m30Total)
print "females under 30: " + str(f30Total)
print "males 30 to 40: " + str(m30to40Total)
print "females 30 to 40: " + str(f30to40Total)
print "males 40 to 50: " + str(m40to50Total)
print "females 40 to 50: " + str(f40to50Total)
print "males over 50: " + str(mOver50Total)
print "females over 50: " + str(fOver50Total)


# output = open('data.pkl', 'wb')
# pickle.dump(data, output)
# output.close()



#######SOME NEW FILE

# import pickle
# pkl_file = open('data.pkl', 'rb')
# data = pickle.load(pkl_file)
# pkl_file.close()