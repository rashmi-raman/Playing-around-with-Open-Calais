from calais import Calais
import os

API_KEY = "v5q6rvm7h4uww6sumjxuw9t7"
calais = Calais(API_KEY, submitter="python-calais demo")

fid = input('Please choose the text of the article to be enriched: \n1. The Economist\n2.The Guardian\n3.The Mirror\n4.The Independent\n5.The Daily Mail\n Choose from 1-5 :')

if fid==1:
	fname = "Text/economist.txt";
	htmlname = "Text/economist.html";
elif fid ==2:
	fname = "Text/guardian.txt";
	htmlname = "Text/guardian.html";
elif fid ==3:
	fname = "Text/mirror.txt";
	htmlname = "Text/mirror.html";
elif fid ==4:
	fname = "Text/independent.txt";
	htmlname = "Text/independent.html";
else:
	fname = "Text/dailymail.txt";
	htmlname = "Text/dailymail.html";


f = open(fname, 'r+')
article = f.read()
f.close()

filter = ['Currency', 'IndustryTerm' , 'MedicalCondition']

result = calais.analyze(article)

#result.print_summary()
result.print_entities()

article = article.decode('ascii', 'replace').encode('ascii', 'replace')
enriched_article = article;

for entity in result.entities:
	if entity['_type'] not in filter:
		name = entity['name']
		print "Resolving " + name
		name = name.decode('ascii', 'replace').encode('ascii', 'replace')
		str = ""
		try:
			link = entity['resolutions'][0]['id']
			str = '<a href=\"' + link + '\">' + name + '</a> '
			print 'Reference detected in OpenCalais'
		except KeyError:
			link = entity['name']
			link = name.replace(' ','_')
			url = "http://en.wikipedia.org/wiki/" + link
			str = '<a href=\"' + url + '\">' + name + '</a> '
			print 'Reference not detected in OpenCalais, hence linking to Wikipedia'
		enriched_article = enriched_article.replace(name,str);

enriched_article = enriched_article.replace("\n","</p><p>");	
fo = open(htmlname, "wb")
fo.write("<html><head><title>Enriched article</title></head><body><p>" + enriched_article + "</body></html>")
fo.close()

print "Updated enriched text : " + htmlname

#fo = open(htmlname, "rb")
#str = fo.read()
#print str
#fo.close()