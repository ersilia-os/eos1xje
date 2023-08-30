# BioGPT embeddings

BioGPT is a pre-trained transformer for biomedical text. This domain-specific model has been trained on large-scale biomedical literature. In this implementation, we use BioGPT to generate numerical embeddings for bioassay and other biomedical texts.

## Identifiers

* EOS model ID: `eos1xje`
* Slug: `biogpt-embeddings`

## Characteristics

* Input: `Text`
* Input Shape: `Single`
* Task: `Representation`
* Output: `Descriptor`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: Biomedical text embedding

## References

* [Publication](https://academic.oup.com/bib/article/23/6/bbac409/6713511?guestAccessKey=a66d9b5d-4f83-4017-bb52-405815c907b9&login=false)
* [Source Code](https://github.com/microsoft/biogpt)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos1xje)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos1xje.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos1xje) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://academic.oup.com/bib/article/23/6/bbac409/6713511?guestAccessKey=a66d9b5d-4f83-4017-bb52-405815c907b9&login=false) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!