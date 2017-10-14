#!utf-8
import aiohttp
import asyncio
import async_timeout
import json
from .logconfig import logging
import time
                
class spider():

    def __init__(seeds):
        self.seeds=selkkljljleds
        
    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(loop))
        async def main(loop):
            async with aiohttp.ClientSession(skip_auto_headers=['User-Agent'],\
            loop=loop) as session:            
                req=self.before_fetch(self.seeds)
                rep=await self.fetch(session,req)
                rep_status,rep_content=await self.check(rep)
                if rep_status!="$$Deprecate":
                    await after_response(rep_content)
                else:
                    self.deprecate_process(req,rep_content)

    def before_fetch(s):
        # before_hooks        
        return s

    async def fetch(self,session,req):
        with async_timeout.timeout(req["wait_time"]):
            async with session.request(req["method"],req["url"],params=req["params"]\
            ,proxy=req["proxy"]) as response:
                return await response.text()

    async def check(self,rep):
        return "$$success",rep

    async def after_response(self,rep):
        #after_hooks
        pass

    def deprecate_process(req,rep):


params= {"limit":500,\
"format":"geojson",\
"ak":'''ZDdiNzc0ZTE1YTg1NGNkMThmZmZkY2EwNTE4MGU1YWY'''}

index=None
with open("./index.json","r",encoding="utf8") as f:
    index=json.loads(f.read())
seeds=({url:"http://geohey.com/s/public_data/{}/query".format(i['uid']),params:params}\
 for i in index["data"]["items"])

 geohey_spider=spider(seeds)
 @geohey_spider.before_hooks
 def