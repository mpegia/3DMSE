# 3DMSE: An Interactive 3D Media Search Engine

This repository contains the implementation of **3DMSE (3D Media Search Engine)**, an interactive web-based system designed to facilitate the exploration, browsing, and multimodal retrieval of 3D models and images. The system leverages the **MuseHash** approach for scalable Bayesian hashing across multiple representations (meshes, point clouds, and multi-view images).

## Overview

3DMSE integrates advanced single-representation, cross-representation, and multi-representation similarity search capabilities on top of public 3D benchmarks such as **BuildingNet_v0** and **ShapeNetCore**. 

### Key Features
- **Multi-representation Retrieval:** Perform searches using combinations of meshes, point clouds and multi-view projections powered by the MuseHash framework.
- **Interactive 3D Visualizer:** Dynamically inspect and interact with 3D assets (rotate, zoom) using Google's `model-viewer.js` (for meshes in GLTF format) and Three.js (for point clouds in PLY format).
- **Flexible Data Management:** Backed by MongoDB for secure metadata organization and fast retrieval filtering across diverse categories.
- **Local Data Export:** Easily download individual 3D models or preview snapshots directly from the UI.

---

## Technology Stack

- **Front-End:** HTML, CSS, JavaScript, `model-viewer.js`, Three.js[cite: 2]
- **Back-End:** PHP[cite: 2]
- **Database:** MongoDB[cite: 2]
- **Retrieval Engine:** MuseHash (Python-based feature extraction and hashing modules)[cite: 2]

---

## Repository Structure

- 3DMeshRetrievalServiceFor3DMesh.py # Core service script for mesh-to-mesh retrieval queries
- searchBy3DMeshQuery.py             # Execution script handling 3D mesh query processing
- searchByQuery.py                   # General query handling script across various modalities
- mongo_funcs.py                     # Database connection and document management helpers for MongoDB
- utils.py                           # Utility functions for data handling and vector transformations
- run3dMeshRetrievalForSinlge3DMesh.sh # Shell wrapper script to execute single-mesh retrieval pipelines

## 📚 Acknowledgments & Reference

This work was supported by the Horizon Europe research and innovation programme under grant agreement HE-101070250 XRECO.

If you use this code or framework in your research, please cite the original MuseHash paper https://github.com/mpegia/MuseHash/tree/main and the following work:

```bibtex
@inproceedings{pegia20243dmse, 
  title={3DMSE: An Interactive 3D Media Search Engine}, 
  author={Pegia, Maria Eirini and Georgalis, Dimitris and Pantelidis, Nick and J{\'o}nsson, Bj{\"o}rn {\TH}{\'o}r and Moumtzidou, Anastasia and Diplaris, Sotiris and Gialampoukidis, Ilias and Vrochidis, Stefanos and Kompatsiaris, Ioannis}, 
  booktitle={Proceedings of the 2024 International Conference on Multimedia Retrieval}, 
  pages={1260--1264}, 
  year={2024} 
}

## 📜 License
This document is licensed under a Creative Commons Attribution 4.0 (CC BY-NC-SA) licence.
 
