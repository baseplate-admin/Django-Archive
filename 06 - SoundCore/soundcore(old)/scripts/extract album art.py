import os

path = f"{os.getcwd()}/Music"

for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        # print(os.path.join(root, name))

        filename = os.path.join(root, name)
        jpg_name = os.path.join(root, name[0:-5])

        print(filename)

        os.system(
            f"ffprobe -v quiet -print_format json -show_format -show_streams '{filename}' > '{jpg_name}.json'"
        )
        os.system(f"ffmpeg -i '{filename}' -c:v copy '{jpg_name}.jpg'")
