#This program will create a nested dictionary describing a city and several
#Attributes to accompany it

Cities =  {
                  'Los Angeles':{
                   'Population': '3,792,621',
                        'State': 'California',
                        'Area': '468.67 sq mi',
                        },
                   
                   'Pittsburgh':{
                    'Population': '305,704',
                         'State': 'Pennsylvania',
                          'Area': '58.34 sq mi'
                         },

                      'Houston':{
                     'Population': '2,099,451',
                         'State': 'Texas',
                          'Area':  '637.4 sq mi'
                         }

          }

for city, stats in Cities.items():
    
    print(f"Here are the states for the City of {city}")
    pop = stats['Population']
    sta = stats['State']
    are = stats['Area']

    Metrics = [pop, sta, are]

    for k in Metrics:
        print(f"{k}\n")














