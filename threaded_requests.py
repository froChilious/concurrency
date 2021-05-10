#!/usr/bin/env python3

from concurrent import futures
import threading
import requests
import time

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local,"session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        pass
        #print(f"read {len(response.content)} from {url}")

def download_all_sites(sites, workers):
    with futures.ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(download_site, sites)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    loops = 10
    workers = {}
    for worker in range(15,21,1):
        workers[worker] = []
        for loop in range(loops):
            start_time = time.time()
            download_all_sites(sites,worker)
            duration = time.time() - start_time
            workers[worker].append(duration)
        print(f"downloaded {len(sites)} in an average {sum(workers[worker])/len(workers[worker]):.2f} seconds with {worker} workers over {loops} loops")

print(workers)