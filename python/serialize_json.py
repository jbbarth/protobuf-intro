from google.protobuf import json_format
from pirate_pb2 import Captain, CrewMember, Boat
# import ipdb; ipdb.set_trace()


captain = Captain(name="Hook", hook=True)
bosun = CrewMember(name="Mr. Smee", rank="bosun")
boat = Boat(name="Jolly Roger",
            captain=captain,
            sailors=[bosun],
            propulsion_kind=Boat.WIND)


print "will write binary representation: /tmp/boat.json"
with open("/tmp/boat.json", "w") as f:
    f.write(json_format.MessageToJson(boat))
