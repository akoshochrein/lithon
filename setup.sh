
if [ ! -d "virtualenv" ]; then
    virtualenv virtualenv
fi

. virtualenv/bin/activate
pip install argparse
pip install --upgrade autopep8

deactivate
