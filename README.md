# intellaugment
`intellaugment` is an NLP tool for textual data augmentation written in Python by Zachary Wilkins. It uses techniques from the linguistic sub-fields of Syntax, Semantics and Pragmatics to massively augment training sets used by models for virtually any NLP task. It will increase the size of the training set for any NLP model, yielding a number of training samples between 2x and 5x the original size, depending on the nature of the training data.


## Sample
To give the augmentation a try, you can run `python3 augment_tester.py --sample` from the command line. It will run the augmentation algorithm on a sample of data taken from from [the Stanford Natural Language Inference corpus](https://nlp.stanford.edu/projects/snli/).

Example input:

| Text | Judgments | Hypothesis |
| ------------- | ------------- | ------------- |
| A man inspects the uniform of a figure in some East Asian country.  | contradiction | The man is sleeping |
| An older and younger man smiling.  | neutral | Two men are smiling and laughing at the cats playing on the floor. |
| A black race car starts up in front of a crowd of people. | contradiction | A man is driving down a lonely road. |
| A soccer game with multiple males playing. | entailment | Some men are playing a sport. |
| A smiling costumed woman is holding an umbrella. | neutral | 	A happy woman in a fairy costume holds an umbrella. |

Example output:

| Text | Judgments | Hypothesis |
| ------------- | ------------- | ------------- |
| A man inspects the uniform of a figure in some East Asian country. | contradiction | The man is sleeping |
| A man inspects the uniform of a figure in an eastern Asian country. | contradiction | The man is sleeping |
| A man inspects the uniform of a figure in some Oriental Asia country. | contradiction | The man is sleeping |
| Ultimately a man inspects the uniform of a figure in some East Asian country. | contradiction | The man is sleeping |
| An older and younger man smiling. | neutral | Two men are smiling and laughing at the cats playing on the floor. |
| An older and younger man smiling basically. | neutral | Two men are smiling and laughing at the cats playing on the floor. |
| A black race car starts up in front of a crowd of people. | contradiction | A man is driving down a lonely road. |
| A black racing car starts in front of a crowd. | contradiction | A man is driving down a lonely road. |
| Apparently a black race car starts up in front of a crowd of people. | contradiction | A man is driving down a lonely road. |
| A soccer game with multiple males playing. | entailment | Some men are playing a sport. |
| A football game with multiple males playing. | entailment | Some men are playing a sport. |
| Certainly a soccer game with multiple males playing. | entailment | Some men are playing a sport. |
| A smiling costumed woman is holding an umbrella. | neutral | A happy woman in a fairy costume holds an umbrella. |
| A smiling dressed woman is holding an umbrella. | neutral | A happy woman in a fairy costume holds an umbrella. |
| Conceivably a smiling costumed woman is holding an umbrella. | neutral | A happy woman in a fairy costume holds an umbrella. |


## Testing
To run the tests for this application, install `pytest` using `pip3 install pytest`, and then run `pytest test_augmentors.py`.


## Machine Learning Applications
This implementation can be utilized for a wide variety of machine learning tasks, including but not limited to:
* textual entailment
* question answering
* information retrieval
* intent classification
* sentiment analysis
* machine translation
* summarization
* topic labeling


## Implementation 

The implementation of this data augmentation algorithm centers around several different "Augmentors", or components in the system that use different NLP and/or linguistic techniques to generate new samples with the same semantic meaning. 

| Name | Description |
| ----- | ------------- | 
| Augmentor | The base class from which all other Augmentors inherit a set of core methods. These methods include testing the augmentor on a single string input, on an input .csv file. See `models.py`. | 
| TranslationAugmentor | This Augmentor translates English text into other languages (e.g. Spanish and German) and back into English, in order to alter the sentence while maintaining its core semantic meaning. Two calls to the Google Translate API are used to achieve this. | 
| NoiseAugmentor | This augmentor adds pragmatic linguistic "noise", i.e. content that can affect an utterance's contextual meaning, but has no material impact on its standalone semantic content, particularly utterance-modifying adverbs. | 
| RelocationAugmentor | This Augmentor moves core semantic content from one part of an utterance to a different part of the utterance, in such a way that the truth-conditional meaning of the utterance is unchanged. For example, given the training sample "The musician will blow the audience away.", this Augmentor would also generate the sample "The musician will blow away the audience." | 



## License
`intellaugment` is released under the MIT License.

