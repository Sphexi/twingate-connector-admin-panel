# Purpose
This Flask based site is meant to be a very rough (emphasis on very) dashboard for a Twingate tenant.  There are two versions of the dashboard currently: the OG really bad and ugly one, and a newer Javascript based one that will update automatically.  It queries the Twingate API and gets a dump of various objects (Connectors, Devices, Users, Service Accounts, and Resources) and displays their details in cards.  There's some rudimentary checks for "good" or "bad" status in some cases to color code them, but it doesn't work well in all cases.

# Setting up
Best idea is to grab the dockercompose.yaml and put your Twingate network name (the subdomain when you log in, ie networkname.twingate.com) and a Read Only API token (go to Settings -> API in the Admin Console to generate one).  You can change the public port if you want, but it's pretty basic.

# How it works
If you want to see the OG bad dashboard then go to:

`server.domain.com:8111`

If you want to see the newer dashboard then go to:

`server.domain.com:8111/index2`

Same idea if you're using an IP address instead, ie `192.168.1.1:8111/index2` to get to the nicer dashboard.

If you want to change the JS or CSS for the better dashboard, look in `static`, the `.js` file is only used by `index2` and there's two style sheets, `style2.css` is for `index2`.
