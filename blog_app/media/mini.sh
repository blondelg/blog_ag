#!/bin/bash

while [ a == a ]
do
for folder in *
do
# test if output folder exists
if [[ ! -d $folder/mini ]] && [[ -d $folder ]]
then
	# if not exists create it
	mkdir $folder/mini
elif [ -d $folder ]
then
	# delete existing images
	rm -f $folder/mini/*
fi

# loop on files
for image in $folder/*
do

	if [[ $image == *.jpg ]] || [[ $image == *.png ]] || [[ $image == *.jpeg ]] || [[ $image == *.JPG ]]
	then
		convert $image -resize 500x500^ -gravity center -crop 500x500+0+0 $folder/mini/$(basename $image)
	fi

	if [[ $image == *.gif ]] || [[ $image == *.GIF ]]
	then
		mkdir tmp
		convert $image -coalesce tmp/temporary.gif
		convert -size $(identify -format "%wx%h" $image) tmp/temporary.gif -resize 500x500^ $folder/mini/$(basename $image)
		convert $folder/mini/$(basename $image) -gravity center -crop 500x500+0+0 +repage $folder/mini/$(basename $image)
	fi

done
done
sleep 1h
done
