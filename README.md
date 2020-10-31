# WKT for DGGS validator
A Python library and command line utility that validates [Well-Known Text](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) -style geometry literal values for Discrete Global Grid Systems (DGGS).

## NOTE: this package is currently non-functional
_this note will be removed when it is_


## Installation
This is a Python utility that is available via the Python Package Index, PyPI at <https://pypi.org/project/wktdggs/> so it may be installed using the PIP program:

```
pip install wktdggs
```

You can also install it locally by downloading or cloning, using [Git](https://git-scm.com) the source files from its [GitHub](https://github.com/) repository at <https://github.com/surroundaustralia/wkt-dggs>. After cloning / downloading navigate into the package's main  directory that contains the `setup.py` file. Then, install it locally like this:

```
python setup.py install
```

## Use
### As a Python Library
To use the utility as a Python library, import it into your Python code and call the `validate` function, something like this:

```python
from wktdggs import validate

# the WKT DGGS literal I want to validate
geom = "<http://w3id.org/dggs/tb16pix> POINT (P123456)"

vresult = validate(geom)

if vresult[0]:
    print("It is valid!")
else:
    print("It is not vaild.")
    print("The validation errors are:")
    print("\n".join(vresult[1]))  # all messages are in a list within vresult[1] 
```

### As a Python command line tool
Use Python to call the command line script `cli.py` within the package like this:

```bash
python cli.py STRING_OR_FILE_PATH [-o {table,json}]

positional arguments:
    STRING_OR_FILE_PATH: a WKT DGGS literal value or a file path

optional arguments:
    -o, --output: the value 'table' or 'json' to return a formatted text table of results or JSON
```

You can present the `cli.py` script with a WKT DGGS string, e.g.:

```bash
python cli.py "<http://w3id.org/dggs/tb16pix> POINT (P123456)"
```

or you can give it a file to read:

```bash
python cli.py /path/to/my/file.txt
```

If giving it a file, it will look for one WKT DGGS geometry per line and validate each. It will report its results with a line number if more than one line is present in the file, e.g.:

```
Line    Valid   Messages
---     ---     ---
1       True    -
2       True    -
3       False   The Geometry Type provided is not valid. 
                It must be one of: POINT, MULTIPOINT, LINESTRING, 
                MULTILINESTRING, POLYGON, MULTIPOLYGON, 
                GEOMETRYCOLLECTION
...             
N       True    -   
```

### As a BASH script
The BASH script `wktdggs.sh` can be called in the same way as the Python `cli.py` script, e.g.:

```bash
sh wktdggs.sh /path/to/my/geometries.txt -o json
```
Which will validate geometries in `geometries.txt` and output results in JSON.


## License  
This code is licensed using the LGPL v3 licence. See the [LICENSE file](LICENSE) for the deed. 

Note [Citation](#citation) below for attribution.


## Citation
To cite this software, please use the following BibTex:

```
@software{wktdggs,
  author = {{Nicholas J. Car}},
  title = {WKT for DGGS validator},
  version = {0.5},
  date = {2020},
  publisher = "SURROUND Australia Pty. Ltd.",
  url = {https://data.surroundaustralia.com/software/wktdggs}
}
```

Or the following RDF:

```
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix sdo: <https://schema.org/> .
@prefix wiki: <https://www.wikidata.org/wiki/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://data.surroundaustralia.com/software/wktdggs>
    a sdo:SoftwareSourceCode , owl:NamedIndividual ;
    sdo:codeRepository <https://github.com/surroundaustralia/wktdggs> ;
    dcterms:type wiki:Q7397 ; # "software"
    dcterms:creator "Nicholas J. Car" ;
    dcterms:date "2020"^^xsd:gYear ;
    dcterms:title "WKT for DGGS validator" ;
    sdo:version "0.1" ;
    dcterms:publisher [
        a sdo:Organization ;
        sdo:name "SURROUND Pty Ltd" ;
        sdo:url <https://surroundaustralia.com> ;
    ]
.
```

## Contacts

*publisher:*  
![](SURROUND-logo-100.png)  
**SURROUND Australia Pty. Ltd.**  
<https://surroundaustralia.com>  

*creator:*  
**Dr Nicholas J. Car**  
*Data Systems Architect*  
SURROUND Australia Pty. Ltd.  
<nicholas.car@surroudaustralia.com>  
<https://orcid.org/0000-0002-8742-7730>  
