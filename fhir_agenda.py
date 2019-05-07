import re

def header():
	return "Quarter\tWorkgroup\tRoom\tCo-chairs\tTopic\tWho is going"
	
def agendaLine(text,quarter):
	if len(text) < 1:
		return ""
	if text[0:1] == "=":
		return ""
	if text[0:3] == "'''": 
		return sessionLine(text,quarter)
	else:
		return contentLine(text)

def sessionLine(text, quarter):
	session = text.split(" - ")
	
	out = []
	out.append(quarter)
	try:
		out.append(workgroups(session[1]))
	except IndexError:
		out.append("")

	try:
		out.append(session[0].replace("'''", ""))
	except IndexError:
		out.append("")
		
	try:
		out.append(session[2])		# cochair
	except IndexError:
		out.append("")
	
	return "\t".join(out) + "\t"
	
def contentLine(text):
	
	return "#STRIPCRBEFORE#" + text[2:len(text)] + "; "
	return text
	
def workgroups(groups):
	groups = groups.replace("PA", "Patient Administration")
	groups = groups.replace("CH", "Child Health")
	groups = groups.replace("FMG", "FHIR Management Group")
	groups = groups.replace("FM", "Financial Management")
	groups = groups.replace("BRR", "Biomedical Research and Regulation")
	groups = groups.replace("BR&R", "Biomedical Research and Regulation")
	groups = groups.replace("CG", "Clinical Genomics")
	groups = groups.replace("EHR", "Electronic Health Records")
	groups = groups.replace("MnM", "Modeling & Methodology")
	groups = groups.replace("AWG", "Attachments")
	groups = groups.replace("CBCP", "Community Based Care and Privacy")
	groups = groups.replace("CDS", "Clinical Decision Support")
	groups = groups.replace("CIC", "Clinical Interoperability Council")
	groups = groups.replace("CIMI", "Clinical Information Modeling Initiative")
	groups = groups.replace("CQI", "Clinical Quality Information")
	groups = groups.replace("Conform", "Conformance & Guidance for Implementation/Testing")
	groups = groups.replace("FGB", "FHIR Governance Board")
	groups = groups.replace("FTSD", "Foundation and Technology Steering Division")
	groups = groups.replace("HCD", "Devices")
	groups = groups.replace("HSI", "Healthcare Standards Integration")
	groups = groups.replace("IHE", "Integrating the Healthcare Enterprise")
	groups = groups.replace("InM", "Implementation & Messaging")
	groups = groups.replace("MH", "Mobile Health")
	groups = groups.replace("OHT", "Open Health Tools")
	groups = groups.replace("PC", "Patient Care")
	groups = groups.replace("Sec", "Security")
	groups = groups.replace("SOA", "Service Oriented Architecture")
	groups = groups.replace("Temp", "Templates")
	#groups = groups.replace("Voc", "Vocabulary")	 # often already written out
	#groups = groups.replace("SD", "Structured Documents")	# false positives
	groups = groups.replace("OO", "Orders & Observations")
	groups = groups.replace("PH", "Public Health, Emergency Response")
	groups = groups.replace("Pharm", "Pharmacy")
	groups = groups.replace("ITS", "Implementation Technology Services")
	groups = groups.replace("II", "Imaging Integration")
	groups = groups.replace("EST", "Electronic Services & Tooling")
	groups = groups.replace("AID", "Application Implementation & Design")
	return groups

tf = 'fhir.before.txt'
file = open(tf, 'r')
text = file.read()
file.close()

text = text.replace("\t", "   ")
output = [header()]
textArray = text.split("\r\n")
quarter = ""
for line in textArray:
	if line[0:2] == "==":
		quarter = line.split("==")[1]
		output.append("#NEWSECTION#")
	else:
		output.append(agendaLine(line, quarter))

text = "\r\n".join(output)

text = text.replace("\r\n#STRIPCRBEFORE#; ", "")
text = text.replace("\r\n#STRIPCRBEFORE#", "")
text = text.replace("; \r\n", "\r\n")
text = text.replace("\r\n\r\n", "\r\n")
text = text.replace("\r\n\r\n", "\r\n")
text = text.replace("#NEWSECTION#","\r\n" + header())

resultFile = open('fhir.after.tsv','w')
resultFile.write(text)
resultFile.close()