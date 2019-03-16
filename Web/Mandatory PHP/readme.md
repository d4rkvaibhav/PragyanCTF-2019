Challenge name:
	
	MANADATORY PHP
Description:

PHP, PHP everywhere get the flag and earn your points there.

We were given index.php in the challenge.

Solution:
To get the first part of flag we have to pass :
	
	if($c>0&&$d>0&&$d>$c&&$a==$c*$c+$d*$d)

	c>0 and d>0 and d>c 
	also a is changed into it's sha256 hash
	so if we put nothing in a the a i.e $a="" the the sha256 will be INF(infinty)
	and put value of $c=1 and $d=INF
	It will pass the first test.

For the second part of flag you can see url encoding of "WoAHh!" is done repetedly 10 times so you just have to url encode "WoAHh!" 10 times which will come out to be WoAHh%25252525252525252521.

Put 

	$b="WoAHh%25252525252525252521"

final url	:	http://159.89.166.12:14000/?val1=""&val2="WoAHh%25252525252525252521"&val3=1&val4=INF

FLAG:

	pctf{b3_c4r3fu1_w1th_pHp_f31145}