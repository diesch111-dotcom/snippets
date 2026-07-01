''' ConvertVolume2.py
convert units of volume using a dictionary
this minimizes the total number of conversion factors

1 pint contains 16 fluid-ounces

check on volume acrefoot (an acre one foot deep)
one acre-foot = 325851.427 gallons = 1233482.076072 liters


works with LinuxMint and Spyder IDE  dns(vegaseat)  15jun2026
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
        print( " %f %s = %0.12f %s" % (x, unit1, outcome, unit2) )
    else:
        print( " This example had an error, check spelling of unit" )
        print("unit1 = {}  unit2 = {}".format(unit1, unit2))
        print("allowed units:")
        print(volume_dict.keys())

# this is the volume conversion dictionary ...
# (note that units won't appear in that order)
volume_dict ={}
# all scale factors are relative to unit 'liter' (factor = 1.0)
# to convert 'liter' to any other volume unit multiply by its factor
# to convert any other volume unit to 'liter' divide by its factor
# to convert any volume unit to any of the other volume units
# go in two steps using 'liter' as a temporary

volume_dict['liter'] = 1.0
volume_dict['microliter'] = 1000000.0
volume_dict['milliliter'] = 1000.0
volume_dict['cubiccentimeter'] = 1000.0
volume_dict['cubicmeter'] = 0.001
# US volumes
volume_dict['pint'] = 2.113376
volume_dict['quart'] = 1.056688
volume_dict['gallon'] = 0.264172
volume_dict['cubicinch'] = 61.02374
volume_dict['cubicfoot'] = 0.03531467
volume_dict['cubicyard'] = 0.001307951
volume_dict['acrefoot'] = 8.107130370183252e-07

# test1: x liter has how many quart?
x = 1.0
unit1 = 'liter'
unit2 = 'quart'
outcome = convert_units(x, unit1, unit2, volume_dict)
show_result(outcome, unit1, unit2)

# test2: x liter has how many cubicinch?
x = 1.0
unit1 = 'liter'
unit2 = 'cubicinch'
outcome = convert_units(x, unit1, unit2, volume_dict)
show_result(outcome, unit1, unit2)

# test3: x pint has how many milliliter?
x = 1.0
unit1 = 'pint'
unit2 = 'milliliter'
outcome = convert_units(x, unit1, unit2, volume_dict)
show_result(outcome, unit1, unit2)

# test4: x gallon has how many liter
x = 1.0
unit1 = 'gallon'
unit2 = 'liter'
outcome = convert_units(x, unit1, unit2, volume_dict)
show_result(outcome, unit1, unit2)

# test5: x acrefoot have how many liter?
x = 1.0
unit1 = 'acrefoot'
unit2 = 'liter'
outcome = convert_units(x, unit1, unit2, volume_dict)
show_result(outcome, unit1, unit2)

# test6 to force an error, misspelled unit 'gallon'
x = 1.0
unit1 = 'gallons'
unit2 = 'liter'
outcome = convert_units(x, unit1, unit2, volume_dict)
show_result(outcome, unit1, unit2)

print("1 acre-foot = 325851.427 gallons = %f liters" % (325851.427*3.785412534258))
print(1/1233482.076072)

''' original delphi code from dns
// volume_conversion_pas.txt

  if (en = 2) then
  begin                   { liter }
    case (re) of
      0  : cf := 1000000.0;    { microliter }
      1  : cf := 1000.0;       { milliliter }
      2  : cf := 1.0;          { liter }
      3  : cf := 0.001;        { cubic meter }
      4  : cf := 2.113376;     { pint(US) }
      5  : cf := 1.056688;     { quart(US) }
      6  : cf := 0.264172;     { gallon(US) }
      7  : cf := 61.02374;     { cubic inch }
      8  : cf := 0.03531467;   { cubic foot }
      9  : cf := 0.001307951;  { cubic yard }
      else
        cf := 1.0;
    end;
  end;
'''
