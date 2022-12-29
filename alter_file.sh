#/bin/bash
cd files
var="["
sed -i"" -e "1s/.*/$var/" twitter.js
rm twitter.js-e
mv twitter.js twitter.json

