#!/usr/bin/python3
import Adafruit_DHT, datetime, dropbox
sensor=Adafruit_DHT.DHT11
gpio=17
temperature = Adafruit_DHT.read_retry(sensor, gpio)
token = "DROPBOX API TOKEN"
dbx = dropbox.Dropbox(token)
print("The temperature is {}C".format(temperature[1]))
timestamp = datetime.datetime.now()
timestamp = str(timestamp.strftime("%Y-%m-%d %H:%M"))
f = open("data.csv", "a")
f.write(timestamp+",")
f.write(str(temperature[1]))
f.write("\n")
f.close()
with open("data.csv", "rb") as data:
    dbx.files_upload(data.read(), '/data.csv', mute = True, mode=dropbox.files.WriteMode.overwrite)
