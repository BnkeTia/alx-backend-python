#!/usr/bin/env python3
"""Module that takes an integer and returns an async task"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """A regular function to create an async task"""

    async_task = asyncio.create_task(wait_random(max_delay))
    return async_task
