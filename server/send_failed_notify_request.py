#!/usr/bin/env python

import beanstalkc
import json
import sys

print "Getting image details from test phase"
beanstalk_host = sys.argv[1]
notify_email  = sys.argv[2]

msg_details = {}
msg_details['action'] = "notify_user"
msg_details['subject'] = "FAIL: Your container build request has failed"
msg_details['msg'] = "Build has failed."
msg_details['notify_email'] = notify_email

print "Pushing notification details to master_tube"
bs = beanstalkc.Connection(host=beanstalk_host)
bs.use("master_tube")
bs.put(json.dumps(msg_details))
print "notification details pushed to master_tube"
