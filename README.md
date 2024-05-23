# Predicting Water Potability

## Project Overview

Access to safe drinking water is essential for health, recognized as a basic human right and a crucial element of effective health protection policies. This project aims to develop a machine-learning model that predicts whether water is safe for human consumption based on various physicochemical parameters. By accurately predicting water potability, we can aid in making informed decisions about water quality management, potentially improving public health outcomes and reducing health care costs.

## Project Structure

- `data/`: This directory contains the dataset used for training and testing the model.
- `notebooks/`: This directory contains Jupyter notebooks for data exploration and model development.
- `src/`: This directory contains the source code for data preprocessing, model training, and prediction.
- `models/`: This directory contains the trained model files.
- `requirements.txt`: This file lists the Python dependencies required for the project.
- `README.md`: This file provides an overview of the project, its structure, and instructions for running the project.

## Dataset

The dataset contains the following physicochemical parameters:

- pH
- Hardness
- Solids
- Chloramines
- Sulfate
- Conductivity
- Organic Carbon
- Trihalomethanes
- Turbidity

The target variable is `Potability`, which indicates whether the water is safe to drink (1) or not (0).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/water-potability-prediction.git
   cd water-potability-prediction ```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Evaluation:
   
To evaluate the model's performance, run the evaluation script:

```bash
Copy code
python app.py
or
streamlit run streamlit_app.py
```

5. Contributing:
   
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

6. Acknowledgements:
   
This project was inspired by the need for improved water quality management and the potential benefits of machine learning in public health.
