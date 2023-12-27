rm -rf dist samaker.egg-info build/


echo "删除成功"

python3 setup.py sdist bdist_wheel
echo "完成"

python3 -m twine upload  dist/*
