# DAVScan 

DAVScan is a quick and lightweight webdav scanner designed to discover hidden files and folders on DAV enabled webservers.
The scanner works by taking advantage of overly privileged/misconfigured WebDAV servers or servers vulnerable to various 
disclosure or authentication bypass vulnerabilities. The scanner attempts to fingerprint the target server and then spider	
the server based on the results of a root PROPFIND request.

## What works:

**Server header fingerprinting** - If the webserver returns a server header, davscan can search for public exploits based on the response.

**Basic DAV scanning with PROPFIND** - Quick scan to find anything that might be visible from DAV.

**Unicode Auth Bypass** - Works using GET haven't added PROPFIND yet.  Not fully tested so double check the work.

**Exclusion of DoS exploit results** - You can exclude denial of service exploits from the searchsploit results.

**Exclusion of MSF modules from exploit results** - Custom searchsploit is included in the repo for this.  Either overwrite existing searchsploit or backup and replace. This feature may or may not end up in the real searchsploit script.

## What doesn't work:

**Authentication** - I've started this, but it's not finished yet.  I'll get to it when I actually need it.

**X header fingerprinting** - It's in there, but isn't working right.  Need to debug this.



**Probably a lot more that I haven't tested yet.**

## What I want to do:

**Build a sqlite database instead of flat file** - Currently output goes to file with a couple blurbs to the screen just to show it's working.  

**Become a fighter pilot!** - I saw Top Gun once and now I'm really stoked about going into the Air Force and living the dream.  "I feel the need for speed!"

## Usage:

`usage: davscan.py [-h] [-a AUTH] [-u USER] [-P PASSWORD] [-o OUTFILE] [-d]`
`                  [-m]`
`                  url`
``
`positional arguments:`
`  url                   url of the server to scan; https://foo.com:8443/`
``
`optional arguments:`
`  -h, --help            show this help message and exit`
`  -a AUTH, --auth AUTH  Basic authentication required; -a basic`
`  -u USER, --user USER  user; -u derpina`
`  -P PASSWORD, --password PASSWORD`
`                        password; -P 'P@$$W0rd'`
`  -o OUTFILE, --out OUTFILE`
`                        output file. defaults to; -o /tmp/davout`
`  -d, --no-dos          exclude DoS modules`
`  -m, --no-msf          exclude MSF modules from results`
