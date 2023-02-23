# Moody-Images

Moody-Images is the images component of the [`Moody`](https://github.com/tsomic/moody) project. It contains all of the facial expressions as `.png` files and a python script to convert them to the `faces.h` file used by [`moody-arduino`](https://github.com/tsomic/moody-arduino).

<br/>

## About

You should not clone this repository on its own but as part of the [`main repository`](https://github.com/tsomic/moody) (go there for details).

This project contains an `images` folder with a subdirectory for every facial expression. These subdirectories are named accordingly and must contain exactly two images each - the two animation frames of each facial expression.

The name of the image files doesn't matter, but note that only `JPEG`, `PNG` and `BMP` files are being processed.  
Also all images have to be 32x16 pixels. They will be upscaled on the Arduino board to fit the whole 128x64 display.

If you would like to create new facial expressions, keep in mind these correct dimensions.  
Furthermore the images should only be black and white, but note that the colors will be inverted when the Arduino board displays them.  
To help creating or editing facial expressions, you can use [this codepen I made](https://codepen.io/nilskeller/full/LYdaBVM).

If you changed the images in any way and want them to be used by the Arduino board, you need to generate a new `faces.h` file by running the [python script](https://github.com/tsomic/moody-images/blob/36e5a57a68c0a09ebdca15dc0849f9e1c6ae8dc2/generate_maps.py). The file will automatically overwrite the current one in the folder of the Arduino project.

<br/>

## Contributing

Contributions are welcome! If you have ideas for new features, find any bugs, or would like to make improvements, please open an issue or submit a pull request.

<br/>

## License

The Moody-Images project is licensed under the GNU GPLv3 license. See the [`LICENSE`](https://github.com/tsomic/moody-images/blob/main/LICENSE) file for more information.
