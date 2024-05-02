import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import prince
# import seaborn as sns
# import statsmodels as sm
# import sys
pd.options.display.max_columns = 20
pd.options.display.max_rows = 20
pd.options.display.max_colwidth = 80
np.set_printoptions(precision=4, suppress=True)


trData = pd.ExcelFile ('SP-Transcribed_Data.xlsx')
#running avg of graph for past 5 years then +/- range to see if following year differs from that
def SigYrsColors(sigYrs):
    # coloring the bar graph where yellow indicates a "signifcant" decline in sharks caught compared to
    # historical data and red indicates a "significant" increase in sharks caught
    colors = []
    for loop in range (0,50,1):
        colors.append ('blue')
    for k in sigYrs:
        if sigYrs [k] [1] == 'below':
            colors [k] = 'yellow'
        elif sigYrs [k] [1] == 'above':
            colors [k] = 'red'
    return colors
def FindSigYrs (sheetName, dataColName, indexColName):
    caughtSheet = pd.read_excel (trData, sheetName)
    sharksCaughtData = caughtSheet [[dataColName]].to_numpy ().flatten ()
    sharksCaughtIndex = caughtSheet [[indexColName]].to_numpy ().flatten ()
    dataSeries = pd.Series (sharksCaughtData, sharksCaughtIndex)
    sigYrs = {}
    runningAvgs = np.array ([])
    runningErrors = np.array ([0,0,0,0,0,0])
    for i in range (0, sharksCaughtData.size - 6, 1):
        runningTotal = 0
        for j in range (i, i + 5, 1):
            runningTotal += sharksCaughtData [j]
        runningAvg = runningTotal / 5
        runningAvgs = np.append (runningAvgs, runningAvg)
        runningErrors = np.append (runningErrors, runningAvg * 0.3)
        if sharksCaughtData [i + 6] < runningAvg * 0.7:
            sigYrs [i + 6] = [sharksCaughtIndex [i + 6],'below']
        elif sharksCaughtData [i + 6] > runningAvg * 1.3:
            sigYrs [i + 6] = [sharksCaughtIndex [i + 6],'above']
    runningAvgsSeries = pd.Series (runningAvgs, sharksCaughtIndex [6:])
    return sigYrs, dataSeries, runningAvgsSeries, runningErrors

plt.ylim (0,40) #general graphs
# plt.ylim (0,30) #running avg graphs

# NSW Shark Control Program - Sharks Caught (p. 52)
# NSWSignificantYears, NSWSeries, NSWRunningAvgsSeries, NSWRunningErrors = FindSigYrs ('NSW_Catch', 'NSW_Sharks_Caught', 'Year')
# print (NSWSignificantYears)
# NSWColors = SigYrsColors (NSWSignificantYears)

# significant plot
# NSWSharksCaughtPlot = NSWSeries.plot (xlabel = 'Year', ylabel = 'Numbers of White Sharks Caught', kind = 'bar', color = NSWColors, title = 'Total numbers of white sharks caught in the NSW shark control program 1950 – 2000 (data supplied by NSW Fisheries)')
# plt.show ()

# " with error bars
# NSWSharksCaughtPlotErrors = NSWSeries.plot (xlabel = 'Year', ylabel = 'Numbers of White Sharks Caught', yerr = NSWRunningErrors, kind = 'bar', color = NSWColors, title = 'Total numbers of white sharks caught in the NSW shark control program 1950 – 2000 (data supplied by NSW Fisheries)')
# plt.show ()

# running avgs plot
# NSWRunningAvgsPlot = NSWRunningAvgsSeries.plot (xlabel = 'Year', ylabel = 'Average Number of White Sharks Caught', kind = 'bar', color = NSWColors [6:], title = 'Running averages of white sharks caught in the NSW shark control program 1950 – 2000 (data supplied by NSW Fisheries)')
# plt.show ()


# QLD Shark Control Program - Sharks Caught (p. 53)
# QLDSignificantYears, QLDSeries, QLDRunningAvgsSeries, QLDRunningErrors = FindSigYrs ('QLD_Catch', 'QLD_Sharks_Caught', 'Year')
# print (QLDSignificantYears)
# QLDColors = SigYrsColors (QLDSignificantYears)

# significant plot
# QLDSharksCaughtPlot = QLDSeries.plot (xlabel = 'Year', ylabel = 'Numbers of White Sharks Caught', kind = 'bar', color = QLDColors, title = 'Total numbers of white sharks caught in the Qld shark control program 1962 – 1998 (data supplied by QDPI)')
# plt.show ()

# " with error bars
# QLDSharksCaughtPlotErrors = QLDSeries.plot (xlabel = 'Year', ylabel = 'Numbers of White Sharks Caught', yerr = QLDRunningErrors, kind = 'bar', color = QLDColors, title = 'Total numbers of white sharks caught in the Qld shark control program 1962 – 1998 (data supplied by QDPI)')
# plt.show ()

# running avgs plot
# QLDRunningAvgsPlot = QLDRunningAvgsSeries.plot (xlabel = 'Year', ylabel = 'Average Number of White Sharks Caught', kind = 'bar', color = QLDColors [6:], title = 'Running averages of white sharks caught in the Qld shark control program 1962 – 1998 (data supplied by QDPI)')
# plt.show ()


# GFCSA - Sharks Caught (p. 55)
# GFCSASignificantYears, GFCSASeries, GFCSARunningAvgsSeries, GFCSARunningErrors = FindSigYrs ('GFCSA_Catch', 'GFCSA_Sharks_Caught', 'Year')
# print (GFCSASignificantYears)
# GFCSAColors = SigYrsColors (GFCSASignificantYears)

# significant plot
# GFCSASharksCaughtPlot = GFCSASeries.plot (xlabel = 'Biennial Years', ylabel = 'Numbers of White Sharks Caught', kind = 'bar', color = GFCSAColors, title = 'White sharks caught by the GFCSA (1938 - 1990)')
# plt.show ()

# " with error bars
# GFCSASharksCaughtPlotErrors = GFCSASeries.plot (xlabel = 'Year', ylabel = 'Numbers of White Sharks Caught', yerr = GFCSARunningErrors, kind = 'bar', color = GFCSAColors, title = 'White sharks caught by the GFCSA (1938 - 1990)')
# plt.show ()

# running avgs plot
# GFCSARunningAvgsPlot = GFCSARunningAvgsSeries.plot (xlabel = 'Year', ylabel = 'Average Number of White Sharks Caught', kind = 'bar', color = GFCSAColors [6:], title = 'Running averages of white sharks caught by the GFCSA (1938 - 1990)')
# plt.show ()
