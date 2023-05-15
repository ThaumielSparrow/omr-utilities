# OMR Utilities

A collection of short scripts related to OMR.

## Pre-requisites

Requirements are provided via frozen lockfile.

```
pip install -r requirements.txt
```

It is necessary to install Audiveris to use OMR scripts. Version 5.2.5 should be installed for maximum compatability.
Audiveris 5.2.5 can be installed from the [Releases](https://github.com/Audiveris/audiveris/releases/tag/5.2.5) page.

Audiveris will automatically install its dependencies. However, Java is required for its installation and operation. 
[Java 11 LTS](https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html) should be installed.

## Schema

CLI is provided via `last_notes.py` file.

A complete pipeline is executed upon running

```
python last_notes.py music_file.pdf
```

Optional arguments can be passed to modify the number of notes to pull or regex of the file search schema.

`output` folder should be deleted between runs to avoid errors.


## Attribution

Attribution should be given to the primary maintainer Luzhou Zhang @ThaumielSparrow.