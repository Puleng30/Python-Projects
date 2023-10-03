
import xml.etree.ElementTree as ET

#loading the XML file
tree = ET.parse('movie.xml')
root = tree.getroot()

#initializing counters
favorite_count = 0
not_favorite_count = 0

#iterating over the movie elements and print descriptions
for movie in root.iter('movie'):
    description = ''.join(movie.find('description').itertext())
    print("Movie Description:", description)

    #code to check if the movie is a favorite or not
    favorite = movie.get('favorite')
    if favorite.lower() == 'true':
        favorite_count += 1
    else:
        not_favorite_count += 1

#printing the count of favorite and not favorite movies
print("Total number of favourite movies:", favorite_count)
print("Total number of disliked movies:", not_favorite_count)
