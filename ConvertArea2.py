''' ConvertArea2.py
convert units of area using a dictionary
this minimizes the total number of conversion factors


works with LinuxMint and Spyder IDE  dns(vegaseat)  15jun2026
'''

"""
curious word origins:
one acre was approximately the amount of land tillable in
one day by one man behind the plow pulled by one ox
"""

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
        print( " %f %s = %0.12f %s" % (x, unit1, outcome, unit2) )
    else:
        print( " There was an error, check spelling of unit" )
        print("unit1 = {}  unit2 = {}".format(unit1, unit2))
        print("allowed units:")
        print(area_dict.keys())

# this is the area conversion dictionary ...
# (note that units won't appear in that order)
area_dict = {}
# the conversion factors are all relative to 'sqmeter' (factor = 1.0)
# to convert sqmeters to any other area unit multiply by its factor
# to convert any other area unit to sqmeter divide by its factor
# to convert any area unit to any of the other area units
# go in two steps using sqmeter as a temporary
area_dict['sqmeter']      = 1.0
area_dict['sqmillimeter'] = 1000000.0
area_dict['sqcentimeter'] = 10000.0
area_dict['sqkilometer']  = 0.000001
area_dict['hectare']      = 0.0001
area_dict['sqinch']       = 1550.003
area_dict['sqfoot']       = 10.76391
area_dict['sqyard']       = 1.19599
area_dict['acre']         = 0.0002471054
area_dict['sqmile']       = 0.0000003861022

# test1: x square-meter have how many square-centimeter?
x = 1.0
unit1 = 'sqmeter'
unit2 = 'sqcentimeter'
outcome = convert_units(x, unit1, unit2, area_dict)
show_result(outcome, unit1, unit2)

# test2: x square-miles have how many acres?
x = 1.0
unit1 = 'sqmile'
unit2 = 'acre'
outcome = convert_units(x, unit1, unit2, area_dict)
show_result(outcome, unit1, unit2)

# test2a: x acres are how many square-miles
# Tamarack California/Nevada fire jul/aug2021
x = 69000.0
unit1 = 'acre'
unit2 = 'sqmile'
outcome = convert_units(x, unit1, unit2, area_dict)
show_result(outcome, unit1, unit2)
# 107.8 sqmile

# test2b: x acres are how many square-miles
# Dixie California fire 01aug2021
x = 250000.0
unit1 = 'acre'
unit2 = 'sqmile'
outcome = convert_units(x, unit1, unit2, area_dict)
show_result(outcome, unit1, unit2)
# 390.6 sqmile

# test3: x square-miles have how many hectares?
x = 1.0
unit1 = 'sqmile'
unit2 = 'hectare'
outcome = convert_units(x, unit1, unit2, area_dict)
show_result(outcome, unit1, unit2)

# test4: x acres have how many hectares?
x = 1.0
unit1 = 'acre'
unit2 = 'hectare'
outcome = convert_units(x, unit1, unit2, area_dict)
show_result(outcome, unit1, unit2)


# test5 to force an error, misspelled unit acre
unit1 = 'hectare'
unit2 = 'acres'
outcome = convert_units(x, unit1, unit2, area_dict)
show_result(outcome, unit1, unit2)


''' original Delphi code from dns
// area_conversion_pas.txt

  if (en = 2) then
  begin                { sq meter }
    case (re) of
      0  : cf := 1000000.0;        { sq millimeter }
      1  : cf := 10000.0;          { sq centimeter }
      2  : cf := 1.0;              { sq meter }
      3  : cf := 0.000001;         { sq kilometer }
      4  : cf := 0.0001;           { hectare }
      5  : cf := 1550.003;         { sq inch }
      6  : cf := 10.76391;         { sq foot }
      7  : cf := 1.19599;          { sq yard }
      8  : cf := 0.0002471054;     { acre }
      9  : cf := 0.0000003861022;  { sq mile }
      else
        cf := 1.0;
    end;
  end;
'''