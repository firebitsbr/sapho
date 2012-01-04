#!/usr/bin/env python
# encoding: utf-8
"""
sapho: templater.py

Created by Scott Roberts.
Copyright (c) 2011 TogaFoamParty Studios. All rights reserved.
"""

import sys
import getopt

help_message = '''
Sapho Templater is for automatically generating, populating, and posting Sapho wiki pages to a Dokuwiki implimentation. This takes a lot of the pain out of generating a new page.
'''
# Filler text pulled from http://www.lipsum.com
lipsum = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
lipsum_short = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
lipsum_word = "Lorem ipsum"

# Indicator Classes
class Indicator_ArpEntryItem(object):
	"""Based on Mandiant's OpenIOC XML specification. Address Resolution Protocol (ARP) is a telecommunications protocol used for resolution of network layer addresses into link layer addresses, a critical function in multiple-access networks. (Wikipedia: http://en.wikipedia.org/wiki/Address_Resolution_Protocol)."""
	
	physicalAddress = lipsum_word
	iPv4Address = "127.0.0.1"
	iPv6Address = "::1"
	interface = lipsum_word
	interfaceType = lipsum_word
	state = lipsum_word
	cache = lipsum_word
	isRouter = False
	lastReachable = "01/01/2001 00:00:00"
	lastUnreachable = "01/01/2001 00:00:00"
	
	def __init__(self, arg):
		super(Indicator_ArpEntryItem, self).__init__()
		self.arg = arg

    def generateWikiTableHeader(self):
        """docstring for generateWikiTableHeader"""
        wikitext = "^ Physical Address ^ IPV4 Address ^ IPV6 Address ^ Interface ^ Interface Type ^ State ^ Cache ^ Router ^ Last Reachable ^ Last Unreachable ^ "
        return wikitext

    def generateWikiTableRow(self, physicalAddress = lipsum_word, iPv4Address = "127.0.0.1", iPv6Address = "::1", interface = lipsum_word, interfaceType = lipsum_word, state = lipsum_word, cache = lipsum_word, isRouter = False, lastReachable = "01/01/2001 00:00:00", lastUnreachable = "01/01/2001 00:00:00"):
        """docstring for generateWikiTableHeader"""
        wikitext = "| %s               | %s           | %s           | %s        | %s             | %s    | %s    | %s     | %s             | %s               | " % (physicalAddress, iPv4Address, iPv6Address, interface, interfaceType, state, cache, str(isRouter), lastReachable, lastUnreachable)    
        return wikitext
    
    def generateDefaultWikiTemplate(self):
        """docstring for generateWikiTemplate"""
        wikitext = ""
        wikitext += generateWikiTableHeader()
        wikitext += generateWikiTableRow()
        
        return wikitext

