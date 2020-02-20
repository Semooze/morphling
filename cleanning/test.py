import pandas as pd
import csv
#help(pd.read_csv)
import asyncio
from aiofile import AIOFile, Reader

# import pdb; pdb.set_trace()


async def main():
    async with AIOFile("/tmp/hello.txt", 'r') as afp:
        async for line in LineReader(afp):
            print(line[:-1])
        data = await afp.read()
        line = data.split(',')
        print(line)
asyncio.run(main())