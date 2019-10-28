=============
Introduction
=============

We first take you through an introduction to the concepts and to snakemake.

You can **get the slides** :download:`here <img/Intro_slides.pdf>`.

Below is a short written introduction, most of which is covered in the slides.

Motivation
-------------

In bioinformatics we often write pipelines, *ie* a set of scripts and tools called in a structured way.
Some obvious examples:

* Single-cell RNA-Seq pipeline
* Genomics variant calling pipeline

Probably at some point during your PhD you have or will need to write your own pipeline (we did!). 


If you are motivated and persistent, or some kind of wizard, you could maybe write your pipeline in ``bash``. 
But here are some aspects that could be hard to implement:

* Forking processes [#f1]_: running independent processes simultaneously
* Rejoining processes: combining the output from independent processes once they have completed
* Setting up process environments (eg access to tools, libraries), allocated resources (threads, RAM), logging to files.
* Creating reports showing, for *eg*, the time taken by each process.
* Deploying your pipeline on different platforms: Mac/Windows/Linux, different clusters, the cloud.
* Sharing your pipeline: readability & how easy it is to modify.
* Restart your pipeline where it last failed/stopped.

Worflow Management Systems (WMS) aim to help us do all this.

Tool
------

Here we will use Snakemake, a python package for writing worflows.

Another really good tool is `nextflow <https://www.nextflow.io/>`_.
We have a few words on it :doc:`here <resources>`.

.. rubric:: Footnotes

.. [#f1] Throughout we call **processes** the basic units of work that go into pipelines.
