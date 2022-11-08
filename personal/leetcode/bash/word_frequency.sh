declare -A words

while read line; do
    for word in $line; do
        if [ -v 'words[$word]' ]; then
            ((words[$word]=${words[$word]}+1))
	else
	    words[$word]=1
	fi
    done
done < words.txt

for word in ${!words[@]}; do
  echo "$word ${words[$word]}"
done |
sort -rn -k2
