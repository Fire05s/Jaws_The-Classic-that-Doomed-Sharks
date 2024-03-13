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

df = pd.read_excel ('Australian_Shark_Incident_Database_Public_Version.xlsx') # file needs to be closed
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

# NSW Shark Control Program - Sharks Caught
# NSWSharksCaughtData = np.array ([8,16,17,21,13,18,17,10,16,15,10,10,10,13,8,11,13,12,11,8,15,7,26,18,29,18,12,
#                                  21,4,8,4,4,7,5,6,5,15,5,5,4,0,5,2,7,6,5,3,3,3,8])
# NSWSeries = pd.Series (NSWSharksCaughtData,index = ['1950-1951','1951-1952','1952-1953','1953-1954',
#                                                     '1954-1955','1955-1956','1956-1957','1957-1958',
#                                                     '1958-1959','1959-1960','1960-1961','1961-1962',
#                                                     '1962-1963','1963-1964','1964-1965','1965-1966',
#                                                     '1966-1967','1967-1968','1968-1969','1969-1970',
#                                                     '1970-1971','1971-1972','1972-1973','1973-1974',
#                                                     '1974-1975','1975-1976','1976-1977','1977-1978',
#                                                     '1978-1979','1979-1980','1980-1981','1981-1982',
#                                                     '1982-1983','1983-1984','1984-1985','1985-1986',
#                                                     '1986-1987','1987-1988','1988-1989','1989-1990',
#                                                     '1990-1991','1991-1992','1992-1993','1993-1994',
#                                                     '1994-1995','1995-1996','1996-1997','1997-1998',
#                                                     '1998-1999','1999-2000'])
# NSWSharkCaughtPlot = NSWSeries.plot (xlabel = 'Year', ylabel = 'Numbers of White Sharks Caught', kind = 'bar', title = 'Total numbers of white sharks caught in the NSW shark control program 1950 – 2000 (data supplied by NSW Fisheries)')
# plt.show ()

# QLD Shark Control Program - Sharks Caught
# QLDSharksCaughtData = np.array ([10,27,35,34,17,30,20,22,16,22,20,15,23,20,16,25,20,20,22,27,15,11,
#                                  16,19,5,15,15,15,8,11,16,13,8,8,1,19,10])
# QLDSeries = pd.Series (QLDSharksCaughtData,index = ['1962-1963','1963-1964','1964-1965','1965-1966',
#                                                     '1966-1967','1967-1968','1968-1969','1969-1970',
#                                                     '1970-1971','1971-1972','1972-1973','1973-1974',
#                                                     '1974-1975','1975-1976','1976-1977','1977-1978',
#                                                     '1978-1979','1979-1980','1980-1981','1981-1982',
#                                                     '1982-1983','1983-1984','1984-1985','1985-1986',
#                                                     '1986-1987','1987-1988','1988-1989','1989-1990',
#                                                     '1990-1991','1991-1992','1992-1993','1993-1994',
#                                                     '1994-1995','1995-1996','1996-1997','1997-1998',
#                                                     '1998-1999'])
# QLDSharkCaughtPlot = QLDSeries.plot (xlabel = 'Year', ylabel = 'Numbers of White Sharks Caught', kind = 'bar', title = 'Total numbers of white sharks caught in the Qld shark control program 1962 – 1998 (data supplied by QDPI)')
# plt.show ()

# GFCSA - Sharks Caught
# GFCSASharksCaughtData = np.array ([19,5,0,5,25,22,27,1,11,13,7,1,8,5,2,4,1,2,2,0,2,2,3,6,1])
# GFCSASeries = pd.Series (GFCSASharksCaughtData,index = ['1938-1939','1940-1941','1942-1946 (WWII)',
#                                                         '1947-1948','1949-1950','1951-1952','1953-1954',
#                                                         '1955-1956','1957-1958','1959-1960','1961-1962',
#                                                         '1963-1964','1965-1966','1967-1968','1969-1970',
#                                                         '1971-1972','1973-1974','1975-1976','1977-1978',
#                                                         '1979-1980','1981-1982','1983-1984','1985-1986',
#                                                         '1987-1988','1989-1990'])
# GFCSASharkCaughtPlot = GFCSASeries.plot (xlabel = 'Biennial Years', ylabel = 'Numbers of White Sharks Caught', kind = 'bar', title = 'White sharks caught by the GFCSA (1938 - 1990)')
# plt.show ()

