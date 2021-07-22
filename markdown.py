markdown_text_section_1 = '''
There was an anomalous increase in booking mismatches between 17 May to 31 May. 
This was due to backend issues leading to the loss of precision in stored address coordinates. 
This issue has been resolved. Since 31 May, the daily mismatch rate has been reduced to 
an average of approximately 10% a day (which is close to the approximate 9.07% daily mismatch rate 
before the backend issues occured)
'''

markdown_text_section_2_1 = '''
Furthermore, for the mismatches after 31 May, the distances between the requested waypoints and the 
offered waypoints are mostly within a reasonable threshold. Over 90% of the offered waypoints are within 50m of the user's 
requested waypoint. This is a reasonable threshold given that the mean length of buildings in Singapore is approximately 
50m (calculated using the 2019 Singapore building footprint data from data.gov.sg). Hence, though some users may receive mismatches,
it may not necessarily be a cause of concern since the offered waypoint is likely to be in the vicinity (ie at the neighbouring building). 
'''
