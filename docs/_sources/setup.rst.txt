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
    
2. If we tell you it's needed, download and extract this tarball: https://oc.ebi.ac.uk/s/C0VgbVAevgVk7wQ .
   We will give you the password. Once you have the tarball do: ::

    $ mv /path/to/tarball/WMS.tar ./
    $ tar -xf WMS.tar 
    $ mv WMS_stuff/data P3/data
    $ mv WMS_stuff/WMS.img P3/config
    $ mkdir P2/data
    $ mv WMS_stuff/P1_genomes.zip P2/data && unzip P2/data/P1_genomes.zip


The tarball contains the datasets we'll use :doc:`later <P3/P3>` and the :term:`singularity` image containing some software we will use. 


3. Set up the :term:`conda` environment and activate it::

        $ conda create --name WMS -c bioconda -c conda-forge --file requirements.txt
        (Proceed? [y])
        $ conda activate WMS

This provides the python libraries and some of the tools we will use.  

Done!
