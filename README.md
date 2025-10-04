# Bird Audio Identification

<a href="https://de.cyverse.org/instantlaunch/0934c370-9e44-11f0-9521-008cfa5ae621" target="_blank" rel="noopener noreferrer"><img src="https://de.cyverse.org/Powered-By-CyVerse-blue.svg"></a>

This repository contains Jupyter Notebooks demonstrating bird species identification from audio recordings using the BirdNET deep learning model.

To use the notebooks in the CyVerse Discovery Environment, click the "Powered by CyVerse" button above.  This will launch a Jupyterlab instance on CyVerse.

An API Key for the MCP notebook can be obtained from AI Verde: [https://chat.cyverse.ai](https://chat.cyverse.ai). A CyVerse staff member will need to create your account first.


## Models and Packages

- **BirdNET Model**: Developed by Cornell University's Lab of Ornithology. [BirdNET Website](https://birdnet.cornell.edu/)
- **birdnet Package**: Python package for programmatic access to BirdNET. [PyPI](https://pypi.org/project/birdnet/)
- **birdnetlib Package**: Alternative Python package for BirdNET integration. [PyPI](https://pypi.org/project/birdnetlib/)
- Additional dependencies: librosa, soundfile, tflite-runtime, tensorflow, fastmcp, langchain_openai, mcp_use

## Data Source

The sample audio data used in this project is sourced from [xeno-canto.org](https://xeno-canto.org/), a collaborative database of wildlife sounds from around the world. The samples used were recorded in Tucson, AZ.
