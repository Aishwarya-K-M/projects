
# Machine Learning & AI Projects

A collection of my projects in machine learning, natural language processing (NLP), and computer vision. These projects explore practical applications of AI, from detecting harmful language in Hinglish text to classifying MRI images using deep learning.

## About Me

I am a Computer Science graduate interested in Artificial Intelligence, Machine Learning, and AI research. I enjoy exploring how machine-learning techniques work, how data preprocessing affects model performance, and how models can be evaluated and improved.

## Projects

### 1. Hinglish Cyberbullying Detection

**Domain:** Natural Language Processing (NLP) and Machine Learning

An NLP-based project exploring cyberbullying detection in Hinglish text using text preprocessing, feature extraction, and machine-learning classification.

**Key components**
- Text preprocessing and slang normalization using Stanza.
- TF-IDF feature extraction.
- Experiments with multiple classification algorithms.
- Ensemble classification using a VotingClassifier.
- Evaluation using accuracy, precision, recall, and F1-score.
- A web interface developed using Flask and frontend technologies.

**Technologies:** Python, Stanza, Scikit-learn, XGBoost, TF-IDF, Pandas, NumPy, Flask, HTML, CSS, JavaScript, Bootstrap.

**Reported experimental results**

| Metric | Score |
|---|---:|
| Accuracy | 91.90% |
| Precision | 92.64% |
| Recall | 91.90% |
| F1-score | 91.79% |

These results reflect the original experimental evaluation and may vary with data splits, preprocessing, and experimental settings.


### 2. MRI Image Classification Using Deep Learning

**Domain:** Computer Vision and Deep Learning

A project exploring MRI image classification using convolutional neural networks (CNNs), image preprocessing, and wavelet-based denoising.

**Key components**
- Image preprocessing, resizing, grayscale conversion, and normalization.
- Image augmentation using random flips and rotations.
- Wavelet-based denoising using the `bior1.3` wavelet.
- Experiments with EfficientNet-B0, ResNet50, and AlexNet.
- Model training and validation.
- Evaluation using classification performance metrics.

**Technologies:** Python, PyTorch, NumPy, Pandas, PyWavelets, Matplotlib, Scikit-learn.

**Experimental notes**

The models were evaluated during the original project, with EfficientNet-B0 achieving a peak validation accuracy of approximately 93.15% in the recorded experiment. This is a validation result, not a guarantee of performance on unseen external data.

The experiments used different fine-tuning strategies across architectures and did not establish whether denoising improved classification compared with the original images. Further controlled experiments would be needed to investigate these questions.



## Technical Skills Demonstrated

- **Programming:** Python
- **Machine Learning:** Classification, ensemble learning, model evaluation
- **Natural Language Processing:** Text preprocessing, TF-IDF, slang normalization
- **Deep Learning:** CNN architectures and transfer learning
- **Computer Vision:** Image preprocessing, augmentation, wavelet denoising
- **Libraries and Frameworks:** Scikit-learn, PyTorch, XGBoost, Stanza, Pandas, NumPy, Flask

## Future Learning Goals

- Conduct more controlled and reproducible experiments.
- Investigate how preprocessing choices affect model performance.
- Improve model evaluation through appropriate baselines and test sets.
- Explore advanced machine-learning and deep-learning methods.

## Repository Structure

```text
projects/
├── README.md
├── Hinglish-Cyberbullying-Detection/
└── MRI-Image-Classification/
```

The folder names above are illustrative. They should match the actual project directory names in this repository.

## Notes

- Dataset availability and usage are subject to the respective dataset licenses and access requirements.
- Large datasets and trained model weights may be excluded from the repository.
- Please refer to each project's documentation for its implementation details, dependencies, and limitations.
