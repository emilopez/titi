import json
fn = 'points.json'
with open(fn) as json_data:
    dat = json.load(json_data)

#imprimir estructura
#print json.dumps(dat, sort_keys=True, indent=2)

'''
///json datafile example///
{
  "points":[
      {"name":"Santo Domingo", "lat":-31.117368, "lon":-60.883001},
      {"name":"Ataliva", "lat":-30.999324, "lon":-61.428412},
      {"name":"C. Vignaud", "lat":-30.838923, "lon":-61.960477}
  ]
}
'''
for po in dat['points']:
    print po['name'], po['lat'], po['lon']