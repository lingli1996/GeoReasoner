<div align="center">  

# 🌐 GeoReasoner: Geo-localization with Reasoning in Street Views using a Large Vision-Language Model

[![Paper](http://img.shields.io/badge/paper-arxiv.2406.18572-B31B1B.svg)](https://arxiv.org/abs/2406.18572)
[![Conference](https://img.shields.io/badge/ICML-2024-blue)]()

![ALT TEXT](/figures/GeoReasoner.png)
</div>

## Release
- Data
    - For Stage 1 (Reasoning Tuning Phase), We have released the SFT data on [![Hugging Face](https://img.shields.io/badge/HuggingFace-GeoReasoner_SFT-FFD21F)](https://huggingface.co/datasets/ling0821/GeoReasoner_SFT).
    - For Stage 2 (Location Tuning Phase), due to copyright issues with Google Street View images, we are unable to directly provide the corresponding data. However, you can retrieve the relevant data by using the official API provided by [Google Street View](https://www.google.com/streetview).

- Code
    - loc_clip: the codebase for computing locatability of street view images.
    - GeoReasoner: a collection of train and inference scripts of GeoReasoner models.

## Usage and License Notices
This project utilizes certain datasets and checkpoints that are subject to their respective original licenses. It is important to emphasize that the collected data from [GeoGuessr]( https://www.geoguessr.com) and [Tuxun](https://tuxun.fun) cannot be used for commercial purposes.

## Description
- For computing locatability of street view images
  - Follow the [MaskFormer instruction](https://github.com/facebookresearch/MaskFormer/blob/main/GETTING_STARTED.md) to ensure that the Inference Demo with Pre-trained Models works correctly.
  - Obtain the percentage for each category from the segmentation results.
  - Calculate the locatability value by referring to the example in the script `loc_clip/locatability_comput.py`.

- For the inference of GeoReasoner models
  - The pre-trained LVLM weights are available at [![Hugging Face](https://img.shields.io/badge/HuggingFace-Qwen_VL_Chat-FFD21F)](https://huggingface.co/Qwen/Qwen-VL-Chat)
  - Our LoRA weights are available at [![Hugging Face](https://img.shields.io/badge/HuggingFace-GeoReasoner_Models-FFD21F)](https://huggingface.co/ling0821/GeoReasoner_Models)
    - Inference steps
      ```
      cd GeoReasoner
      git clone https://github.com/QwenLM/Qwen-VL.git
      cd Qwen-VL
      pip install -r requirements.txt
      mkdir Qwen-VL-Models 
      mkdir LoRA
      ```
      - Then download the pre-trained LVLM weights into the `Qwen-VL-Models` folder and the LoRA weights into the `LoRA` folder.
      ```Python
      python infer.py # with the test image
      # Due to the inherent randomness in LVLM generation, the generated reasons may not always be consistent.
      ```
    - Training steps (Reasoning Tuning Phase)
      ```
      cd GeoReasoner
      git clone https://github.com/QwenLM/Qwen-VL.git
      cd Qwen-VL
      pip install -r requirements.txt
      mkdir Qwen-VL-Models 
      mkdir LoRA
      mkdir Dataset
      ```
      - Then download the pre-trained LVLM weights into the `Qwen-VL-Models` folder and the SFT data into the `Dataset` folder.
      ```
      mv finetune_lora_reason.sh Qwen-VL/finetune
      cd Qwen-VL
      sh finetune/finetune_lora_reason.sh
      ```


## Acknowledgments
We are very grateful for the source codes and outstanding contributions from [MaskFormer](https://github.com/facebookresearch/MaskFormer), [Sentence-BERT](https://github.com/UKPLab/sentence-transformers) and [Qwen-VL](https://github.com/QwenLM/Qwen-VL).

## Citation
```
@inproceedings{li2024georeasoner,
  title={GeoReasoner: Geo-localization with Reasoning in Street Views using a Large Vision-Language Model},
  author={Li, Ling and Ye, Yu and Zeng, Wei},
  booktitle={International Conference on Machine Learning (ICML)},
  year={2024}
}
```



<!-- Official implementation of the paper "GeoReasoner: Geo-localization with Reasoning in Street Views using a Large Vision-Language Model", to appear in ICML 2024.

Coming soon. -->
