============
Setup
============

Requirements:

* python3
* git
* bcftools
* bgzip

Step 1: Code & Environment
----------------------------

.. code-block:: shell

    git clone https://github.com/bricoletc/WMS_teaching
    cd WMS_teaching

Venv and pip (recommended)
``````````````````````````

.. code-block:: shell

    python3 -m venv venv && source venv/bin/activate
    pip install -r pip_requirements.txt

Now install bcftools and bgzip. For eg on Debian-like systems: ``sudo apt-get install bcftools tabix``
    
Alternative: :term:`Conda`
``````````````````````````
.. code-block:: shell

        conda create --name WMS -c bioconda -c conda-forge --file conda-requirements.txt
        (Proceed? [y])
        conda activate WMS

        pip install $(grep "gramtools" pip-requirements.txt)
    
Step 2: Data
-------------
Download this tarball: https://oc.ebi.ac.uk/s/4liZWUYp1kFluCY .

.. code-block:: shell

    mv /path/to/tarball/WMS.tar.gz ./
    tar -xf WMS.tar.gz
    cp -r data_WMS/P3/* P3/data
    mkdir P2/data P2/data/genomes
    cp data_WMS/P2/* P2/data/genomes


The tarball contains the datasets we'll use in :doc:`P2 <P2>` and :doc:`P3 <P3/P3>`.

