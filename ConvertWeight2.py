''' ConvertWeight2.py
convert units of weight using a dictionary
this minimizes the total number of conversion factors
  

works with LinuxMint and Spyder IDE  dns(vegaseat)  15jun2026
'''

'''
courious fact
The Earth's weight is 5,972,000,000,000,000,000,000 Metric Tons
The Earth gains between 100 and 1,000 tons from space dust each day
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
        print(weight_dict.keys())

# this is the weight conversion dictionary ...
# (note that units won't appear in that order)
weight_dict ={}
# all scale factors are relative to unit 'kilogram' (factor = 1.0)
# to convert 'kilogram' to any other distance unit multiply by its factor
# to convert any other weight unit to 'kilogram' divide by its factor
# to convert any weight unit to any of the other weight units
# go in two steps using 'kilogram' as a temporary

weight_dict['kilogram'] = 1.0
weight_dict['gram'] = 1000.0
weight_dict['milligram'] = 1000000.0
weight_dict['microgram'] = 1000000000.0
weight_dict['tonne_metric'] = 0.001
weight_dict['dram'] = 564.38339
weight_dict['grain'] = 15432.358
weight_dict['ounce'] = 35.273962
weight_dict['pound'] = 2.2046226
weight_dict['ton_short'] = 0.0011023113

# test1: x kilogram has how many pound?
x = 1.0
unit1 = 'kilogram'
unit2 = 'pound'
outcome = convert_units(x, unit1, unit2, weight_dict)
show_result(outcome, unit1, unit2)

# test2: x pound has how many ounce?
x = 1.0
unit1 = 'pound'
unit2 = 'ounce'
outcome = convert_units(x, unit1, unit2, weight_dict)
show_result(outcome, unit1, unit2)

# test3: x kilogram has how many ounce?
x = 1.0
unit1 = 'kilogram'
unit2 = 'ounce'
outcome = convert_units(x, unit1, unit2, weight_dict)
show_result(outcome, unit1, unit2)

# test4: x metric tonne has how many kilogram?
x = 1.120
unit1 = 'tonne_metric'
unit2 = 'kilogram'
outcome = convert_units(x, unit1, unit2, weight_dict)
show_result(outcome, unit1, unit2)

# test5 to force an error, misspelled unit 'grams'
x = 1.0
unit1 = 'grams'
unit2 = 'milligram'
outcome = convert_units(x, unit1, unit2, weight_dict)
show_result(outcome, unit1, unit2)

''' original delphi code from dns
// weight_conversion_pas.txt

  if (en = 3) then
  begin                       { kilogram }
    case (re) of
      0  : cf := 1000000000.0;  { microgram }
      1  : cf := 1000000.0;     { milligram }
      2  : cf := 1000.0;        { gram }
      3  : cf := 1.0;           { kilogram }
      4  : cf := 0.001;         { tonne (metric) }
      5  : cf := 564.38339;     { dram (avd) }
      6  : cf := 15432.358;     { grain }
      7  : cf := 35.273962;     { ounce (avd) }
      8  : cf := 2.2046226;     { pound (avd) }
      9  : cf := 0.0011023113;  { ton (short) }
      else
        cf := 1.0;
    end;
  end;
'''