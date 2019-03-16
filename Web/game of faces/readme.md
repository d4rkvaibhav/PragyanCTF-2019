The Game of Faces, welcomes you. In this era, where AIs generate a lot of faces, we would like you to contribute to the same by uploading your image. Thank you for contributing, to continue.

Solution:
There is a upload file hidden form we have to upload any file and then in the next step got a base64 string:
	
	VGhlX3Njcm9sbF9zYXlzPXRoZV9uaWdodF9raW5nVlN2YWx5cmlhbi50eHQ==

On decoding this it reveals out:
	
	The_scroll_says=the_night_kingVSvalyrian.txt

So on opening the link http://159.89.166.12:15000/the_night_kingVSvalyrian.txt i got the flag:

	pctf{You_L00K_Wi3Rd_IN_H3R3}
	