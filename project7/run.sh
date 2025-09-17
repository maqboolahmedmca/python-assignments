export PYTHONPATH=$(pwd)/..

rm -rf output

python3 rss_feed_extractor.py
echo 'Finished RSS feed extraction'
