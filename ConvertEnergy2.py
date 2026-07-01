''' ConvertEnergy2.py
convert units of energy using a dictionary
this minimizes the total number of conversion factors

calories listed on food labels are Calories (kilocalories) big C
it takes 1 calorie to heat 1 milliliter of water by 1 degree Celcius


works with LinuxMint and Spyder IDE  dns(vegaseat)  15jun2026
'''

'''
curious fact
173,000 trillion watts of solar power strikes the Earth continuously
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
        print( " There was an error, check spelling of unit" )
        print("unit1 = {}  unit2 = {}".format(unit1, unit2))
        print("allowed units:")
        print(energy_dict.keys())

# this is the energy conversion dictionary ...
# (note that units won't appear in that order)
energy_dict ={}
# all scale factors are relative to unit 'calorie' (factor = 1.0)
# to convert 'calorie' to any other energy unit multiply by its factor
# to convert any other energy unit to 'calorie' divide by its factor
# to convert any energy unit to any of the other energy units
# go in two steps using 'calorie' as a temporary

energy_dict['calorie'] = 1.0
energy_dict['kilocalorie'] = 0.001
# one joule is equal to one watt-second
energy_dict['joule'] = 4.1868
energy_dict['watt-second'] = 4.1868
energy_dict['watt-hour'] = 0.001163
energy_dict['kilowatt-hour'] = 0.000001163
energy_dict['liter-atmosphere'] = 0.0413205
energy_dict['horsepower-hour(metric)'] = 0.00000158124
energy_dict['erg'] = 4186800.0
energy_dict['btu'] = 0.00396832

# test1: x kilowatt-hour has how many btu?
x = 1.0
unit1 = 'kilowatt-hour'
unit2 = 'btu'
outcome = convert_units(x, unit1, unit2, energy_dict)
show_result(outcome, unit1, unit2)

# test2: x kilowatt-hour has how many calorie?
x = 1.0
unit1 = 'kilowatt-hour'
unit2 = 'calorie'
outcome = convert_units(x, unit1, unit2, energy_dict)
show_result(outcome, unit1, unit2)

# test3: x erg has how many joule?
x = 1.0
unit1 = 'erg'
unit2 = 'joule'
outcome = convert_units(x, unit1, unit2, energy_dict)
show_result(outcome, unit1, unit2)

# watch out that the result does not get too small!
# test4: x erg has how many kilocalorie?
#x = 1000000.0
x = 1.0
unit1 = 'erg'
unit2 = 'kilocalorie'
outcome = convert_units(x, unit1, unit2, energy_dict)
show_result(outcome, unit1, unit2)


# test5 to force an error, misspelled unit 'erg'
x = 1.0
unit1 = 'joule'
unit2 = 'ergs'
outcome = convert_units(x, unit1, unit2, energy_dict)
show_result(outcome, unit1, unit2)

''' original delphi code from dns
// energy_conversion.pas

if (en = 0) then
  begin                { calorie }
    case (re) of
      0  : cf := 1.0;              { calorie }
      1  : cf := 0.001;            { kilocalorie }
      2  : cf := 4.1868;           { joule or watt-second }
      3  : cf := 0.001163;         { watt-hour }
      4  : cf := 0.000001163;      { kilowatt-hour }
      5  : cf := 0.0413205;        { liter-atmosphere }
      6  : cf := 0.00000158124;    { horsepower-hour metric }
      7  : cf := 4186800;          { erg }
      8  : cf := 0.00396832;       { btu }
      else
        cf := 1.0;
    end;
  end;
'''