# Organizing my data

## Dependencies

- parallel

## Test Dir

```
├── one
│   └── file1
├── three
│   ├── file1
│   └── file2
└── two
    └── file1
```

In particular:

one/file1 | two/file1 = Same data, same name
one/file1 | three/file1 = Different data, same name
one/file1 | three/file2 = Same data, Different name

Of course, this also imply a case with different data and different name.


``` 
	find DIR -type f -printf "%h %f %s\n" | python main.py -t d [--dest DESTDIR]
```

or

```
	find /usr/local/src/fdupes/testdir/ -type d | parallel --no-notice du -s
```
