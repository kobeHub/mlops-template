# 🚀 ML Project Template using Cookiecutter 🍪

A logical, standardized, and flexible project structure for Machine Learning and Data Science.

📌 Features
+ 📦 Organized ML workflow: Data processing, model training, inference, and visualization
+ 🔄 Reproducible ML Pipelines: Integration with DVC, CI/CD, and CML
+ ✅ Best Practices: Unit testing with Pytest, linting with Black, and automated workflows
+ 🤖 Highly Customizable: Create only the components you need using Cookiecutter prompts

## 🛠️ Installation

### 1️⃣ Install cookiecutter

Using pipx
```bash
pipx install cookiecutter
```

Using conda:
```bash
conda create -n mlops cookiecutter -c conda-forge
conda activate mlops
conda install cookiecutter
```

### 🎯 Create Your ML Project

Simply run the following command to create a project using this template:
```
cookiecutter https://github.com/kobeHub/mlop-template
```
You will be prompted to enter details like:
+ Author
+ Project Name
+ Open Source License
+ Included Features (Visualization, Training, Inference, etc.)

## 🏗 Project Structure

A project covering the full ML lifecycle including training, inference, and visualization:

```bash
📂 My_ML_Project/   # 🚀 Root directory of the ML project
├── 📜 LICENSE      # 📄 License file
├── ⚙️ Makefile      # 🛠 Task automation
├── 📄 README.md     # 📘 Project documentation
├── 🛠 config/       # ⚙️ Configuration files
├── 📂 data/         # 📊 Data directory
│   ├── 📂 processed/  # 📈 Processed data storage
│   └── 📂 raw/        # 📂 Raw data storage
├── 🏗 environment.yml  # 🏢 Conda environment setup
├── 📑 metadata.yaml   # 📋 Metadata for experiments
├── 📂 models/        # 🏗 Trained models directory
├── 📂 reports/       # 📊 Reports and figures
│   └── 📂 figures/    # 📸 Visualization outputs
├── 📋 requirements.txt # 📦 Dependency list
├── 📂 src/           # 🏗 Source code for the project
│   ├── 📄 __init__.py  # 🔹 Module initializer
│   ├── ⚙ cmds/       # 🖥 Command-line scripts
│   │   ├── 📄 __init__.py
│   │   ├── 🖥 cmd_main.py        # 🎯 Main entry point
│   │   ├── 🤖 inference_main.py  # 🔍 Inference command
│   │   └── 🏋 train_main.py      # 🏋 Training command
│   ├── 📂 data/       # 📊 Data processing scripts
│   │   ├── 📄 __init__.py
│   │   ├── 📊 dataloader.py   # 📥 Loads data
│   │   └── 📜 raw_loading.py  # 📂 Handles raw data
│   ├── 📂 engines/    # 🔥 ML engines (training/inference)
│   │   ├── 📄 __init__.py
│   │   ├── ⚡ inference.py  # 🔍 Runs inference
│   │   └── 🔥 train.py      # 🏋 Training logic
│   ├── 📂 model/      # 🏗 Model architecture
│   │   ├── 📄 __init__.py
│   │   ├── 🏗 arch.py   # 🏢 Model definitions
│   │   └── 🧱 layers.py # 🧩 Model layers
│   └── 📂 visualization/ # 📊 Data visualization tools
│       ├── 📄 __init__.py
│       └── 📊 evaluation.py # 📉 Model evaluation
└── 🧪 tests/          # 🛠 Testing suite
    ├── 📜 README.md
    └── 🛠 test_llm_api_demo.py  # ✅ API test for LLM
```

Or a simplified structure focused on API calls to an LLM:
```bash
📂 my_ml_project/
├── 📜 LICENSE
├── 📄 README.md
├── 🛠 config/
├── 📑 metadata.yaml
├── 📊 reports/
│   └── 📈 figures/
├── 📋 requirements.txt
├── 🏗 environment.yml
├── ⚙️ Makefile 
├── 📂 src/
│   ├── 📄 __init__.py
│   ├── ⚙ cmds/
│   │   ├── 🖥 cmd_main.py
│   ├── 📂 engines/
│   │   ├── ⚡ __init__.py
└── 🧪 tests/
    ├── 📝 README.md
    └── 🛠 test_llm_api_demo.py
```