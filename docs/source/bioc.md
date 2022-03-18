# bioc - BioC data structures and encoder/decoder for Python

[BioC XML / JSON format](http://bioc.sourceforge.net/) can be used to
share text documents and annotations.

`bioc` exposes an API familiar to users of the standard library
`marshal` and `pickle` modules.

Development of `bioc` happens on GitHub:
<https://github.com/bionlplab/bioc>

## Getting started

Installing `bioc`

```shell
$ pip install bioc
```

### XML

Encoding the BioC collection object `collection`:

```python
import bioc

# Serialize ``collection`` to a BioC formatted ``str``.
bioc.dumps(collection)

# Serialize ``collection`` as a BioC formatted stream to ``fp``.
with open(filename, 'w') as fp
    bioc.dump(collection, fp)
```

Compact encoding:

```python
import bioc
bioc.dumps(collection, pretty_print=False)
```

Incremental BioC serialisation:

```python
from bioc import biocxml
with biocxml.iterwrite(filename) as writer:
    writer.write_collection_info(collection)
    for document in collection.documents:
        writer.write_document(document)
```

Decoding the BioC XML file:

```python
import bioc

# Deserialize ``s`` to a BioC collection object.
collection = bioc.loads(s)

# Deserialize ``fp`` to a BioC collection object.
with open(filename, 'r') as fp:
    collection = bioc.load(fp)
```

Incrementally decoding the BioC XML file:

```python
from bioc import biocxml

# read from a file
with biocxml.iterparse(filename) as reader:
    collection_info = reader.get_collection_info()
    for document in reader:
        # process document
        ...

# read from a ByteIO
with biocxml.iterparse(open(filename, 'rb')) as reader:
    collection_info = reader.get_collection_info()
    for document in reader:
        # process document
        ...
```

`get_collection_info` can be called after the `with` statement.

Together with Python coroutines, this can be used to generate BioC XML
in an asynchronous, non-blocking fashion.

```python
from bioc import biocxml

with biocxml.iterparse(source) as reader, biocxml.iterwrite(dest) as writer:
    collection_info = reader.get_collection_info()
    writer.write_collection_info(collection_info)
    for document in reader:
        # modify the document
        ...
        writer.write_document(document)
```

### Json

Encoding the BioC collection object `collection`:

```python
import bioc

# Serialize ``collection`` to a BioC Json formatted ``str``.
bioc.dumps(collection, BioCFileType.BIOC_JSON, indent=2)

# Serialize ``collection`` as a BioC Json formatted stream to ``fp``.
with open(filename, 'w') as fp
    bioc.dump(collection, BioCFileType.BIOC_JSON, fp, indent=2)
```

Compact encoding:

```python
import bioc
bioc.dumps(collection, BioCFileType.BIOC_JSON)
```

Decoding the BioC Json file:

```python
import bioc

# Deserialize ``s`` to a BioC collection object.
collection = bioc.loads(s, BioCFileType.BIOC_JSON)

# Deserialize ``fp`` to a BioC collection object.
with open(filename, 'r') as fp:
    collection = bioc.load(fp, BioCFileType.BIOC_JSON)
```

### Json Lines

Incrementally encoding the BioC structure:

```python
from bioc import BioCJsonIterWriter
with open(filename, 'w', encoding='utf8') as fp:
    writer = BioCJsonIterWriter(fp, level=bioc.PASSAGE)
    for doc in collection.documents:
         for passage in doc.passages:
             writer.write(passage)
```

or

```python
from bioc import toJSON
import jsonlines
with jsonlines.open(filename, 'w') as writer:
    for doc in collection.documents:
         for passage in doc.passages:
             writer.write(toJSON(passage))
```

Incrementally decoding the BioC Json lines file:

```python
from bioc import BioCJsonIterReader
with open(filename, 'r', encoding='utf8') as fp:
    reader = BioCJsonIterReader(fp, level=bioc.PASSAGE)
    for passage in reader:
        # process passage
        ...
```

or

```python
from bioc import fromJSON
import jsonlines
with jsonlines.open(filename) as reader:
    for obj in reader:
        passage = fromJSON(obj, level=bioc.PASSAGE)
        ...
```

## Developer guide

### Testing the code

```shell
$ pytest cov=bioc tests
```

### Publish BioC to PyPI and TestPyPI

First, you need a PyPI user account. You can create an account using the
form on the PyPI/TestPyPI website.

Now you’ll create a PyPI/TestPyPI API token so you will be able to
securely upload your project.

Go to <https://pypi.org/manage/account/#api-tokens> and create a new API
token; don’t limit its scope to a particular project, since you are
creating a new project.

```shell
$ python -m build
```

Using local package with pip

```shell
$ pip install --force-reinstall dist/PACKAGE.whl
```

Using TestPyPI with pip

```shell
$ twine upload --repository testpypi dist/*
$ pip install --index-url https://test.pypi.org/simple/ bioc
```