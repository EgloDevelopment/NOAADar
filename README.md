# NOAADar
System used to detect undocumented boats and large ships using neural networks and NOAA buoys across the coast.

# Installation
This installation is designed specifically for a fresh installation of  Alpine Linux

```
apk update
apk add nano
cp config.example.json config.json
nano config.json
```

Now is when you should update your variables to make the application work

```
chmod +x install.sh
./install.sh
```

The app should now be deployed using pm2 to run every 10 minutes