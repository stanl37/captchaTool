import imports - calls on imports.py. just a list of modules to import.

import tools - calls on tools.py. has a few functions

      log() - prints out the current time in "[HH:MM:SS.MS] ". Milliseconds have three digits. The space after the brackets is included. This function is used whenever printing is needed.

      fileLen(fname) - prints out the length of a file. I don't think this ever used.

      loadConfig(configname) - loads up config.json. See config for example setup.

      formatEmail(configEmail) - removes @gmail.com if it's part of an email (gets to just the stem). If an email is bad it'll spit out something in console.

import signin - calls on signin.py. has a few important functions

    signin(driver, email, password, verbose) - headless signin process. called on by driverStart, you'll probably never need to call this.

    manual(the same as above) - pretty much signin() but not headless. used for additional google auth. called on by driverStart, you'll probably never need to call this.

import cookies - calls on cookies.py, functions relating to sessions/cookies

    cookieCheck(driver, email, verbose) - checks for cookies, and if they are there loads them (calls on loadCookies). called on by driverStart, you'll probably never need to call this.

    saveCookies(driver, file, verbose) - saves cookies to three different files, where "file" is the email stem. Saves cookies for Google, Gmail, and YouTube. called on by driverStart, you'll probably never need to call this. Better directory control is needed here

    loadCookies(driver, file, verbose) - loads cookies. doesn't check if files are present, which is why cookieCheck() is used. called on by driverStart, you'll probably never need to call this.

import driverstart - calls on driverstart.py. THE MOST IMPORTANT TO STARTING DRIVER! YOU SHOULD CALL DRIVERSTART()!

    driverStart(email, password, proxy, verbose) - starts the driver (with a proxy if included). also calls on cookieCheck to load cookies. then runs signin() and/or manual() to sign in. also saves session cookies. returns the driver as the email stem, for manipulation in other functions. call on this to initate driver/session process!

    headless() - creates a headless driver process. used by driverstart()
    head() - creates a headed driver process. used by driverstart()

import activity - calls on activity.py. functions to generating activity for the gmails.

    search(driver, verbose) - random activity on google.

    pooky(driver, verbose) - random activity on Supreme.

    youtube(driver, verbose) - random activity on YouTube.
