# intellaugment
`intellaugment` is an NLP tool for textual data augmentation written in Python by Zachary Wilkins. It uses techniques from NLP and the linguistic sub-fields of Syntax, Semantics and Pragmatics to massively augment training sets used by models for virtually any machine learning task. It will increase the size of a provided training set, yielding a number of new samples between 2x and 5x its original size, depending on the nature of the training data.


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


## Implementation 

The implementation of this data augmentation algorithm centers around several different "Augmentors", or components in the system that use different NLP and/or linguistic techniques to generate new samples with the same semantic meaning. 

| Name | Description |
| ----- | ------------- | 
| Augmentor | The base class from which all other Augmentors inherit a set of core methods. These methods include providing the ability to test the augmentor on a single string input and running the Augmentor against an input .csv file. See `models.py`. | 
| TranslationAugmentor | This Augmentor translates English text into other languages (e.g. Spanish and German) and back into English, in order to alter the sentence while maintaining its core semantic meaning. Two calls to the Google Translate API are used to achieve this. | 
| NoiseAugmentor | This augmentor adds pragmatic linguistic "noise", i.e. content that can affect an utterance's contextual meaning, but has no material impact on its standalone semantic content, particularly utterance-modifying adverbs. | 
| RelocationAugmentor | This Augmentor moves core semantic content from one part of an utterance to a different part of the utterance, in such a way that the truth-conditional meaning of the utterance is unchanged. For example, given the training sample "The musician will blow the audience away.", this Augmentor would also generate the sample "The musician will blow away the audience." | 


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


## Best Practices

It is important to follow several core best practices when incorporating augmentation into your machine learning pipeline:

* *Never* use data augmentation on your model's validation set or test set. Restrict augmentation to your training set only.
* Augmentation should not be used as a replacement for cleaning and normalizing your training data.
* As always during model training, you should be cognizant of the bias-variance tradeoff when incorporating data augmentation. As you would when tuning hyperparameters, be vigilant about potential overfitting, particularly if your training set is very small.


## Testing
To run the tests for this application, install `pytest` using `pip3 install pytest`, and then run `pytest test_augmentors.py`.


## License
`intellaugment` is released under the MIT License.

