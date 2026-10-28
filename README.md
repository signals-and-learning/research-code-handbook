# Suggestions for high-quality research code

The most important thing for research code, is that it should be reproducible: 

*you (and others) should be able to repeat your own results.* 

I give some suggestion based on my own experience bellow

## Some advice:

1. For larger experiments / code base don't use jupyter notebooks. Use python scripts. (see [link](https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI/edit?slide=id.g362da58057_0_639#slide=id.g362da58057_0_639) for some reasoning)
2. Save intermediate results.
3. Use version control


## Some resources:


### How to organize your code

I recomend following the guidelines provided here: [link]
(https://github.com/paperswithcode/releasing-research-code/blob/master/templates/README.md)


### Running remotely
I highly recomend running experiments remotely.
 e have access to the following:
- National Academic Infrastructure for Supercomputing in Sweden (NAISS) [link](https://www.naiss.se/)
- Local division server (only for PhD / Postdocs)

Master students and visitors might have limited access to the above. Then I recoment:
- [Google Colab](https://colab.research.google.com/)
- [Kaggle](https://www.kaggle.com/)
- [Lightning AI](https://lightning.ai/)


Google colab and Kaggle have as default interface jupyter notebooks. And these are ok for small experiments, but as your code base grows, I recomend refactoring your code into scripts and accessing their resorces from the terminal:
-  Access the GPU from terminal: [using the Colab CLI](resources/google-colab/).
- Access the GPU from terminal [example using the Kaggle CLI](resources/kaggle/).

