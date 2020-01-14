=================
Useful Resources
=================

The snakemake tutorial: https://snakemake.readthedocs.io/en/stable/tutorial/tutorial.html.

Nextflow
-----------

Nextflow is also a great workflow manager, with a lot of examples and `users in bioinformatics <https://github.com/nextflow-io/awesome-nextflow>`_.

One key difference is that Nextflow does not compute the workflow DAG before running: thus it does not know what the final target is (Snakemake's `all` rule). For large workflows that means it starts running faster. 

To link processes and pass data through it relies on *channels* instead of files. Channels can contain filenames, but also any other data which can be manipulated in different ways (for example, filtered) during workflow execution.

In one sentence Snakemake is 'output-oriented' while Nextflow is 'process-oriented'. 

Here is my take on some differences. The more stars the better.

===============================  ================================  ===============================================
What I want                         snakemake                          nextflow
===============================  ================================  ===============================================
Easy scripting                      [**] Python <3                   [*] Java scripting derivative: Groovy
Getting going fast                  [**] Rules and files           [*] Processes and channels
Visualise DAG                    [**] Get before the run           [*] Get only after the run
Good Documentation               [**]                              [**]
Start workflow quickly           [*] Needs to compute DAG          [**] No need for DAG
Clean working directory [#f1]_   [*] Execution where files are     [**] Execution in isolated directories
Getting run statistics           [*] html reports, benchmark rule   [**] html reports, ``--with-trace``
Data communication                [*] always files                  [**] Manipulate channels with ``operators``
Rerun where I stopped            [**]                                [**]
Environment control [#f2]_          [**]                           [**]
Execution abstraction [#f3]_            [**]                        [**]
===============================  ================================  ===============================================

Ultimately both are great and actively developed.

.. [#f1] nextflow does not rely on file names to link processes and runs each process in its own working directory: thus you can names files whatever you like
        in the workflow script. snakemake can use ``shadow`` directive to execute a rule in this way.
.. [#f2] run in conda environment, in docker/singularity image...
.. [#f3] run on clusters, AWS...

Glossary
----------

.. glossary::
    conda 
        A tool for building virtual software environments. https://conda.readthedocs.io/en/latest/

    singularity
        A tool for building containers, which are mini-operating systems with isolated software environments.
        https://sylabs.io/guides

