# Body Mass Index (BMI) Calculator

The Body Mass Index (BMI) is a widely used measure to assess an individual's body weight in relation to their height. It provides a simple numeric indicator that helps classify people into different weight categories. Calculating BMI involves a straightforward formula based on height and weight.

## Calculating BMI

The BMI is calculated using the following formula:

$$ BMI = \frac{Weight}{Height^2} $$

## BMI Categories

The World Health Organization (WHO) provides the following classification based on BMI ranges:

- **Underweight:** BMI less than 18.5
- **Normal weight:** BMI between 18.5 and 24.9
- **Overweight:** BMI between 25 and 29.9
- **Obese Class I:** BMI between 30 and 34.9
- **Obese Class II:** BMI between 35 and 39.9
- **Obese Class III:** BMI 40 or greater

Understanding your BMI category can be an important step in evaluating your overall health and assessing potential health risks associated with weight. Keep in mind that while BMI is a useful screening tool, it does not directly measure body fat and may not be suitable for everyone, such as athletes with high muscle mass.

Remember, consulting with a healthcare professional provides a more comprehensive evaluation of your health status.


## Virtual Environment

In this repo you will find a [requirements.txt](requirements.txt) file. It contains all the libraries you will need.

```BASH
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

## How to start

Open the terminal or command prompt. Navigate to the directory where the BMI.ipynb file is located and type:

```
jupyter notebook
```



If there are missing dependencies, you will need to install them using the !pip install dependency_name command directly in a code cell.

Enjoy!