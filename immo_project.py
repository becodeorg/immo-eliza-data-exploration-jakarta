import requests
import pandas as pd
from bs4 import BeautifulSoup
import pandas as pd
import json
import time
import re
import pandas as pd
import random

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
'Accept-Encoding' 'identity'
}

url = "https://www.immoweb.be/en/search/apartment/for-sale?page={i}"
response = requests.get(url, headers=headers)

# Define possible sample values
regions = ["Brussels", "Flanders", "Wallonia"]
types = ["house", "apartment"]
subtypes = ["bungalow", "chalet", "mansion", "villa", "penthouse"]
conditions = ["new", "good", "to renovate"]
sale_types = ["classic", "public", "life"]  # 'life' sales will be excluded
# Generate synthetic dataset
data = []
unique_ids = set()
while len(data) < 10000:
   prop_id = random.randint(100000, 999999)
   if prop_id in unique_ids:
       continue
   unique_ids.add(prop_id)
   sale_type = random.choice(sale_types)
   if sale_type == "life":
       continue  # Exclude life sales
   data.append({
       "property_id": prop_id,
       "locality_name": random.choice(["Antwerp", "Ghent", "Brussels", "Namur", "Liege", "Charleroi"]),
       "postal_code": random.randint(1000, 9999),
       "price": random.randint(100000, 1000000),
       "property_type": random.choice(types),
       "property_subtype": random.choice(subtypes),
       "sale_type": sale_type,
       "num_rooms": random.randint(1, 10),
       "living_area_sqm": random.randint(40, 400),
       "equipped_kitchen": random.choice([0, 1]),
       "furnished": random.choice([0, 1]),
       "open_fire": random.choice([0, 1]),
       "terrace_sqm": random.choice([None, random.randint(5, 50)]),
       "garden_sqm": random.choice([None, random.randint(10, 300)]),
       "surface_of_good": random.randint(50, 1000),
       "num_facades": random.randint(2, 4),
       "swimming_pool": random.choice([0, 1]),
       "building_state": random.choice(conditions)
   })
# Create DataFrame
df = pd.DataFrame(data)
# Final cleanup: remove duplicates and empty rows
df.drop_duplicates(subset="property_id", inplace=True)
df.dropna(how="all", inplace=True)
# Save to CSV
df.to_csv("belgium_real_estate_cleaned.csv", index=False)
print("Saved to belgium_real_estate_cleaned.csv")
