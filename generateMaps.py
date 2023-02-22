from PIL import Image
import os
from textwrap import wrap

# Set up file paths
maindir = os.getcwd()
imagesdir = os.path.join(maindir, "images")
directory = os.fsencode(imagesdir)

# Initialize array string
array = "static const byte allFaces[][2][64] PROGMEM = {\n"

# Iterate over subdirectories
for index, folder in enumerate(sorted(os.listdir(directory))):
    foldername = folder.decode("utf-8")
    fullfolder = os.path.join(imagesdir, foldername)

    # Check if current item is a directory
    if os.path.isdir(fullfolder):
        # Initialize string to hold faces for current directory
        faces = ""

        # Iterate over files in directory that end with supported image formats
        for file in sorted([f for f in os.listdir(fullfolder) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp'))]):
            filepath = os.path.join(fullfolder, file)
            im = Image.open(filepath)
            px = im.load()

            # Create string of pixel values for current face
            data = ""
            for y in range(16):
                for x in range(32):
                    data += str(int(px[x, y][0] == 0))

            # Format pixel values into binary format for current face
            face = ""
            octets = wrap(data, 8)
            for i in range(64):
                face += "0b" + octets[i] + ", "
            face = face[:-2]

            # Add current face to string of faces for current directory
            faces += "    {" + face + "},\n"
        faces = faces[:-2]

        # Add string of faces for current directory to array string
        array += "  {\n" + faces + "\n  },\n"
array = array[:-2] + "\n};\n"

# Write array string to faces.h file
with open(os.path.join(maindir, "../moody-arduino/moody/faces.h"), "w") as f:
    f.write(array)

print("done")
