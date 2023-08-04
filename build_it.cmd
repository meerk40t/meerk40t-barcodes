mkdir dist
mkdir old_dist
move dist\* old_dist
python setup.py sdist bdist_wheel --universal
twine.exe upload dist\*