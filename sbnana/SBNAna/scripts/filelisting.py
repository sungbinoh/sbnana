## Do 'setup sam_web_client' before using this macro

from __future__ import print_function
import sys
import os
import samweb_cli
from ROOT import TFile, gDirectory

def print_usage():
    print("Usage: python3 <output_file_name> <samweb definition>")
    sys.exit(1)

if len(sys.argv) != 3:
    print("Error: Incorrect number of arguments.")
    print_usage()

out_name = sys.argv[1]
samweb_def = sys.argv[2]

samweb = samweb_cli.SAMWebClient(experiment='sbn')
files = samweb.listFiles("defname: %s " % (samweb_def))

f = open(out_name, "w")

for file in files:
    loc = samweb.locateFile(file)
    pnfs = loc[0]['full_path'][8:]
    stream = os.popen("./my_pnfsToXRootD %s/%s" % (pnfs,file))
    xroot = stream.read()
    f.write(xroot)

f.close()
