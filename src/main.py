import os
import asyncio
import aiofiles


async def copy_file(source_path, dest_path, chunk_size=65536):
    """
    Asynchronously copies a file from source_path to dest_path.

    Args:
        source_path (str): The path to the source file.
        dest_path (str): The path to the destination file.
        chunk_size (int, optional): The size of chunks to read/write. 
                                     Defaults to 65536 bytes (64KB).
    """
    print(f"Copying {source_path} to {dest_path}")
    try:
        async with aiofiles.open(source_path, 'rb') as f_in:
            async with aiofiles.open(dest_path, 'wb') as f_out:
                while True:
                    chunk = await f_in.read(chunk_size)
                    if not chunk:
                        break
                    await f_out.write(chunk)
        print(f"Finished copying {source_path} to {dest_path}")
        return True
    except FileNotFoundError:
        print(f"File not found: {source_path}")
    except Exception as e:
        print(f"Error copying file {source_path} to {dest_path}: {e}")
    return False


async def main():
    DIR = '/input'

    tasks = []

    for name in os.listdir('/output'):
        os.remove(os.path.join('/output', name))
        print(f"Removed existing file: {name}")

    for name in os.listdir(DIR):
        tasks.append(copy_file(
            os.path.join(DIR, name),
            os.path.join('/output', name)
        ))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
