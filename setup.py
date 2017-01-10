# Copyright 2016 Florian Lehner. All rights reserved.
#
# The contents of this file are licensed under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

from setuptools import setup, find_packages
import re

with open('README.md') as f:
    readme = f.read()

with open('panonoctl/__init__.py', 'r') as fd:
    versionNr = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

setup(
    name='panonoctl',
    version=versionNr,
    py_modules=['panonoctl'],
    packages=find_packages(),
    long_description=readme,
    include_package_data=True,
    description = 'Python API to interact with the PANONO 360-camera',
    author = 'Florian Lehner',
    author_email = 'dev@der-flo.net',
    url = 'https://github.com/florianl/panonoctl/',
    download_url = 'https://github.com/florianl/panonoctl/archive/master.tar.gz',
    keywords = ['Panono', 'API '],
    install_requires=['websocket-client', 'simplejson'],
    classifiers=[   'Development Status :: 4 - Beta',
                    'Intended Audience :: Developers',
                    'Programming Language :: Python'
                ],
    license = 'Apache License 2.0'
)
