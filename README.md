# NOAADar
System used to detect undocumented boats and large ships using neural networks and NOAA buoys across the coast.


# Notes
This system is reliable within a certain range, but at long range in bad weather a boat could easily blend into the waves, or vice versa, the system could hit on
whitecaps and other waves, or low flying birds, which is why manual review of the images is needed before dispatching personnel to a location.

The time used in the notifications is based on the system time.


# Installation
This installation is designed specifically for a fresh installation of Alpine Linux

```
apk update
apk add nano git
git clone https://github.com/EgloDevelopment/NOAADar
cd NOAADar
cp config.example.json config.json
nano config.json
```

Now is when you should update your variables to make the application function properly

```
chmod +x install.sh
./install.sh
```

The app should now be deployed using pm2 to run every 10 minutes


# Running
This system can eat up resources, as images are stored in memory.

We were able to successfully monitor from West Florida to the Texas Coastline with 10 minute checks, with under a minute of running time total, from script run 
to script end, including upload messages to Telegram with locations.

This system has been hard coded to work with Telegram and NOAA only, further implementations are going to be coming soon.


# Description of variables
```
MODE: PRODUCTION || TESTING (Determines wether the system will use a image that is guaranteed to hit, used to test configuration)
SAVE_IMAGES: YES || NO (Determines when the script runs if the neural network will save the images it runs on)
ALERT_ON_RUN: YES || NO (Determines if the system will send a Telegram message when it runs)
STATIONS: ["XXXXX", "XXXXX", "XXXXX"...] (Array of station ID's from the NOAA website)
MINIMUM_CONFIDENCE_LEVEL: FLOAT <1 (Percent of confidence the neural network needs to have to hit)
TELEGRAM_TOKEN: TELEGRAM TOKEN (Telegram bot token used to send messages and alerts)
TELEGRAM_CHANNEL_ID: TELEGRAM CHANNEL ID (Determines where to send the messages and alerts)
```