import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# import seaborn as sns
# import statsmodels as sm
# import sys
pd.options.display.max_columns = 20
pd.options.display.max_rows = 20
pd.options.display.max_colwidth = 80
np.set_printoptions(precision=4, suppress=True)

df = pd.read_excel ('Australian_Shark_Incident_Database_Public_Version.xlsx')
# columnNameSeries = df.columns
# print (columnNameSeries)
# sharkNameSeries = df [['Shark.common.name']].value_counts()
# print (sharkNameSeries)
# print (df.groupby('State')[['Shark.length.m']].agg(['mean','min','max']))
# print (np.full (5,5))

# Number of Yearly Incidents
# incidentYears = df[['Incident.year']].drop_duplicates()
# print (incidentYears)
# yearlyIncidentSeries = df [['Incident.year']].value_counts().sort_index()
# print (yearlyIncidentSeries)
# yearlyIncidentPlot = plt.plot (incidentYears.values, yearlyIncidentSeries.values)
# plt.xlabel ('Incident Year')
# plt.ylabel ('Number of Yearly Shark Incidents')
# plt.title ('Number of Yearly Incidents from 1791 - 2023')
# plt.show ()

trData = pd.ExcelFile ('SP-Transcribed_Data.xlsx')

# NSW Shark Control Program - Sharks Caught (p. 52)
# NSWCaughtSheet = pd.read_excel (trData, 'NSW_Catch')
# NSWSharksCaughtData = NSWCaughtSheet [['NSW_Sharks_Caught']].to_numpy ().flatten ()
# NSWSharksCaughtIndex = NSWCaughtSheet [['Year']].to_numpy ().flatten ()
# NSWSeries = pd.Series (NSWSharksCaughtData, NSWSharksCaughtIndex)
# NSWSharksCaughtPlot = NSWSeries.plot (xlabel = 'Year', ylabel = 'Numbers of White Sharks Caught', kind = 'bar', title = 'Total numbers of white sharks caught in the NSW shark control program 1950 – 2000 (data supplied by NSW Fisheries)')
# plt.show ()

# QLD Shark Control Program - Sharks Caught (p. 53)
# QLDCaughtSheet = pd.read_excel (trData, 'QLD_Catch')
# QLDSharksCaughtData = QLDCaughtSheet [['QLD_Sharks_Caught']].to_numpy ().flatten ()
# QLDSharksCaughtIndex = QLDCaughtSheet [['Year']].to_numpy ().flatten ()
# QLDSeries = pd.Series (QLDSharksCaughtData, QLDSharksCaughtIndex)
# QLDSharksCaughtPlot = QLDSeries.plot (xlabel = 'Year', ylabel = 'Numbers of White Sharks Caught', kind = 'bar', title = 'Total numbers of white sharks caught in the Qld shark control program 1962 – 1998 (data supplied by QDPI)')
# plt.show ()

# GFCSA - Sharks Caught (p. 55)
# GFCSACaughtSheet = pd.read_excel (trData, 'GFCSA_Catch')
# GFCSASharksCaughtData = GFCSACaughtSheet [['GFCSA_Sharks_Caught']].to_numpy ().flatten ()
# GFCSASharksCaughtIndex = GFCSACaughtSheet [['Year']].to_numpy ().flatten ()
# GFCSASeries = pd.Series (GFCSASharksCaughtData, GFCSASharksCaughtIndex)
# GFCSASharksCaughtPlot = GFCSASeries.plot (xlabel = 'Biennial Years', ylabel = 'Numbers of White Sharks Caught', kind = 'bar', title = 'White sharks caught by the GFCSA (1938 - 1990)')
# plt.show ()

# NSW Shark Control Program - Catch per Unit Effort (p. 59)
# NSWCPUESheet = pd.read_excel (trData, 'NSW_CPUE')
# NSWCPUEData = NSWCPUESheet [['NSW_CPUE']].to_numpy ().flatten ()
# NSWCPUEIndex = NSWCPUESheet [['Year']].to_numpy ().flatten ()
# NSWCPUESeries = pd.Series (NSWCPUEData, NSWCPUEIndex)
# NSWCPUEPlot = NSWCPUESeries.plot (xlabel = 'Year', ylabel = 'CPUE (number of sharks per 1000 net sets)', title = 'Catch per unit effort of white sharks in the NSW shark control program (information supplied by NSW Fisheries)')
# plt.show ()

# QLD Shark Control Program - Catch per Unit Effort (Nets) (p. 59)
# QLDCPUEnetsSheet = pd.read_excel (trData, 'QLD_CPUE-Nets')
# QLDCPUEnetsData = QLDCPUEnetsSheet [['QLD_CPUE-Nets']].to_numpy ().flatten ()
# QLDCPUEnetsIndex = QLDCPUEnetsSheet [['Year']].to_numpy ().flatten ()
# QLDCPUEnetsSeries = pd.Series (QLDCPUEnetsData, QLDCPUEnetsIndex)
# QLDCPUEnetsPlot = QLDCPUEnetsSeries.plot (xlabel = 'Year', ylabel = 'CPUE', title = 'Catch per unit effort of white sharks in the Qld shark control program (Gold Coast - nets)')
# plt.show ()

# QLD Shark Control Program - Catch per Unit Effort (Drum-lines) (p. 60)
# QLDCPUEdlSheet = pd.read_excel (trData, 'QLD_CPUE-Drum-lines')
# QLDCPUEdlData = QLDCPUEdlSheet [['QLD_CPUE-Drum-lines']].to_numpy ().flatten ()
# QLDCPUEdlIndex = QLDCPUEdlSheet [['Year']].to_numpy ().flatten ()
# QLDCPUEdlSeries = pd.Series (QLDCPUEdlData, QLDCPUEdlIndex)
# QLDCPUEdlPlot = QLDCPUEdlSeries.plot (xlabel = 'Year', ylabel = 'CPUE', title = 'Catch per unit effort of white sharks in the Qld shark control program (Gold Coast and Pt Lookout - drum-lines)')
# plt.show ()
