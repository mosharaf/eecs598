"""Cluster profile for Assignment 1

Instructions:
Wait for the profile instance to start, and then log in to the host using the ssh command in the ListView below.
Note that the data can be accessed readonly on any node at `/bigdata`
"""

import geni.urn as urn
import geni.portal as portal
import geni.rspec.pg as rspec
import geni.aggregate.cloudlab as cloudlab

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()

# Create three raw PC
# m510 at Utha using Ubuntu 16.04
nodes = []
for i in range(3):
    node = request.RawPC("node-{}".format(i))
    node.hardware_type = "m510"
    node.disk_image = urn.Image(cloudlab.Utah, "emulab-ops:UBUNTU16-64-STD")
    nodes.append(node)

# The remote file system is represented by special node.
fsnode = request.RemoteBlockstore("fsnode", "/bigdata")
# This URN is displayed in the web interface for your dataset.
fsnode.dataset = "urn:publicid:IDN+utah.cloudlab.us:michigan-bigdata-pg0+ltdataset+BigData-W19"
fsnode.readonly = True

link = request.Link('link')
for node in nodes:
    link.addInterface(node.addInterface())
link.addInterface(fsnode.interface)
# Special attributes for this link that we must use.
link.best_effort = True
link.vlan_tagging = True

# We need to manually mount the dataset as readonly due to the noload option
for node in nodes:
    node.addService(rspec.Execute(shell="bash", command="sudo mount -o ro,noload /dev/sda /bigdata"))

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
