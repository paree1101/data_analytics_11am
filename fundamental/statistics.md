# Statistics — Lecture Notes

## What is Statistics?
- **Statistics:** The science of collecting, summarizing, analysing, and interpreting data to make informed decisions and draw conclusions under uncertainty.

## Two Main Branches
- **Descriptive statistics:** Summarize and describe features of a dataset (tables, charts, measures of centre and spread).
- **Inferential statistics:** Use sample data to make estimates, predictions, or decisions about a population (confidence intervals, hypothesis tests, regression).

## Types of Data
- **Qualitative (categorical):** Nominal (labels, e.g., colour) and ordinal (ordered categories, e.g., rating).
- **Quantitative (numeric):** Discrete (counts) and continuous (measurements).

## Measures of Central Tendency
- **Mean (average):** Sum of values divided by count.
- **Median:** Middle value when data are ordered — robust to outliers.
- **Mode:** Most frequent value(s).

## Measures of Dispersion
- **Range:** Max − Min.
- **Interquartile Range (IQR):** Q3 − Q1, robust measure.
- **Variance (σ²/sample variance s²):** Average squared deviation from the mean.
- **Standard deviation (σ or s):** Square root of variance — same units as data.

## Shape & Distribution
- **Skewness:** Asymmetry of the distribution (right/positive skew vs left/negative skew).
- **Kurtosis:** "Peakedness" and tail weight relative to normal.
- **Common distributions:** Normal (Gaussian), Binomial, Poisson, Exponential, Uniform.

## Probability Basics
- **Probability:** Measure between 0 and 1 of an event's occurrence.
- **Conditional probability:** P(A|B) — probability of A given B.
- **Independence:** P(A∩B) = P(A)P(B) if A and B independent.

## Sampling & Central Limit Theorem
- **Sampling:** Process of selecting observations from a population.
- **Sampling error:** Variability between sample statistics and true population parameters.
- **Central Limit Theorem (CLT):** For large sample sizes, the sampling distribution of the sample mean is approximately normal regardless of population distribution (under mild conditions).

## Confidence Intervals
- Interval estimate for a parameter (e.g., mean): point estimate ± margin of error.
- Interpret as: "If we repeated sampling many times, X% of such intervals would contain the true parameter." (avoid saying probability about a fixed parameter).

## Hypothesis Testing (brief)
- **Null hypothesis (H0):** Default/no-effect statement.
- **Alternative hypothesis (H1):** Statement we seek evidence for.
- **Test statistic:** Summary metric computed from data (e.g., t-statistic, z-score).
- **P-value:** Probability of observing data at least as extreme as observed under H0.
- **Significance level (α):** Threshold to reject H0 (commonly 0.05).
- **Type I error:** Reject H0 when true (false positive).
- **Type II error:** Fail to reject H0 when false (false negative).

## Common Tests
- **z-test / t-test:** Compare means (t-test for small samples/unknown σ).
- **Chi-square test:** Categorical association / goodness-of-fit.
- **ANOVA:** Compare means across >2 groups.
- **Non-parametric tests:** Mann–Whitney U, Wilcoxon, Kruskal–Wallis (when assumptions fail).

## Correlation & Regression
- **Correlation (Pearson r):** Measures linear relationship between two variables (range −1 to 1). Correlation ≠ causation.
- **Simple linear regression:** Model relationship y = β0 + β1x + ε; estimate slope β1 and intercept β0.
- **Multiple regression:** Multiple predictors to explain variation in a response.
- Check assumptions: linearity, independence, homoscedasticity, normality of residuals, multicollinearity.

## Data Visualization (key plots)
- **Histogram:** Distribution of a single numeric variable.
- **Boxplot:** Median, IQR, and outliers.
- **Scatterplot:** Relationship between two numeric variables.
- **Bar chart / Pie chart:** Categorical summaries (use pie sparingly).
- **QQ-plot:** Check normality by comparing quantiles.

## Practical Workflow
1. Define question and identify variables.
2. Collect or import data; inspect structure and types.
3. Clean data: handle missing values, outliers, and types.
4. Explore with descriptive stats and visualizations.
5. Formal analysis: tests, models, estimation.
6. Validate results and check assumptions.
7. Communicate findings (plots, summaries, limitations).

## Short Code Examples
- Compute basic stats with Python (Pandas):
```python
import pandas as pd
df = pd.read_csv('data.csv')
df.describe()
```
- Perform a t-test in Python (SciPy):
```python
from scipy import stats
stats.ttest_ind(sample1, sample2)
```
- Simple linear regression with statsmodels:
```python
import statsmodels.api as sm
X = sm.add_constant(df['x'])
model = sm.OLS(df['y'], X).fit()
print(model.summary())
```

## Common Pitfalls
- Confusing correlation with causation.
- Ignoring data quality and outliers.
- Running many tests without correcting for multiple comparisons.
- Violating model assumptions without checking.

## Further Reading
- Introductory texts: "Introduction to the Practice of Statistics", "Statistics" (Freedman/Pisani/Purves).
- Online resources: Khan Academy statistics, Coursera, StatQuest (YouTube).

---

Prepared as concise lecture notes on core statistical concepts, tests, and practical steps.

## How Statistics Are Represented — Charts & Examples
Below are common visual representations, when to use them, and short code examples (Python / Matplotlib & Seaborn). Use these to illustrate distributions, relationships, and summaries.

- **Histogram** — shows distribution of a single numeric variable; useful to see shape, skew, and modality.
```python
import matplotlib.pyplot as plt
import seaborn as sns
sns.histplot(data=df, x='age', bins=20, kde=True)
plt.title('Age distribution')
plt.show()
```

- **Boxplot** — summarizes median, IQR, and outliers; great for comparing distributions across groups.
```python
sns.boxplot(x='group', y='income', data=df)
plt.title('Income by group')
plt.show()
```

- **Scatterplot** — shows relationship between two numeric variables; add regression line to inspect trend.
```python
sns.scatterplot(x='hours_studied', y='score', data=df)
sns.regplot(x='hours_studied', y='score', data=df, scatter=False, color='red')
plt.title('Score vs Hours Studied')
plt.show()
```

- **Bar chart** — categorical comparisons (counts or aggregated metric like mean).
```python
df.groupby('category')['sales'].sum().plot(kind='bar')
plt.title('Total sales by category')
plt.show()
```

- **Line chart** — time series trends (use when x-axis is time-ordered).
```python
df.set_index('date').sales.plot()
plt.title('Sales over time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()
```

- **Heatmap (correlation matrix)** — show pairwise correlations to understand relationships.
```python
corr = df.corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='vlag')
plt.title('Correlation matrix')
plt.show()
```

- **QQ-plot** — check normality of a variable by comparing quantiles to a theoretical normal.
```python
import scipy.stats as stats
import matplotlib.pyplot as plt
stats.probplot(df['residuals'], dist='norm', plot=plt)
plt.title('QQ-plot of residuals')
plt.show()
```

- **Pie chart** — shows parts of a whole; use sparingly and only for few categories.
```python
df['region'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.ylabel('')
plt.title('Distribution by region')
plt.show()
```

### Quick Excel equivalents
- Histogram: `Insert > Chart > Histogram` or use Data Analysis ToolPak.
- Boxplot: `Insert > Insert Statistic Chart > Box and Whisker`.
- PivotTable + PivotChart: aggregate and visualize categorical summaries.

### Display Tips
- Always label axes and add a descriptive title.
- Use legends and color palettes that are colorblind-friendly.
- For comparisons, use consistent scales across charts.
- Avoid chart junk — keep visuals clear and focused on the message.

