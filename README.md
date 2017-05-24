# DAVScan 

DAVScan is a quick and lightweight webdav scanner designed to discover hidden files and folders on DAV enabled webservers.
The scanner works by taking advantage of overly privileged/misconfigured WebDAV servers or servers vulnerable to various 
disclosure or authentication bypass vulnerabilities. The scanner attempts to fingerprint the target server and then spider	
the server based on the results of a root PROPFIND request.

## Notes:

If you actually take the time to read my shitty code, you'll notice that I decided to change up some of the core of davscan to use beautiful soup which will require libxml.  I decided to do this as a result of running into a REALLY bad dav config that returned almost 500mb of XML data and killed the xmltree library.  BS can.. well... handle that much BS.  It will take a little bit longer to collect and parse out everything, but now DAVScan should be able to handle as much shit as you can shovel into it (assuming you don't run out of memory).  
## What works:

**Server header fingerprinting** - If the webserver returns a server header, davscan can search for public exploits based on the response.

**Basic DAV scanning with PROPFIND** - Quick scan to find anything that might be visible from DAV.

**IIS/6.0 Unicode Auth Bypass** - Works using GET for files and PROPFIND for folders.  Not fully tested so double check the work.

**Exclusion of DoS exploit results** - You can exclude denial of service exploits from the searchsploit results.

**Exclusion of MSF modules from exploit results** - Custom searchsploit is included in the repo for this.  Either overwrite existing searchsploit or backup and replace. This feature may or may not end up in the real searchsploit script.

**Proxy Capable**  - You can specify an http(s) proxy to use.  This will just pass a proxy the requests session.  I added this in becuase of the need for NTLM auth that requests just can't do at this point in time.

**Authentication** - Just basic auth works right now.  If you need anything like tokenization or something weird, let me know and I'll work on it.  Not a high priority to add further functionality to this though.  Most one off auth needs can be handled using burp and the proxy flag.

## What doesn't work:


**X header fingerprinting** - It's in there, but isn't working right.  I might have this working right now, but not fully tested yet.  

**My ability to proerly document things** - When I switched out the native xml for beautiful soup that came with some requirements I didn't know I wa supposed to tell you about.  You'll want to install that as well as the C library libxml beause it makes things faster.  It also doesn't shit the bed if you feed it half a gig of WebDAV XML. Go ahead, ask me how I found that one out.

**Probably a lot more that I haven't tested and whatever the issues might be in the github assuming people care to tell me what is tarded..**

## What I want to do:

**Build a sqlite database instead of flat file** - Currently output goes to file with a couple blurbs to the screen just to show it's working.  

**Become a fighter pilot!** - I saw Top Gun once and now I'm really stoked about going into the Air Force and living the dream.  "I feel the need for speed!"

## Contributing:
Did you know that you can help fix my bad code for me?  It could be like your day job but with no pay and a smidge more recognition since I gain almost nothing from your hard work here.  On the bright side I won't demand you come in on the weekend to play catch up.  Hell I won't even complain if you submit code you wrote when you were drunk.  In case you haven't noticed that's when I do some of my best-ish work.  Just don't submit some silly shit like fixng a typo.  Those are there by design. 


## Usage:

`Usage: davscan.py [-h] [-D DEPTH] [-a AUTH] [-u USER] [-p PASSWORD]         `

`                 [-o OUTFILE] [-P PROXY] [-d] [-m]  url                                                      `

`                                                                            `
`positional arguments:                                                       `

`  url                   url of the server to scan; https://foo.com:8443/    `
`                                                                            `

`optional arguments:                                                         `

`  -h, --help            show this help message and exit                     `

`  -D DEPTH, --depth DEPTH  How many folders deep should davscan go (default is infinity); -d 1    ` 

`  -a AUTH, --auth AUTH  Basic authentication required; -a basic             `

`  -u USER, --user USER  user; -u derpina                                    `

`  -p PASSWORD, --password PASSWORD password; -P 'P@$$W0rd'                  `

`  -o OUTFILE, --out OUTFILE output file. defaults to; -o /tmp/davout`

`  -P PROXY, --proxy PROXY  proxy server if needed.; -P http://user:pass@1.2.3.4:8080/                   `

`  -d, --no-dos          exclude DoS modules                               `
`  -m, --no-msf          exclude MSF modules from results                  `
`                                                                          `
