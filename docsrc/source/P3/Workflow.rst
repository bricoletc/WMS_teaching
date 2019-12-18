Build a full workflow
======================


The task
----------

We want to perform read mapping and variant genotyping against a genome graph, a data structure which contains known genetic variation observed in a population or a species.

We will use `gramtools <https://github.com/iqbal-lab-org/gramtools>`_ to do this, which I develop. 

Let's hope we don't find any bugs along the way :-)

The data
---------

We have 5 read sets from `Mycobacterium tuberculosis`, a bacterial pathogen. We also have its reference genome and a VCF containing known variants.
The data files are in `P3/data`.


Desired workflow
-----------------

.. figure:: ../img/P3_dag.svg

    The steps of the workflow to implement.
    Two samples are shown here, but you have a total of 10 at your disposal.

.. tip::
    Start by using only two samples, as in the provided `config/samples.tsv`.

    Then when your workflow works with two samples, run on all 10 using:: 

        mv config/all_samples.tsv config/samples.tsv

Key information
----------------

Below is some key information to help you write the workflow.

Starting point
````````````````
Here is the Snakefile we start from:

.. literalinclude:: P3_dir/toComplete_Snakefile
        :language: python

Gramtools commands
````````````````````

Get information on available gramtools commands by running ``singularity exec P3/config/WMS.img gramtools``

Tips:

* ``build`` takes a `kmer-size` option, reasonable values are < 12.
* gramtools commands after ``build`` use a `run directory`, which you create in the ``quasimap`` phase. This 
  directory should contain all results for a given sample.

Other processes
`````````````````

* In process **mergeVcfs**, we need to combine the vcfs from ``infer`` into one vcf using the program ``bcftools``.
  ``bcftools`` requires compressed and indexed vcfs as input. You can compress using ``bgzip``.

* The process **plots** uses the python3 script in P3/scripts/analyse_variant.py. Try running it on its own to see options.
  The script uses the excellent python package
  `scikit-allel <https://scikit-allel.readthedocs.io/en/stable/index.html>`_ for analysing genetic variation, if you're interested!

