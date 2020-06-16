import requests
import html
import datetime
r = requests.get('https://api.particle.io/v1/devices/33003b000b47373336373936/temperature?access_token=1c476acb47bd0b944a031e2859ef7160e4b72a66')
temp = ("%.2f" % r.json()["result"])
r = requests.get('https://api.particle.io/v1/devices/33003b000b47373336373936/conductivity?access_token=1c476acb47bd0b944a031e2859ef7160e4b72a66')
cond = ("%.2f" % r.json()["result"])
r = requests.get('https://api.particle.io/v1/devices/33003b000b47373336373936/ph?access_token=1c476acb47bd0b944a031e2859ef7160e4b72a66')
ph = ("%.2f" % r.json()["result"])
now = datetime.datetime.now()
date_stamp = now.strftime("%Y-%b-%d %H:%M")
f = open('/var/www/html/aquarium/aquarium.csv', 'a')
f.write(date_stamp + "," + temp + "," + cond + "," + ph + "\n")     # use back slash symbol
f.close()
f = open('/var/www/html/aquarium/aquarium.html', 'w')
message = """
<h1>Aquarium Conditions</h1>
<p>The temperature in the aquarium is %s</p>
<p>The conductivity in the aquarium is %s</p>
<p>The pH in the aquarium is %s</p>
<p>This reading was last updated at %s</p>
<p>Follow links below to see graphs of data</p>
<p><a href="aquarium_temp.html">Temperature</a>
<a href="aquarium_cond.html">Conductivity</a>
<a href="aquarium_ph.html">pH</a>
</p>
""" % (html.escape(temp), html.escape(cond), html.escape(ph), html.escape(date_stamp))
f.write(message)
f.close()
print("Finished")


