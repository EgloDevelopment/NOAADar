# NOAADar
System used to detect undocumented boats and large ships using neural networks and NOAA buoys across the coast.

# Notes
This system is reliable within a certain range, but at long range in bad weather a boat could easily blend into the waves, or vice versa, the system could hit on
whitecaps and other waves, or low flying birds, which is why manual review of the images is needed before dispatching personnel to a location.

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
to script end.