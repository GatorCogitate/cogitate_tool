# cogitate_tool

## Development Doc

After pulling the repo, use `pipenv shell` in `cogitate_tool/` to enter the virtual
environment. Use `exit` to exit. Under the virtual environment, use
`pipenv install package_name` to install new packages.

### 1. File Structure

```bash
.
├── cogitate_tool.py ------------- *main function*
├── driller.py ------------------- *PyDriller*
├── Pipfile ---------------------- *Package file*
├── Pipfile.lock ----------------- *Package version lock file*
├── pyinquirer ------------------- *CLI demo*
│   ├── hello.py ----------------- *Demo Hello World*
│   ├── img ---------------------- *Images for markdown*
│   │   ├── interactive.png
│   │   └── result.png
│   ├── intactv.py --------------- *Examples for choices question*
│   └── pyinquirer.md ------------ *Demo documentation*
└── README.md
```

### 2. CLI

The [homepage](https://github.com/CITGuru/PyInquirer) for `PyInquirer`. And a
[helpful site](https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df).

The available attributes can be found at their homepage.

### PyDriller
