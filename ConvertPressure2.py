''' ConvertPressure2.py
convert units of pressure using a dictionary
this minimizes the total number of conversion factors

  
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
        print(pressure_dict.keys())

# this is the pressure conversion dictionary ...
# (note that units won't appear in that order)
pressure_dict ={}
# all scale factors are relative to unit 'atm' (factor = 1.0)
# to convert 'atm' to any other weight unit multiply by its factor
# to convert any other pressure unit to 'atm' divide by its factor
# to convert any pressure unit to any of the other pressure units
# go in two steps using 'atm' as a temporary

pressure_dict['atm'] = 1.0
pressure_dict['bar'] = 1.01325
pressure_dict['kilopascal'] = 101.325
pressure_dict['torr'] = 760.0
# note: a torr is 1 mm of Hg
pressure_dict['kg/sqcm'] = 1.033227
pressure_dict['kg/sqm'] = 10332.27
pressure_dict['lb/sqinch'] = 14.69595
pressure_dict['ton_short/sqfoot'] = 1.058108
pressure_dict['inch of Hg'] = 29.92126
pressure_dict['foot of water'] = 33.89854

# test1: x atm has how many torr?
x = 1.0
unit1 = 'atm'
unit2 = 'torr'
outcome = convert_units(x, unit1, unit2, pressure_dict)
show_result(outcome, unit1, unit2)

# test2: x atm has how many kilopascal?
x = 0.1
unit1 = 'atm'
unit2 = 'kilopascal'
outcome = convert_units(x, unit1, unit2, pressure_dict)
show_result(outcome, unit1, unit2)

# test3: x kg/sqcm has how many lb/sqinch?
x = 1.0
unit1 = 'kg/sqcm'
unit2 = 'lb/sqinch'
outcome = convert_units(x, unit1, unit2, pressure_dict)
show_result(outcome, unit1, unit2)


# test4 to force an error, misspelled unit 'atms'
x = 1.0
unit1 = 'atms'
unit2 = 'foot of water'
outcome = convert_units(x, unit1, unit2, pressure_dict)
show_result(outcome, unit1, unit2)

''' original delphi code from dns
// pressure_conversion_pas.txt

  if (en = 0) then
  begin                { atm }
    case (re) of
      0  : cf := 1.0;        { atm }
      1  : cf := 1.01325;    { bar }
      2  : cf := 101.325;    { kilopascal }
      3  : cf := 760;        { torr }
      4  : cf := 1.033227;   { kg/sqcm }
      5  : cf := 10332.27;   { kg/sqm }
      6  : cf := 14.69595;   { lb/sqinch }
      7  : cf := 1.058108;   { ton(sh)/sqfoot }
      8  : cf := 29.92126;   { inch of Hg }
      9  : cf := 33.89854;   { foot of water }
      else
        cf := 1.0;
    end;
  end;
'''