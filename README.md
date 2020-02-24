[![Actions Status](https://github.com/Semooze/morphling/workflows/Morphling/badge.svg)](https://github.com/Semooze/Morphling/actions)


# Morpling

This library use to transform and reformat various data type. (Right now it just support specific case which is reformat csv)
## How to use

Available command 
```shell
morphling --help
```

Available option for command
```shell
morphling clean-csv --help
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