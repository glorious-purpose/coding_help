echo -e
while read line; do
  echo "Evaluating $line"
  #if [[ $line =~ ^[0-9]{3}-[0-9]{3}-[0-9]{4}$ ]]; then
  # if [[ $line =~ ^\([0-9]{3}\)[[:space:]][0-9]{3}-[0-9]{4}$ ]]; then
  if [[ $line =~ ^(\([0-9]{3}\)[[:space:]]|[0-9]{3}-)[0-9]{3}-[0-9]{4}$ ]]; then
    echo $line
    echo -e
  else
    echo "Failed to meet criteria."
    echo -e
  fi
done < file.txt

echo "One liner:"
echo -e
while read line; do [[ $line =~ ^(\([0-9]{3}\)[[:space:]]|[0-9]{3}-)[0-9]{3}-[0-9]{4}$ ]] && echo $line; done < file.txt
