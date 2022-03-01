import imports #datetime, requests, colorama, various selenium, etc.
import tools #log(), fileLen(fname), loadConfig(configname), formatEmail(configEmail)
import signin #signin(driver, email, password, verbose), manual(driver, email, password, verbose)
import cookies #cookieCheck(driver, email, verbose), saveCookies(driver, file, verbose), loadCookies(driver, file, verbose)
import driverstart #driverStart(email, password, proxy, verbose), headless(), head()
global driver

import activity #search(driver, time), pooky(driver, time), youtube(driver, time)


config = tools.loadConfig('config.json')
verbose = config["verbose"]
info = config["info"]
emailCount = len(info)
if verbose == True: print(tools.log() + "Emails: " + str(emailCount))

#for x in info:
email = tools.formatEmail(x[0])
if verbose == True: print(tools.log() + "Using email: " + email)
email = driverstart.driverStart(email, x[1], x[2], verbose) #email is now the driver
