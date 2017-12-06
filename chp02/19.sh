cut -f 1 data/hightemp.txt | sort | uniq -c | sort -k 1 -nr
