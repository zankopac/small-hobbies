#!/usr/bin/env python3

#import requests
import asyncio
import aiohttp
import time

start =time.time()
url = "https://www.xn--franek-l2a.si/api/find_approximate"
terms = ["abeceda", "asdfjh"]
results = []

words =  []

async def get_symbols():
	async with aiohttp.ClientSession() as session:
		tasks = [session.post(url, data = {"term":w}, ssl=False) for w in words]
		responses =await asyncio.gather(*tasks)
		
		for i in range(len(responses)):
			body = await responses[i].json()
			if len(body["response"]) > 0:
				firstSuggested = body["response"][0]["text"]
				print(words[i]+", firstSuggested: "+firstSuggested)
				if words[i] == firstSuggested:
					#print(str(count) + " / " + str(len(words)))
					print("correct: " + words[i])


#asyncio.run(get_symbols())
end = time.time()
#print(results)



def solve(s):
	st_arr = []

	for i in range(len(s)-1,-1,-1):
		for j in range(len(st_arr)):
			st_arr.append(s[i]+st_arr[j])
		#if len(s[i]) > 2:
		st_arr.append(s[i])
	return st_arr

def keep(w):
	for l in w:
		spl = w.split(l)
		spl2 = spl[1:-1]
		if '' in spl2:
			return False
	return True






letterList = []
numOfLetters = len(letterList)

#for n in range(3,numOfLetters):
	
letters = "raabspel"
words = solve(letters)
words = list(filter(lambda w: len(w)>2, words))
words = list(dict.fromkeys(words))
words = list(filter(lambda w: keep(w), words))
print(words)




count = 0

asyncio.run(get_symbols())
"""
for w in words:
	


	response = requests.post("https://www.xn--franek-l2a.si/api/find_approximate", data = {"term":w})
	body = response.json()
	if len(body["response"]) > 0:
		firstSuggested = body["response"][0]["text"]
		if w == firstSuggested:
			print(str(count) + " / " + str(len(words)))
			print(w)
	count = count+1

"""



