# Notice for the src folder

In order to integrate all of the features from each individual team while also minimizing
redundancy, the structure for our program will be designed around 4 core modules:

* `cogitate_menu.py`
  * Will contain the main execution of the program as well as the majority of the
    UI-centered features and implementation. This class should contain **no**
    data-oriented code.
* `data_miner.py`
  * Will contain any relevant features concerning the retrieval and storage of contributor
    information with as little data wrangling as possible. Please refer to the Github
    issues (*to be created*) concerning what data **is** and **is not** necessary
    to be collected and stored.
* `data_processor.py`
  * Will contain any relevant features concerning the post-retrieval processing
    and interpretation of data. No statistics produced here should be written to
    the `contributor_data.json` file.
* `json_handler.py`
  * Contains the methods for reading and writing to the `contributor_data.json`
  file.
