#!/usr/bin/python

import webapp
import random


class aleatorioServidor(webapp.webApp):

	def process(self, parsedRequest):
		return ("307 Temporary Redirect" + "\n" +  "Location: http://localhost:1234/" + str(random.randrange(10000000000000)), "")

if __name__ == "__main__":
	servaleat = aleatorioServidor("localhost", 1234)
