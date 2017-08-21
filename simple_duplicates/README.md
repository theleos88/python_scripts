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


# Usage

Check the ```Makefile```

# Conventions

Using ```|``` as delimiter for both objects and csv files.
