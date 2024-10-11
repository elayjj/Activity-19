restaurant = [
  {"name" : "Vikings Luxury Buffet", "location" : "Pasay City", "ID" : 1, "cuisine type" : "Buffet", "established year" : 2011, "website" : "www.vikings.ph"},
  {"name" : "Antonio's Restaurant", "location" : "Tagaytay", "ID" : 2, "cuisine type" : "Fine Dining", "established year" : 2002, "website" : "www.antoniosrestaurant.ph"},
  {"name" : "Mesa Filipino Moderne", "location" : "Makati City", "ID" : 3, "cuisine type" : "Filipino", "established year" : 2009, "website" : "www.mesa.ph"},
  {"name" : "Manam Comfort Filipino", "location" : "Quezon City", "ID" : 4, "cuisine type" : "Filipino", "established year" : 2013, "website" : "www.manam.ph"},
  {"name" : "Ramen Nagi", "location" : "Various Locations", "ID" : 5, "cuisine type" : "Japanese", "established year" : 2013, "website" : "www.ramennagi.com.ph"}
]

for restaurant in restaurant:

   print(f"name: {restaurant['name']}, location: {restaurant['location']}, ID: {restaurant['ID']}, cuisine type: {restaurant['cuisine type']}, established year: {restaurant['established year']}, website: {restaurant['website']},")