# Name of the conda environment
ENV_NAME ?= {{cookiecutter.project_slug}}
PYTHON_INTERPRETER = python

# Paths to main scripts
CMD_MAIN = src.cmds.cmd_main
{% if cookiecutter.include_training == "y" %}
TRAIN_MAIN = src.cmds.train_main
{% endif %}
{% if cookiecutter.include_inference == "y" %}
INFERENCE_MAIN = src.cmds.inference_main
{% endif %}

# 🌱 Create Conda Environment
.PHONY: create-env
create-env:
	@echo "Creating Conda environment from environment.yml..."
	@conda env create -f environment.yml

# 🚀 Run Command Line Interface
.PHONY: run-cmd
run-cmd:
	@echo "Executing: $(PYTHON_INTERPRETER) -m $(CMD_MAIN)"
	@$(PYTHON_INTERPRETER) -m $(CMD_MAIN)

{% if cookiecutter.include_training == "y" %}
# 🏋 Train Model
.PHONY: run-train
run-train:
	@echo "Executing: $(PYTHON_INTERPRETER) -m $(TRAIN_MAIN)"
	@$(PYTHON_INTERPRETER) -m $(TRAIN_MAIN)
{% endif %}

{% if cookiecutter.include_inference == "y" %}
# 🤖 Run Inference
.PHONY: run-inference
run-inference:
	@echo "Executing: $(PYTHON_INTERPRETER) -m $(INFERENCE_MAIN)"
	@$(PYTHON_INTERPRETER) -m $(INFERENCE_MAIN)
{% endif %}

# 🗑 Clean Environment
.PHONY: clean-env
clean-env:
	@echo "Removing Conda environment: $(ENV_NAME)"
	@conda remove --name $(ENV_NAME) --all -y

# 🧹 Clean Cache
.PHONY: clean-cache
clean-cache:
	@echo "Removing cache files..."
	@find . -name "__pycache__" -type d -exec rm -rf {} +

# 🏗 Install Project Requirements (If using requirements.txt)
.PHONY: install-requirements
install-requirements:
	@echo "Installing dependencies from requirements.txt..."
	@pip install -r requirements.txt