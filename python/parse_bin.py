from pirate_pb2 import Boat
# import ipdb; ipdb.set_trace()


print "will parse bin /tmp/boat.bin"
with open("/tmp/boat.bin", "rb") as f:
    raw = f.read()
boat = Boat()
boat.ParseFromString(raw)
print "Parsed boat: {}".format(boat)
