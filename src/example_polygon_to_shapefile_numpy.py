# creation du shapefile pour les zones de l'acpg
import numpy as np
import GGlib

zones = ['Baie des chaleurs','Canal de Grande-Rivière','Nord Shediac Valley','Western Bradelle Valley','Eastern Bradelle Valley']

sud_coordinates = [("47°56’13’’","65°18’01’’"),("47°54’25’’","65°18’01’’"),("48°06’18’’","64°36’00’’"),("48°12’03’’","64°36’00’’")],[("48°16’01’’","64°33’07’’"),("48°09’32’’","64°33’07’’"),("48°06’18’’","64°20’13’’"),("48°18’10’’","64°21’07’’")],[("48°27’36’’","63°48’39’’"),("48°07’04’’","64°00’00’’"),("48°07’04’’","63°45’00’’"),("48°27’36’’","63°25’15’’")],[("47°45’46’’","63°18’21’’"),("47°13’12’’","63°18’21’’"),("47°13’12’’","63°08’31’’"),("47°45’46’’","63°08’31’’")],[("47°35’27’’","62°34’04’’"),("47°01’00’’","62°38’13’’"),("47°01’00’’","62°26’20’’"),("47°35’27’’","62°25’55’’")]
#print(coordinates[0])# return liste of point
#print(coordinates[0][0]) # return pair (x,y)
#print (coordinates[0][0][0]) # return x or y

sud_coordinates = np.array(sud_coordinates)
zones = np.array(zones)

#inverser x & y de tous les points de la liste
new_sud_coordinates = np.array([])
polygone = np.array([])
for zone in sud_coordinates:
	for point in zone:
		latitude = point[1]
		longitude = point[0]
		point[0] = latitude
		point[1] = longitude
		polygone = np.append(polygone,point)
	new_sud_coordinates = np.append(new_sud_coordinates,polygone)
	polygone = np.array([])
sud_coordinates = np.array(new_sud_coordinates)
sud_coordinates = np.reshape(sud_coordinates,(20,2))
#print(len(sud_coordinates))


#convertir tous les points en degree decimal
coordinates = np.array([])
deg_coordinates = np.array([])
for coord in sud_coordinates:
	x = coord[0]
	y = coord[1]
	x,y = GGlib.sud2deg(x,y)
	x = GGlib.changer_direction(x)
	coordinate = np.array([x,y])
	deg_coordinates = np.append(deg_coordinates,coordinate)
deg_coordinates = np.reshape(deg_coordinates,(5,4,2))

#print(deg_coordinates)


acpg_zones = {}
# assembler les zone et les coordonées dans un dictionnaire
for i in range(len(zones)):
	acpg_zones.update({zones[i] : deg_coordinates[i]})


#print(acpg_zones)

#ecrire les polygons dans un fichier .shp
GGlib.ecriture_polygon_2shp(acpg_zones, "zone_de_peche_acpg.shp")
#print(acpg_zones)


