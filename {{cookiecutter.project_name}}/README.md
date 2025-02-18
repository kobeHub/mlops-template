# 🚀 {{cookiecutter.project_name}}

Project generated using the MLOps-Template Cookiecutter.

## 📋 Requirements

+ Python 3
+ Conda (optional, for environment management)
+ Make (for running automated tasks)

## 🏃🏻 Running Project

✅ Setup Environment

Create a Conda environment using the provided environment.yml:

```bash
make create-env
conda activate {{cookiecutter.project_slug}}
```
Alternatively, install dependencies via pip:
```bash
make install-requirements
```

## 🚀 Running Commands

### 1️⃣ Run Main Command

```bash
make run-cmd
```

### 2️⃣ Clean Environment

```bash
make clean-env
```