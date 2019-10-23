A more in-depth view
=====================

You can first work either on improving the workflow or on answering a biological question.

.. contents::
    :depth: 2

Workflow improvement
-------------------------------------

Use the Snakemake readthedocs webpage for help!

Logging
`````````

Add logging to one or more rules, to capture stdout and stderr in files.

`relevant doc <https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#>`_

Benchmarking
`````````````

Snakemake can measure CPU/wall clock time and RAM use of each rule.

Find out how, and try it out on a rule.

Restarts
``````````

What does Snakemake rely on to know where in the DAG to restart after a failed run?

.. tip::
    Search the doc for ``timestamps``.


* Try modifying a file yourself such that Snakemake will re-run the workflow from rule ``mergeVcfs``.
* Find out the command-line option to re-run the workflow from any user-specified rule. `relevant doc <https://snakemake.readthedocs.io/en/stable/project_info/faq.html>`_


Cluster
`````````

Figure out how to submit the workflow to the cluster. Note that cluster parameters should not go in the workflow itself, otherwise it is no longer independent of where it is run.
`relevant doc <https://snakemake.readthedocs.io/en/stable/snakefiles/configuration.html#>`_

For testing, ask us if there is cluster access, or if we can run it for you on EBI cluster (which uses LSF).

Analysis improvement: Drug resistance prediction
------------------------------------------------- 

The dataset contains at least one sample which is resistant to a drug against tuberculosis (TB).
Can you find which samples are resistant to which known TB drugs?

You can use the `mykrobe <https://github.com/mykrobe-tools/mykrobe>`_ program to do this. It is available in
the singularity image::

    singularity exec P3/WMS.img mykrobe

Check the drug resistance predictions by `mykrobe` are present in the VCFs you produced using the workflow.

Running mykrobe and making a report could be added to the workflow.

.. tip::
    Use the -f option in mykrobe else it will not predict anything. This is because we are working with a slice of the genome.
