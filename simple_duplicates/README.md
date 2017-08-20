# Organizing my data

``` 
	find DIR -type f -printf "%h %f %s\n" | python main.py -t d [--dest DESTDIR]
```

or

```
	find /usr/local/src/fdupes/testdir/ -type d | parallel --no-notice du -s
```
