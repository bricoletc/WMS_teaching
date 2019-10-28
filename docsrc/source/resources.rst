=================
Useful Resources
=================

The snakemake tutorial: https://snakemake.readthedocs.io/en/stable/tutorial/tutorial.html.

Nextflow
-----------

Is a strong alternative workflow manager to snakemake, also with a lot of examples and users in bioinformatics.

The key difference is that Nextflow does not compute the workflow DAG before running: instead of pre-computing all dependencies like snakemake, it runs
as soon as it sees a process which can consume data it has at its disposal. 

To pass data around it relies on a more general concept of *channels* instead of *files*. Channels
can be created inside and outside *processes* (the equivalent of snakemake *rules*) and can be manipulated in many ways in the workflow script.

Here is our take on some differences. The more stars the better.

===============================  ================================  ===============================================
What I want                         snakemake                          nextflow
===============================  ================================  ===============================================
Easy scripting                      [**] Python!                   [*] Java scripting derivative: Groovy
Getting going fast                  [**] Rules and files           [*] Processes and channels
Visualise DAG                    [**] Get before the run           [*] Get only after the run
Good Documentation               [**]                              [*]
Start workflow quickly           [*] Needs to compute DAG          [**] No need for DAG
Clean working directory [#f1]_   [*] Execution where files are     [**] Execution in isolated directories
Getting run statistics           [*] html reports, benchmark rule   [**] html reports, ``--with-trace``
Data communication                [*] always files or directories    [**] Manipulate channels with ``operators``
Rerun where I stopped            [**]                                [**]
Environment control [#f2]_          [**]                           [**]
Execution abstraction [#f3]_            [**]                        [**]
===============================  ================================  ===============================================

Ultimately both are great and actively developed, and we do encourage you to have a look at nextflow also.

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

