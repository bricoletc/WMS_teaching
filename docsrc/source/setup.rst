============
Setup
============


The first thing to do is open a terminal and make sure these commands are available: ``git``, ``conda``, ``singularity``.

They should output help messages.  If they don't please let us know.

Now:

1. Download the git repository and move into it::

    $ git clone https://github.com/bricoletc/WMS_teaching
    $ cd WMS_teaching

Note: you can now view these pages locally using ``gio open docs/index.html``, if you want.
    
2. Download and extract this tarball ::

    $ wget https://oc.ebi.ac.uk/apps/files/?dir=/Teaching&fileid=3487362
    $ tar -xf WMS_stuff.tar
    $ mv WMS_stuff/data data

It contains the dataset we'll use :doc:`later <P3>` and the singularity image containing some software we will use. 


3. Set up the :term:`conda` environment ::

        $ conda create --name WMS -c bioconda -c conda-forge --file requirements.txt

This provides the python libraries and some of the tools we will use.  

