.. LiveObs Automation Suite documentation master file, created by
   sphinx-quickstart on Thu May 25 09:34:40 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to LiveObs Automation Suite's documentation!
====================================================
The LiveObs Automation Suite contains a suite of tests that through automated
GUI interaction via Selenium ensure that the LiveObs application is working
inline with the specification.

Installation
------------
You can install the test suite via pip using the following command:

.. code-block:: bash

   pip install git+git://github.com/BJSS/BJSS_liveobs_automation.git@OPTIONAL_VERSION_NUMBER


Usage
-----
Once you've got the test suite installed you can then run the test suites via

.. code-block:: bash

   behave


If you want to run a particular suite you can use

.. code-block:: bash

   behave --tags=regression,feature-specific-tag

.. toctree::
   :maxdepth: 2
   :caption: Steps:
   :glob:

   steps/*



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
