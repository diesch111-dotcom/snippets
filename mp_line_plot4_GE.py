''' mp_line_plot4_GE.py

here we use a list of y values (prices) and a matching list of x values 
(days) for:
plt.plot(x, y [, color, marker, size, linewidth, linestyle])

'GE_price_list' created by dns program 'Allport_data_GE1.py' from 
information (a csv file) from yahoo.finance

one may save plot as file  'GE_day_val_2026Q1Q2.png'

used LinuxMint with Spyder IDE (has MatPLotLib included + science stuff)
dns (vegaseat)  03jul2026
'''

import matplotlib.pyplot as plt


# GE aerospace first half of 2026 (most of the listed days)
GE_price_list = [
320.75, 324.32, 327.54, 323.64, 314.4, 321.59, 324.17, 327.23, 
318.88, 319.86, 295.06, 297.47, 292.48, 298.86, 306.79, 308.71, 
309.93, 308.355, 306.22, 321.0, 316.74, 316.33, 313.81, 312.89, 
315.34, 327.08, 329.58, 334.6, 343.22, 338.99, 345.64, 342.89, 
340.84, 342.26, 345.74, 334.14, 339.77, 327.03, 323.11, 321.93, 
326.52, 325.11, 306.7, 304.0, 302.09, 300.96, 291.61, 286.79, 
291.54, 290.63, 296.56, 285.24, 282.81, 273.26, 283.74, 292.68, 
281.16, 288.69, 288.7, 308.1, 313.02, 308.35, 311.9, 318.0, 
313.93, 298.29, 304.17, 303.6, 286.73, 276.29, 282.34, 284.6, 
284.57, 289.2, 283.57, 289.93, 286.51, 280.52, 286.68, 305.815, 
302.63, 297.15, 300.77, 297.61, 294.71, 291.54, 281.53, 285.99, 
285.28, 300.17, 301.76, 302.84, 314.49, 317.21, 320.82, 323.76, 
324.675, 317.72, 314.64, 327.7, 328.0, 322.06, 330.44, 318.71, 
332.8, 335.3, 342.26, 351.73, 357.03, 357.72, 355.12, 356.47, 
365.88, 371.36, 373.71, 373.73, 
 ]


day_list = list(range(1, len(GE_price_list)+1))

# default is a line plot
# use color='red' or 'r' a linewidth lw=2 (pixels) and
# linestyle ls='--' or ls='dashed'
#plt.plot(day_list, GE_price_list, c='r', lw=2, ls='--')
# color and linestyle can be combined to 'r--'
plt.plot(day_list, GE_price_list, 'r--', lw=2)
# add some additional info
plt.ylabel('GE prices')
plt.xlabel('days')
plt.title('GE prices jan to jun 2026')
#plt.grid()
plt.show()

# right click on the plot picture and select 'safe plot as...'
