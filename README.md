# Moody-Images

Moody-Images is the images component of the [`Moody`](https://github.com/tsomic/moody) project. It contains all of the facial expressions as `.png` files and a python script to convert them to the `faces.h` file used by [`moody-arduino`](https://github.com/tsomic/moody-arduino).

<br/>

## About

You should not clone this repository on its own but as part of the [`main repository`](https://github.com/tsomic/moody) (go there for details).

This project contains an `images` folder with a subdirectory for every facial expression. These subdirectories are named accordingly and must contain exactly two images each - the two animation frames of each facial expression.

To change these images (adding, removing, editing) I suggest using the [`moody-mapper`](https://github.com/tsomic/moody-mapper), as every image has to be converted to binary data for the arduino to use. The [`moody-mapper`](https://github.com/tsomic/moody-mapper) does this automatically and also includes an image editor specifically for facial expressions.

You can add images here by yourself, but it is not recommended.  
All images have to be 32x16 pixels. They will be upscaled on the Arduino board to fit the whole 128x64 display.
Furthermore the images should be in black and white.
Every other color gets converted to be black or white, but note that the colors will be inverted when the Arduino board displays them.  

Be aware that you cannot remove the `hot`, `cold` or `shock` facial expressions, because they are hard-coded into the Arduino project. You would firstly have to edit that code too.

<br/>

## Contributing

Contributions are welcome! If you have ideas for new features, find any bugs, or would like to make improvements, please open an issue or submit a pull request.

<br/>

## License

The Moody-Images project is licensed under the GNU GPLv3 license. See the [`LICENSE`](https://github.com/tsomic/moody-images/blob/main/LICENSE) file for more information.
