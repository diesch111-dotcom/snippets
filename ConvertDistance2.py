''' ConvertDistance2.py
convert units of distance using a dictionary
this minimizes the total number of conversion factors


works with LinuxMint and Spyder IDE  dns(vegaseat)  15jun2026
'''

'''
curious fact
the average distance to the Moon is 384,403 km (238,857 miles)
'''

def convert_units(x, unit1, unit2, conv_dict):
    """
    unit conversion with optional error trapping
    the units have to be keys in the given conversion dictionary
    """
    if (unit1 in conv_dict) and (unit2 in conv_dict):
        factor1 = conv_dict[unit1]
        factor2 = conv_dict[unit2]
        return factor2*x/factor1
    else:
        return False

def show_result(outcome, unit1, unit2):
    if outcome:
        print( " %f %s = %f %s" % (x, unit1, outcome, unit2) )
    else:
        print( " This example had an error, check spelling of unit" )
        print("unit1 = {}  unit2 = {}".format(unit1, unit2))
        print("allowed units:")
        print(dist_dict.keys())

# this is the distance conversion dictionary ...
# (note that units won't appear in that order)
dist_dict ={}
# all scale factors are relative to unit 'meter' (factor = 1.0)
# to convert 'meter' to any other distance unit multiply by its factor
# to convert any other distance unit to 'meter' divide by its factor
# to convert any distance unit to any of the other distance units
# go in two steps using 'meter' as a temporary

dist_dict['meter'] = 1.0
dist_dict['micron'] = 1000000.0
dist_dict['millimeter'] = 1000.0
dist_dict['centimeter'] = 100.0
dist_dict['kilometer'] = 0.001
dist_dict['inch'] = 100.0/2.54
dist_dict['foot'] = 100.0/30.48
dist_dict['yard'] = 100.0/91.44
dist_dict['mile'] = 0.001/1.609344
dist_dict['rod'] = 1.0/5.029

# test1: x meter has how many centimeter?
x = 1.0
unit1 = 'meter'
unit2 = 'centimeter'
outcome = convert_units(x, unit1, unit2, dist_dict)
show_result(outcome, unit1, unit2)

# test2: x mile has how many foot (feet)?
x = 1.0
unit1 = 'mile'
unit2 = 'kilometer'
outcome = convert_units(x, unit1, unit2, dist_dict)
show_result(outcome, unit1, unit2)

# test2a: x km has how miles?
x = 19.0
unit1 = 'kilometer'
unit2 = 'mile'
outcome = convert_units(x, unit1, unit2, dist_dict)
show_result(outcome, unit1, unit2)

# test3: x yard has how many rod?
x = 1.0
unit1 = 'yard'
unit2 = 'rod'
outcome = convert_units(x, unit1, unit2, dist_dict)
show_result(outcome, unit1, unit2)


# test4 to force an error, misspelled unit 'inch'
x = 1.0
unit1 = 'inchs'
unit2 = 'centimeter'
outcome = convert_units(x, unit1, unit2, dist_dict)
show_result(outcome, unit1, unit2)

''' original Delphi code from dns
// distance_conversion_pas.txt

  if (en = 3) then
  begin                      { meter }
    case (re) of
      0  : cf := 1000000.0;    { micron }
      1  : cf := 1000.0;       { millimeter }
      2  : cf := 100.0;        { centimeter }
      3  : cf := 1.0;          { meter }
      4  : cf := 0.001;        { kilometer }
      5  : cf := 100.0/2.54;   { inch }
      6  : cf := 100.0/30.48;  { foot }
      7  : cf := 100.0/91.44;  { yard }
      8  : cf := 0.001/1.609344;  { mile }
      9  : cf := 1.0/5.029;    { rod }
    else
      cf := 1.0;
    end;
  end;
'''