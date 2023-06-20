print('1-światła powinny się NIE świecić:')
# is the light switch in AUTOMATIC mode
isAutomaticMode = True
 
# is the level of day-lighr above 80%
is80PercentLight = True
 
# is the Sun ligthing directly into the driver's face
isDirectLight = False
 
# is it rainy, foggy or other weather conditions are present
isRainy = False
 
turnLightsOn = isAutomaticMode and (is80PercentLight is not isDirectLight is not isRainy)
 
print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
print('')
'''
przerwa

'''
print('2-światła powinny się świecić')
# is the light switch in AUTOMATIC mode
isAutomaticMode = True
 
# is the level of day-lighr above 80%
is80PercentLight = False
 
# is the Sun ligthing directly into the driver's face
isDirectLight = False
 
# is it rainy, foggy or other weather conditions are present
isRainy = False
 
turnLightsOn = isAutomaticMode and (is80PercentLight is isDirectLight) and not isRainy
 
print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
print('')
'''
przerwa

'''
print('3-światła powinny się świecić:')
# is the light switch in AUTOMATIC mode
isAutomaticMode = True
 
# is the level of day-lighr above 80%
is80PercentLight = True
 
# is the Sun ligthing directly into the driver's face
isDirectLight = False
 
# is it rainy, foggy or other weather conditions are present
isRainy = True
 
turnLightsOn = isAutomaticMode and (not is80PercentLight is isDirectLight) is isRainy
 
print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
print('')
'''
przerwa

'''
print('4-światła powinny się świecić:')
# is the light switch in AUTOMATIC mode
isAutomaticMode = True
 
# is the level of day-lighr above 80%
is80PercentLight = True
 
# is the Sun ligthing directly into the driver's face
isDirectLight = True
 
# is it rainy, foggy or other weather conditions are present
isRainy = False
 
turnLightsOn = isAutomaticMode and (is80PercentLight is isDirectLight) is not isRainy
 
print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
print('')
'''
przerwa

'''
print('5-światła powinny się świecić:')
# is the light switch in AUTOMATIC mode
isAutomaticMode = True
 
# is the level of day-lighr above 80%
is80PercentLight = False
 
# is the Sun ligthing directly into the driver's face
isDirectLight = False
 
# is it rainy, foggy or other weather conditions are present
isRainy = True
 
turnLightsOn = isAutomaticMode and not (is80PercentLight and isDirectLight) is isRainy
 
print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
print('')
'''
przerwa

'''
print('6-światła NIE powinny się świecić:')
# is the light switch in AUTOMATIC mode
isAutomaticMode = False
 
# is the level of day-lighr above 80%
is80PercentLight = True
 
# is the Sun ligthing directly into the driver's face
isDirectLight = False
 
# is it rainy, foggy or other weather conditions are present
isRainy = True
 
turnLightsOn = isAutomaticMode and not is80PercentLight is isDirectLight is not isRainy
 
print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
print('')
'''
przerwa

'''
