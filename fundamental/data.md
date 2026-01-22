# Data — Lecture Notes

## Definition
- **Data:** Raw facts, figures, measurements or observations collected about entities or events. When processed, organized, or interpreted, data becomes information that supports decision-making.

## Characteristics of Data (The 5 V's)
- **Volume:** Amount of data (small to petabytes/exabytes).
- **Velocity:** Speed at which data is generated and processed.
- **Variety:** Different types and formats (structured, unstructured, semi-structured).
- **Veracity:** Trustworthiness and quality of the data.
- **Value:** Usefulness and insights derived from the data.

## Types of Data
- **Structured data:** Highly organized, fits tabular schemas (databases, CSV). Easy to query with SQL.
- **Semi-structured data:** Has tags or markers but not fixed schema (JSON, XML, YAML).
- **Unstructured data:** No predefined model (text, images, audio, video, PDFs).
- **Time-series data:** Ordered observations indexed by time (sensor data, logs, stock prices).
- **Transactional data:** Records of events or transactions (sales, bank transfers).

## Data Formats & Storage
- **Formats:** CSV, JSON, XML, Parquet, Avro, TXT, images (PNG, JPEG), audio (MP3, WAV), video (MP4).
- **Storage options:** Relational databases (PostgreSQL, MySQL), NoSQL (MongoDB, Cassandra), data lakes (S3, HDFS), data warehouses (BigQuery, Redshift).

## Data Lifecycle
1. **Collection** — sensors, forms, logs, APIs, scraping.
2. **Ingestion** — import into storage (batch or streaming).
3. **Processing / Cleaning** — transform, normalize, handle missing values, deduplicate.
4. **Storage** — store raw and processed data appropriately.
5. **Analysis / Modeling** — exploratory analysis, statistical modeling, ML.
6. **Visualization & Reporting** — present insights via charts, dashboards.
7. **Archival / Deletion** — comply with retention policies and privacy rules.

## Data Quality Dimensions
- **Accuracy:** Correctness of values.
- **Completeness:** Missing or present values.
- **Consistency:** Uniform format and standards across datasets.
- **Timeliness:** Data is up-to-date when needed.
- **Uniqueness:** No duplicate records.

## Example Use Cases
- Business intelligence: sales analysis, customer segmentation.
- Machine learning: prediction, classification, recommendation systems.
- Monitoring & observability: system logs and metrics.
- Research: surveys, experiments, scientific measurements.

## Short Code Examples
- Read CSV with Python (Pandas):
```python
import pandas as pd

df = pd.read_csv('data/sales.csv')
print(df.head())
```
- Parse JSON in JavaScript (node):
```javascript
const fs = require('fs');
const obj = JSON.parse(fs.readFileSync('data/config.json', 'utf8'));
console.log(obj);
```
- Simple SQL query (structured data):
```sql
SELECT customer_id, SUM(amount) as total_spent
FROM transactions
WHERE transaction_date >= '2025-01-01'
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10;
```

## Data Privacy & Ethics
- Be aware of personal data (PII) and legal frameworks (GDPR, CCPA).
- Anonymize or pseudonymize sensitive data before sharing.
- Obtain consent and document data provenance.

## Best Practices
- Define clear schemas and catalog datasets.
- Track lineage and metadata (who changed what and when).
- Validate data at ingestion and automate quality checks.
- Use version control for code and configuration; use managed storage for backups.

## Quick Study Tips
- Inspect a real dataset: check schema, missing values, and basic statistics.
- Practice cleaning tasks: remove duplicates, impute missing values, normalize types.
- Build a small pipeline: ingest CSV → clean → analyze → visualize.

---

Prepared as concise lecture notes on the concept, types, lifecycle, and uses of data.

