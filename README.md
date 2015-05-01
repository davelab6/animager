Animager
=======

##A tool to easily animate your graphic design or illustration project.

Save and git commit step by step, your graphic design process and use Animager to build a video to show the progress.
Animager users Git - a version control system to record and grab all the stages of your design project. Use [Sparkleshare](http://sparkleshare.org/) to easily commit file. What Animager does is rolling the git commits and capture the image for each commit as a temporary image, collect all temporary images and build a video.


###Supported image formats

Animager uses imagemagick to convert the images. Supported image format list is [here.](http://www.imagemagick.org/script/formats.php) 


###Dependencies
  - ffmpeg
  - imagemagick
  - python3
  - C++ compiler - g++


###Install


```
cd src
```

```
sh install.sh
```

###How to use animager

Once you are done and ready to generate a video..

```
animager -p hd-720p -i [path-to-your-image] -o [path-to-your-output-folder]
```

Example: `animager -p hd-720p -i /home/lahiru/sparkleshare/test/drawing.svg -o /home/lahiru/desktop`

If you don't mention -o [path-to-your-output-folder] here, video will be saved as ~/animager/out.mp4

###Other options

- Get a list of profiles
`animager -plist all`

- Create a new profile
`animager -pnew profileName -h height -w weight -f frameRate`

Example: `animager -pnew test -h 240 -w 320 -f 30`




###ToDo


###Credits


###License


Animager is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published bythe Free Software Foundation, either version 2 of the License, or (at your option) any later version.
