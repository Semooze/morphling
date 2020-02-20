import asyncio

from aiofile import AIOFile, LineReader


class Reader:
    def __init__(self):
        return

    async def _async_read(self, file_path):
        async with AIOFile(file_path, 'r') as afp:
            return await afp.read()

    def read(self, file_path):
        return asyncio.run(self._async_read(file_path))

    async def _async_read_line(self, file_path):
        async with AIOFile(file_path, 'r') as afp:
            async for line in LineReader(afp):
                print(line)
                # return afpl.readline()

    def read_line(self, file_path):
        return asyncio.run(self._async_read_line(file_path))
