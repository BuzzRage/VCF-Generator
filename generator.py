#!/usr/bin/python


# TODO:
# - User interface for entering info
# - Format thoses infos according to the RFC 6350 (which version ?)
# - Export result !


# Required Properties
RPROP = "BEGIN VERSION FN N END".split()

# Supported Properties
SPROP = "ADR BDAY CATEGORIES EMAIL NAME NICKNAME NOTE RELATED REV ROLE TEL TITLE TZ UID ".split()


vCard = ""

vCard += "BEGIN:VCARD"
vCard += "VERSION:3.0"

# Insert content here

vCard += "END:VCARD"


# vCards example:
# 
# BEGIN:VCARD
# VERSION:3.0
# N:Gump;Forrest;;Mr.;
# FN:Forrest Gump
# ORG:Bubba Gump Shrimp Co.
# TITLE:Shrimp Man
# PHOTO;VALUE=URI;TYPE=GIF:http://www.example.com/dir_photos/my_photo.gif
# TEL;TYPE=WORK,VOICE:(111) 555-1212
# TEL;TYPE=HOME,VOICE:(404) 555-1212
# ADR;TYPE=WORK,PREF:;;100 Waters Edge;Baytown;LA;30314;United States of America
# LABEL;TYPE=WORK,PREF:100 Waters Edge\nBaytown\, LA 30314\nUnited States of America
# ADR;TYPE=HOME:;;42 Plantation St.;Baytown;LA;30314;United States of America
# LABEL;TYPE=HOME:42 Plantation St.\nBaytown\, LA 30314\nUnited States of America
# EMAIL:forrestgump@example.com
# REV:2008-04-24T19:52:43Z
# END:VCARD