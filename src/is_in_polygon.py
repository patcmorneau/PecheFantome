import matplotlib.pyplot as plt
import numpy as np
import csv
import GGlib
from shapely.geometry import Point, Polygon

liste_coord = []
coordinates = []
with open('data_for_example/Baiedeschaleurs.csv') as csvfile:
	data = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in data:
		# print(row[0])
		coord = row[0].split(",")
		latitude = float(coord[0])
		longitude = float(coord[1])
		coordinates += [latitude, longitude]
		liste_coord += [coordinates]
		coordinates = []
print(liste_coord[0])

points_in_baieDesChaleurs = np.array(liste_coord)
#print(points_in_baieDesChaleurs)

points_x = np.array([])
points_y = np.array([])
for i in range(len(points_in_baieDesChaleurs)):
	points_x = np.append(points_x, points_in_baieDesChaleurs[i][0])
	points_y = np.append(points_y, points_in_baieDesChaleurs[i][1])





# creation du dictionnaire pour les zones / polygones
zones = ['Baie des chaleurs','Canal de Grande-Rivière','Nord Shediac Valley','Western Bradelle Valley','Eastern Bradelle Valley']

sud_coordinates = [("47°56’13’’","65°18’01’’"),("47°54’25’’","65°18’01’’"),("48°06’18’’","64°36’00’’"),("48°12’03’’","64°36’00’’"),("47°56’13’’","65°18’01’’")],[("48°16’01’’","64°33’07’’"),("48°09’32’’","64°33’07’’"),("48°06’18’’","64°20’13’’"),("48°18’10’’","64°21’07’’")],[("48°27’36’’","63°48’39’’"),("48°07’04’’","64°00’00’’"),("48°07’04’’","63°45’00’’"),("48°27’36’’","63°25’15’’")],[("47°45’46’’","63°18’21’’"),("47°13’12’’","63°18’21’’"),("47°13’12’’","63°08’31’’"),("47°45’46’’","63°08’31’’")],[("47°35’27’’","62°34’04’’"),("47°01’00’’","62°38’13’’"),("47°01’00’’","62°26’20’’"),("47°35’27’’","62°25’55’’")]
#print(coordinates[0])# return liste of point
#print(coordinates[0][0]) # return pair (x,y)
#print (coordinates[0][0][0]) # return x or y


#inverser x & y de tous les points de la liste de liste de tuple
new_sud_coordinates = []
#new_sud_coordinates = np.empty([0])
polygone = []
#polygone = np.array(polygone,dtype='int')
for zone in sud_coordinates:
	for point in zone:
		point = list(point)
		latitude = point[1]
		longitude = point[0]
		point[0] = latitude
		point[1] = longitude
		polygone += [point]
	new_sud_coordinates += [polygone]
	polygone = []
sud_coordinates = new_sud_coordinates

#convertir tous les points en degree decimal
acpg_zones = {}
coordinates = []
deg_coordinates = []
for zone in sud_coordinates:

	for coord in zone:
		x = coord[0]
		y = coord[1]
		x,y = GGlib.sud2deg(x,y)
		x = GGlib.changer_direction(x)
		coordinate = [x,y]
		coordinates += [coordinate]
	deg_coordinates += [coordinates]
	coordinates = []


#ecrire les polygons dans un fichier .shp
for i in range(len(zones)):
	acpg_zones.update({zones[i] : deg_coordinates[i]})
#print(acpg_zones)

polygon_baieDesChaleurs = acpg_zones['Baie des chaleurs']
print(polygon_baieDesChaleurs)

vertice_x = []
vertice_y = []
for i in range(len(polygon_baieDesChaleurs)):
	vertice_x += [polygon_baieDesChaleurs[i][0]]
	vertice_y += [polygon_baieDesChaleurs[i][1]]


#plt.scatter(points_x,points_y)
#plt.plot(vertice_x,vertice_y)
#plt.show()

test_points_x = points_x[0]
test_points_y = points_y[0]

test_point = Point(test_points_x,test_points_y)
polygon = Polygon(polygon_baieDesChaleurs)

#print(test_point.within(polygon))

def is_it_in_poly(point,polygon):
	x = point[0]
	y = point[1]
	point = Point(x,y)
	polygon = Polygon(polygon)
	result = point.within(polygon)
	return result


#result = is_it_in_poly(test_point,polygon)
#print(result)

