import os
import asyncio
import aiofiles
import shutil


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
        if os.path.isfile(source_path):
            async with aiofiles.open(source_path, 'rb') as f_in:
                async with aiofiles.open(dest_path, 'wb') as f_out:
                    while True:
                        chunk = await f_in.read(chunk_size)
                        if not chunk:
                            break
                        await f_out.write(chunk)
            print(f"Finished copying file {source_path} to {dest_path}")
        else:
            for item in os.listdir(source_path):
                await copy_file(
                    os.path.join(source_path, item),
                    os.path.join(dest_path, item)
                )
        return True
    except FileNotFoundError:
        print(f"File not found: {source_path}")
    except Exception as e:
        print(f"Error copying file {source_path} to {dest_path}: {e}")
    return False


async def main():
    DIR = '/input'

    for name in os.listdir('/output'):
        if os.path.isdir(os.path.join('/output', name)):
            shutil.rmtree(os.path.join('/output', name))
            print(f"Removed existing directory: {name}")
        else:
            os.remove(os.path.join('/output', name))
            print(f"Removed existing file: {name}")

    for name in os.listdir(DIR):
        await copy_file(
            os.path.join(DIR, name),
            os.path.join('/output', name)
        )


if __name__ == "__main__":
    asyncio.run(main())
