#!/usr/bin/python


# TODO:
# - User interface for entering info
# - Format thoses infos according to the RFC 6350 (which version ?)
# - Export result !

#TOCHECK:
# - "Individual lines within vCard are delimited by the [RFC5322] line
#   break, which is a CRLF sequence (U+000D followed by U+000A)."
#   C'est \r\n ou \n\r ?

# Required Properties
RPROP = "BEGIN VERSION FN N END".split()

# Supported Properties
SPROP = "ADR BDAY CATEGORIES EMAIL NAME NICKNAME NOTE RELATED REV ROLE TEL TITLE TZ UID ".split()


vCard = ""

vCard += "BEGIN:VCARD\n\r"
vCard += "VERSION:3.0\n\r"

print("VCARDS generator - Entrez vos informations: ")
name 		= input("Nom: ")
surname = input("Prenom: ")
tel 		= input("Tel: ")
email 	= input("Email: ")

# TODO: Verifier les inputs

vCard += "N:"+name+";"+surname+";\n\r"
vCard += "FN:"+surname+" "+name+"\n\r"
vCard += "TEL;TYPE=cell:(+33)"+tel+"\n\r"
vCard += "EMAIL:"+email+"\n\r"

vCard += "END:VCARD\n\r"

print("\nGenerated vCard:\n\n")
print(vCard)

# TODO: exporter/enregistrer dans un fichier



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