# NSW Shark Control Program - Catch per Unit Effort
# NSWCPUEData = np.array ([1.8,3.1,3.7,4.1,2.6,3.3,3.2,1.9,2.9,2.9,1.9,1.9,2.1,2.5,1.5,2.0,2.7,2.3,2.2,
#                          1.4,3.2,1.4,4.3,2.9,4.5,2.8,1.9,3.3,0.6,1.2,0.6,0.6,1.4,1.1,1.2,1.1,2.5,0.9,
#                          1.1,0.9,0,1.0,0.3,1.3,1.2,1.1,0.6,0.6,0.6,2.8])
# NSWCPUESeries = pd.Series (NSWCPUEData,index = ['1950-1951','1951-1952','1952-1953','1953-1954',
#                                                 '1954-1955','1955-1956','1956-1957','1957-1958',
#                                                 '1958-1959','1959-1960','1960-1961','1961-1962',
#                                                 '1962-1963','1963-1964','1964-1965','1965-1966',
#                                                 '1966-1967','1967-1968','1968-1969','1969-1970',
#                                                 '1970-1971','1971-1972','1972-1973','1973-1974',
#                                                 '1974-1975','1975-1976','1976-1977','1977-1978',
#                                                 '1978-1979','1979-1980','1980-1981','1981-1982',
#                                                 '1982-1983','1983-1984','1984-1985','1985-1986',
#                                                 '1986-1987','1987-1988','1988-1989','1989-1990',
#                                                 '1990-1991','1991-1992','1992-1993','1993-1994',
#                                                 '1994-1995','1995-1996','1996-1997','1997-1998',
#                                                 '1998-1999','1999-2000'])
# NSWCPUEPlot = NSWCPUESeries.plot (xlabel = 'Year', ylabel = 'CPUE (number of sharks per 1000 net sets)', title = 'Catch per unit effort of white sharks in the NSW shark control program (information supplied by NSW Fisheries)')
# plt.show ()

# QLD Shark Control Program - Catch per Unit Effort (Nets)
# QLDCPUEnetsData = np.array ([0.30,1.10,0.80,1.10,0.30,1.10,0.33,0.85,0.68,0.68,0.41,0.51,0.41,0.29,
#                              0.20,0.60,0.62,0.48,0.38,0.38,0.30,0.38,0.38,0.08,0.08,0.00,0.17,0.17,
#                              0.00,0.00,0.00,0.17,0.17,0.17,0.00,0.09,0.18])
# QLDCPUEnetsSeries = pd.Series (QLDCPUEnetsData,index = ['1962-1963','1963-1964','1964-1965','1965-1966',
#                                                         '1966-1967','1967-1968','1968-1969','1969-1970',
#                                                         '1970-1971','1971-1972','1972-1973','1973-1974',
#                                                         '1974-1975','1975-1976','1976-1977','1977-1978',
#                                                         '1978-1979','1979-1980','1980-1981','1981-1982',
#                                                         '1982-1983','1983-1984','1984-1985','1985-1986',
#                                                         '1986-1987','1987-1988','1988-1989','1989-1990',
#                                                         '1990-1991','1991-1992','1992-1993','1993-1994',
#                                                         '1994-1995','1995-1996','1996-1997','1997-1998',
#                                                         '1998-1999'])
# QLDCPUEnetsPlot = QLDCPUEnetsSeries.plot (xlabel = 'Year', ylabel = 'CPUE', title = 'Catch per unit effort of white sharks in the Qld shark control program (Gold Coast - nets)')
# plt.show ()

# QLD Shark Control Program - Catch per Unit Effort (Drum-lines)
# QLDCPUEdlData = np.array ([0.09,0.21,0.51,0.21,0.13,0.52,0.45,0.40,0.22,0.34,0.26,0.08,0.29,0.15,0.14,0.10,
#                            0.16,0.15,0.13,0.13,0.07,0.08,0.07,0.07,0.01,0.08,0.08,0.05,0.05,0.09,0.18,
#                            0.09,0.08,0.12,0.05,0.02])
# QLDCPUEdlSeries = pd.Series (QLDCPUEdlData,index = ['1962-1963','1963-1964','1964-1965','1965-1966',
#                                                     '1966-1967','1967-1968','1968-1969','1969-1970',
#                                                     '1970-1971','1971-1972','1972-1973','1973-1974',
#                                                     '1974-1975','1975-1976','1976-1977','1977-1978',
#                                                     '1978-1979','1979-1980','1980-1981','1981-1982',
#                                                     '1982-1983','1983-1984','1984-1985','1985-1986',
#                                                     '1986-1987','1987-1988','1988-1989','1989-1990',
#                                                     '1990-1991','1991-1992','1992-1993','1993-1994',
#                                                     '1994-1995','1995-1996','1996-1997','1997-1998'])
# QLDCPUEdlPlot = QLDCPUEdlSeries.plot (xlabel = 'Year', ylabel = 'CPUE', title = 'Catch per unit effort of white sharks in the Qld shark control program (Gold Coast and Pt Lookout - drum-lines)')
# plt.show ()