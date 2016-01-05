import sears
import kmart
import urllib
import json
import sys
import os

def get_html2(x):
	a = sears.get_cells( sears.cell1, x)
	b = sears.make_rows(a)
	return b

def get_html(x):
	a = sears.get_cells( sears.cell0, x)
	b = sears.make_rows(a)
	return b

def get(keyword):
	a = sears.get_from_internet( 'Sears',keyword)
	b = kmart.get_from_internet( 'Kmart',keyword)
	a.extend(b)
	return a

def get_json(keyword):
	a = sears.get_from_internet( 'Sears',keyword)
	b = json.dumps(a)
	return b


