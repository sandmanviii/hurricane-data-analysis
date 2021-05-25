# -*- coding: utf-8 -*-
"""
Created on Tue May 25 15:11:28 2021

@author: Corey.Sanders
"""

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
def update_damages(damages, conversion):
  damages_update = []
  for value in range(len(damages)):
    if damages[value] == "Damages not recorded":
      damages_update.append(damages[value])
    elif "M" in damages[value]:
      parsed_val = damages[value].strip("M")
      float_val = float(parsed_val)
      damages_update.append(float_val * conversion['M'])
    elif "B" in damages[value]:
      parsed_val = damages[value].strip("B")
      float_val = float(parsed_val)
      damages_update.append(float_val * conversion['B'])
    else:
      print("Invalid Entry")
      continue
  return damages_update

updated_damages_list = update_damages(damages, conversion)
print("Converted damages to useable values: {}".format(updated_damages_list))
# 2 
# Create a Table
def table_creation(names, months, years, max_sustained_winds, areas_affected, deaths, updated_damages_list):
  combined_table = {}
  for index in range(len(names)):
    value_dict = {"Name": names[index], "Month": months[index], "Year": years[index], "Max Sustained Wind": max_sustained_winds[index], "Areas Affected": areas_affected[index], "Damage": updated_damages_list[index], "Death": deaths[index]}
    

    combined_table.update({names[index]: value_dict})

  return combined_table
# Create and view the hurricanes dictionary
hurricanes_dict = table_creation(names, months, years, max_sustained_winds, areas_affected, deaths, updated_damages_list)
print("Hurricane Dictionary: {}".format(hurricanes_dict))
# 3
# Organizing by Year
def organized_year(hurricane):
  hurricanes_year = {}
  lst = []
  for value in hurricane.values():
    current_year = value["Year"]
    if current_year not in lst:
      lst.append(current_year)
  for i in lst:
    hurricane_year = {i : []}
    hurricanes_year.update(hurricane_year)
  for i in hurricanes_year:
    for value in hurricane.values():
      if  i == value["Year"]:
        hurricanes_year[i].append(value)
  return hurricanes_year

# create a new dictionary of hurricanes with year and key
hurricanes_by_year = organized_year(hurricanes_dict)
print("Hurricanes indexed by year: {}".format(hurricanes_by_year))

# 4
# Counting Damaged Areas
def count_areas(areas_affected):
  locations = {}
  for region in areas_affected:
    for country in region:
      if country not in locations.keys():
        locations.update({country: 0})
  for key in locations.keys():
    count = 0
    for i in areas_affected:
      for y in i:
        if key == y:
          count += 1
    locations[key] = count
  return locations



    
# create dictionary of areas to store the number of hurricanes involved in
areas_affected_count = count_areas(areas_affected)
print("Data of areas affected paired with count of hurricanes: {}".format(areas_affected_count))
#print(areas_affected_count)
# 5 
# Calculating Maximum Hurricane Count
def max_hit_count(areas_affected_count):
  max_key = max(areas_affected_count, key=areas_affected_count.get)
  max_val = areas_affected_count[max_key]
  return max_key, max_val

  
highest_area, hit_count = max_hit_count(areas_affected_count)
print("The area with the highest number of hurricanes is {} with a total of {} hurricanes.".format(highest_area, hit_count))

# find most frequently affected area and the number of hurricanes involved in
def highest_deaths(hurricanes_dict):
  return_val = {}
  max_deaths = 0
  for item in hurricanes_dict.values():
    if max_deaths < item["Death"]:
      max_deaths = item["Death"]
      return_val = item["Name"]
  return return_val, max_deaths

# 6
# Calculating the Deadliest Hurricane
max_death_hurricane, death_count = highest_deaths(hurricanes_dict)
print("The hurricane with the most deaths is {} with {} deaths.".format(max_death_hurricane,death_count))
#print(max_death_count)


# find highest mortality hurricane and the number of deaths
def mortality_ranking(hurricanes_dict):
  mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
  updated_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  for item in hurricanes_dict.values():
    if item["Death"] == 0:
      updated_dict[0].append(item)
    elif item["Death"] <= 100 and item["Death"] > 0:
      updated_dict[1].append(item)
    elif item["Death"] <= 500 and item["Death"] > 100:
      updated_dict[2].append(item)
    elif item["Death"] <= 1000 and item["Death"] > 500:
      updated_dict[3].append(item)
    elif item["Death"] <= 10000 and item["Death"] > 1000:
      updated_dict[4].append(item)
    else:
      updated_dict[5].append(item)
  return updated_dict

mortality_dict = mortality_ranking(hurricanes_dict)
print("The hurricanes ranked by mortality: {}".format(mortality_dict))
              
  
# 7
# Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key


# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
def costly_hurricane(hurricanes_dict):
  max_cost = 0
  hurricane_name = ""
  for item in hurricanes_dict.values():
    if item["Damage"] == "Damages not recorded":
      continue
    if item["Damage"] > max_cost:
      max_cost = item["Damage"]
      hurricane_name = item["Name"]
  return hurricane_name, max_cost

hurricane_name, max_cost = costly_hurricane(hurricanes_dict)
print("The hurricane with the higest cost in damage is {} with {} dollars worth of damages".format(hurricane_name, max_cost))
# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
def damage_rating(hurricanes_dict):
  scale = {0: [], 1: [], 2:[], 3:[], 4:[], 5:[]}
  for item in hurricanes_dict.values():
    if item["Damage"] == "Damages not recorded":
      continue
    elif item["Damage"] == 0:
      scale[0].append(item)
    elif item["Damage"] <= 100000000 and item["Damage"] > 0:
      scale[1].append(item)
    elif item["Damage"] <= 1000000000 and item["Damage"] > 100000000:
      scale[2].append(item)
    elif item["Damage"] <= 10000000000 and item["Damage"] > 1000000000:
      scale[3].append(item)
    elif item["Damage"] <= 50000000000 and item["Damage"] > 10000000000:
      scale[4].append(item)
    else:
      scale[5].append(item)
  return scale

damage_rating_dict = damage_rating(hurricanes_dict)
print("Hurricanes rated by damage: {}".format(damage_rating_dict))

  
# categorize hurricanes in new dictionary with damage severity as key
