"""
    Converts A youtube video to GIF.
        Accepts : URL <-- Query
"""

# Import BytesIO for in memory management
import io

# Optional typing helpers
#   BinaryIO <-- IO object
from typing import Optional, BinaryIO

# Import ImageIO for converting MP4 to GIF.
import imageio

# Async to sync for enabling caching the sync
from asgiref.sync import async_to_sync

# Django HTTP response
#   Http404         <-- For showing 404 page
#   HttpResponse    <-- For showing gif response
from django.http import Http404, HttpResponse

# Django cache Framework
from django.views.decorators.cache import cache_page

# Pytube for YouTube-DL replacement
from pytube import YouTube

# Import random for Generating A random string
import random

# import string for Generating a random string
import string

# Import os for getting current directory and removing files
import os

# Import asyncio for async friendly operations
import asyncio


# Create your views here.


async def mp4_to_gif(url: str, buffer: BinaryIO) -> None:
    """
        Converts a mp4 to a gif.
            Input:
                binary: Byte like object

    """

    async def youtube_downloader(link: Optional[str], binary: BinaryIO) -> None:
        """
            Downloads the youtube file and writes it to a BytesIO object.
                Input:
                    link    <-- Str / Youtube link
                    binary  <-- Io Object / io.BytesIO()
                Output:
                    Bytes written to binary object
        """
        yt = YouTube(link)  # Query youtube
        stream = yt.streams.get_by_itag(137)  # Get 1080p/mp4
        stream.stream_to_buffer(binary)  # Write to binary object

    async def add_files_to_delete(file_location: str):
        """
            File delete helper function.
                Input:
                    file_location <-- String / Path
                Output:
                    Deleted File
        """
        await asyncio.sleep(.01)
        os.remove(file_location)

    async def get_temp_file_location(file_type: str) -> str:

        """
            Random File Name generator Helper Function
                Input:
                    file_type  <-- File MIME Type eg: '.mp4, .mp3
                Output:
                    random file name generated.
                    if input if ('.mp4) it may return C:\\Programming\\Social Media\\core\\temp\\fmfvbnsjmdfdsoue.mp4
        """
        # Check if theres a temp dir.
        if not os.path.isdir(f'{os.getcwd()}/temp'):
            os.mkdir(f'{os.getcwd()}/temp')  # Make a temp dir.
        file_name = ''.join(random.choice(string.ascii_lowercase) for _ in
                            range(16))  # Generate a random string consisting of 16 characters.

        file_path = f'{os.getcwd()}/temp/{file_name}.{file_type}'  # Combine Current Dir and file_type

        # Check if file exists.
        #   if file is there, execute the function again. If no file is there return the path
        if os.path.isfile(file_path):
            await get_temp_file_location(file_type)

        elif not os.path.isfile(file_path):
            return file_path

    # In memory object for youtube_downloader
    in_memory = io.BytesIO()
    # Pass the url to Youtube Downloader
    await youtube_downloader(url, in_memory)

    # Generate a random .mp4 file in 'currentdir/temp/'
    binary_to_mp4_location = await get_temp_file_location('mp4')

    f = open(binary_to_mp4_location, 'wb')  # Open the file for write binary operation
    f.write(in_memory.getvalue())  # Write Binary content to file generated above
    f.close()  # Close the file so we can delete this

    in_memory.truncate(0)  # Remove the unnecessary bytes
    in_memory.seek(0)  # set Cursor POS to 0

    reader = imageio.get_reader(binary_to_mp4_location)  # Read the content of files from the .mp4 file
    fps = reader.get_meta_data()['fps']  # Get FPS data

    # Generate a random .gif file in currentdir/temp/
    save_location = await get_temp_file_location('gif')
    # Save the modified GIF binary data to the file
    writer = imageio.get_writer(save_location, fps=fps)

    # Some weird thing copied from docs
    for i, im in enumerate(reader):
        writer.append_data(im)

    # Close the file so that we can delete this.
    writer.close()

    # Open the file again so that we can flush binary to buffer
    f = open(save_location, 'rb')  # Open as read binary mode.
    buffer.write(f.read())  # Flush binary content from file to buffer
    f.close()  # Close the file for delete

    # Delete the temporary files.
    await add_files_to_delete(binary_to_mp4_location)
    await add_files_to_delete(save_location)


@cache_page(60 * 15)
@async_to_sync
async def youtube_to_gif(request):
    """
        Converts a youtube video to gif.
            Accepts:
                GET
            Returns:
                'image/gif'
    """
    if request.method == "GET":
        # Get the url from query
        url = request.GET['url']

        # if theres no url return HTTP404
        if not url:
            return Http404

        # In_memory_gif object for getting the values from the main function
        in_memory_gif = io.BytesIO()

        # Get the data
        await mp4_to_gif(url, in_memory_gif)

        # save the data to variable
        data = in_memory_gif.getvalue()

        # Memory management
        in_memory_gif.truncate(0)
        in_memory_gif.seek(0)

        return HttpResponse(data, content_type='image/gif')
    elif request.method == "POST":
        return Http404
