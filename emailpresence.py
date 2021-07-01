import argparse
import sys
from banner.banner import banner_design
from function import *
banner=banner_design()


parser=argparse.ArgumentParser(description="Subdomain enumeration", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-d", "--domain", help="domain name for subdomain enumeration", type=str, required=True)
parser.add_argument("-f", "--first", help="first name", type=str, required=True)
parser.add_argument("-l", "--last", help="last name", type=str, required=True)
parser.add_argument("-o","--output", help="output filename to save the results", type=str, required=True)
parser.add_argument("-a", "--api", help="Security trails api key", type=str, required=True)
args=parser.parse_args()

if len(sys.argv) <7:
    sys.exit()
elif sys.argv[2]==args.domain and sys.argv[4]==args.first and sys.argv[6]==args.last and sys.argv[8]==args.api and sys.argv[10]==args.output:
    emailpresence(args.domain,args.first, args.last, args.api, args.output)