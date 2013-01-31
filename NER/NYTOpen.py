from calais import Calais
import os

API_KEY = "v5q6rvm7h4uww6sumjxuw9t7"
calais = Calais(API_KEY, submitter="python-calais demo")

f = open("Text/test.txt", 'r+')
NYT = f.read()
f.close()

result = calais.analyze(NYT)

result.print_summary()
result.print_entities()
