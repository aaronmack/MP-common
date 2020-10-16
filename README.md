## MP (Meta Possibility)

* This is a common repository, for MP

![Upload Python Package mp-common-pkg](https://github.com/aaronmack/MP-common/workflows/Upload%20Python%20Package%20mp-common-pkg/badge.svg?branch=master)

## Construction

```bash
# build
python3 setup.py sdist bdist_wheel
# -> or
python3 setup.py sdist

# check 
pip install twine
twine check dist/*

# register
https://pypi.org/account/register/

# E-mail validation
Validation your email

# upload
twine upload dist/*

# install 
pip install mp-common-pkg

# using
import common_pkg.common as cpc
file_path = r""
cpc.compute_md5(file_path)

# upgrade 
pip install mp-common-pkg --upgrade
```

## Problems

* error: invalid command 'bdist_wheel'

```bash
pip install wheel
```