class Indicator_DnsEntryItem(object:
    """Based on Mandiant's OpenIOC XML specification. The Domain Name System (DNS) is a hierarchical distributed naming system for computers, services, or any resource connected to the Internet or a private network. It associates various information with domain names assigned to each of the participating entities. Most importantly, it translates domain names meaningful to humans into the numerical identifiers associated with networking equipment for the purpose of locating and addressing these devices worldwide. (Wikipedia: http://en.wikipedia.org/wiki/Domain_Name_System)."""
                             
	RecordName = lipsum
	RecordType = lipsum
	TimeToLive = "01/01/2001 00:00:00"
	Flags = lipsum
	Host = lipsum
	IPv4Address = lipsum
    IPv6Address = lipsum
	PrimaryServerName = lipsum
	AdministratorName = lipsum
	Refresh = "01/01/2001 00:00:00"
	Retry = "01/01/2001 00:00:00"
	Expire = "01/01/2001 00:00:00"
	DefaultTimeToLive = "01/01/2001 00:00:00"
	MailboxName = lipsum
	MailboxErrorsName = lipsum
	MxHost = lipsum
	Bitmask = lipsum
	OriginalTimeToLive = "01/01/2001 00:00:00"
	ExpirationDate = "01/01/2001 00:00:00"
	DateSigned = "01/01/2001 00:00:00"
	CreationDate = "01/01/2001 00:00:00"
	LookupTimeout = "01/01/2001 00:00:00"
	CacheTimeout = "01/01/2001 00:00:00"
	
# Wiki Classes
class WikiTemplater(object):
    doku_username = "sapho"
    doku_password = "sapho_password"
    
    # Major Page Types
    def generateSetPage(pagename):
        wikitext = "====== Summary ======\n"
        wikitext += "%s" % lipsum
        wikitext += "==== Hypotheses ====\n"
        wikitext += "  * [[https://localhost/ach/%s|%s]]" % (hypothesispath, hypothesisname)
        
        wikitext += "====== Compromise Vector & Persistence ======\n"
        wikitext += "==== Compromise Vector ====\n"
        wikitext += "%s" % lipsum
        
        wikitext += "===== Persistence =====\n"
        wikitext += "%s" % lipsum
        
        wikitext += "====== Detection =====\n"
        wikitext += "==== ArcSight Content ====\n"
        wikitext += "  * %s" % lipsum_short
        
        wikitext += "==== Netwitness Content ====\n"
        wikitext += "  * %s" % lipsum_short
        
        wikitext += "==== Open Tickets ====\n"
        wikitext += "  * %s" % lipsum_short
        
        wikitext += "===== Indicators =====\n"
        wikitext += "==== Known Compromised Hosts ====\n"
        wikitext += "^ IP Address ^ Host Name ^ User Name ^ Title ^ Department ^ Notes ^\n"
        wikitext += "|            |           |           |       |            |       |\n"
        
        wikitext += "==== Known Compromised Accounts ====\n"
        wikitext += "^ Username ^ User ^ Notes ^\n"
        wikitext += "|          |      |       |\n"
        
        wikitext += "==== IP Indicators ====\n"
        wikitext += "^ IP Address ^ Location ^ URL ^ Research ^ Notes ^\n"
        wikitext += "|            |          |     |          |       |\n"
        
        wikitext += "==== URL Indicators ====\n"
        wikitext += "^ URL ^ Associated IP Addresses ^ Location ^ Research ^ Notes ^\n"
        wikitext += "|     |                         |          |          |       |\n"
        
        wikitext += "==== Known Attacker Ports ====\n"
        wikitext += "^ Port ^ Type ^ Service ^ Notes ^\n"
        wikitext += "|      |      |         |       |\n"
        
        wikitext += "==== Bad User Agent Strings ====\n"
        wikitext += "^  UserAgent String        ^ Notes ^\n"
        wikitext += "|                          |       |\n"
        
        wikitext += "==== Known Malicious Files ====\n"
        wikitext += "^ Filename ^ Type ^ Size ^ MD5 ^ SSDeep ^ File ^ Report ^ Notes ^\n"
        wikitext += "|          |      |      |     |        |      |        |       |\n"
        
        return [intrusion:pagename, wikitext]
    
    def generateWikiStartTemplate():
        wikitext = "====== Summary ======\n"
        wikitext += "===== Terms and Processes =====\n"
        wikitext += "  * [[Activity Classification]]\n"
        wikitext += "  * [[Wiki Conventions]]\n"
        
        wikitext += "====== News ======\n"
        wikitext += "===== SANS ISC =====\n"
        wikitext += "{{rss>http://isc.sans.edu/rssfeed_full.xml 5 author date 1h }}\n"
        wikitext += "===== Team Cymru =====\n"
        wikitext += "{{rss>http://www.team-cymru.org/News/secnews.rss 5 author date 1h }}\n"
        
        wikitext += "====== Intrusion Campaigns ======\n"
        wikitext += "===== Alpha Campaign =====\n"
        wikitext += "  * [[intrusion:Alpha Alpha]] - **Date Identified:** -\n"
        wikitext += "  * [[intrusion:Alpha Bravo]] - **Date Identified:** -\n"
        wikitext += "**C2:** - **Exfil:** -"
        wikitext += "===== Bravo Campaign =====\n"
        wikitext += "  * [[intrusion:Bravo Alpha]] - **Date Identified:** -\n"
        wikitext += "  * [[intrusion:Bravo Bravo]] - **Date Identified:** -\n"
        wikitext += "**C2:** - **Exfil:** -\n"
        
        wikitext += "====== Third Party Intelligence ======\n"
        wikitext += "  * [[thirdpartyintel:TPI-Alpha]] - **Date Received:** -\n"
        wikitext += "  * [[thirdpartyintel:TPI-Bravo]] - **Date Received:** -\n"
        wikitext += "  * [[thirdpartyintel:Archive]] - **Date Received:** -\n"
        
        wikitext += "====== Known Malicious Tools ======\n"
        wikitext += "===== Exploits =====\n"
        wikitext += "  * [[malcode:Alpha.exploit]] - Exploitation tool Alpha.\n"
        wikitext += "===== Implants =====\n"
        wikitext += "  * Alpha\n"
        wikitext += "    * AA: [[malcode:Alpha.implant]]\n"
        wikitext += "  * Bravo\n"
        wikitext += "    * BA: [[malcode:Bravo.implant]]\n"
        wikitext += "===== Utilities =====\n"
        wikitext += "  * [[malcode:Alpha.util]] - Alpha.util summary.\n"
        
        wikitext += "====== Sapho Tools ======\n"
        wikitext += "  * [[Sapho.util]] - Sapho.util summary.\n"
        
        wikitext += "====== Known Threat Actors ======\n"
        wikitext += "===== Known Threat Groups =====\n"
        wikitext += "  * [[actor:Actor Alpha]]\n"
        wikitext += "  * [[actor:Actor Bravo]]\n"
        wikitext += "===== Known Threat Actors =====\n"
        wikitext += "  * [[actor:Person Alpha]]\n"
        wikitext += "  * [[actor:Person Bravo]]\n"
        
        wikitext += "====== Templates ======\n"
        wikitext += "  * [[template:Set Page Template]]\n"
        wikitext += "  * [[template:Compromise Page Template]]\n"
        wikitext += "  * [[template:Attacker Tool Page Template]]\n"
        
        return wikitext
    
    def generateThirdPartyIntelligencePage(self):
        """docstring for generateThirdPartyIntelligencePage"""
        pass
    
    def generateExploitPage(self):
        """docstring for generateExploitPage"""
        pass
    
    def generateImplantsPage(self):
        """docstring for generateImplantsPage"""
        pass
    def generateUtilitiesPage(self):
        """docstring for generateUtilitiesPage"""
        pass
    def generateSaphoToolPage(self):
        """docstring for generateSaphoToolPage"""
        pass
    
    def generateKnownThreatGroupPage(self):
        """docstring for generateKnownThreatGroupPage"""
        pass
    
    def generateKnownThreatActorPage(self, actor_identifier=lipsum_word, date_audited="01/01/2000", given_name=lipsum_word, date_of_birth="01/01/2001", country_of_birth=lipsum_word, location=lipsum_word age="00", names_aliases = [lipsum_word, lipsum_word, lipsum_word], email_addresses = [lipsum_word, lipsum_word, lipsum_word], social_media_sites = ["twitter", "facebook", "linkedin"]):
        """Allows programatic generation of a page of a thrat actor. If no factors are given this generates a template page with dummy values."""
        wikitext = "====== %s ======" % actor_identifier
        wikitext += "^ Date Audited     | %s |" % date_audited
        wikitext += "^ Name             | %s |" % given_name
        wikitext += "^ DOB              | %s |" % date_of_birth
        wikitext += "^ Country of Birth | %s |" % country_of_birth
        wikitext += "^ Location         | %s |" % location
        wikitext += "^ Age              | %s |" % age
        
        wikitext += "===== Names/Aliases ====="
        for name_alias in names_aliases:
            wikitext += "  * %s" % name_alias
        
        wikitext += "===== Email Addresses ====="
        for email_address in email_addresses:
            wikitext += "  * %s" % email_address
        
        wikitext += "===== Social Media Sites ====="
        """Ideally would be formatted as tables. First version will be formatted as bullets."""
        wikitext += "^ IM Names | %s |" % date_audited
        wikitext += "^ Site/group Affiliation | %s |" % date_audited
        wikitext += "^ URLs | %s |" % date_audited
        wikitext += "^ Domain Data | %s |" % date_audited
        wikitext += "===== Screen Shots ====="
        wikitext += "===== Tools Used =====" 
        wikitext += "^ Google Searches and Links | %s |" % date_audited
        
        return wikitext
    
    # Common Elements Generators
    
    # Indicators
    def generateArpEntryIndicator( interface = lipsum, physicalAddress = lipsum, iPv6Address = lipsum
                                  iPv4Address = lipsum, cache = lipsum, interfaceType = lipsum, state = lipsum, isRouter = False, lastReachable = "01/01/2001 00:00:00", lastUnreachable = "01/01/2001 00:00:00"):
        wikitext = ""
    
    
    def generateNewsArticle(self, title=lipsum_short, author=lipsum_word, date="20000101", url="hxxp://www.example.com/article", article_body=lipsum):
        wikitext = "==== %s ====" % title
        wikitext += "^ Author | %s |" % author
        wikitext += "^ Date   | %s |" % date
        wikitext += "^ URL    | %s |" % url
        
        for line in artcile_body.split("\n"):
            print "> %s" % line
    
    
    def generateCookieIndicator(self, cookie_identifier = lipsum_word, browser_name = lipsum_word, browser_version = lipsum_word, username = lipsum_word, hostname = lipsum_word, cookie_path = lipsum_word, cookie_name = lipsum_word, cookie_value = lipsum_word, file_name = lipsum_word, file_path = lipsum_word, is_secure = lipsum_word, is_http_only = lipsum_word, creation_date = lipsum_word, expiration_date = lipsum_word, last_accessed_date = lipsum_word, last_modified_date = lipsum_word, cookie_flags = lipsum_word):
        """Generates text for a cookie."""
        wikitext = ""
        wikitext += " ^ BrowserName        | %s |" % (browser_name)
        wikitext += " ^ BrowserVersion     | %s |" % (browser_version)
        wikitext += " ^ Username           | %s |" % (username)
        wikitext += " ^ Host Name          | %s |" % (hostname)
        wikitext += " ^ Cookie Path        | %s |" % (cookie_path)
        wikitext += " ^ Cookie Name        | %s |" % (cookie_name)
        wikitext += " ^ Cookie Value       | %s |" % (cookie_value)
        wikitext += " ^ File Name          | %s |" % (file_name)
        wikitext += " ^ File Path          | %s |" % (file_path)
        wikitext += " ^ Is Secure          | %s |" % (is_secure)
        wikitext += " ^ Is Http Only       | %s |" % (is_http_only)
        wikitext += " ^ Creation Date      | %s |" % (creation_date)
        wikitext += " ^ Expiration Date    | %s |" % (expiration_date)
        wikitext += " ^ Last Accessed Date | %s |" % (last_accessed_date)
        wikitext += " ^ Last Modified Date | %s |" % (last_modified_date)
        wikitext += " ^ Cookie Flags       | %s |" % (cookie_flags)
        
        if cookie_identifier != lipsum_word:
            return [cookie_identifier, wikitext]
        else:
            print "Error: No identifier given to cookie."
            return [cookie_identifier, wikitext]
    
    
    def postAsPage(self, pagename, wikitext):
        """docstring for postAsPage"""
        pass

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "ho:v", ["help", "output="])
        except getopt.error, msg:
            raise Usage(msg)
        
        # option processing
        for option, value in opts:
            if option == "-v":
                verbose = True
            if option in ("-h", "--help"):
                raise Usage(help_message)
            if option in ("-o", "--output"):
                output = value
            
    except Usage, err:
        print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
        print >> sys.stderr, "\t for help use --help"
        return 2


if __name__ == "__main__":
    sys.exit(main())