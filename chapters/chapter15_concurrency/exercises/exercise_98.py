# Exercise 98 - Asynchronous Processing
# Write an asynchronous function that fetches data from multiple sources and processes it concurrently.
# The function should take a list of sources and return a list of processed data.

import asyncio
import random


async def fetch_data(source: str) -> str:
    await asyncio.sleep(random.uniform(0.1, 1.0))  # Simulate a network delay
    return f"Data from {source}"


async def process_data(sources: list[str]) -> list[str]:
    tasks = [fetch_data(source) for source in sources]
    results = await asyncio.gather(*tasks)
    return results
