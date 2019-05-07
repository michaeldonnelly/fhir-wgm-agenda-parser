# fhir-wgm-agenda-parser
Take the FHIR-I agenda for an HL7 WGM and turn it into a TSV file.

1. Go to the [FHIR agenda page](http://wiki.hl7.org/index.php?title=FHIR_Agenda_201905_WGM)
2. Edit the wiki page
3. Copy the contents starting with the first line of actual schedule
4. Paste it into the file fhir.before.txt in the same directory with fhir_agenda.py
5. Run fhir_agenda.py
6. The results will be in fhir.after.tsv
7. Open fhir.after.tsv with Excel
