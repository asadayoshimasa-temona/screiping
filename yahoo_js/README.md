docker build -t yahoo-screiping ./yahoo_js

docer run -it -v $(pwd)/yahoo_js:/app yahoo-screiping /bin/bash 