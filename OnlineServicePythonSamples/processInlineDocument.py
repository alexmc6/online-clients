#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import json

endpointUrl = "https://api.annomarket.com/online-processing/item/"
shopItemId = "2"
keyId = "<your-credentials-here>"
password = "<your-credentials-here>"

# create a password manager
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.
password_mgr.add_password(None, endpointUrl, keyId ,password)
handler = urllib2.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib2.build_opener(handler)

# Install the opener.
# Now all calls to urllib2.urlopen use our opener.
urllib2.install_opener(opener)

data = {
	"document" : "Tiruchirappalli is the " +
				"fourth largest city in the Indian state of " +
				"Tamil Nadu and is the administrative headquarters " +
				"of Tiruchirappalli District. Its recorded " +
				"history begins in the 3rd century BC, " +
				"when it was under the rule of the Cholas. " +
				"The city has also been ruled by the Pandyas, " +
				"Pallavas, Vijayanagar Empire, Nayak Dynasty, " +
				"the Carnatic state and the British. " +
				"It played a crucial role in the Carnatic Wars " +
				"(1746�63) between the British and the French " +
				"East India companies. During British rule, the city " +
				"was popular for the Trichinopoly cigar, its unique brand " +
				"of cheroot. Monuments include the Rockfort (pictured), the " +
				"Ranganathaswamy temple and the Jambukeswarar temple. " +
				"It is an important educational centre in Tamil Nadu, " +
				"housing nationally recognised institutions such as the " +
				"Indian Institute of Management and the National " +
				"Institute of Technology.",
	"mimeType" : "text/plain"
}
#json serialize
jsonData = json.dumps(data)
print(jsonData)

headers = {
                'Accept' : "application/gate+json",
				'Content-type': "application/json",
				'Accept-Encoding':"gzip",
}

#Prepare request
request = urllib2.Request(endpointUrl+shopItemId,jsonData,headers)

response=urllib2.urlopen(request)

print response.read()

# Getting the code
print "\n\n\nThis gets the code: ", response.code  

# Get the Headers. 
print "The Headers are: ", response.info()
