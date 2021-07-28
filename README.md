# intellaugment
`intellaugment` is an NLP tool for textual data augmentation written in Python by Zachary Wilkins. It uses techniques from the linguistic sub-fields of Syntax, Semantics and Pragmatics to massively augment training sets used by models for virtually any NLP task.


## Sample
To give the augmentation a try, you can run `python3 augment_tester.py --sample` from the command line. It will run the augmentation algorithm on a sample of data taken from from [the Stanford Natural Language Inference corpus](https://nlp.stanford.edu/projects/snli/). This will take the following .csv as input:

| Text  | Judgments | Hypothesis |
| ------------- | ------------- | ------------- |
| A man inspects the uniform of a figure in some East Asian country.  | contradiction | The man is sleeping |
| An older and younger man smiling.  | neutral | Two men are smiling and laughing at the cats playing on the floor. |
| A black race car starts up in front of a crowd of people. | contradiction | A man is driving down a lonely road. |
| A soccer game with multiple males playing. | entailment | Some men are playing a sport. |
| A smiling costumed woman is holding an umbrella. | neutral | 	A happy woman in a fairy costume holds an umbrella. |

...and increase the number of training samples by 5x, returning the following .csv as output:

| Text  | Judgments | Hypothesis |
| ------------- | ------------- | ------------- |
| A man inspects the uniform of a figure in some East Asian country.  | contradiction | The man is sleeping |
| An older and younger man smiling.  | neutral | Two men are smiling and laughing at the cats playing on the floor. |
| A black race car starts up in front of a crowd of people. | contradiction | A man is driving down a lonely road. |
| A soccer game with multiple males playing. | entailment | Some men are playing a sport. |
| A smiling costumed woman is holding an umbrella. | neutral | 	A happy woman in a fairy costume holds an umbrella. |


## Usage
To install this application locally, create a Python virtual environment and run `pip3 install -r requirements.txt` from the command line. 

Next, place the training set that you would like to augment as a `.csv` file inside the `/data/input/` directory. Run the command `python3 app.py data/input/your_dataset.csv`. After the process is finished, the command line will print `**Augmentation complete**` and you will find your augmented training set as `data/output/your_dataset_augmented.csv`.


## Testing
To run the tests for this application, install pytest using `pip3 install pytest` and then run `pytest -m tests/`.


## Applications
This implementation can be utilized for a wide variety of machine learning tasks, including but not limited to:
* textual entailment
* question answering
* information retrieval
* intent classification
* sentiment analysis
* machine translation
* summarization
* topic labeling


## License
`intellaugment` is released under the MIT License.

