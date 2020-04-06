#!/bin/bash


# loop in raw image
for image in blog_ag/blog_app/media/photos/raw/*
do
	
	# test if each raw image has been resized
	if [[ ! -e blog_ag/blog_app/media/photos/$(basename $image) ]]
	then
	# rezise
	if [[ $image == *.jpg ]] || [[ $image == *.png ]] ||     [[ $image == *.jpeg ]] || [[ $image == *.JPG ]]
	then
		echo rezise $image
		convert $image -define jpeg:extent=800kb blog_ag/blog_app/media/photos/$(basename $image)
	fi
	fi

	# test if each raw image has been miniaturised
        if [[ ! -e blog_ag/blog_app/media/photos/mini/$(basename $image) ]]
	then
	echo make mini $image
	if [[ $image == *.jpg ]] || [[ $image == *.png ]] || [[ $image == *.jpeg ]] || [[ $image == *.JPG ]]
	then
		convert $image -resize 500x500^ -gravity center -crop 500x500+0+0 blog_ag/blog_app/media/photos/mini/$(basename $image)
	fi

	if [[ $image == *.gif ]] || [[ $image == *.GIF ]]
	then
		mkdir blog_ag/blog_app/media/tmp
		convert $image -coalesce blog_ag/blog_app/media/tmp/temporary.gif
		convert -size $(identify -format "%wx%h" $image) blog_ag/blog_app/media/tmp/temporary.gif -resize 500x500^ blog_ag/blog_app/media/photos/mini/$(basename $image)
		convert blog_ag/blog_app/media/photos/mini/$(basename $image) -gravity center -crop 500x500+0+0 +repage blog_ag/blog_app/media/photos/mini/$(basename $image)
	fi
	fi

done
