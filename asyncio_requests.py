import asyncio
import time
import aiohttp

async def download_site(session,url):
    async with session.get(url) as response:
        pass
        #print(f"Read {response.content_length} from {url}")

async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session,url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions = True)

def main():
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    duration = time.time() - start
    print(f"Downloaded {len(sites)} sites in {duration} seconds")
    return duration

if __name__ == "__main__":
    durations = []
    for loop in range(10):
        duration = main()
        durations.append(duration)
    print(sum(durations)/len(durations))
    