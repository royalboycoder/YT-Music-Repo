import os
import re
import textwrap

import aiofiles
import aiohttp
import numpy as np
import random

from PIL import Image, ImageChops, ImageOps, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from youtubesearchpython.__future__ import VideosSearch

from Royalkifeelings.etc import colors
from Royalkifeelings.callmusic.config import YOUTUBE_IMG_URL



def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


def add_corners(im):
    bigsize = (im.size[0] * 3, im.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    ImageDraw.Draw(mask).ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(im.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, im.split()[-1])
    im.putalpha(mask)


async def play_thumb(videoid):
    if os.path.isfile(f"cache/pfinal{videoid}.png"):
        return f"cache/pfinal{videoid}.png"
    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                result["viewCount"]["short"]
            except:
                pass
            try:
                result["channel"]["name"]
            except:
                pass

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/play{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        border = random.choice(colors)
        youtube = Image.open(f"cache/play{videoid}.png")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        enhancer = ImageEnhance.Brightness(image2)
        img = enhancer.enhance(1.1)
        try:
            os.remove(f"cache/pfinal{videoid}.png")
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass 
        img.save(f"cache/pfinal{videoid}.png")
        return f"cache/pfinal{videoid}.png"
    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL


async def queue_thumb(videoid):
    if os.path.isfile(f"cache/qfinal{videoid}.png"):
        return f"cache/quefinal{videoid}.png"
    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                result["viewCount"]["short"]
            except:
                pass
            try:
                result["channel"]["name"]
            except:
                pass

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/queue{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        border = random.choice(colors)
        youtube = Image.open(f"cache/play{videoid}.png")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        enhancer = ImageEnhance.Brightness(image2)
        img = enhancer.enhance(1.1)
        try:
            os.remove(f"cache/qfinal{videoid}.png")
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass
        img.save(f"cache/qfinal{videoid}.png")
        return f"cache/qfinal{videoid}.png"
    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL
