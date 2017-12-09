echo "=== コーパス中で頻出する述語と格パターンの組み合わせ ==="
sort output/45.txt | uniq -c | sort -k 1 -nr | head

echo "=== 「する」という動詞の格パターン ==="
grep "^する" output/45.txt | sort | uniq -c | sort  -k 1 -nr | head

echo "=== 「見る」という動詞の格パターン ==="
grep "^見る" output/45.txt | sort | uniq -c | sort  -k 1 -nr | head

echo "=== 「与える」という動詞の格パターン ==="
grep "^与える" output/45.txt | sort | uniq -c | sort  -k 1 -nr | head
