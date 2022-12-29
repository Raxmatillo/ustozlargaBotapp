cyrilic=["ю","Ю","я","Я","ё","Ё","ш","Ш","ч","Ч","ў","Ў",
          "қ","Қ","ғ","Ғ","ц","Ц","й","Й","у","У","к","К",
    "е","Е","н","Н","г","Г","щ","Щ","з","З","х","Х",
    "э","Э","ж","Ж","д","Д","л","Л","о","О","р","Р",
    "п","П","а","А","в","В","ф","Ф","с","С","м","М",
    "и","И","т","Т","б","Б","қ","Қ","ҳ","Ҳ","ғ","Ғ","ь"];
     

latin=["yu","Yu","ya","Ya","yo","Yo","sh","Sh","ch","Ch","o'","O'",
          "q","Q","g'","G'","ts","Ts","y","Y","u","U","k","K","e","E",
    "n","N","g","G","sh","Sh","z","Z","x","X","e","E","j","J",
    "d","D","l","L","o","O","r","R","p","P","a","A","v","V","f",
    "F","s","S","m","M","i","I","t","T","b","B","q","Q","h","H",
    "g'","G'","'"];



def ToCyrilic(word):
	for x in range(len(cyrilic)):
		word = word.replace(latin[x], cyrilic[x])
	return word

def ToLatin(word):
	for x in range(len(latin)):
		word = word.replace(cyrilic[x], latin[x])
	return word