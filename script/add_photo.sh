#!/bin/bash

# settings
image=$1
path_raw=blog_app/media/photos/raw/
path_resized=blog_app/media/photos/
path_mini=blog_app/media/photos/mini/
path_tmp=blog_app/media/photos/tmp/

# resize
convert $path_raw$image -define jpeg:extent=800kb $path_resized$image

# make mini
convert $path_raw$image -resize 500x500^ -gravity center -crop 500x500+0+0 $path_mini$image
if [[ $image == *.gif ]] || [[ $image == *.GIF ]]
then
	mkdir path_tmp
	convert $path_raw$image -coalesce $path_tmp"temporary.gif"
	convert -size $(identify -format "%wx%h" $image) $path_tmp"temporary.gif" -resize 500x500^ $path_mini$image
	convert blog_ag/blog_app/media/photos/mini/$(basename $image) -gravity center -crop 500x500+0+0 +repage $path_mini$image
fi
