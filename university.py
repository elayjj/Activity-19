university = [
  {"name" : "University of the Philippines", "location" : "Quezon City", "ID" : 1, "established year" : 1908, "type" : "Public", "website" : "www.up.edu.ph"},
  {"name" : "Ateneo de Manila University", "location" : "Quezon City", "ID" : 2, "established year" : 1859, "type" : "Private", "website" : "www.ateneo.edu"},
  {"name" : "De La Salle University", "location" : "Manila", "ID" : 3, "established year" : 1911, "type" : "Private", "website" : "www.dlsu.edu.ph"},
  {"name" : "University of Santo Tomas", "location" : "Manila", "ID" : 3, "established year" : 1611, "type" : "Private", "website" : "www.ust.edu.ph"},
  {"name" : "Polytechnic University of the Philippines", "location" : "Manila", "ID" : 5, "established year" : 1904, "type" : "Private", "website" : "www.pup.edu.ph"}
]

for university in university:

    print(f"name: {university['name']}, location: {university['location']}, ID: {university['ID']}, established year: {university['established year']}, type: {university['type']}, website: {university['website']},")