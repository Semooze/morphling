[![Actions Status](https://github.com/Semooze/morphling/workflows/Morphling/badge.svg)](https://github.com/Semooze/Morphling/actions)


# Morpling

This library use to transform and reformat various data type. (Right now it just support specific case which is reformat csv)

## Install 

```shell
$ pip install morphling
```

## How to use

Available command 
```shell
$ morphling --help
Usage: morphling [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  clean-csv  This function will rewrite csv file with double qoute embrace a string
  when it is in different line.
```

Available option for command
```shell
$ morphling clean-csv --help
Usage: morphling clean-csv [OPTIONS]

  This function will rewrite csv file with double qoute embrace a string
  when it is in different line.

  args:

      * src: Location where intput file live.

      * des: Location where output file will be placed. Note that it the
      directory must exist.

Options:
  --src TEXT  Location where intput file live.
  --des TEXT  Location where output file will be placed. Note that it the
              directory must exist.
  --help      Show this message and exit.

```

Reformat csv
```shell
morphling clean-csv --src=source-path --des=./destination-path
```

For example
```shell
morphling clean-csv --src=./rawdata.csv --des=./test_clean.csv
```

The above example will create new file name 'test_clean.csv' which have the same data with 'rawdata.csv' but add double qoute when
data in the same field is in different line. Basically it takes around 2 minutes to complete (for file ~760MB).


## For development

* Clone the repo 
* Create a directory name 'output_file' inside the directory test
* Run test by following three command

```shell
$ python -m unittest
```
