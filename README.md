- original (python)
```

stringValueList = ["s", None, "1", ""]
int64ValueList = [1, None, 0, 1000]
```


- protobuf instance
```

stringValueList {
  value: "s"
}
stringValueList {
}
stringValueList {
  value: "1"
}
stringValueList {
}


int64ValueList {
  value: 1
}
int64ValueList {
}
int64ValueList {
}
int64ValueList {
  value: 1000
}
```

- json
```
{
  "stringValueList": [
    "s",
    "",
    "1",
    ""
  ],
  "int64ValueList": [
    "1",
    "0",
    "0",
    "1000"
  ]
}
```