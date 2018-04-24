from google.protobuf import json_format
from pirate_pb2 import Boat
# import ipdb; ipdb.set_trace()


print "will parse json /tmp/boat.json"
with open("/tmp/boat.json", "rb") as f:
    raw = f.read()
boat = json_format.Parse(raw, Boat)
print "Parsed boat: {}".format(boat)
