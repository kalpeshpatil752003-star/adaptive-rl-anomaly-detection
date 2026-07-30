# 📁 PROJECT EXPORT FOR LLMs

## 📊 Project Information

- **Project Name**: `adaptive_rl_anomaly_detection`
- **Generated On**: 2026-07-30 15:43:06 (Asia/Calcutta / GMT+06:30)
- **Total Files Processed**: 102
- **Export Tool**: Easy Whole Project to Single Text File for LLMs v1.1.0
- **Tool Author**: Jota / José Guilherme Pandolfi

### ⚙️ Export Configuration

| Setting | Value |
|---------|-------|
| Language | `en` |
| Max File Size | `1 MB` |
| Include Hidden Files | `false` |
| Output Format | `both` |

## 🌳 Project Structure

```
├── 📁 adaptive_rl_anomaly_detection.egg-info/
│   ├── 📄 dependency_links.txt (1 B)
│   ├── 📄 PKG-INFO (177 B)
│   ├── 📄 SOURCES.txt (254 B)
│   └── 📄 top_level.txt (4 B)
├── 📁 checkpoints/
│   ├── 📁 autoencoder/
│   ├── 📁 isolation_forest/
│   ├── 📁 lof/
│   ├── 📁 ocsvm/
│   └── 📁 rl/
├── 📁 configs/
├── 📁 datasets/
│   ├── 📁 external/
│   ├── 📁 processed/
│   └── 📁 raw/
│       ├── 📄 Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv (73.55 MB)
│       ├── 📄 Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv (73.34 MB)
│       ├── 📄 Friday-WorkingHours-Morning.pcap_ISCX.csv (55.62 MB)
│       ├── 📄 industry.csv (749 B)
│       ├── 📄 Monday-WorkingHours.pcap_ISCX.csv (168.73 MB)
│       ├── 📄 Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv (79.25 MB)
│       ├── 📄 Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv (49.61 MB)
│       ├── 📄 Tuesday-WorkingHours.pcap_ISCX.csv (128.82 MB)
│       └── 📄 Wednesday-workingHours.pcap_ISCX.csv (214.74 MB)
├── 📁 docs/
├── 📁 logs/
│   └── 📄 framework.log (117.21 KB)
├── 📁 notebooks/
│   ├── 📁 logs/
│   │   └── 📄 framework.log (447 B)
│   ├── 📁 trained_models/
│   │   ├── 📄 isolation_forest.joblib (1.46 MB)
│   │   ├── 📄 local_outlier_factor.joblib (70.19 MB)
│   │   └── 📄 one_class_svm.joblib (1.39 MB)
│   ├── 📄 01_test_config.ipynb (2.72 KB)
│   ├── 📄 02_test_seed.ipynb (1.46 KB)
│   ├── 📄 03_test_logger.ipynb (1.33 KB)
│   ├── 📄 04_test_timer.ipynb.ipynb (1.74 KB)
│   ├── 📄 05_test_loader.ipynb (2.91 KB)
│   ├── 📄 06_test_cleaner.ipynb (3.55 KB)
│   ├── 📄 07_test_encoder.ipynb (6.98 KB)
│   ├── 📄 08_test_scaler.ipynb (5.46 KB)
│   ├── 📄 09_test_splitter.ipynb (4.91 KB)
│   ├── 📄 10_test_correlation.ipynb (5.99 KB)
│   ├── 📄 11_test_statistics.ipynb (8.9 KB)
│   ├── 📄 12_test_selector.ipynb (6.19 KB)
│   ├── 📄 13_test_dimensionality_reduction.ipynb (6.49 KB)
│   ├── 📄 14_test_feature_pipeline.ipynb (6.06 KB)
│   ├── 📄 15_base_model.ipynb (1.58 KB)
│   ├── 📄 16_Isolation_Forest.ipynb (26.16 KB)
│   ├── 📄 17_local_outlier_factor.ipynb.ipynb (18.66 KB)
│   └── 📄 18_one_class_svm.ipynb (22.09 KB)
├── 📁 outputs/
│   ├── 📁 figures/
│   ├── 📁 history/
│   ├── 📁 metrics/
│   ├── 📁 models/
│   ├── 📁 predictions/
│   └── 📁 reports/
├── 📁 src/
│   ├── 📁 __pycache__/
│   │   └── 📄 __init__.cpython-312.pyc (163 B)
│   ├── 📁 config/
│   │   ├── 📁 __pycache__/
│   │   │   ├── 📄 __init__.cpython-312.pyc (361 B)
│   │   │   ├── 📄 config.cpython-312.pyc (5.39 KB)
│   │   │   ├── 📄 isolation_forest_config.cpython-312.pyc (1.08 KB)
│   │   │   ├── 📄 local_outlier_factor_config.cpython-312.pyc (1.96 KB)
│   │   │   └── 📄 one_class_svm_config.cpython-312.pyc (1.16 KB)
│   │   ├── 📄 __init__.py (202 B)
│   │   ├── 📄 config.py (4.25 KB)
│   │   ├── 📄 isolation_forest_config.py (495 B)
│   │   ├── 📄 local_outlier_factor_config.py (1.33 KB)
│   │   └── 📄 one_class_svm_config.py (528 B)
│   ├── 📁 ensemble/
│   │   └── 📄 __init__.py
│   ├── 📁 evaluation/
│   │   └── 📄 __init__.py
│   ├── 📁 feature_engineering/
│   │   ├── 📁 __pycache__/
│   │   │   ├── 📄 __init__.cpython-312.pyc (183 B)
│   │   │   ├── 📄 correlation_analysis.cpython-312.pyc (3.01 KB)
│   │   │   ├── 📄 dimensionality_reduction.cpython-312.pyc (3.11 KB)
│   │   │   ├── 📄 feature_pipeline.cpython-312.pyc (3.1 KB)
│   │   │   ├── 📄 feature_selector.cpython-312.pyc (5.5 KB)
│   │   │   └── 📄 statistical_features.cpython-312.pyc (2.66 KB)
│   │   ├── 📄 __init__.py
│   │   ├── 📄 correlation_analysis.py (1.75 KB)
│   │   ├── 📄 dimensionality_reduction.py (1.86 KB)
│   │   ├── 📄 feature_pipeline.py (2.28 KB)
│   │   ├── 📄 feature_selector.py (4.83 KB)
│   │   └── 📄 statistical_features.py (1.53 KB)
│   ├── 📁 models/
│   │   ├── 📁 __pycache__/
│   │   │   ├── 📄 __init__.cpython-312.pyc (477 B)
│   │   │   ├── 📄 base_model.cpython-312.pyc (7.37 KB)
│   │   │   ├── 📄 isolation_forest.cpython-312.pyc (6.6 KB)
│   │   │   ├── 📄 local_outlier_factor.cpython-312.pyc (6.26 KB)
│   │   │   └── 📄 one_class_svm.cpython-312.pyc (6.44 KB)
│   │   ├── 📄 __init__.py (315 B)
│   │   ├── 📄 autoencoder.py
│   │   ├── 📄 base_model.py (5.88 KB)
│   │   ├── 📄 isolation_forest.py (4.2 KB)
│   │   ├── 📄 local_outlier_factor.py (4.1 KB)
│   │   ├── 📄 model_factory.py
│   │   └── 📄 one_class_svm.py (4.25 KB)
│   ├── 📁 pipelines/
│   │   └── 📄 __init__.py
│   ├── 📁 preprocessing/
│   │   ├── 📁 __pycache__/
│   │   │   ├── 📄 __init__.cpython-312.pyc (177 B)
│   │   │   ├── 📄 cleaner.cpython-312.pyc (4.14 KB)
│   │   │   ├── 📄 encoder.cpython-312.pyc (3.87 KB)
│   │   │   ├── 📄 loader.cpython-312.pyc (3.47 KB)
│   │   │   ├── 📄 scaler.cpython-312.pyc (5.66 KB)
│   │   │   └── 📄 splitter.cpython-312.pyc (3.09 KB)
│   │   ├── 📄 __init__.py
│   │   ├── 📄 cleaner.py (2.72 KB)
│   │   ├── 📄 encoder.py (2.61 KB)
│   │   ├── 📄 loader.py (2.02 KB)
│   │   ├── 📄 scaler.py (4.45 KB)
│   │   └── 📄 splitter.py (2.67 KB)
│   ├── 📁 rl/
│   │   └── 📄 __init__.py
│   ├── 📁 utils/
│   │   ├── 📁 __pycache__/
│   │   │   ├── 📄 __init__.cpython-312.pyc (169 B)
│   │   │   ├── 📄 logger.cpython-312.pyc (2.18 KB)
│   │   │   ├── 📄 seed.cpython-312.pyc (2.69 KB)
│   │   │   └── 📄 timer.cpython-312.pyc (2.49 KB)
│   │   ├── 📄 __init__.py
│   │   ├── 📄 logger.py (1.34 KB)
│   │   ├── 📄 seed.py (1.54 KB)
│   │   └── 📄 timer.py (1.29 KB)
│   ├── 📁 visualization/
│   │   └── 📄 __init__.py
│   └── 📄 __init__.py
├── 📁 tests/
├── 📄 nohup.out (2.73 KB)
├── 📄 pyproject.toml (344 B)
├── 📄 README.md
├── 📄 requirements.txt
└── 📄 setup_project.sh (1.24 KB)
```

## 📑 Table of Contents

**Project Files:**

- [📄 adaptive_rl_anomaly_detection.egg-info/dependency_links.txt](#📄-adaptive-rl-anomaly-detection-egg-info-dependency-links-txt)
- [📄 adaptive_rl_anomaly_detection.egg-info/SOURCES.txt](#📄-adaptive-rl-anomaly-detection-egg-info-sources-txt)
- [📄 adaptive_rl_anomaly_detection.egg-info/top_level.txt](#📄-adaptive-rl-anomaly-detection-egg-info-top-level-txt)
- [📄 logs/framework.log](#📄-logs-framework-log)
- [📄 notebooks/logs/framework.log](#📄-notebooks-logs-framework-log)
- [📄 src/config/__init__.py](#📄-src-config-init-py)
- [📄 src/config/config.py](#📄-src-config-config-py)
- [📄 src/config/isolation_forest_config.py](#📄-src-config-isolation-forest-config-py)
- [📄 src/config/local_outlier_factor_config.py](#📄-src-config-local-outlier-factor-config-py)
- [📄 src/config/one_class_svm_config.py](#📄-src-config-one-class-svm-config-py)
- [📄 src/ensemble/__init__.py](#📄-src-ensemble-init-py)
- [📄 src/evaluation/__init__.py](#📄-src-evaluation-init-py)
- [📄 src/feature_engineering/__init__.py](#📄-src-feature-engineering-init-py)
- [📄 src/feature_engineering/correlation_analysis.py](#📄-src-feature-engineering-correlation-analysis-py)
- [📄 src/feature_engineering/dimensionality_reduction.py](#📄-src-feature-engineering-dimensionality-reduction-py)
- [📄 src/feature_engineering/feature_pipeline.py](#📄-src-feature-engineering-feature-pipeline-py)
- [📄 src/feature_engineering/feature_selector.py](#📄-src-feature-engineering-feature-selector-py)
- [📄 src/feature_engineering/statistical_features.py](#📄-src-feature-engineering-statistical-features-py)
- [📄 src/models/__init__.py](#📄-src-models-init-py)
- [📄 src/models/autoencoder.py](#📄-src-models-autoencoder-py)
- [📄 src/models/base_model.py](#📄-src-models-base-model-py)
- [📄 src/models/isolation_forest.py](#📄-src-models-isolation-forest-py)
- [📄 src/models/local_outlier_factor.py](#📄-src-models-local-outlier-factor-py)
- [📄 src/models/model_factory.py](#📄-src-models-model-factory-py)
- [📄 src/models/one_class_svm.py](#📄-src-models-one-class-svm-py)
- [📄 src/pipelines/__init__.py](#📄-src-pipelines-init-py)
- [📄 src/preprocessing/__init__.py](#📄-src-preprocessing-init-py)
- [📄 src/preprocessing/cleaner.py](#📄-src-preprocessing-cleaner-py)
- [📄 src/preprocessing/encoder.py](#📄-src-preprocessing-encoder-py)
- [📄 src/preprocessing/loader.py](#📄-src-preprocessing-loader-py)
- [📄 src/preprocessing/scaler.py](#📄-src-preprocessing-scaler-py)
- [📄 src/preprocessing/splitter.py](#📄-src-preprocessing-splitter-py)
- [📄 src/rl/__init__.py](#📄-src-rl-init-py)
- [📄 src/utils/__init__.py](#📄-src-utils-init-py)
- [📄 src/utils/logger.py](#📄-src-utils-logger-py)
- [📄 src/utils/seed.py](#📄-src-utils-seed-py)
- [📄 src/utils/timer.py](#📄-src-utils-timer-py)
- [📄 src/visualization/__init__.py](#📄-src-visualization-init-py)
- [📄 src/__init__.py](#📄-src-init-py)
- [📄 pyproject.toml](#📄-pyproject-toml)
- [📄 README.md](#📄-readme-md)
- [📄 requirements.txt](#📄-requirements-txt)
- [📄 setup_project.sh](#📄-setup-project-sh)

---

## 📈 Project Statistics

| Metric | Count |
|--------|-------|
| Total Files | 102 |
| Total Directories | 42 |
| Text Files | 43 |
| Binary Files | 59 |
| Total Size | 917.1 MB |

### 📄 File Types Distribution

| Extension | Count |
|-----------|-------|
| `.py` | 34 |
| `.pyc` | 27 |
| `.ipynb` | 18 |
| `.csv` | 9 |
| `.txt` | 4 |
| `.joblib` | 3 |
| `.log` | 2 |
| `no extension` | 1 |
| `.out` | 1 |
| `.toml` | 1 |
| `.md` | 1 |
| `.sh` | 1 |

## 💻 File Code Contents

### <a id="📄-adaptive-rl-anomaly-detection-egg-info-dependency-links-txt"></a>📄 `adaptive_rl_anomaly_detection.egg-info/dependency_links.txt`

**File Info:**
- **Size**: 1 B
- **Extension**: `.txt`
- **Language**: `text`
- **Location**: `adaptive_rl_anomaly_detection.egg-info/dependency_links.txt`
- **Relative Path**: `adaptive_rl_anomaly_detection.egg-info`
- **Created**: 2026-07-25 06:13:02 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 06:13:02 (Asia/Calcutta / GMT+06:30)
- **MD5**: `68b329da9893e34099c7d8ad5cb9c940`
- **SHA256**: `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b`
- **Encoding**: ASCII

**File code content:**

```text


```

---

### <a id="📄-adaptive-rl-anomaly-detection-egg-info-sources-txt"></a>📄 `adaptive_rl_anomaly_detection.egg-info/SOURCES.txt`

**File Info:**
- **Size**: 254 B
- **Extension**: `.txt`
- **Language**: `text`
- **Location**: `adaptive_rl_anomaly_detection.egg-info/SOURCES.txt`
- **Relative Path**: `adaptive_rl_anomaly_detection.egg-info`
- **Created**: 2026-07-25 06:13:02 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 06:13:02 (Asia/Calcutta / GMT+06:30)
- **MD5**: `1efbb65fc29aa42c07c242a416f5ba37`
- **SHA256**: `4e9d0d199b4b2a7ceae760ab289dd4a631787c12f26acd695c3accfa018c8fb7`
- **Encoding**: ASCII

**File code content:**

```text
README.md
pyproject.toml
./src/__init__.py
adaptive_rl_anomaly_detection.egg-info/PKG-INFO
adaptive_rl_anomaly_detection.egg-info/SOURCES.txt
adaptive_rl_anomaly_detection.egg-info/dependency_links.txt
adaptive_rl_anomaly_detection.egg-info/top_level.txt
```

---

### <a id="📄-adaptive-rl-anomaly-detection-egg-info-top-level-txt"></a>📄 `adaptive_rl_anomaly_detection.egg-info/top_level.txt`

**File Info:**
- **Size**: 4 B
- **Extension**: `.txt`
- **Language**: `text`
- **Location**: `adaptive_rl_anomaly_detection.egg-info/top_level.txt`
- **Relative Path**: `adaptive_rl_anomaly_detection.egg-info`
- **Created**: 2026-07-25 06:13:02 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 06:13:02 (Asia/Calcutta / GMT+06:30)
- **MD5**: `369990b384d3cb76276c5aa5c98725c9`
- **SHA256**: `ef8aed55fba64258003f3479ff60a060ddb8301d170110a0d2dfa0ce4ea04eb3`
- **Encoding**: ASCII

**File code content:**

```text
src

```

---

## 🚫 Binary/Excluded Files

The following files were not included in the text content:

- `adaptive_rl_anomaly_detection.egg-info/PKG-INFO`

## 🚫 Binary/Excluded Files

The following files were not included in the text content:

- `datasets/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv`
- `datasets/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv`
- `datasets/raw/Friday-WorkingHours-Morning.pcap_ISCX.csv`
- `datasets/raw/industry.csv`
- `datasets/raw/Monday-WorkingHours.pcap_ISCX.csv`
- `datasets/raw/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv`
- `datasets/raw/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv`
- `datasets/raw/Tuesday-WorkingHours.pcap_ISCX.csv`
- `datasets/raw/Wednesday-workingHours.pcap_ISCX.csv`

### <a id="📄-logs-framework-log"></a>📄 `logs/framework.log`

**File Info:**
- **Size**: 117.21 KB
- **Extension**: `.log`
- **Language**: `text`
- **Location**: `logs/framework.log`
- **Relative Path**: `logs`
- **Created**: 2026-07-30 15:14:16 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-30 15:14:16 (Asia/Calcutta / GMT+06:30)
- **MD5**: `90ac4dfa3969dbef1061c098abe525d5`
- **SHA256**: `d40579705dee5e118c57521a5f5a4a00d5b8e670a76c6814a385ab1306e5e5d6`
- **Encoding**: ASCII

**File code content:**

```text
2026-07-25 06:50:09 | INFO     | AdaptiveRL | Loading industry.csv started.
2026-07-25 06:50:09 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/industry.csv
2026-07-25 06:50:09 | INFO     | AdaptiveRL | Loaded industry.csv | Shape=(43, 1)
2026-07-25 06:50:09 | INFO     | AdaptiveRL | Loading industry.csv completed in 0.0299 seconds.
2026-07-25 06:50:26 | INFO     | AdaptiveRL | Rows: 43
2026-07-25 06:50:26 | INFO     | AdaptiveRL | Columns: 1
2026-07-25 06:50:26 | INFO     | AdaptiveRL | Memory Usage: 0.00 MB
2026-07-25 06:54:50 | INFO     | AdaptiveRL | Loading industry.csv started.
2026-07-25 06:54:50 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/industry.csv
2026-07-25 06:54:50 | INFO     | AdaptiveRL | Loaded industry.csv | Shape=(43, 1)
2026-07-25 06:54:50 | INFO     | AdaptiveRL | Loading industry.csv completed in 0.0223 seconds.
2026-07-25 06:54:57 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-25 06:54:57 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 0.0023 seconds.
2026-07-25 06:54:57 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-25 06:54:57 | INFO     | AdaptiveRL | Removed 0 duplicate rows.
2026-07-25 06:54:57 | INFO     | AdaptiveRL | Removing Duplicates completed in 0.0212 seconds.
2026-07-25 06:54:57 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-25 06:54:57 | INFO     | AdaptiveRL | Removed 0 rows containing missing values.
2026-07-25 06:54:57 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.0019 seconds.
2026-07-25 06:54:57 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-25 06:54:57 | INFO     | AdaptiveRL | Removed 0 constant columns.
2026-07-25 06:54:57 | INFO     | AdaptiveRL | Removing Constant Columns completed in 0.0053 seconds.
2026-07-25 06:54:57 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (43, 1)
2026-07-25 06:56:38 | INFO     | AdaptiveRL | Loading industry.csv started.
2026-07-25 06:56:38 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/industry.csv
2026-07-25 06:56:38 | INFO     | AdaptiveRL | Loaded industry.csv | Shape=(43, 1)
2026-07-25 06:56:38 | INFO     | AdaptiveRL | Loading industry.csv completed in 0.0183 seconds.
2026-07-25 06:56:38 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-25 06:56:38 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 0.0007 seconds.
2026-07-25 06:56:38 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-25 06:56:38 | INFO     | AdaptiveRL | Removed 0 duplicate rows.
2026-07-25 06:56:38 | INFO     | AdaptiveRL | Removing Duplicates completed in 0.0026 seconds.
2026-07-25 06:56:38 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-25 06:56:38 | INFO     | AdaptiveRL | Removed 0 rows containing missing values.
2026-07-25 06:56:38 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.0025 seconds.
2026-07-25 06:56:38 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-25 06:56:38 | INFO     | AdaptiveRL | Removed 0 constant columns.
2026-07-25 06:56:38 | INFO     | AdaptiveRL | Removing Constant Columns completed in 0.0022 seconds.
2026-07-25 06:56:38 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (43, 1)
2026-07-25 06:56:38 | INFO     | AdaptiveRL | Encoding Features started.
2026-07-25 06:56:38 | INFO     | AdaptiveRL | Encoded feature: Industry
2026-07-25 06:56:38 | INFO     | AdaptiveRL | Encoding Features completed in 0.0292 seconds.
2026-07-25 07:00:05 | INFO     | AdaptiveRL | Loading industry.csv started.
2026-07-25 07:00:05 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/industry.csv
2026-07-25 07:00:05 | INFO     | AdaptiveRL | Loaded industry.csv | Shape=(43, 1)
2026-07-25 07:00:05 | INFO     | AdaptiveRL | Loading industry.csv completed in 0.0142 seconds.
2026-07-25 07:00:05 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-25 07:00:05 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 0.0022 seconds.
2026-07-25 07:00:05 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-25 07:00:05 | INFO     | AdaptiveRL | Removed 0 duplicate rows.
2026-07-25 07:00:05 | INFO     | AdaptiveRL | Removing Duplicates completed in 0.0045 seconds.
2026-07-25 07:00:05 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-25 07:00:05 | INFO     | AdaptiveRL | Removed 0 rows containing missing values.
2026-07-25 07:00:05 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.0026 seconds.
2026-07-25 07:00:05 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-25 07:00:05 | INFO     | AdaptiveRL | Removed 0 constant columns.
2026-07-25 07:00:05 | INFO     | AdaptiveRL | Removing Constant Columns completed in 0.0031 seconds.
2026-07-25 07:00:05 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (43, 1)
2026-07-25 07:00:05 | INFO     | AdaptiveRL | Encoding Features started.
2026-07-25 07:00:05 | INFO     | AdaptiveRL | Encoded feature: Industry
2026-07-25 07:00:05 | INFO     | AdaptiveRL | Encoding Features completed in 0.0029 seconds.
2026-07-25 07:01:11 | INFO     | AdaptiveRL | Loading industry.csv started.
2026-07-25 07:01:11 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/industry.csv
2026-07-25 07:01:11 | INFO     | AdaptiveRL | Loaded industry.csv | Shape=(43, 1)
2026-07-25 07:01:11 | INFO     | AdaptiveRL | Loading industry.csv completed in 0.0157 seconds.
2026-07-25 07:01:11 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-25 07:01:11 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 0.0010 seconds.
2026-07-25 07:01:11 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-25 07:01:11 | INFO     | AdaptiveRL | Removed 0 duplicate rows.
2026-07-25 07:01:11 | INFO     | AdaptiveRL | Removing Duplicates completed in 0.0034 seconds.
2026-07-25 07:01:11 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-25 07:01:11 | INFO     | AdaptiveRL | Removed 0 rows containing missing values.
2026-07-25 07:01:11 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.0016 seconds.
2026-07-25 07:01:11 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-25 07:01:11 | INFO     | AdaptiveRL | Removed 0 constant columns.
2026-07-25 07:01:11 | INFO     | AdaptiveRL | Removing Constant Columns completed in 0.0027 seconds.
2026-07-25 07:01:11 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (43, 1)
2026-07-25 07:01:11 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-25 07:01:11 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.0014 seconds.
2026-07-25 07:01:11 | INFO     | AdaptiveRL | Encoding completed.
2026-07-25 07:01:16 | INFO     | AdaptiveRL | Loading industry.csv started.
2026-07-25 07:01:16 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/industry.csv
2026-07-25 07:01:16 | INFO     | AdaptiveRL | Loaded industry.csv | Shape=(43, 1)
2026-07-25 07:01:16 | INFO     | AdaptiveRL | Loading industry.csv completed in 0.0071 seconds.
2026-07-25 07:01:16 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-25 07:01:16 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 0.0019 seconds.
2026-07-25 07:01:16 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-25 07:01:16 | INFO     | AdaptiveRL | Removed 0 duplicate rows.
2026-07-25 07:01:16 | INFO     | AdaptiveRL | Removing Duplicates completed in 0.0033 seconds.
2026-07-25 07:01:16 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-25 07:01:16 | INFO     | AdaptiveRL | Removed 0 rows containing missing values.
2026-07-25 07:01:16 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.0022 seconds.
2026-07-25 07:01:16 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-25 07:01:16 | INFO     | AdaptiveRL | Removed 0 constant columns.
2026-07-25 07:01:16 | INFO     | AdaptiveRL | Removing Constant Columns completed in 0.0019 seconds.
2026-07-25 07:01:16 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (43, 1)
2026-07-25 07:01:16 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-25 07:01:16 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.0011 seconds.
2026-07-25 07:01:16 | INFO     | AdaptiveRL | Encoding completed.
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Loading industry.csv started.
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/industry.csv
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Loaded industry.csv | Shape=(43, 1)
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Loading industry.csv completed in 0.0167 seconds.
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 0.0010 seconds.
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Removed 0 duplicate rows.
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Removing Duplicates completed in 0.0032 seconds.
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Removed 0 rows containing missing values.
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.0019 seconds.
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Removed 0 constant columns.
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Removing Constant Columns completed in 0.0023 seconds.
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (43, 1)
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.0015 seconds.
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Encoding completed.
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Scaler (standard) fitted on 1 numerical columns.
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Scaling Dataset started.
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Scaling Dataset completed in 0.0029 seconds.
2026-07-25 07:03:12 | INFO     | AdaptiveRL | Scaling completed.
2026-07-25 07:12:59 | INFO     | AdaptiveRL | Loading industry.csv started.
2026-07-25 07:12:59 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/industry.csv
2026-07-25 07:12:59 | INFO     | AdaptiveRL | Loaded industry.csv | Shape=(43, 1)
2026-07-25 07:12:59 | INFO     | AdaptiveRL | Loading industry.csv completed in 0.0186 seconds.
2026-07-25 07:12:59 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-25 07:12:59 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 0.0012 seconds.
2026-07-25 07:12:59 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-25 07:12:59 | INFO     | AdaptiveRL | Removed 0 duplicate rows.
2026-07-25 07:12:59 | INFO     | AdaptiveRL | Removing Duplicates completed in 0.0043 seconds.
2026-07-25 07:12:59 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-25 07:12:59 | INFO     | AdaptiveRL | Removed 0 rows containing missing values.
2026-07-25 07:12:59 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.0022 seconds.
2026-07-25 07:13:00 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-25 07:13:00 | INFO     | AdaptiveRL | Removed 0 constant columns.
2026-07-25 07:13:00 | INFO     | AdaptiveRL | Removing Constant Columns completed in 0.0029 seconds.
2026-07-25 07:13:00 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (43, 1)
2026-07-25 07:13:00 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-25 07:13:00 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.0015 seconds.
2026-07-25 07:13:00 | INFO     | AdaptiveRL | Encoding completed.
2026-07-25 07:13:00 | INFO     | AdaptiveRL | Scaler (standard) fitted on 1 numerical columns.
2026-07-25 07:13:00 | INFO     | AdaptiveRL | Scaling Dataset started.
2026-07-25 07:13:00 | INFO     | AdaptiveRL | Scaling Dataset completed in 0.0023 seconds.
2026-07-25 07:13:00 | INFO     | AdaptiveRL | Scaling completed.
2026-07-25 07:13:05 | INFO     | AdaptiveRL | Dataset Splitting started.
2026-07-25 07:13:05 | INFO     | AdaptiveRL | Dataset Splitting completed in 0.0141 seconds.
2026-07-25 07:13:05 | INFO     | AdaptiveRL | Train=30 | Validation=6 | Test=7
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Loading industry.csv started.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/industry.csv
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Loaded industry.csv | Shape=(43, 1)
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Loading industry.csv completed in 0.0309 seconds.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 0.0007 seconds.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Removed 0 duplicate rows.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Removing Duplicates completed in 0.0118 seconds.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Removed 0 rows containing missing values.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.0017 seconds.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Removed 0 constant columns.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Removing Constant Columns completed in 0.0068 seconds.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (43, 1)
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.0016 seconds.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Encoding completed.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Scaler (standard) fitted on 1 numerical columns.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Scaling Dataset started.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Scaling Dataset completed in 0.0024 seconds.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Scaling completed.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Identified 0 correlated features.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Correlation Analysis started.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Correlation Analysis completed in 0.0010 seconds.
2026-07-26 04:52:38 | INFO     | AdaptiveRL | Remaining features: 1
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Loading industry.csv started.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/industry.csv
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Loaded industry.csv | Shape=(43, 1)
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Loading industry.csv completed in 0.0157 seconds.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 0.0008 seconds.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Removed 0 duplicate rows.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Removing Duplicates completed in 0.0024 seconds.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Removed 0 rows containing missing values.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.0022 seconds.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Removed 0 constant columns.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Removing Constant Columns completed in 0.0029 seconds.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (43, 1)
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.0017 seconds.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Encoding completed.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Scaler (standard) fitted on 1 numerical columns.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Scaling Dataset started.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Scaling Dataset completed in 0.0021 seconds.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Scaling completed.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Identified 0 correlated features.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Correlation Analysis started.
2026-07-26 04:57:41 | INFO     | AdaptiveRL | Correlation Analysis completed in 0.0018 seconds.
2026-07-26 04:57:42 | INFO     | AdaptiveRL | Remaining features: 1
2026-07-26 04:57:49 | INFO     | AdaptiveRL | Statistical Analysis started.
2026-07-26 04:57:49 | INFO     | AdaptiveRL | Statistical Analysis completed in 0.0132 seconds.
2026-07-26 04:57:49 | INFO     | AdaptiveRL | Computed statistics for 1 features.
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Loading industry.csv started.
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/industry.csv
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Loaded industry.csv | Shape=(43, 1)
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Loading industry.csv completed in 0.0192 seconds.
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 0.0014 seconds.
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Removed 0 duplicate rows.
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Removing Duplicates completed in 0.0030 seconds.
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Removed 0 rows containing missing values.
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.0019 seconds.
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Removed 0 constant columns.
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Removing Constant Columns completed in 0.0025 seconds.
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (43, 1)
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.0015 seconds.
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Encoding completed.
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Scaler (standard) fitted on 1 numerical columns.
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Scaling Dataset started.
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Scaling Dataset completed in 0.0019 seconds.
2026-07-26 05:00:31 | INFO     | AdaptiveRL | Scaling completed.
2026-07-26 05:00:36 | INFO     | AdaptiveRL | Feature Selection (variance) started.
2026-07-26 05:00:36 | INFO     | AdaptiveRL | Feature Selection (variance) completed in 0.0085 seconds.
2026-07-26 05:00:36 | INFO     | AdaptiveRL | Selected 1 features.
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Loading industry.csv started.
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/industry.csv
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Loaded industry.csv | Shape=(43, 1)
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Loading industry.csv completed in 0.0207 seconds.
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 0.0014 seconds.
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Removed 0 duplicate rows.
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Removing Duplicates completed in 0.0032 seconds.
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Removed 0 rows containing missing values.
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.0022 seconds.
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Removed 0 constant columns.
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Removing Constant Columns completed in 0.0025 seconds.
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (43, 1)
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.0016 seconds.
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Encoding completed.
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Scaler (standard) fitted on 1 numerical columns.
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Scaling Dataset started.
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Scaling Dataset completed in 0.0023 seconds.
2026-07-26 05:02:45 | INFO     | AdaptiveRL | Scaling completed.
2026-07-26 05:02:52 | INFO     | AdaptiveRL | Training pca started.
2026-07-26 05:02:52 | INFO     | AdaptiveRL | Training pca completed in 0.0122 seconds.
2026-07-26 05:02:52 | INFO     | AdaptiveRL | Reducer fitted.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Loading industry.csv started.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/industry.csv
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Loaded industry.csv | Shape=(43, 1)
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Loading industry.csv completed in 0.0211 seconds.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Feature Pipeline started.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 0.0010 seconds.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Removed 0 duplicate rows.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Removing Duplicates completed in 0.0023 seconds.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Removed 0 rows containing missing values.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.0023 seconds.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Removed 0 constant columns.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Removing Constant Columns completed in 0.0025 seconds.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (43, 1)
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.0016 seconds.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Encoding completed.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Scaler (standard) fitted on 1 numerical columns.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Scaling Dataset started.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Scaling Dataset completed in 0.0029 seconds.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Scaling completed.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Identified 0 correlated features.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Correlation Analysis started.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Correlation Analysis completed in 0.0013 seconds.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Remaining features: 1
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Feature Pipeline completed in 0.0585 seconds.
2026-07-26 05:07:34 | INFO     | AdaptiveRL | Pipeline completed. Final shape: (43, 1)
2026-07-26 08:06:29 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv started.
2026-07-26 08:06:29 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Monday-WorkingHours.pcap_ISCX.csv
2026-07-26 08:06:32 | INFO     | AdaptiveRL | Loaded Monday-WorkingHours.pcap_ISCX.csv | Shape=(529918, 79)
2026-07-26 08:06:32 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv completed in 2.9049 seconds.
2026-07-26 08:06:32 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv started.
2026-07-26 08:06:32 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Tuesday-WorkingHours.pcap_ISCX.csv
2026-07-26 08:06:34 | INFO     | AdaptiveRL | Loaded Tuesday-WorkingHours.pcap_ISCX.csv | Shape=(445909, 79)
2026-07-26 08:06:34 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv completed in 1.9116 seconds.
2026-07-26 08:06:34 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv started.
2026-07-26 08:06:34 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Wednesday-workingHours.pcap_ISCX.csv
2026-07-26 08:06:38 | INFO     | AdaptiveRL | Loaded Wednesday-workingHours.pcap_ISCX.csv | Shape=(692703, 79)
2026-07-26 08:06:38 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv completed in 3.5425 seconds.
2026-07-26 08:06:38 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv started.
2026-07-26 08:06:38 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
2026-07-26 08:06:38 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv | Shape=(170366, 79)
2026-07-26 08:06:38 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv completed in 0.6331 seconds.
2026-07-26 08:06:38 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv started.
2026-07-26 08:06:38 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
2026-07-26 08:06:39 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv | Shape=(288602, 79)
2026-07-26 08:06:39 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv completed in 1.0676 seconds.
2026-07-26 08:06:39 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv started.
2026-07-26 08:06:39 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Morning.pcap_ISCX.csv
2026-07-26 08:06:40 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Morning.pcap_ISCX.csv | Shape=(191033, 79)
2026-07-26 08:06:40 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv completed in 0.8068 seconds.
2026-07-26 08:06:40 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv started.
2026-07-26 08:06:40 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
2026-07-26 08:06:41 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv | Shape=(286467, 79)
2026-07-26 08:06:41 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv completed in 1.1716 seconds.
2026-07-26 08:08:43 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv started.
2026-07-26 08:08:43 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Monday-WorkingHours.pcap_ISCX.csv
2026-07-26 08:08:45 | INFO     | AdaptiveRL | Loaded Monday-WorkingHours.pcap_ISCX.csv | Shape=(529918, 79)
2026-07-26 08:08:45 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv completed in 2.2281 seconds.
2026-07-26 08:08:45 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv started.
2026-07-26 08:08:45 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Tuesday-WorkingHours.pcap_ISCX.csv
2026-07-26 08:08:47 | INFO     | AdaptiveRL | Loaded Tuesday-WorkingHours.pcap_ISCX.csv | Shape=(445909, 79)
2026-07-26 08:08:47 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv completed in 1.7914 seconds.
2026-07-26 08:08:47 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv started.
2026-07-26 08:08:47 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Wednesday-workingHours.pcap_ISCX.csv
2026-07-26 08:08:50 | INFO     | AdaptiveRL | Loaded Wednesday-workingHours.pcap_ISCX.csv | Shape=(692703, 79)
2026-07-26 08:08:50 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv completed in 3.2411 seconds.
2026-07-26 08:08:50 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv started.
2026-07-26 08:08:50 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
2026-07-26 08:08:51 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv | Shape=(170366, 79)
2026-07-26 08:08:51 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv completed in 0.7015 seconds.
2026-07-26 08:08:51 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv started.
2026-07-26 08:08:51 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
2026-07-26 08:08:52 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv | Shape=(288602, 79)
2026-07-26 08:08:52 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv completed in 1.0538 seconds.
2026-07-26 08:08:52 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv started.
2026-07-26 08:08:52 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Morning.pcap_ISCX.csv
2026-07-26 08:08:53 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Morning.pcap_ISCX.csv | Shape=(191033, 79)
2026-07-26 08:08:53 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv completed in 0.7656 seconds.
2026-07-26 08:08:53 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv started.
2026-07-26 08:08:53 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
2026-07-26 08:08:54 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv | Shape=(286467, 79)
2026-07-26 08:08:54 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv completed in 1.1008 seconds.
2026-07-26 08:08:54 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv started.
2026-07-26 08:08:54 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
2026-07-26 08:08:55 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv | Shape=(225745, 79)
2026-07-26 08:08:55 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv completed in 0.9988 seconds.
2026-07-26 08:08:57 | INFO     | AdaptiveRL | Combined dataset shape=(2830743, 79)
2026-07-26 08:10:31 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-26 08:10:44 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 12.8449 seconds.
2026-07-26 08:10:44 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-26 08:10:58 | INFO     | AdaptiveRL | Removed 308381 duplicate rows.
2026-07-26 08:10:58 | INFO     | AdaptiveRL | Removing Duplicates completed in 14.1744 seconds.
2026-07-26 08:10:58 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-26 08:11:00 | INFO     | AdaptiveRL | Removed 1564 rows containing missing values.
2026-07-26 08:11:00 | INFO     | AdaptiveRL | Removing Missing Values completed in 1.8040 seconds.
2026-07-26 08:11:00 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-26 08:11:02 | INFO     | AdaptiveRL | Removed 8 constant columns.
2026-07-26 08:11:02 | INFO     | AdaptiveRL | Removing Constant Columns completed in 2.2389 seconds.
2026-07-26 08:11:02 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (2520798, 71)
2026-07-26 08:13:33 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-26 08:13:33 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.5451 seconds.
2026-07-26 08:13:33 | INFO     | AdaptiveRL | Encoding completed.
2026-07-26 08:13:47 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-26 08:13:47 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.0014 seconds.
2026-07-26 08:13:47 | INFO     | AdaptiveRL | Encoding completed.
2026-07-26 08:13:53 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-26 08:13:53 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.0013 seconds.
2026-07-26 08:13:53 | INFO     | AdaptiveRL | Encoding completed.
2026-07-26 08:16:21 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-26 08:16:22 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.6026 seconds.
2026-07-26 08:16:22 | INFO     | AdaptiveRL | Encoding completed.
2026-07-26 08:17:16 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-26 08:17:16 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.0014 seconds.
2026-07-26 08:17:16 | INFO     | AdaptiveRL | Encoding completed.
2026-07-26 08:18:00 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv started.
2026-07-26 08:18:00 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Monday-WorkingHours.pcap_ISCX.csv
2026-07-26 08:18:02 | INFO     | AdaptiveRL | Loaded Monday-WorkingHours.pcap_ISCX.csv | Shape=(529918, 79)
2026-07-26 08:18:02 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv completed in 2.8325 seconds.
2026-07-26 08:18:02 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv started.
2026-07-26 08:18:02 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Tuesday-WorkingHours.pcap_ISCX.csv
2026-07-26 08:18:04 | INFO     | AdaptiveRL | Loaded Tuesday-WorkingHours.pcap_ISCX.csv | Shape=(445909, 79)
2026-07-26 08:18:04 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv completed in 1.7375 seconds.
2026-07-26 08:18:04 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv started.
2026-07-26 08:18:04 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Wednesday-workingHours.pcap_ISCX.csv
2026-07-26 08:18:08 | INFO     | AdaptiveRL | Loaded Wednesday-workingHours.pcap_ISCX.csv | Shape=(692703, 79)
2026-07-26 08:18:08 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv completed in 3.3639 seconds.
2026-07-26 08:18:08 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv started.
2026-07-26 08:18:08 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
2026-07-26 08:18:08 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv | Shape=(170366, 79)
2026-07-26 08:18:08 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv completed in 0.6693 seconds.
2026-07-26 08:18:08 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv started.
2026-07-26 08:18:08 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
2026-07-26 08:18:09 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv | Shape=(288602, 79)
2026-07-26 08:18:09 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv completed in 1.0178 seconds.
2026-07-26 08:18:09 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv started.
2026-07-26 08:18:09 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Morning.pcap_ISCX.csv
2026-07-26 08:18:10 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Morning.pcap_ISCX.csv | Shape=(191033, 79)
2026-07-26 08:18:10 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv completed in 0.7323 seconds.
2026-07-26 08:18:10 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv started.
2026-07-26 08:18:10 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
2026-07-26 08:18:11 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv | Shape=(286467, 79)
2026-07-26 08:18:11 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv completed in 1.0453 seconds.
2026-07-26 08:18:11 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv started.
2026-07-26 08:18:11 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
2026-07-26 08:18:12 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv | Shape=(225745, 79)
2026-07-26 08:18:12 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv completed in 0.8833 seconds.
2026-07-26 08:18:13 | INFO     | AdaptiveRL | Combined dataset shape=(2830743, 79)
2026-07-26 08:18:16 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-26 08:29:32 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv started.
2026-07-26 08:29:32 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Monday-WorkingHours.pcap_ISCX.csv
2026-07-26 08:29:34 | INFO     | AdaptiveRL | Loaded Monday-WorkingHours.pcap_ISCX.csv | Shape=(529918, 79)
2026-07-26 08:29:34 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv completed in 2.5017 seconds.
2026-07-26 08:29:34 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv started.
2026-07-26 08:29:34 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Tuesday-WorkingHours.pcap_ISCX.csv
2026-07-26 08:29:36 | INFO     | AdaptiveRL | Loaded Tuesday-WorkingHours.pcap_ISCX.csv | Shape=(445909, 79)
2026-07-26 08:29:36 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv completed in 1.9231 seconds.
2026-07-26 08:29:36 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv started.
2026-07-26 08:29:36 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Wednesday-workingHours.pcap_ISCX.csv
2026-07-26 08:29:39 | INFO     | AdaptiveRL | Loaded Wednesday-workingHours.pcap_ISCX.csv | Shape=(692703, 79)
2026-07-26 08:29:39 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv completed in 3.0840 seconds.
2026-07-26 08:29:39 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv started.
2026-07-26 08:29:39 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
2026-07-26 08:29:40 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv | Shape=(170366, 79)
2026-07-26 08:29:40 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv completed in 0.6628 seconds.
2026-07-26 08:29:40 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv started.
2026-07-26 08:29:40 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
2026-07-26 08:29:41 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv | Shape=(288602, 79)
2026-07-26 08:29:41 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv completed in 0.9520 seconds.
2026-07-26 08:29:41 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv started.
2026-07-26 08:29:41 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Morning.pcap_ISCX.csv
2026-07-26 08:29:41 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Morning.pcap_ISCX.csv | Shape=(191033, 79)
2026-07-26 08:29:41 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv completed in 0.7300 seconds.
2026-07-26 08:29:41 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv started.
2026-07-26 08:29:41 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
2026-07-26 08:29:42 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv | Shape=(286467, 79)
2026-07-26 08:29:42 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv completed in 1.0630 seconds.
2026-07-26 08:29:42 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv started.
2026-07-26 08:29:42 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
2026-07-26 08:29:43 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv | Shape=(225745, 79)
2026-07-26 08:29:43 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv completed in 0.9186 seconds.
2026-07-26 08:29:44 | INFO     | AdaptiveRL | Combined dataset shape=(2830743, 79)
2026-07-26 08:30:08 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-26 08:30:10 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 1.9254 seconds.
2026-07-26 08:30:10 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-26 08:30:21 | INFO     | AdaptiveRL | Removed 308381 duplicate rows.
2026-07-26 08:30:21 | INFO     | AdaptiveRL | Removing Duplicates completed in 10.8842 seconds.
2026-07-26 08:30:21 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-26 08:30:22 | INFO     | AdaptiveRL | Removed 1564 rows containing missing values.
2026-07-26 08:30:22 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.6298 seconds.
2026-07-26 08:30:22 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-26 08:30:24 | INFO     | AdaptiveRL | Removed 8 constant columns.
2026-07-26 08:30:24 | INFO     | AdaptiveRL | Removing Constant Columns completed in 1.9043 seconds.
2026-07-26 08:30:24 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (2520798, 71)
2026-07-26 08:30:30 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-26 08:30:30 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.2856 seconds.
2026-07-26 08:30:30 | INFO     | AdaptiveRL | Encoding completed.
2026-07-26 08:35:18 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv started.
2026-07-26 08:35:18 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Monday-WorkingHours.pcap_ISCX.csv
2026-07-26 08:35:21 | INFO     | AdaptiveRL | Loaded Monday-WorkingHours.pcap_ISCX.csv | Shape=(529918, 79)
2026-07-26 08:35:21 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv completed in 2.5222 seconds.
2026-07-26 08:35:21 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv started.
2026-07-26 08:35:21 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Tuesday-WorkingHours.pcap_ISCX.csv
2026-07-26 08:35:23 | INFO     | AdaptiveRL | Loaded Tuesday-WorkingHours.pcap_ISCX.csv | Shape=(445909, 79)
2026-07-26 08:35:23 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv completed in 1.8006 seconds.
2026-07-26 08:35:23 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv started.
2026-07-26 08:35:23 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Wednesday-workingHours.pcap_ISCX.csv
2026-07-26 08:35:26 | INFO     | AdaptiveRL | Loaded Wednesday-workingHours.pcap_ISCX.csv | Shape=(692703, 79)
2026-07-26 08:35:26 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv completed in 3.0248 seconds.
2026-07-26 08:35:26 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv started.
2026-07-26 08:35:26 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
2026-07-26 08:35:26 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv | Shape=(170366, 79)
2026-07-26 08:35:26 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv completed in 0.6242 seconds.
2026-07-26 08:35:26 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv started.
2026-07-26 08:35:26 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
2026-07-26 08:35:27 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv | Shape=(288602, 79)
2026-07-26 08:35:27 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv completed in 1.0225 seconds.
2026-07-26 08:35:27 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv started.
2026-07-26 08:35:27 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Morning.pcap_ISCX.csv
2026-07-26 08:35:28 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Morning.pcap_ISCX.csv | Shape=(191033, 79)
2026-07-26 08:35:28 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv completed in 0.8124 seconds.
2026-07-26 08:35:28 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv started.
2026-07-26 08:35:28 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
2026-07-26 08:35:29 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv | Shape=(286467, 79)
2026-07-26 08:35:29 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv completed in 1.0673 seconds.
2026-07-26 08:35:29 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv started.
2026-07-26 08:35:29 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
2026-07-26 08:35:30 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv | Shape=(225745, 79)
2026-07-26 08:35:30 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv completed in 0.9013 seconds.
2026-07-26 08:35:31 | INFO     | AdaptiveRL | Combined dataset shape=(2830743, 79)
2026-07-26 08:35:33 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-26 08:35:36 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 2.3530 seconds.
2026-07-26 08:35:36 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-26 08:35:46 | INFO     | AdaptiveRL | Removed 308381 duplicate rows.
2026-07-26 08:35:46 | INFO     | AdaptiveRL | Removing Duplicates completed in 10.2971 seconds.
2026-07-26 08:35:46 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-26 08:35:47 | INFO     | AdaptiveRL | Removed 1564 rows containing missing values.
2026-07-26 08:35:47 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.7237 seconds.
2026-07-26 08:35:47 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-26 08:35:49 | INFO     | AdaptiveRL | Removed 8 constant columns.
2026-07-26 08:35:49 | INFO     | AdaptiveRL | Removing Constant Columns completed in 1.9413 seconds.
2026-07-26 08:35:49 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (2520798, 71)
2026-07-26 08:35:54 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-26 08:35:55 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.2962 seconds.
2026-07-26 08:35:55 | INFO     | AdaptiveRL | Encoding completed.
2026-07-26 08:35:58 | INFO     | AdaptiveRL | Scaler (standard) fitted on 70 feature columns.
2026-07-26 08:35:59 | INFO     | AdaptiveRL | Scaling Dataset started.
2026-07-26 08:36:01 | INFO     | AdaptiveRL | Scaling Dataset completed in 1.9535 seconds.
2026-07-26 08:36:01 | INFO     | AdaptiveRL | Scaling completed.
2026-07-26 08:38:12 | INFO     | src.models.isolation_forest | Training Isolation Forest...
2026-07-26 08:38:12 | INFO     | src.models.isolation_forest | Training samples: 2520798
2026-07-26 08:38:27 | INFO     | src.models.isolation_forest | Isolation Forest training completed.
2026-07-26 14:58:31 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv started.
2026-07-26 14:58:31 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Monday-WorkingHours.pcap_ISCX.csv
2026-07-26 14:58:35 | INFO     | AdaptiveRL | Loaded Monday-WorkingHours.pcap_ISCX.csv | Shape=(529918, 79)
2026-07-26 14:58:35 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv completed in 3.6821 seconds.
2026-07-26 14:58:35 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv started.
2026-07-26 14:58:35 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Tuesday-WorkingHours.pcap_ISCX.csv
2026-07-26 14:58:37 | INFO     | AdaptiveRL | Loaded Tuesday-WorkingHours.pcap_ISCX.csv | Shape=(445909, 79)
2026-07-26 14:58:37 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv completed in 2.6596 seconds.
2026-07-26 14:58:37 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv started.
2026-07-26 14:58:37 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Wednesday-workingHours.pcap_ISCX.csv
2026-07-26 14:58:42 | INFO     | AdaptiveRL | Loaded Wednesday-workingHours.pcap_ISCX.csv | Shape=(692703, 79)
2026-07-26 14:58:42 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv completed in 4.3800 seconds.
2026-07-26 14:58:42 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv started.
2026-07-26 14:58:42 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
2026-07-26 14:58:43 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv | Shape=(170366, 79)
2026-07-26 14:58:43 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv completed in 0.9789 seconds.
2026-07-26 14:58:43 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv started.
2026-07-26 14:58:43 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
2026-07-26 14:58:44 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv | Shape=(288602, 79)
2026-07-26 14:58:44 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv completed in 1.3314 seconds.
2026-07-26 14:58:44 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv started.
2026-07-26 14:58:44 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Morning.pcap_ISCX.csv
2026-07-26 14:58:45 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Morning.pcap_ISCX.csv | Shape=(191033, 79)
2026-07-26 14:58:45 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv completed in 0.9643 seconds.
2026-07-26 14:58:45 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv started.
2026-07-26 14:58:45 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
2026-07-26 14:58:46 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv | Shape=(286467, 79)
2026-07-26 14:58:46 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv completed in 1.4268 seconds.
2026-07-26 14:58:46 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv started.
2026-07-26 14:58:46 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
2026-07-26 14:58:48 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv | Shape=(225745, 79)
2026-07-26 14:58:48 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv completed in 1.2481 seconds.
2026-07-26 14:58:49 | INFO     | AdaptiveRL | Combined dataset shape=(2830743, 79)
2026-07-26 14:59:00 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-26 14:59:06 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 6.5219 seconds.
2026-07-26 14:59:06 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-26 14:59:27 | INFO     | AdaptiveRL | Removed 308381 duplicate rows.
2026-07-26 14:59:27 | INFO     | AdaptiveRL | Removing Duplicates completed in 20.2942 seconds.
2026-07-26 14:59:27 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-26 14:59:28 | INFO     | AdaptiveRL | Removed 1564 rows containing missing values.
2026-07-26 14:59:28 | INFO     | AdaptiveRL | Removing Missing Values completed in 1.1011 seconds.
2026-07-26 14:59:28 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-26 14:59:31 | INFO     | AdaptiveRL | Removed 8 constant columns.
2026-07-26 14:59:31 | INFO     | AdaptiveRL | Removing Constant Columns completed in 3.2111 seconds.
2026-07-26 14:59:31 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (2520798, 71)
2026-07-26 14:59:38 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-26 14:59:38 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.4554 seconds.
2026-07-26 14:59:38 | INFO     | AdaptiveRL | Encoding completed.
2026-07-26 14:59:47 | INFO     | AdaptiveRL | Scaler (standard) fitted on 70 feature columns.
2026-07-26 14:59:49 | INFO     | AdaptiveRL | Scaling Dataset started.
2026-07-26 14:59:52 | INFO     | AdaptiveRL | Scaling Dataset completed in 3.5069 seconds.
2026-07-26 14:59:52 | INFO     | AdaptiveRL | Scaling completed.
2026-07-26 15:00:34 | INFO     | src.models.isolation_forest | Training Isolation Forest...
2026-07-26 15:00:34 | INFO     | src.models.isolation_forest | Training samples: 2520798
2026-07-26 15:00:54 | INFO     | src.models.isolation_forest | Isolation Forest training completed.
2026-07-26 15:05:50 | INFO     | src.models.isolation_forest | Isolation Forest saved -> trained_models/isolation_forest.joblib
2026-07-26 15:06:02 | INFO     | src.models.isolation_forest | Isolation Forest loaded <- trained_models/isolation_forest.joblib
2026-07-26 15:11:48 | INFO     | src.models.isolation_forest | Isolation Forest loaded <- trained_models/isolation_forest.joblib
2026-07-26 15:20:00 | INFO     | src.models.isolation_forest | Isolation Forest loaded <- trained_models/isolation_forest.joblib
2026-07-26 15:24:24 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv started.
2026-07-26 15:24:24 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Monday-WorkingHours.pcap_ISCX.csv
2026-07-26 15:24:27 | INFO     | AdaptiveRL | Loaded Monday-WorkingHours.pcap_ISCX.csv | Shape=(529918, 79)
2026-07-26 15:24:27 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv completed in 3.5911 seconds.
2026-07-26 15:24:27 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv started.
2026-07-26 15:24:27 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Tuesday-WorkingHours.pcap_ISCX.csv
2026-07-26 15:24:30 | INFO     | AdaptiveRL | Loaded Tuesday-WorkingHours.pcap_ISCX.csv | Shape=(445909, 79)
2026-07-26 15:24:30 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv completed in 2.3910 seconds.
2026-07-26 15:24:30 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv started.
2026-07-26 15:24:30 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Wednesday-workingHours.pcap_ISCX.csv
2026-07-26 15:24:34 | INFO     | AdaptiveRL | Loaded Wednesday-workingHours.pcap_ISCX.csv | Shape=(692703, 79)
2026-07-26 15:24:34 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv completed in 3.9080 seconds.
2026-07-26 15:24:34 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv started.
2026-07-26 15:24:34 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
2026-07-26 15:24:35 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv | Shape=(170366, 79)
2026-07-26 15:24:35 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv completed in 0.8910 seconds.
2026-07-26 15:24:35 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv started.
2026-07-26 15:24:35 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
2026-07-26 15:24:36 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv | Shape=(288602, 79)
2026-07-26 15:24:36 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv completed in 1.2973 seconds.
2026-07-26 15:24:36 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv started.
2026-07-26 15:24:36 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Morning.pcap_ISCX.csv
2026-07-26 15:24:37 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Morning.pcap_ISCX.csv | Shape=(191033, 79)
2026-07-26 15:24:37 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv completed in 0.9575 seconds.
2026-07-26 15:24:37 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv started.
2026-07-26 15:24:37 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
2026-07-26 15:24:38 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv | Shape=(286467, 79)
2026-07-26 15:24:38 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv completed in 1.3493 seconds.
2026-07-26 15:24:38 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv started.
2026-07-26 15:24:38 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
2026-07-26 15:24:39 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv | Shape=(225745, 79)
2026-07-26 15:24:39 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv completed in 1.2031 seconds.
2026-07-26 15:24:41 | INFO     | AdaptiveRL | Combined dataset shape=(2830743, 79)
2026-07-26 15:24:43 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-26 15:24:46 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 3.0499 seconds.
2026-07-26 15:24:46 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-26 15:24:58 | INFO     | AdaptiveRL | Removed 308381 duplicate rows.
2026-07-26 15:24:58 | INFO     | AdaptiveRL | Removing Duplicates completed in 12.2129 seconds.
2026-07-26 15:24:58 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-26 15:24:59 | INFO     | AdaptiveRL | Removed 1564 rows containing missing values.
2026-07-26 15:24:59 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.7390 seconds.
2026-07-26 15:24:59 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-26 15:25:02 | INFO     | AdaptiveRL | Removed 8 constant columns.
2026-07-26 15:25:02 | INFO     | AdaptiveRL | Removing Constant Columns completed in 2.3344 seconds.
2026-07-26 15:25:02 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (2520798, 71)
2026-07-26 15:25:22 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-26 15:25:22 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.3994 seconds.
2026-07-26 15:25:22 | INFO     | AdaptiveRL | Encoding completed.
2026-07-26 15:25:34 | INFO     | AdaptiveRL | Scaler (standard) fitted on 70 feature columns.
2026-07-26 15:25:35 | INFO     | AdaptiveRL | Scaling Dataset started.
2026-07-26 15:25:37 | INFO     | AdaptiveRL | Scaling Dataset completed in 2.0903 seconds.
2026-07-26 15:25:37 | INFO     | AdaptiveRL | Scaling completed.
2026-07-26 15:25:46 | INFO     | src.models.isolation_forest | Training Isolation Forest...
2026-07-26 15:25:46 | INFO     | src.models.isolation_forest | Training samples: 2520798
2026-07-26 15:26:07 | INFO     | src.models.isolation_forest | Isolation Forest training completed.
2026-07-26 15:27:09 | INFO     | src.models.isolation_forest | Isolation Forest loaded <- trained_models/isolation_forest.joblib
2026-07-26 15:27:13 | INFO     | src.models.isolation_forest | Isolation Forest loaded <- trained_models/isolation_forest.joblib
2026-07-28 14:20:09 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv started.
2026-07-28 14:20:09 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Monday-WorkingHours.pcap_ISCX.csv
2026-07-28 14:20:12 | INFO     | AdaptiveRL | Loaded Monday-WorkingHours.pcap_ISCX.csv | Shape=(529918, 79)
2026-07-28 14:20:12 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv completed in 2.7824 seconds.
2026-07-28 14:20:12 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv started.
2026-07-28 14:20:12 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Tuesday-WorkingHours.pcap_ISCX.csv
2026-07-28 14:20:14 | INFO     | AdaptiveRL | Loaded Tuesday-WorkingHours.pcap_ISCX.csv | Shape=(445909, 79)
2026-07-28 14:20:14 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv completed in 2.1300 seconds.
2026-07-28 14:20:14 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv started.
2026-07-28 14:20:14 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Wednesday-workingHours.pcap_ISCX.csv
2026-07-28 14:20:17 | INFO     | AdaptiveRL | Loaded Wednesday-workingHours.pcap_ISCX.csv | Shape=(692703, 79)
2026-07-28 14:20:17 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv completed in 3.3604 seconds.
2026-07-28 14:20:17 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv started.
2026-07-28 14:20:17 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
2026-07-28 14:20:18 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv | Shape=(170366, 79)
2026-07-28 14:20:18 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv completed in 0.6871 seconds.
2026-07-28 14:20:18 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv started.
2026-07-28 14:20:18 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
2026-07-28 14:20:19 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv | Shape=(288602, 79)
2026-07-28 14:20:19 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv completed in 1.0482 seconds.
2026-07-28 14:20:19 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv started.
2026-07-28 14:20:19 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Morning.pcap_ISCX.csv
2026-07-28 14:20:20 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Morning.pcap_ISCX.csv | Shape=(191033, 79)
2026-07-28 14:20:20 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv completed in 0.8197 seconds.
2026-07-28 14:20:20 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv started.
2026-07-28 14:20:20 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
2026-07-28 14:20:21 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv | Shape=(286467, 79)
2026-07-28 14:20:21 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv completed in 1.2202 seconds.
2026-07-28 14:20:21 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv started.
2026-07-28 14:20:21 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
2026-07-28 14:20:22 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv | Shape=(225745, 79)
2026-07-28 14:20:22 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv completed in 0.9902 seconds.
2026-07-28 14:20:23 | INFO     | AdaptiveRL | Combined dataset shape=(2830743, 79)
2026-07-28 14:22:03 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-28 14:22:06 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 2.4769 seconds.
2026-07-28 14:22:06 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-28 14:22:17 | INFO     | AdaptiveRL | Removed 308381 duplicate rows.
2026-07-28 14:22:17 | INFO     | AdaptiveRL | Removing Duplicates completed in 11.4410 seconds.
2026-07-28 14:22:17 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-28 14:22:18 | INFO     | AdaptiveRL | Removed 1564 rows containing missing values.
2026-07-28 14:22:18 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.8409 seconds.
2026-07-28 14:22:18 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-28 14:22:20 | INFO     | AdaptiveRL | Removed 8 constant columns.
2026-07-28 14:22:20 | INFO     | AdaptiveRL | Removing Constant Columns completed in 1.9268 seconds.
2026-07-28 14:22:20 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (2520798, 71)
2026-07-28 14:22:39 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-28 14:22:40 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.3430 seconds.
2026-07-28 14:22:40 | INFO     | AdaptiveRL | Encoding completed.
2026-07-28 14:22:54 | INFO     | AdaptiveRL | Scaler (standard) fitted on 70 feature columns.
2026-07-28 14:22:56 | INFO     | AdaptiveRL | Scaling Dataset started.
2026-07-28 14:22:58 | INFO     | AdaptiveRL | Scaling Dataset completed in 2.4052 seconds.
2026-07-28 14:22:58 | INFO     | AdaptiveRL | Scaling completed.
2026-07-28 14:24:48 | INFO     | src.models.local_outlier_factor | Local Outlier Factor initialized.
2026-07-28 14:24:55 | INFO     | src.models.local_outlier_factor | Training Local Outlier Factor...
2026-07-28 14:34:29 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv started.
2026-07-28 14:34:29 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Monday-WorkingHours.pcap_ISCX.csv
2026-07-28 14:34:32 | INFO     | AdaptiveRL | Loaded Monday-WorkingHours.pcap_ISCX.csv | Shape=(529918, 79)
2026-07-28 14:34:32 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv completed in 2.5927 seconds.
2026-07-28 14:34:32 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv started.
2026-07-28 14:34:32 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Tuesday-WorkingHours.pcap_ISCX.csv
2026-07-28 14:34:34 | INFO     | AdaptiveRL | Loaded Tuesday-WorkingHours.pcap_ISCX.csv | Shape=(445909, 79)
2026-07-28 14:34:34 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv completed in 1.9624 seconds.
2026-07-28 14:34:34 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv started.
2026-07-28 14:34:34 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Wednesday-workingHours.pcap_ISCX.csv
2026-07-28 14:34:37 | INFO     | AdaptiveRL | Loaded Wednesday-workingHours.pcap_ISCX.csv | Shape=(692703, 79)
2026-07-28 14:34:37 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv completed in 3.1047 seconds.
2026-07-28 14:34:37 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv started.
2026-07-28 14:34:37 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
2026-07-28 14:34:38 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv | Shape=(170366, 79)
2026-07-28 14:34:38 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv completed in 0.6936 seconds.
2026-07-28 14:34:38 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv started.
2026-07-28 14:34:38 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
2026-07-28 14:34:39 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv | Shape=(288602, 79)
2026-07-28 14:34:39 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv completed in 1.0514 seconds.
2026-07-28 14:34:39 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv started.
2026-07-28 14:34:39 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Morning.pcap_ISCX.csv
2026-07-28 14:34:39 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Morning.pcap_ISCX.csv | Shape=(191033, 79)
2026-07-28 14:34:39 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv completed in 0.7483 seconds.
2026-07-28 14:34:39 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv started.
2026-07-28 14:34:39 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
2026-07-28 14:34:41 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv | Shape=(286467, 79)
2026-07-28 14:34:41 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv completed in 1.0859 seconds.
2026-07-28 14:34:41 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv started.
2026-07-28 14:34:41 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
2026-07-28 14:34:41 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv | Shape=(225745, 79)
2026-07-28 14:34:41 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv completed in 0.9264 seconds.
2026-07-28 14:34:43 | INFO     | AdaptiveRL | Combined dataset shape=(2830743, 79)
2026-07-28 14:35:03 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-28 14:35:06 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 2.7989 seconds.
2026-07-28 14:35:06 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-28 14:35:17 | INFO     | AdaptiveRL | Removed 308381 duplicate rows.
2026-07-28 14:35:17 | INFO     | AdaptiveRL | Removing Duplicates completed in 11.2685 seconds.
2026-07-28 14:35:17 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-28 14:35:18 | INFO     | AdaptiveRL | Removed 1564 rows containing missing values.
2026-07-28 14:35:18 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.7978 seconds.
2026-07-28 14:35:18 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-28 14:35:20 | INFO     | AdaptiveRL | Removed 8 constant columns.
2026-07-28 14:35:20 | INFO     | AdaptiveRL | Removing Constant Columns completed in 1.8999 seconds.
2026-07-28 14:35:20 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (2520798, 71)
2026-07-28 14:35:32 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-28 14:35:32 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.3005 seconds.
2026-07-28 14:35:32 | INFO     | AdaptiveRL | Encoding completed.
2026-07-28 14:35:36 | INFO     | AdaptiveRL | Scaler (standard) fitted on 70 feature columns.
2026-07-28 14:35:37 | INFO     | AdaptiveRL | Scaling Dataset started.
2026-07-28 14:35:40 | INFO     | AdaptiveRL | Scaling Dataset completed in 2.6242 seconds.
2026-07-28 14:35:40 | INFO     | AdaptiveRL | Scaling completed.
2026-07-28 14:39:24 | INFO     | src.models.local_outlier_factor | Local Outlier Factor initialized.
2026-07-28 14:39:28 | INFO     | src.models.local_outlier_factor | Training Local Outlier Factor...
2026-07-28 14:39:34 | INFO     | src.models.local_outlier_factor | Training completed.
2026-07-28 14:40:39 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv started.
2026-07-28 14:40:39 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Monday-WorkingHours.pcap_ISCX.csv
2026-07-28 14:40:42 | INFO     | AdaptiveRL | Loaded Monday-WorkingHours.pcap_ISCX.csv | Shape=(529918, 79)
2026-07-28 14:40:42 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv completed in 2.5842 seconds.
2026-07-28 14:40:42 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv started.
2026-07-28 14:40:42 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Tuesday-WorkingHours.pcap_ISCX.csv
2026-07-28 14:40:44 | INFO     | AdaptiveRL | Loaded Tuesday-WorkingHours.pcap_ISCX.csv | Shape=(445909, 79)
2026-07-28 14:40:44 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv completed in 1.9046 seconds.
2026-07-28 14:40:44 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv started.
2026-07-28 14:40:44 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Wednesday-workingHours.pcap_ISCX.csv
2026-07-28 14:40:47 | INFO     | AdaptiveRL | Loaded Wednesday-workingHours.pcap_ISCX.csv | Shape=(692703, 79)
2026-07-28 14:40:47 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv completed in 3.0064 seconds.
2026-07-28 14:40:47 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv started.
2026-07-28 14:40:47 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
2026-07-28 14:40:48 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv | Shape=(170366, 79)
2026-07-28 14:40:48 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv completed in 0.6292 seconds.
2026-07-28 14:40:48 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv started.
2026-07-28 14:40:48 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
2026-07-28 14:40:49 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv | Shape=(288602, 79)
2026-07-28 14:40:49 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv completed in 0.9654 seconds.
2026-07-28 14:40:49 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv started.
2026-07-28 14:40:49 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Morning.pcap_ISCX.csv
2026-07-28 14:40:49 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Morning.pcap_ISCX.csv | Shape=(191033, 79)
2026-07-28 14:40:49 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv completed in 0.7215 seconds.
2026-07-28 14:40:49 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv started.
2026-07-28 14:40:49 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
2026-07-28 14:40:50 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv | Shape=(286467, 79)
2026-07-28 14:40:50 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv completed in 1.0480 seconds.
2026-07-28 14:40:50 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv started.
2026-07-28 14:40:50 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
2026-07-28 14:40:51 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv | Shape=(225745, 79)
2026-07-28 14:40:51 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv completed in 0.9246 seconds.
2026-07-28 14:40:53 | INFO     | AdaptiveRL | Combined dataset shape=(2830743, 79)
2026-07-28 14:40:59 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-28 14:41:01 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 2.3127 seconds.
2026-07-28 14:41:01 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-28 14:41:11 | INFO     | AdaptiveRL | Removed 308381 duplicate rows.
2026-07-28 14:41:11 | INFO     | AdaptiveRL | Removing Duplicates completed in 11.0631 seconds.
2026-07-28 14:41:11 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-28 14:41:12 | INFO     | AdaptiveRL | Removed 1564 rows containing missing values.
2026-07-28 14:41:12 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.6530 seconds.
2026-07-28 14:41:12 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-28 14:41:14 | INFO     | AdaptiveRL | Removed 8 constant columns.
2026-07-28 14:41:14 | INFO     | AdaptiveRL | Removing Constant Columns completed in 1.9016 seconds.
2026-07-28 14:41:14 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (2520798, 71)
2026-07-28 14:42:23 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-28 14:42:24 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.3137 seconds.
2026-07-28 14:42:24 | INFO     | AdaptiveRL | Encoding completed.
2026-07-28 14:42:28 | INFO     | AdaptiveRL | Scaler (standard) fitted on 70 feature columns.
2026-07-28 14:42:29 | INFO     | AdaptiveRL | Scaling Dataset started.
2026-07-28 14:42:31 | INFO     | AdaptiveRL | Scaling Dataset completed in 2.7145 seconds.
2026-07-28 14:42:31 | INFO     | AdaptiveRL | Scaling completed.
2026-07-28 14:42:35 | INFO     | src.models.local_outlier_factor | Local Outlier Factor initialized.
2026-07-28 14:44:22 | INFO     | src.models.local_outlier_factor | Local Outlier Factor initialized.
2026-07-28 14:44:25 | WARNING  | src.models.local_outlier_factor | Sampling 500000 rows for Local Outlier Factor training.
2026-07-28 14:44:25 | INFO     | src.models.local_outlier_factor | Training Local Outlier Factor...
2026-07-28 14:46:01 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv started.
2026-07-28 14:46:01 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Monday-WorkingHours.pcap_ISCX.csv
2026-07-28 14:46:03 | INFO     | AdaptiveRL | Loaded Monday-WorkingHours.pcap_ISCX.csv | Shape=(529918, 79)
2026-07-28 14:46:03 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv completed in 2.5824 seconds.
2026-07-28 14:46:03 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv started.
2026-07-28 14:46:03 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Tuesday-WorkingHours.pcap_ISCX.csv
2026-07-28 14:46:05 | INFO     | AdaptiveRL | Loaded Tuesday-WorkingHours.pcap_ISCX.csv | Shape=(445909, 79)
2026-07-28 14:46:05 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv completed in 2.0153 seconds.
2026-07-28 14:46:05 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv started.
2026-07-28 14:46:05 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Wednesday-workingHours.pcap_ISCX.csv
2026-07-28 14:46:09 | INFO     | AdaptiveRL | Loaded Wednesday-workingHours.pcap_ISCX.csv | Shape=(692703, 79)
2026-07-28 14:46:09 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv completed in 3.1328 seconds.
2026-07-28 14:46:09 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv started.
2026-07-28 14:46:09 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
2026-07-28 14:46:09 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv | Shape=(170366, 79)
2026-07-28 14:46:09 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv completed in 0.6249 seconds.
2026-07-28 14:46:09 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv started.
2026-07-28 14:46:09 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
2026-07-28 14:46:10 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv | Shape=(288602, 79)
2026-07-28 14:46:10 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv completed in 0.9500 seconds.
2026-07-28 14:46:10 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv started.
2026-07-28 14:46:10 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Morning.pcap_ISCX.csv
2026-07-28 14:46:11 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Morning.pcap_ISCX.csv | Shape=(191033, 79)
2026-07-28 14:46:11 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv completed in 0.6727 seconds.
2026-07-28 14:46:11 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv started.
2026-07-28 14:46:11 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
2026-07-28 14:46:12 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv | Shape=(286467, 79)
2026-07-28 14:46:12 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv completed in 1.0349 seconds.
2026-07-28 14:46:12 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv started.
2026-07-28 14:46:12 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
2026-07-28 14:46:13 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv | Shape=(225745, 79)
2026-07-28 14:46:13 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv completed in 0.8902 seconds.
2026-07-28 14:46:14 | INFO     | AdaptiveRL | Combined dataset shape=(2830743, 79)
2026-07-28 14:46:25 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-28 14:46:27 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 2.4501 seconds.
2026-07-28 14:46:27 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-28 14:46:39 | INFO     | AdaptiveRL | Removed 308381 duplicate rows.
2026-07-28 14:46:39 | INFO     | AdaptiveRL | Removing Duplicates completed in 12.1548 seconds.
2026-07-28 14:46:39 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-28 14:46:40 | INFO     | AdaptiveRL | Removed 1564 rows containing missing values.
2026-07-28 14:46:40 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.7436 seconds.
2026-07-28 14:46:40 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-28 14:46:42 | INFO     | AdaptiveRL | Removed 8 constant columns.
2026-07-28 14:46:42 | INFO     | AdaptiveRL | Removing Constant Columns completed in 1.9274 seconds.
2026-07-28 14:46:42 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (2520798, 71)
2026-07-28 14:46:48 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-28 14:46:48 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.3200 seconds.
2026-07-28 14:46:48 | INFO     | AdaptiveRL | Encoding completed.
2026-07-28 14:46:53 | INFO     | AdaptiveRL | Scaler (standard) fitted on 70 feature columns.
2026-07-28 14:46:54 | INFO     | AdaptiveRL | Scaling Dataset started.
2026-07-28 14:46:56 | INFO     | AdaptiveRL | Scaling Dataset completed in 2.7548 seconds.
2026-07-28 14:46:56 | INFO     | AdaptiveRL | Scaling completed.
2026-07-28 14:47:03 | INFO     | src.models.local_outlier_factor | Local Outlier Factor initialized.
2026-07-28 14:47:05 | WARNING  | src.models.local_outlier_factor | Sampling 100000 rows for Local Outlier Factor training.
2026-07-28 14:47:05 | INFO     | src.models.local_outlier_factor | Training Local Outlier Factor...
2026-07-28 14:47:12 | INFO     | src.models.local_outlier_factor | Training completed.
2026-07-28 14:50:49 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv started.
2026-07-28 14:50:49 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Monday-WorkingHours.pcap_ISCX.csv
2026-07-28 14:50:51 | INFO     | AdaptiveRL | Loaded Monday-WorkingHours.pcap_ISCX.csv | Shape=(529918, 79)
2026-07-28 14:50:51 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv completed in 2.6996 seconds.
2026-07-28 14:50:51 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv started.
2026-07-28 14:50:51 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Tuesday-WorkingHours.pcap_ISCX.csv
2026-07-28 14:50:54 | INFO     | AdaptiveRL | Loaded Tuesday-WorkingHours.pcap_ISCX.csv | Shape=(445909, 79)
2026-07-28 14:50:54 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv completed in 2.1857 seconds.
2026-07-28 14:50:54 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv started.
2026-07-28 14:50:54 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Wednesday-workingHours.pcap_ISCX.csv
2026-07-28 14:50:57 | INFO     | AdaptiveRL | Loaded Wednesday-workingHours.pcap_ISCX.csv | Shape=(692703, 79)
2026-07-28 14:50:57 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv completed in 3.3760 seconds.
2026-07-28 14:50:57 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv started.
2026-07-28 14:50:57 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
2026-07-28 14:50:58 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv | Shape=(170366, 79)
2026-07-28 14:50:58 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv completed in 0.7408 seconds.
2026-07-28 14:50:58 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv started.
2026-07-28 14:50:58 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
2026-07-28 14:50:59 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv | Shape=(288602, 79)
2026-07-28 14:50:59 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv completed in 1.1303 seconds.
2026-07-28 14:50:59 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv started.
2026-07-28 14:50:59 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Morning.pcap_ISCX.csv
2026-07-28 14:51:00 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Morning.pcap_ISCX.csv | Shape=(191033, 79)
2026-07-28 14:51:00 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv completed in 0.7947 seconds.
2026-07-28 14:51:00 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv started.
2026-07-28 14:51:00 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
2026-07-28 14:51:01 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv | Shape=(286467, 79)
2026-07-28 14:51:01 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv completed in 1.2044 seconds.
2026-07-28 14:51:01 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv started.
2026-07-28 14:51:01 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
2026-07-28 14:51:02 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv | Shape=(225745, 79)
2026-07-28 14:51:02 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv completed in 1.0761 seconds.
2026-07-28 14:51:03 | INFO     | AdaptiveRL | Combined dataset shape=(2830743, 79)
2026-07-28 14:51:04 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-28 14:51:07 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 2.2667 seconds.
2026-07-28 14:51:07 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-28 14:51:18 | INFO     | AdaptiveRL | Removed 308381 duplicate rows.
2026-07-28 14:51:18 | INFO     | AdaptiveRL | Removing Duplicates completed in 12.0986 seconds.
2026-07-28 14:51:18 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-28 14:51:19 | INFO     | AdaptiveRL | Removed 1564 rows containing missing values.
2026-07-28 14:51:19 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.8831 seconds.
2026-07-28 14:51:19 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-28 14:51:21 | INFO     | AdaptiveRL | Removed 8 constant columns.
2026-07-28 14:51:21 | INFO     | AdaptiveRL | Removing Constant Columns completed in 2.0089 seconds.
2026-07-28 14:51:21 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (2520798, 71)
2026-07-28 14:51:25 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-28 14:51:26 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.2843 seconds.
2026-07-28 14:51:26 | INFO     | AdaptiveRL | Encoding completed.
2026-07-28 14:51:30 | INFO     | AdaptiveRL | Scaler (standard) fitted on 70 feature columns.
2026-07-28 14:51:31 | INFO     | AdaptiveRL | Scaling Dataset started.
2026-07-28 14:51:34 | INFO     | AdaptiveRL | Scaling Dataset completed in 3.2063 seconds.
2026-07-28 14:51:34 | INFO     | AdaptiveRL | Scaling completed.
2026-07-28 14:51:39 | INFO     | src.models.local_outlier_factor | Local Outlier Factor initialized.
2026-07-28 14:51:43 | WARNING  | src.models.local_outlier_factor | Sampling 100000 rows for Local Outlier Factor training.
2026-07-28 14:51:43 | INFO     | src.models.local_outlier_factor | Training Local Outlier Factor...
2026-07-28 14:51:50 | INFO     | src.models.local_outlier_factor | Training completed.
2026-07-28 14:58:16 | INFO     | src.models.local_outlier_factor | Local Outlier Factor saved -> trained_models/isolation_forest.joblib
2026-07-28 14:58:56 | INFO     | src.models.local_outlier_factor | Local Outlier Factor saved -> trained_models/local_outlier_factor.joblib
2026-07-28 15:00:57 | INFO     | src.models.local_outlier_factor | Local Outlier Factor loaded <- trained_models/local_outlier_factor.joblib
2026-07-28 15:02:38 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv started.
2026-07-28 15:02:38 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Monday-WorkingHours.pcap_ISCX.csv
2026-07-28 15:02:41 | INFO     | AdaptiveRL | Loaded Monday-WorkingHours.pcap_ISCX.csv | Shape=(529918, 79)
2026-07-28 15:02:41 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv completed in 2.6618 seconds.
2026-07-28 15:02:41 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv started.
2026-07-28 15:02:41 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Tuesday-WorkingHours.pcap_ISCX.csv
2026-07-28 15:05:54 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv started.
2026-07-28 15:05:54 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Monday-WorkingHours.pcap_ISCX.csv
2026-07-28 15:05:56 | INFO     | AdaptiveRL | Loaded Monday-WorkingHours.pcap_ISCX.csv | Shape=(529918, 79)
2026-07-28 15:05:56 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv completed in 2.5829 seconds.
2026-07-28 15:05:56 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv started.
2026-07-28 15:05:56 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Tuesday-WorkingHours.pcap_ISCX.csv
2026-07-28 15:05:58 | INFO     | AdaptiveRL | Loaded Tuesday-WorkingHours.pcap_ISCX.csv | Shape=(445909, 79)
2026-07-28 15:05:58 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv completed in 1.9650 seconds.
2026-07-28 15:05:58 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv started.
2026-07-28 15:05:58 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Wednesday-workingHours.pcap_ISCX.csv
2026-07-28 15:06:01 | INFO     | AdaptiveRL | Loaded Wednesday-workingHours.pcap_ISCX.csv | Shape=(692703, 79)
2026-07-28 15:06:01 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv completed in 3.0257 seconds.
2026-07-28 15:06:01 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv started.
2026-07-28 15:06:01 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
2026-07-28 15:06:01 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv | Shape=(170366, 79)
2026-07-28 15:06:01 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv completed in 0.6529 seconds.
2026-07-28 15:06:01 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv started.
2026-07-28 15:06:01 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
2026-07-28 15:06:02 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv | Shape=(288602, 79)
2026-07-28 15:06:02 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv completed in 1.0050 seconds.
2026-07-28 15:06:02 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv started.
2026-07-28 15:06:02 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Morning.pcap_ISCX.csv
2026-07-28 15:06:03 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Morning.pcap_ISCX.csv | Shape=(191033, 79)
2026-07-28 15:06:03 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv completed in 0.7439 seconds.
2026-07-28 15:06:03 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv started.
2026-07-28 15:06:03 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
2026-07-28 15:06:04 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv | Shape=(286467, 79)
2026-07-28 15:06:04 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv completed in 1.1629 seconds.
2026-07-28 15:06:04 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv started.
2026-07-28 15:06:04 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
2026-07-28 15:06:05 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv | Shape=(225745, 79)
2026-07-28 15:06:05 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv completed in 0.9957 seconds.
2026-07-28 15:06:06 | INFO     | AdaptiveRL | Combined dataset shape=(2830743, 79)
2026-07-28 15:06:10 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-28 15:06:12 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 2.4423 seconds.
2026-07-28 15:06:12 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-28 15:06:23 | INFO     | AdaptiveRL | Removed 308381 duplicate rows.
2026-07-28 15:06:23 | INFO     | AdaptiveRL | Removing Duplicates completed in 10.9877 seconds.
2026-07-28 15:06:23 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-28 15:06:24 | INFO     | AdaptiveRL | Removed 1564 rows containing missing values.
2026-07-28 15:06:24 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.9148 seconds.
2026-07-28 15:06:24 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-28 15:06:26 | INFO     | AdaptiveRL | Removed 8 constant columns.
2026-07-28 15:06:26 | INFO     | AdaptiveRL | Removing Constant Columns completed in 2.0341 seconds.
2026-07-28 15:06:26 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (2520798, 71)
2026-07-28 15:06:30 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-28 15:06:31 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.2864 seconds.
2026-07-28 15:06:31 | INFO     | AdaptiveRL | Encoding completed.
2026-07-28 15:06:36 | INFO     | AdaptiveRL | Scaler (standard) fitted on 70 feature columns.
2026-07-28 15:06:37 | INFO     | AdaptiveRL | Scaling Dataset started.
2026-07-28 15:06:39 | INFO     | AdaptiveRL | Scaling Dataset completed in 2.4900 seconds.
2026-07-28 15:06:39 | INFO     | AdaptiveRL | Scaling completed.
2026-07-28 15:06:48 | INFO     | src.models.isolation_forest | Training Isolation Forest...
2026-07-28 15:06:48 | INFO     | src.models.isolation_forest | Training samples: 2520798
2026-07-28 15:07:02 | INFO     | src.models.isolation_forest | Isolation Forest training completed.
2026-07-28 15:07:46 | INFO     | src.models.isolation_forest | Isolation Forest saved -> trained_models/isolation_forest.joblib
2026-07-28 15:07:49 | INFO     | src.models.isolation_forest | Isolation Forest loaded <- trained_models/isolation_forest.joblib
2026-07-28 15:08:00 | INFO     | src.models.isolation_forest | Isolation Forest loaded <- trained_models/isolation_forest.joblib
2026-07-28 15:08:22 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv started.
2026-07-28 15:08:22 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Monday-WorkingHours.pcap_ISCX.csv
2026-07-28 15:08:24 | INFO     | AdaptiveRL | Loaded Monday-WorkingHours.pcap_ISCX.csv | Shape=(529918, 79)
2026-07-28 15:08:24 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv completed in 2.7628 seconds.
2026-07-28 15:08:24 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv started.
2026-07-28 15:08:24 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Tuesday-WorkingHours.pcap_ISCX.csv
2026-07-28 15:08:27 | INFO     | AdaptiveRL | Loaded Tuesday-WorkingHours.pcap_ISCX.csv | Shape=(445909, 79)
2026-07-28 15:08:27 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv completed in 2.1574 seconds.
2026-07-28 15:08:27 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv started.
2026-07-28 15:08:27 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Wednesday-workingHours.pcap_ISCX.csv
2026-07-28 15:08:30 | INFO     | AdaptiveRL | Loaded Wednesday-workingHours.pcap_ISCX.csv | Shape=(692703, 79)
2026-07-28 15:08:30 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv completed in 3.5467 seconds.
2026-07-28 15:08:30 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv started.
2026-07-28 15:08:30 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
2026-07-28 15:08:31 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv | Shape=(170366, 79)
2026-07-28 15:08:31 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv completed in 0.7138 seconds.
2026-07-28 15:08:31 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv started.
2026-07-28 15:08:31 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
2026-07-28 15:08:32 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv | Shape=(288602, 79)
2026-07-28 15:08:32 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv completed in 1.0878 seconds.
2026-07-28 15:08:32 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv started.
2026-07-28 15:08:32 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Morning.pcap_ISCX.csv
2026-07-28 15:08:33 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Morning.pcap_ISCX.csv | Shape=(191033, 79)
2026-07-28 15:08:33 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv completed in 0.7915 seconds.
2026-07-28 15:08:33 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv started.
2026-07-28 15:08:33 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
2026-07-28 15:08:34 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv | Shape=(286467, 79)
2026-07-28 15:08:34 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv completed in 1.1446 seconds.
2026-07-28 15:08:34 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv started.
2026-07-28 15:08:34 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
2026-07-28 15:08:35 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv | Shape=(225745, 79)
2026-07-28 15:08:35 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv completed in 1.0851 seconds.
2026-07-28 15:08:38 | INFO     | AdaptiveRL | Combined dataset shape=(2830743, 79)
2026-07-28 15:08:39 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-28 15:24:04 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv started.
2026-07-28 15:24:04 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Monday-WorkingHours.pcap_ISCX.csv
2026-07-28 15:24:05 | INFO     | AdaptiveRL | Loaded Monday-WorkingHours.pcap_ISCX.csv | Shape=(529918, 79)
2026-07-28 15:24:05 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv completed in 1.7582 seconds.
2026-07-28 15:24:05 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv started.
2026-07-28 15:24:05 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Tuesday-WorkingHours.pcap_ISCX.csv
2026-07-28 15:24:07 | INFO     | AdaptiveRL | Loaded Tuesday-WorkingHours.pcap_ISCX.csv | Shape=(445909, 79)
2026-07-28 15:24:07 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv completed in 1.3242 seconds.
2026-07-28 15:24:07 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv started.
2026-07-28 15:24:07 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Wednesday-workingHours.pcap_ISCX.csv
2026-07-28 15:24:09 | INFO     | AdaptiveRL | Loaded Wednesday-workingHours.pcap_ISCX.csv | Shape=(692703, 79)
2026-07-28 15:24:09 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv completed in 2.0359 seconds.
2026-07-28 15:24:09 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv started.
2026-07-28 15:24:09 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
2026-07-28 15:24:09 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv | Shape=(170366, 79)
2026-07-28 15:24:09 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv completed in 0.4208 seconds.
2026-07-28 15:24:09 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv started.
2026-07-28 15:24:09 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
2026-07-28 15:24:10 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv | Shape=(288602, 79)
2026-07-28 15:24:10 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv completed in 0.6356 seconds.
2026-07-28 15:24:10 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv started.
2026-07-28 15:24:10 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Morning.pcap_ISCX.csv
2026-07-28 15:24:10 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Morning.pcap_ISCX.csv | Shape=(191033, 79)
2026-07-28 15:24:10 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv completed in 0.4582 seconds.
2026-07-28 15:24:10 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv started.
2026-07-28 15:24:10 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
2026-07-28 15:24:11 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv | Shape=(286467, 79)
2026-07-28 15:24:11 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv completed in 0.7137 seconds.
2026-07-28 15:24:11 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv started.
2026-07-28 15:24:11 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
2026-07-28 15:24:12 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv | Shape=(225745, 79)
2026-07-28 15:24:12 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv completed in 0.6261 seconds.
2026-07-28 15:24:12 | INFO     | AdaptiveRL | Combined dataset shape=(2830743, 79)
2026-07-28 15:24:14 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-28 15:24:15 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 1.4670 seconds.
2026-07-28 15:24:15 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-28 15:24:23 | INFO     | AdaptiveRL | Removed 308381 duplicate rows.
2026-07-28 15:24:23 | INFO     | AdaptiveRL | Removing Duplicates completed in 7.6189 seconds.
2026-07-28 15:24:23 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-28 15:24:24 | INFO     | AdaptiveRL | Removed 1564 rows containing missing values.
2026-07-28 15:24:24 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.6241 seconds.
2026-07-28 15:24:24 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-28 15:24:25 | INFO     | AdaptiveRL | Removed 8 constant columns.
2026-07-28 15:24:25 | INFO     | AdaptiveRL | Removing Constant Columns completed in 1.3028 seconds.
2026-07-28 15:24:25 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (2520798, 71)
2026-07-28 15:24:29 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-28 15:24:29 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.2110 seconds.
2026-07-28 15:24:29 | INFO     | AdaptiveRL | Encoding completed.
2026-07-28 15:24:33 | INFO     | AdaptiveRL | Scaler (standard) fitted on 70 feature columns.
2026-07-28 15:24:34 | INFO     | AdaptiveRL | Scaling Dataset started.
2026-07-28 15:24:33 | INFO     | AdaptiveRL | Scaling Dataset completed in 1.4222 seconds.
2026-07-28 15:24:33 | INFO     | AdaptiveRL | Scaling completed.
2026-07-28 15:24:43 | INFO     | src.models.local_outlier_factor | Local Outlier Factor initialized.
2026-07-28 15:24:45 | WARNING  | src.models.local_outlier_factor | Sampling 100000 rows for Local Outlier Factor training.
2026-07-28 15:24:46 | INFO     | src.models.local_outlier_factor | Training Local Outlier Factor...
2026-07-28 15:24:51 | INFO     | src.models.local_outlier_factor | Training completed.
2026-07-28 15:25:07 | INFO     | src.models.local_outlier_factor | Local Outlier Factor saved -> trained_models/local_outlier_factor.joblib
2026-07-28 15:25:58 | INFO     | src.models.local_outlier_factor | Local Outlier Factor loaded <- trained_models/local_outlier_factor.joblib
2026-07-28 15:27:12 | INFO     | src.models.local_outlier_factor | Local Outlier Factor loaded <- trained_models/local_outlier_factor.joblib
2026-07-28 15:28:08 | INFO     | src.models.local_outlier_factor | Local Outlier Factor loaded <- trained_models/local_outlier_factor.joblib
2026-07-30 15:02:00 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv started.
2026-07-30 15:02:00 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Monday-WorkingHours.pcap_ISCX.csv
2026-07-30 15:02:03 | INFO     | AdaptiveRL | Loaded Monday-WorkingHours.pcap_ISCX.csv | Shape=(529918, 79)
2026-07-30 15:02:03 | INFO     | AdaptiveRL | Loading Monday-WorkingHours.pcap_ISCX.csv completed in 2.8785 seconds.
2026-07-30 15:02:03 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv started.
2026-07-30 15:02:03 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Tuesday-WorkingHours.pcap_ISCX.csv
2026-07-30 15:02:05 | INFO     | AdaptiveRL | Loaded Tuesday-WorkingHours.pcap_ISCX.csv | Shape=(445909, 79)
2026-07-30 15:02:05 | INFO     | AdaptiveRL | Loading Tuesday-WorkingHours.pcap_ISCX.csv completed in 2.1867 seconds.
2026-07-30 15:02:05 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv started.
2026-07-30 15:02:05 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Wednesday-workingHours.pcap_ISCX.csv
2026-07-30 15:02:08 | INFO     | AdaptiveRL | Loaded Wednesday-workingHours.pcap_ISCX.csv | Shape=(692703, 79)
2026-07-30 15:02:08 | INFO     | AdaptiveRL | Loading Wednesday-workingHours.pcap_ISCX.csv completed in 3.3030 seconds.
2026-07-30 15:02:08 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv started.
2026-07-30 15:02:08 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
2026-07-30 15:02:09 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv | Shape=(170366, 79)
2026-07-30 15:02:09 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv completed in 0.7179 seconds.
2026-07-30 15:02:09 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv started.
2026-07-30 15:02:09 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv
2026-07-30 15:02:10 | INFO     | AdaptiveRL | Loaded Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv | Shape=(288602, 79)
2026-07-30 15:02:10 | INFO     | AdaptiveRL | Loading Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv completed in 1.1234 seconds.
2026-07-30 15:02:10 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv started.
2026-07-30 15:02:10 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Morning.pcap_ISCX.csv
2026-07-30 15:02:11 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Morning.pcap_ISCX.csv | Shape=(191033, 79)
2026-07-30 15:02:11 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Morning.pcap_ISCX.csv completed in 0.7886 seconds.
2026-07-30 15:02:11 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv started.
2026-07-30 15:02:11 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
2026-07-30 15:02:12 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv | Shape=(286467, 79)
2026-07-30 15:02:12 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv completed in 1.1931 seconds.
2026-07-30 15:02:12 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv started.
2026-07-30 15:02:12 | INFO     | AdaptiveRL | Reading /home/kalpe/projects/adaptive_rl_anomaly_detection/datasets/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
2026-07-30 15:02:13 | INFO     | AdaptiveRL | Loaded Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv | Shape=(225745, 79)
2026-07-30 15:02:13 | INFO     | AdaptiveRL | Loading Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv completed in 0.9750 seconds.
2026-07-30 15:02:14 | INFO     | AdaptiveRL | Combined dataset shape=(2830743, 79)
2026-07-30 15:02:23 | INFO     | AdaptiveRL | Replacing Infinite Values started.
2026-07-30 15:02:25 | INFO     | AdaptiveRL | Replacing Infinite Values completed in 2.6037 seconds.
2026-07-30 15:02:25 | INFO     | AdaptiveRL | Removing Duplicates started.
2026-07-30 15:02:36 | INFO     | AdaptiveRL | Removed 308381 duplicate rows.
2026-07-30 15:02:36 | INFO     | AdaptiveRL | Removing Duplicates completed in 11.5469 seconds.
2026-07-30 15:02:36 | INFO     | AdaptiveRL | Removing Missing Values started.
2026-07-30 15:02:37 | INFO     | AdaptiveRL | Removed 1564 rows containing missing values.
2026-07-30 15:02:37 | INFO     | AdaptiveRL | Removing Missing Values completed in 0.7037 seconds.
2026-07-30 15:02:37 | INFO     | AdaptiveRL | Removing Constant Columns started.
2026-07-30 15:02:39 | INFO     | AdaptiveRL | Removed 8 constant columns.
2026-07-30 15:02:39 | INFO     | AdaptiveRL | Removing Constant Columns completed in 2.1373 seconds.
2026-07-30 15:02:39 | INFO     | AdaptiveRL | Cleaning completed. Final shape: (2520798, 71)
2026-07-30 15:03:01 | INFO     | AdaptiveRL | Encoding Dataset started.
2026-07-30 15:03:01 | INFO     | AdaptiveRL | Encoding Dataset completed in 0.3521 seconds.
2026-07-30 15:03:01 | INFO     | AdaptiveRL | Encoding completed.
2026-07-30 15:03:09 | INFO     | AdaptiveRL | Scaler (standard) fitted on 70 feature columns.
2026-07-30 15:03:10 | INFO     | AdaptiveRL | Scaling Dataset started.
2026-07-30 15:03:13 | INFO     | AdaptiveRL | Scaling Dataset completed in 2.7388 seconds.
2026-07-30 15:03:13 | INFO     | AdaptiveRL | Scaling completed.
2026-07-30 15:06:01 | INFO     | src.models.one_class_svm | One-Class SVM initialized.
2026-07-30 15:06:31 | WARNING  | src.models.one_class_svm | Dataset contains 2520798 samples. Sampling 50000 rows for One-Class SVM training.
2026-07-30 15:06:31 | INFO     | src.models.one_class_svm | Training One-Class SVM...
2026-07-30 15:06:52 | INFO     | src.models.one_class_svm | Training samples: 50000 | Features: 70
2026-07-30 15:06:52 | INFO     | src.models.one_class_svm | One-Class SVM training completed successfully.
2026-07-30 15:14:09 | INFO     | src.models.one_class_svm | One-Class SVM saved -> trained_models/one_class_svm.joblib
2026-07-30 15:14:16 | INFO     | src.models.one_class_svm | One-Class SVM loaded <- trained_models/one_class_svm.joblib

```

---

### <a id="📄-notebooks-logs-framework-log"></a>📄 `notebooks/logs/framework.log`

**File Info:**
- **Size**: 447 B
- **Extension**: `.log`
- **Language**: `text`
- **Location**: `notebooks/logs/framework.log`
- **Relative Path**: `notebooks/logs`
- **Created**: 2026-07-25 06:32:45 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 06:32:45 (Asia/Calcutta / GMT+06:30)
- **MD5**: `d86ac859fd47159d08c7d9dae938a9c6`
- **SHA256**: `654dcbab3e439e8e7704ea80a3e2056a361290f49edac112280b5598ccea0c90`
- **Encoding**: ASCII

**File code content:**

```text
2026-07-25 06:15:47 | INFO     | AdaptiveRL | Logger initialized successfully.
2026-07-25 06:15:47 | WARNING  | AdaptiveRL | This is a warning.
2026-07-25 06:15:47 | ERROR    | AdaptiveRL | This is an error message.
2026-07-25 06:32:38 | INFO     | AdaptiveRL | Sleep Test started.
2026-07-25 06:32:40 | INFO     | AdaptiveRL | Sleep Test completed in 2.0080 seconds.
2026-07-25 06:32:45 | INFO     | AdaptiveRL | demo executed in 1.0002 seconds.

```

---

## 🚫 Binary/Excluded Files

The following files were not included in the text content:

- `notebooks/trained_models/isolation_forest.joblib`
- `notebooks/trained_models/local_outlier_factor.joblib`
- `notebooks/trained_models/one_class_svm.joblib`

## 🚫 Binary/Excluded Files

The following files were not included in the text content:

- `notebooks/01_test_config.ipynb`
- `notebooks/02_test_seed.ipynb`
- `notebooks/03_test_logger.ipynb`
- `notebooks/04_test_timer.ipynb.ipynb`
- `notebooks/05_test_loader.ipynb`
- `notebooks/06_test_cleaner.ipynb`
- `notebooks/07_test_encoder.ipynb`
- `notebooks/08_test_scaler.ipynb`
- `notebooks/09_test_splitter.ipynb`
- `notebooks/10_test_correlation.ipynb`
- `notebooks/11_test_statistics.ipynb`
- `notebooks/12_test_selector.ipynb`
- `notebooks/13_test_dimensionality_reduction.ipynb`
- `notebooks/14_test_feature_pipeline.ipynb`
- `notebooks/15_base_model.ipynb`
- `notebooks/16_Isolation_Forest.ipynb`
- `notebooks/17_local_outlier_factor.ipynb.ipynb`
- `notebooks/18_one_class_svm.ipynb`

## 🚫 Binary/Excluded Files

The following files were not included in the text content:

- `src/__pycache__/__init__.cpython-312.pyc`

## 🚫 Binary/Excluded Files

The following files were not included in the text content:

- `src/config/__pycache__/__init__.cpython-312.pyc`
- `src/config/__pycache__/config.cpython-312.pyc`
- `src/config/__pycache__/isolation_forest_config.cpython-312.pyc`
- `src/config/__pycache__/local_outlier_factor_config.cpython-312.pyc`
- `src/config/__pycache__/one_class_svm_config.cpython-312.pyc`

### <a id="📄-src-config-init-py"></a>📄 `src/config/__init__.py`

**File Info:**
- **Size**: 202 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/config/__init__.py`
- **Relative Path**: `src/config`
- **Created**: 2026-07-26 15:34:14 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-26 15:34:14 (Asia/Calcutta / GMT+06:30)
- **MD5**: `636710b76bc7d32fd8d0b2ee8cf289a9`
- **SHA256**: `cfb629e570d9ba79a26264d941c74f94717e839a3e374361d3f57f03f0408aac`
- **Encoding**: ASCII

**File code content:**

```python
from .isolation_forest_config import IsolationForestConfig
from .local_outlier_factor_config import LocalOutlierFactorConfig

__all__ = [
    "IsolationForestConfig",
    "LocalOutlierFactorConfig",
]


```

---

### <a id="📄-src-config-config-py"></a>📄 `src/config/config.py`

**File Info:**
- **Size**: 4.25 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/config/config.py`
- **Relative Path**: `src/config`
- **Created**: 2026-07-25 06:49:18 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 06:49:18 (Asia/Calcutta / GMT+06:30)
- **MD5**: `6254c1fbcb3b808cb1c9fd9310359101`
- **SHA256**: `aac4f50505a674865a35639a3c9986be08b56c9553a30a7591d5add6b4627052`
- **Encoding**: ASCII

**File code content:**

```python
"""
Central configuration module for the Adaptive Reinforcement Learning
Ensemble-based Network Anomaly Detection framework.

This module defines all framework-wide configuration values in a
centralized, strongly typed, and immutable manner.

Author:
    Kalpesh Patil

Python:
    3.12
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import torch


# =============================================================================
# PATH CONFIGURATION
# =============================================================================


@dataclass(frozen=True)
class PathConfig:
    """
    Defines all filesystem paths used throughout the framework.
    """

    project_root: Path = Path(__file__).resolve().parents[2]

    dataset_dir: Path = field(init=False)
    raw_data_dir: Path = field(init=False)
    processed_data_dir: Path = field(init=False)
    external_data_dir: Path = field(init=False)

    checkpoint_dir: Path = field(init=False)
    log_dir: Path = field(init=False)
    output_dir: Path = field(init=False)

    def __post_init__(self) -> None:
        object.__setattr__(self, "dataset_dir", self.project_root / "datasets")
        object.__setattr__(self, "raw_data_dir", self.dataset_dir / "raw")
        object.__setattr__(self, "processed_data_dir", self.dataset_dir / "processed")
        object.__setattr__(self, "external_data_dir", self.dataset_dir / "external")

        object.__setattr__(self, "checkpoint_dir", self.project_root / "checkpoints")
        object.__setattr__(self, "log_dir", self.project_root / "logs")
        object.__setattr__(self, "output_dir", self.project_root / "outputs")


# =============================================================================
# DATASET CONFIGURATION
# =============================================================================


@dataclass(frozen=True)
class DatasetConfig:
    """
    Dataset-related configuration.
    """

    dataset_name: str = "CICIDS2017"

    file_extension: str = ".csv"

    target_column: str = "Label"

    shuffle: bool = True


# =============================================================================
# TRAINING CONFIGURATION
# =============================================================================


@dataclass(frozen=True)
class TrainingConfig:
    """
    Hyperparameters used across the framework.
    """

    random_seed: int = 42

    test_size: float = 0.20

    validation_size: float = 0.10

    batch_size: int = 128

    num_workers: int = 4

    learning_rate: float = 1e-3

    epochs: int = 100

    device: str = (
        "cuda"
        if torch.cuda.is_available()
        else "cpu"
    )


# =============================================================================
# LOGGING CONFIGURATION
# =============================================================================


@dataclass(frozen=True)
class LoggingConfig:
    """
    Logging-related settings.
    """

    logger_name: str = "AdaptiveRL"

    log_level: str = "INFO"

    log_filename: str = "framework.log"

    console_logging: bool = True

    file_logging: bool = True


# =============================================================================
# EVALUATION CONFIGURATION
# =============================================================================


@dataclass(frozen=True)
class EvaluationConfig:
    """
    Metrics used throughout experiments.
    """

    metrics: tuple[str, ...] = (
        "accuracy",
        "precision",
        "recall",
        "f1",
        "roc_auc",
        "confusion_matrix",
    )


# =============================================================================
# ROOT CONFIGURATION
# =============================================================================


@dataclass(frozen=True)
class FrameworkConfig:
    """
    Root configuration object.

    Every module should import this object instead of creating its own
    configuration values.
    """

    paths: PathConfig = field(default_factory=PathConfig)

    dataset: DatasetConfig = field(default_factory=DatasetConfig)

    training: TrainingConfig = field(default_factory=TrainingConfig)

    logging: LoggingConfig = field(default_factory=LoggingConfig)

    evaluation: EvaluationConfig = field(default_factory=EvaluationConfig)


config = FrameworkConfig()
```

---

### <a id="📄-src-config-isolation-forest-config-py"></a>📄 `src/config/isolation_forest_config.py`

**File Info:**
- **Size**: 495 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/config/isolation_forest_config.py`
- **Relative Path**: `src/config`
- **Created**: 2026-07-26 08:01:19 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-26 08:01:19 (Asia/Calcutta / GMT+06:30)
- **MD5**: `3fe80d470683dc1fb5e519fe0c57b4f2`
- **SHA256**: `632f573f65b894911d66422eca2c07af1c454864774ed4821d3e8a873d2d6a69`
- **Encoding**: ASCII

**File code content:**

```python
"""
Configuration for Isolation Forest.
"""

from dataclasses import dataclass
from typing import Literal


@dataclass(slots=True)
class IsolationForestConfig:
    """
    Configuration parameters for Isolation Forest.
    """

    n_estimators: int = 200

    contamination: float | Literal["auto"] = 0.05

    max_samples: int | float | Literal["auto"] = "auto"

    max_features: float = 1.0

    bootstrap: bool = False

    random_state: int = 42

    n_jobs: int = -1

    verbose: int = 0
```

---

### <a id="📄-src-config-local-outlier-factor-config-py"></a>📄 `src/config/local_outlier_factor_config.py`

**File Info:**
- **Size**: 1.33 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/config/local_outlier_factor_config.py`
- **Relative Path**: `src/config`
- **Created**: 2026-07-30 15:43:00 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-30 15:43:00 (Asia/Calcutta / GMT+06:30)
- **MD5**: `33bfc87d5a7c5d79a87657166b00b1b5`
- **SHA256**: `57f2bfb8c5a77233224910e370b52234ea4f0f8286704455641720e8545eb23f`
- **Encoding**: ASCII

**File code content:**

```python
"""
Configuration for the Local Outlier Factor anomaly detection model.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


@dataclass(slots=True)
class LocalOutlierFactorConfig:
    """
    Configuration for sklearn.neighbors.LocalOutlierFactor.

    Parameters
    ----------
    n_neighbors : int
        Number of neighbors used to compute the local density.

    algorithm : {"auto", "ball_tree", "kd_tree", "brute"}
        Neighbor search algorithm.

    leaf_size : int
        Leaf size passed to BallTree or KDTree.

    metric : str
        Distance metric.

    p : int
        Power parameter for the Minkowski metric.

    contamination : float | {"auto"}
        Expected proportion of anomalies.

    novelty : bool
        Enables prediction on unseen data.
        Must remain True for deployment and inference.

    n_jobs : int
        Number of CPU cores used.
        -1 means use all available cores.
    """

    n_neighbors: int = 20

    algorithm: Literal[
        "auto",
        "ball_tree",
        "kd_tree",
        "brute",
    ] = "auto"

    leaf_size: int = 30

    metric: str = "minkowski"

    p: int = 2

    contamination: float | Literal["auto"] = 0.05

    novelty: bool = True


    random_state: int = 42

    n_jobs: int = -1

    max_training_samples: int = 100000


```

---

### <a id="📄-src-config-one-class-svm-config-py"></a>📄 `src/config/one_class_svm_config.py`

**File Info:**
- **Size**: 528 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/config/one_class_svm_config.py`
- **Relative Path**: `src/config`
- **Created**: 2026-07-30 15:36:44 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-30 15:36:44 (Asia/Calcutta / GMT+06:30)
- **MD5**: `d598f56b72c653bcaa236df9e82ca987`
- **SHA256**: `b241fc4ea57b7f837d2e9d5e3758726abed678b993f879ddbacb2910ab56b73d`
- **Encoding**: ASCII

**File code content:**

```python
"""
Configuration for the One-Class SVM anomaly detection model.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class OneClassSVMConfig:
    """
    Configuration for One-Class SVM.
    """

    kernel: str = "rbf"

    degree: int = 3

    gamma: str | float = "scale"

    coef0: float = 0.0

    tol: float = 1e-3

    nu: float = 0.05

    shrinking: bool = True

    cache_size: int = 200

    verbose: bool = False

    max_iter: int = -1

    random_state: int = 42

    max_training_samples: int = 50000
```

---

### <a id="📄-src-ensemble-init-py"></a>📄 `src/ensemble/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/ensemble/__init__.py`
- **Relative Path**: `src/ensemble`
- **Created**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-src-evaluation-init-py"></a>📄 `src/evaluation/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/evaluation/__init__.py`
- **Relative Path**: `src/evaluation`
- **Created**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

## 🚫 Binary/Excluded Files

The following files were not included in the text content:

- `src/feature_engineering/__pycache__/__init__.cpython-312.pyc`
- `src/feature_engineering/__pycache__/correlation_analysis.cpython-312.pyc`
- `src/feature_engineering/__pycache__/dimensionality_reduction.cpython-312.pyc`
- `src/feature_engineering/__pycache__/feature_pipeline.cpython-312.pyc`
- `src/feature_engineering/__pycache__/feature_selector.cpython-312.pyc`
- `src/feature_engineering/__pycache__/statistical_features.cpython-312.pyc`

### <a id="📄-src-feature-engineering-init-py"></a>📄 `src/feature_engineering/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/feature_engineering/__init__.py`
- **Relative Path**: `src/feature_engineering`
- **Created**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-src-feature-engineering-correlation-analysis-py"></a>📄 `src/feature_engineering/correlation_analysis.py`

**File Info:**
- **Size**: 1.75 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/feature_engineering/correlation_analysis.py`
- **Relative Path**: `src/feature_engineering`
- **Created**: 2026-07-26 04:51:06 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-26 04:51:06 (Asia/Calcutta / GMT+06:30)
- **MD5**: `f9022d5b78edde6a9ee5ead8434ee1f4`
- **SHA256**: `0bf769348231a64dca26b3facf1ca4a76a1363dd047c9d1e16cbafff149a78ba`
- **Encoding**: ASCII

**File code content:**

```python
"""
Correlation analysis utilities.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from src.utils.logger import get_logger
from src.utils.timer import Timer

logger = get_logger()


class CorrelationAnalyzer:
    """
    Remove highly correlated numerical features.
    """

    def __init__(self, threshold: float = 0.95) -> None:
        self.threshold = threshold
        self.removed_features: list[str] = []

    def fit(self, dataframe: pd.DataFrame) -> None:
        """
        Identify highly correlated columns.
        """

        numeric_df = dataframe.select_dtypes(include="number")

        correlation_matrix = numeric_df.corr().abs()

        upper_triangle = correlation_matrix.where(
            np.triu(
                np.ones(correlation_matrix.shape),
                k=1,
            ).astype(bool)
        )

        self.removed_features = [
            column
            for column in upper_triangle.columns
            if any(upper_triangle[column] > self.threshold)
        ]

        logger.info(
            f"Identified {len(self.removed_features)} correlated features."
        )

    def transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Remove correlated columns.
        """

        dataframe = dataframe.copy()

        with Timer("Correlation Analysis"):

            dataframe = dataframe.drop(
                columns=self.removed_features,
                errors="ignore",
            )

        logger.info(
            f"Remaining features: {dataframe.shape[1]}"
        )

        return dataframe

    def fit_transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        self.fit(dataframe)

        return self.transform(dataframe)
```

---

### <a id="📄-src-feature-engineering-dimensionality-reduction-py"></a>📄 `src/feature_engineering/dimensionality_reduction.py`

**File Info:**
- **Size**: 1.86 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/feature_engineering/dimensionality_reduction.py`
- **Relative Path**: `src/feature_engineering`
- **Created**: 2026-07-26 05:02:24 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-26 05:02:24 (Asia/Calcutta / GMT+06:30)
- **MD5**: `260ab359b05274ed2bf3b0d8e571cd42`
- **SHA256**: `bfa73e246b0dba1762a70cf7f03070f69fff7fdd79334abd11e4d189f82f9aaa`
- **Encoding**: ASCII

**File code content:**

```python
"""
Dimensionality reduction utilities.
"""

from __future__ import annotations

import pandas as pd

from sklearn.decomposition import PCA
from sklearn.decomposition import IncrementalPCA

from src.utils.logger import get_logger
from src.utils.timer import Timer

logger = get_logger()


class DimensionalityReducer:
    """
    Generic dimensionality reduction interface.
    """

    SUPPORTED_METHODS = (
        "pca",
        "incremental_pca",
    )

    def __init__(
        self,
        method: str = "pca",
        n_components: float | int = 0.95,
        batch_size: int = 512,
    ) -> None:

        if method not in self.SUPPORTED_METHODS:
            raise ValueError(
                f"Unsupported method '{method}'."
            )

        self.method = method

        if method == "pca":

            self.reducer = PCA(
                n_components=n_components
            )

        else:

            self.reducer = IncrementalPCA(
                n_components=n_components,
                batch_size=batch_size,
            )

    def fit(
        self,
        dataframe: pd.DataFrame,
    ) -> None:

        with Timer(f"Training {self.method}"):

            self.reducer.fit(dataframe)

        logger.info("Reducer fitted.")

    def transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        transformed = self.reducer.transform(dataframe)

        columns = [
            f"PC{i+1}"
            for i in range(transformed.shape[1])
        ]

        return pd.DataFrame(
            transformed,
            columns=columns,
            index=dataframe.index,
        )

    def fit_transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        self.fit(dataframe)

        return self.transform(dataframe)

    @property
    def explained_variance(self):

        return self.reducer.explained_variance_ratio_
```

---

### <a id="📄-src-feature-engineering-feature-pipeline-py"></a>📄 `src/feature_engineering/feature_pipeline.py`

**File Info:**
- **Size**: 2.28 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/feature_engineering/feature_pipeline.py`
- **Relative Path**: `src/feature_engineering`
- **Created**: 2026-07-26 05:07:18 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-26 05:07:18 (Asia/Calcutta / GMT+06:30)
- **MD5**: `668b077cb3611ee87a3a0aa2d574b493`
- **SHA256**: `0dbb7ae97a7c49d1e1e4584f9274c15b87456b10d2c16c284f8e9089ee58cf59`
- **Encoding**: ASCII

**File code content:**

```python
"""
End-to-end feature engineering pipeline.
"""

from __future__ import annotations

from typing import Optional

import pandas as pd

from src.preprocessing.cleaner import DataCleaner
from src.preprocessing.encoder import DataEncoder
from src.preprocessing.scaler import DataScaler

from src.feature_engineering.correlation_analysis import (
    CorrelationAnalyzer,
)
from src.feature_engineering.feature_selector import (
    FeatureSelector,
)
from src.feature_engineering.dimensionality_reduction import (
    DimensionalityReducer,
)

from src.utils.logger import get_logger
from src.utils.timer import Timer

logger = get_logger()


class FeaturePipeline:
    """
    Complete preprocessing + feature engineering pipeline.
    """

    def __init__(
        self,
        cleaner: Optional[DataCleaner] = None,
        encoder: Optional[DataEncoder] = None,
        scaler: Optional[DataScaler] = None,
        correlation: Optional[CorrelationAnalyzer] = None,
        selector: Optional[FeatureSelector] = None,
        reducer: Optional[DimensionalityReducer] = None,
    ) -> None:

        self.cleaner = cleaner or DataCleaner()
        self.encoder = encoder or DataEncoder()
        self.scaler = scaler or DataScaler()

        self.correlation = correlation
        self.selector = selector
        self.reducer = reducer

    def fit_transform(
        self,
        dataframe: pd.DataFrame,
        target=None,
    ) -> pd.DataFrame:
        """
        Execute the complete pipeline.
        """

        with Timer("Feature Pipeline"):

            dataframe = self.cleaner.clean(dataframe)

            dataframe = self.encoder.fit_transform(dataframe)

            dataframe = self.scaler.fit_transform(dataframe)

            if self.correlation is not None:
                dataframe = self.correlation.fit_transform(
                    dataframe
                )

            if self.selector is not None:
                dataframe = self.selector.fit_transform(
                    dataframe,
                    target,
                )

            if self.reducer is not None:
                dataframe = self.reducer.fit_transform(
                    dataframe
                )

        logger.info(
            f"Pipeline completed. Final shape: {dataframe.shape}"
        )

        return dataframe
```

---

### <a id="📄-src-feature-engineering-feature-selector-py"></a>📄 `src/feature_engineering/feature_selector.py`

**File Info:**
- **Size**: 4.83 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/feature_engineering/feature_selector.py`
- **Relative Path**: `src/feature_engineering`
- **Created**: 2026-07-26 05:01:42 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-26 05:01:42 (Asia/Calcutta / GMT+06:30)
- **MD5**: `dfaaa4c193203c547c41a9c8fb4a5ff4`
- **SHA256**: `806a2793e83c8aac512eb58cd602452c3f0aacd8e5aeac216043196ac1499670`
- **Encoding**: ASCII

**File code content:**

```python
"""
Feature selection utilities.
"""

from __future__ import annotations

from typing import Optional

import pandas as pd

from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import mutual_info_classif

from src.utils.logger import get_logger
from src.utils.timer import Timer

logger = get_logger()


class FeatureSelector:
    """
    Generic feature selection interface.
    """

    SUPPORTED_METHODS = (
        "variance",
        "mutual_info",
        "anova",
        "random_forest",
        "extra_trees",
    )

    def __init__(
        self,
        method: str = "variance",
        k: int = 20,
        threshold: float = 0.0,
        random_state: int = 42,
    ) -> None:

        if method not in self.SUPPORTED_METHODS:
            raise ValueError(
                f"Unsupported method '{method}'. "
                f"Choose from {self.SUPPORTED_METHODS}"
            )

        self.method = method
        self.k = k
        self.threshold = threshold
        self.random_state = random_state

        self.selected_features: list[str] = []

    def fit(
        self,
        X: pd.DataFrame,
        y: Optional[pd.Series] = None,
    ) -> None:

        with Timer(f"Feature Selection ({self.method})"):

            if self.method == "variance":

                selector = VarianceThreshold(
                    threshold=self.threshold
                )

                selector.fit(X)

                self.selected_features = (
                    X.columns[
                        selector.get_support()
                    ].tolist()
                )

            elif self.method == "mutual_info":

                if y is None:
                    raise ValueError(
                        "Target values are required."
                    )

                selector = SelectKBest(
                    score_func=mutual_info_classif,
                    k=min(self.k, X.shape[1]),
                )

                selector.fit(X, y)

                self.selected_features = (
                    X.columns[
                        selector.get_support()
                    ].tolist()
                )

            elif self.method == "anova":

                if y is None:
                    raise ValueError(
                        "Target values are required."
                    )

                selector = SelectKBest(
                    score_func=f_classif,
                    k=min(self.k, X.shape[1]),
                )

                selector.fit(X, y)

                self.selected_features = (
                    X.columns[
                        selector.get_support()
                    ].tolist()
                )

            elif self.method == "random_forest":

                if y is None:
                    raise ValueError(
                        "Target values are required."
                    )

                model = RandomForestClassifier(
                    n_estimators=200,
                    random_state=self.random_state,
                    n_jobs=-1,
                )

                model.fit(X, y)

                importance = pd.Series(
                    model.feature_importances_,
                    index=X.columns,
                )

                self.selected_features = (
                    importance
                    .sort_values(ascending=False)
                    .head(min(self.k, X.shape[1]))
                    .index
                    .tolist()
                )

            elif self.method == "extra_trees":

                if y is None:
                    raise ValueError(
                        "Target values are required."
                    )

                model = ExtraTreesClassifier(
                    n_estimators=200,
                    random_state=self.random_state,
                    n_jobs=-1,
                )

                model.fit(X, y)

                importance = pd.Series(
                    model.feature_importances_,
                    index=X.columns,
                )

                self.selected_features = (
                    importance
                    .sort_values(ascending=False)
                    .head(min(self.k, X.shape[1]))
                    .index
                    .tolist()
                )

        logger.info(
            f"Selected {len(self.selected_features)} features."
        )

    def transform(
        self,
        X: pd.DataFrame,
    ) -> pd.DataFrame:

        return X[self.selected_features].copy()

    def fit_transform(
        self,
        X: pd.DataFrame,
        y: Optional[pd.Series] = None,
    ) -> pd.DataFrame:

        self.fit(X, y)

        return self.transform(X)
```

---

### <a id="📄-src-feature-engineering-statistical-features-py"></a>📄 `src/feature_engineering/statistical_features.py`

**File Info:**
- **Size**: 1.53 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/feature_engineering/statistical_features.py`
- **Relative Path**: `src/feature_engineering`
- **Created**: 2026-07-26 04:57:02 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-26 04:57:02 (Asia/Calcutta / GMT+06:30)
- **MD5**: `0cb8b255cb9c9da166e02ae0c52bef8f`
- **SHA256**: `7e6bf9348b869f3664d306dfeeb5a14952b58639c11148235a809bac4227e45e`
- **Encoding**: ASCII

**File code content:**

```python
"""
Statistical feature analysis utilities.
"""

from __future__ import annotations

import pandas as pd

from src.utils.logger import get_logger
from src.utils.timer import Timer

logger = get_logger()


class StatisticalFeatureAnalyzer:
    """
    Computes descriptive statistics for numerical features.
    """

    def __init__(self) -> None:
        self.summary: pd.DataFrame | None = None

    def analyze(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Generate descriptive statistics.
        """

        with Timer("Statistical Analysis"):

            numeric_df = dataframe.select_dtypes(include="number")

            self.summary = pd.DataFrame({
                "mean": numeric_df.mean(),
                "std": numeric_df.std(),
                "variance": numeric_df.var(),
                "min": numeric_df.min(),
                "max": numeric_df.max(),
                "median": numeric_df.median(),
                "skewness": numeric_df.skew(),
                "kurtosis": numeric_df.kurt(),
                "missing": numeric_df.isna().sum(),
            })

        logger.info(
            f"Computed statistics for {len(self.summary)} features."
        )

        return self.summary

    def top_variance(
        self,
        n: int = 10,
    ) -> pd.DataFrame:

        if self.summary is None:
            raise ValueError(
                "Run analyze() first."
            )

        return self.summary.sort_values(
            by="variance",
            ascending=False,
        ).head(n)
```

---

## 🚫 Binary/Excluded Files

The following files were not included in the text content:

- `src/models/__pycache__/__init__.cpython-312.pyc`
- `src/models/__pycache__/base_model.cpython-312.pyc`
- `src/models/__pycache__/isolation_forest.cpython-312.pyc`
- `src/models/__pycache__/local_outlier_factor.cpython-312.pyc`
- `src/models/__pycache__/one_class_svm.cpython-312.pyc`

### <a id="📄-src-models-init-py"></a>📄 `src/models/__init__.py`

**File Info:**
- **Size**: 315 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/models/__init__.py`
- **Relative Path**: `src/models`
- **Created**: 2026-07-30 15:36:44 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-30 15:36:44 (Asia/Calcutta / GMT+06:30)
- **MD5**: `489c3e032bc4d49c9c031104ea7a3eb1`
- **SHA256**: `e1fe8cd6d680d62f1bb4fe7481ee52b5160e500a920f3d79588437a1268c192e`
- **Encoding**: ASCII

**File code content:**

```python
"""
Machine Learning Models.
"""

from .isolation_forest import IsolationForestModel
from .local_outlier_factor import LocalOutlierFactorModel


from ..config.isolation_forest_config import IsolationForestConfig

__all__ = [
    "IsolationForestModel",
    "IsolationForestConfig",
    "LocalOutlierFactorModel",
]

```

---

### <a id="📄-src-models-autoencoder-py"></a>📄 `src/models/autoencoder.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/models/autoencoder.py`
- **Relative Path**: `src/models`
- **Created**: 2026-07-26 06:19:44 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-26 06:19:44 (Asia/Calcutta / GMT+06:30)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-src-models-base-model-py"></a>📄 `src/models/base_model.py`

**File Info:**
- **Size**: 5.88 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/models/base_model.py`
- **Relative Path**: `src/models`
- **Created**: 2026-07-26 14:58:05 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-26 14:58:05 (Asia/Calcutta / GMT+06:30)
- **MD5**: `d9562f3f6bb35ab88baa0bd648d71d9f`
- **SHA256**: `a61d5d2c7288fe094e4aaa9f0b7e7d28aaaf861333aec038c08a39a8d5a1b26e`
- **Encoding**: ASCII

**File code content:**

```python
"""
Base classes for all anomaly detection models.

This module defines the abstract interface that every anomaly detection
model in the framework must implement.

Author: Kalpesh Patil
Project:
Adaptive Multi-Paradigm Network Anomaly Detection:
Fusion of Unsupervised Models via Reinforcement Learning
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Optional
import logging

import joblib
import numpy as np
import pandas as pd


@dataclass(slots=True)
class ModelMetadata:
    """
    Stores metadata describing a trained model.
    """

    model_name: str
    model_version: str = "1.0.0"
    training_timestamp: Optional[str] = None
    training_time_seconds: Optional[float] = None
    n_features: Optional[int] = None
    random_state: Optional[int] = None
    additional_info: dict[str, Any] = field(default_factory=dict)


class BaseAnomalyModel(ABC):
    """
    Abstract base class for all anomaly detection models.

    Every anomaly detection model must inherit from this class and
    implement the required abstract methods.

    Standard prediction convention:

        predict():
            0 -> Normal
            1 -> Anomaly

        anomaly_score():
            Higher score = More anomalous
    """

    def __init__(
        self,
        model_name: str,
        random_state: Optional[int] = None,
    ) -> None:
        self.model_name = model_name
        self.random_state = random_state

        self._is_fitted: bool = False
        self._model: Any = None

        self.metadata = ModelMetadata(
            model_name=model_name,
            random_state=random_state,
        )
        self.logger = logging.getLogger(self.model_name)

    # ------------------------------------------------------------------
    # Abstract API
    # ------------------------------------------------------------------

    @abstractmethod
    def fit(self, X: pd.DataFrame | np.ndarray) -> "BaseAnomalyModel":
        """
        Train the anomaly detection model.

        Parameters
        ----------
        X : pd.DataFrame | np.ndarray
            Training feature matrix.

        Returns
        -------
        BaseAnomalyModel
            The trained model.
        """

    @abstractmethod
    def predict(self, X: pd.DataFrame | np.ndarray) -> np.ndarray:
        """
        Predict anomalies.

        Returns
        -------
        np.ndarray

            Binary predictions.

            0 = Normal
            1 = Anomaly
        """

    @abstractmethod
    def anomaly_score(self, X: pd.DataFrame | np.ndarray) -> np.ndarray:
        """
        Compute anomaly scores.

        Higher score always indicates a more anomalous sample.
        """

    # ------------------------------------------------------------------
    # Public utility methods
    # ------------------------------------------------------------------

    @property
    def is_fitted(self) -> bool:
        """
        Indicates whether the model has been trained.
        """
        return self._is_fitted

    def save(self, filepath: str | Path) -> None:
        """
        Save the model to disk.

        Parameters
        ----------
        filepath : str | Path
            Destination path.
        """
        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)

        joblib.dump(self, filepath)

    @classmethod
    def load(cls, filepath: str | Path) -> Any:
        """
        Load a previously saved model.

        Parameters
        ----------
        filepath : str | Path
            Saved model path.

        Returns
        -------
        BaseAnomalyModel
        """
        return joblib.load(filepath)

    # ------------------------------------------------------------------
    # Protected helper methods
    # ------------------------------------------------------------------

    def _validate_input(
        self,
        X: pd.DataFrame | np.ndarray,
    ) -> np.ndarray:
        """
        Validate the input feature matrix.

        Parameters
        ----------
        X : pd.DataFrame | np.ndarray
            Feature matrix.

        Returns
        -------
        np.ndarray
            Validated NumPy array.
        """

        # Accept pandas DataFrame
        if isinstance(X, pd.DataFrame):
            X = X.to_numpy()

        # Accept NumPy arrays
        elif not isinstance(X, np.ndarray):
            raise TypeError(
                "Input must be a pandas DataFrame or NumPy ndarray."
            )

        if X.ndim != 2:
            raise ValueError(
                "Input array must be two-dimensional."
            )

        if X.shape[0] == 0:
            raise ValueError(
                "Input array cannot be empty."
            )

        if X.shape[1] == 0:
            raise ValueError(
                "Input array must contain at least one feature."
            )

        return X

    def _check_is_fitted(self) -> None:
        """
        Ensure the model has already been trained.
        """

        if not self._is_fitted:
            raise RuntimeError(
                f"{self.model_name} has not been fitted yet."
            )

    def _set_fitted(
        self,
        n_features: int,
        training_time: Optional[float] = None,
    ) -> None:
        """
        Mark model as trained and update metadata.
        """

        self._is_fitted = True

        self.metadata.training_timestamp = (
            datetime.now().isoformat(timespec="seconds")
        )

        self.metadata.n_features = n_features
        self.metadata.training_time_seconds = training_time

    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"model_name='{self.model_name}', "
            f"is_fitted={self._is_fitted})"
        )
```

---

### <a id="📄-src-models-isolation-forest-py"></a>📄 `src/models/isolation_forest.py`

**File Info:**
- **Size**: 4.2 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/models/isolation_forest.py`
- **Relative Path**: `src/models`
- **Created**: 2026-07-26 07:58:10 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-26 07:58:10 (Asia/Calcutta / GMT+06:30)
- **MD5**: `b913c98e1a875dac69593122c7248908`
- **SHA256**: `ee73f40a7f2ac7d9e61d7c6add48d9f6a78752ef0193de860a2ef866217ce5ce`
- **Encoding**: ASCII

**File code content:**

```python
"""
Isolation Forest model wrapper for the Adaptive RL Anomaly Detection framework.

Responsibilities
----------------
- Train an Isolation Forest model.
- Produce anomaly scores.
- Produce binary predictions.
- Save/load trained models.
- Provide a common interface for the ensemble.

Author: Adaptive RL Framework
"""

from __future__ import annotations

from pathlib import Path
import time
from typing import Optional

import numpy as np
from sklearn.ensemble import IsolationForest

from src.config.isolation_forest_config import IsolationForestConfig
from src.models.base_model import BaseAnomalyModel
from src.utils.logger import get_logger

logger = get_logger(__name__)


class IsolationForestModel(BaseAnomalyModel):
    """
    Wrapper around sklearn IsolationForest.

    Notes
    -----
    decision_function() and score_samples() return larger values for more
    normal samples. This wrapper inverts score_samples() so larger scores
    consistently indicate more anomalous samples across ensemble models.
    """

    def __init__(
        self,
        config: Optional[IsolationForestConfig] = None,
    ) -> None:
        self.config = config or IsolationForestConfig()
        super().__init__(
            model_name="IsolationForest",
            random_state=self.config.random_state,
        )

        self._model = IsolationForest(
            n_estimators=self.config.n_estimators,
            contamination=self.config.contamination,
            max_samples=self.config.max_samples,
            max_features=self.config.max_features,
            bootstrap=self.config.bootstrap,
            random_state=self.config.random_state,
            n_jobs=self.config.n_jobs,
            verbose=self.config.verbose,
        )

    def fit(self, X: np.ndarray) -> "IsolationForestModel":
        """Train the Isolation Forest and update training metadata."""
        X = self._validate_input(X)

        logger.info("Training Isolation Forest...")
        logger.info("Training samples: %d", len(X))

        start_time = time.perf_counter()
        self._model.fit(X)
        self._set_fitted(
            n_features=X.shape[1],
            training_time=time.perf_counter() - start_time,
        )

        logger.info("Isolation Forest training completed.")
        return self

    def anomaly_score(self, X: np.ndarray) -> np.ndarray:
        """
        Return anomaly scores where larger values indicate more anomalous data.
        """
        self._check_is_fitted()
        X = self._validate_input(X)

        return -self._model.score_samples(X)

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict binary anomaly labels: 1 for anomaly and 0 for normal.
        """
        self._check_is_fitted()
        X = self._validate_input(X)

        predictions = self._model.predict(X)
        return np.where(predictions == -1, 1, 0)

    def normalized_scores(self, X: np.ndarray) -> np.ndarray:
        """Normalize anomaly scores to the [0, 1] interval."""
        scores = self.anomaly_score(X)
        minimum = scores.min()
        maximum = scores.max()

        if maximum == minimum:
            return np.zeros_like(scores)

        return (scores - minimum) / (maximum - minimum)

    def save(self, filepath: str | Path) -> None:
        """Persist the wrapper, estimator, configuration, and metadata."""
        super().save(filepath)
        logger.info("Isolation Forest saved -> %s", filepath)

    @classmethod
    def load(cls, filepath: str | Path) -> "IsolationForestModel":
        """Load a previously saved Isolation Forest wrapper."""
        model = super().load(filepath)

        if not isinstance(model, cls):
            raise TypeError(
                f"Expected a saved {cls.__name__}, got {type(model).__name__}."
            )

        logger.info("Isolation Forest loaded <- %s", filepath)
        return model

    @property
    def estimator(self) -> IsolationForest:
        """Return the underlying scikit-learn estimator."""
        return self._model

    def __repr__(self) -> str:
        return (
            "IsolationForestModel("
            f"n_estimators={self.config.n_estimators}, "
            f"contamination={self.config.contamination}, "
            f"is_fitted={self.is_fitted})"
        )

```

---

### <a id="📄-src-models-local-outlier-factor-py"></a>📄 `src/models/local_outlier_factor.py`

**File Info:**
- **Size**: 4.1 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/models/local_outlier_factor.py`
- **Relative Path**: `src/models`
- **Created**: 2026-07-30 15:36:44 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-30 15:36:44 (Asia/Calcutta / GMT+06:30)
- **MD5**: `fd0e7f9ba059fd78bdff23fc5e5de21f`
- **SHA256**: `69ea11834291dbb8625344c524d4d9836c7ec6e9922aa768814ddcdd39cfe33a`
- **Encoding**: ASCII

**File code content:**

```python
"""
Local Outlier Factor (LOF) anomaly detection model.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from sklearn.neighbors import LocalOutlierFactor

from src.config.local_outlier_factor_config import LocalOutlierFactorConfig
from src.models.base_model import BaseAnomalyModel
from src.utils.logger import get_logger

logger = get_logger(__name__)


class LocalOutlierFactorModel(BaseAnomalyModel):
    """
    Wrapper around sklearn's Local Outlier Factor.

    The wrapper provides a unified interface for all anomaly
    detection models in the framework.

    Predictions
    ----------
    0 -> Normal
    1 -> Anomaly
    """

    def __init__(
        self,
        config: LocalOutlierFactorConfig,
    ) -> None:
        super().__init__(
            model_name="LocalOutlierFactor",
            random_state=config.random_state,
        )

        self.config = config

        self._model = LocalOutlierFactor(
            n_neighbors=config.n_neighbors,
            algorithm=config.algorithm,
            leaf_size=config.leaf_size,
            metric=config.metric,
            p=config.p,
            contamination=config.contamination,
            novelty=config.novelty,
            n_jobs=config.n_jobs,
        )

        logger.info("Local Outlier Factor initialized.")

    def fit(self, X, y=None):
        """
        Train the LOF model.
        """

        X = self._validate_input(X)
        if len(X) > self.config.max_training_samples:
            logger.warning(
                "Sampling %d rows for Local Outlier Factor training.",
                self.config.max_training_samples,
            )
        
            rng = np.random.default_rng(self.config.random_state)
        
            indices = rng.choice(
                len(X),
                self.config.max_training_samples,
                replace=False,
            )
        
            X = X[indices]

        logger.info("Training Local Outlier Factor...")

        self._model.fit(X, y)
        self.training_samples = X.shape[0]
        self.training_features = X.shape[1]

        self._set_fitted(True)

        logger.info("Training completed.")
        return self

    def predict(
        self,
        X,
    ) -> np.ndarray:
        """
        Predict anomalies.

        Returns
        -------
        ndarray

        0 -> Normal

        1 -> Anomaly
        """

        self._check_is_fitted()

        X = self._validate_input(X)

        predictions = self._model.predict(X)

        predictions = np.where(
            predictions == -1,
            1,
            0,
        )

        return predictions

    def anomaly_score(
        self,
        X,
    ) -> np.ndarray:
        """
        Compute anomaly scores.

        Larger score means more anomalous.
        """

        self._check_is_fitted()

        X = self._validate_input(X)

        scores = -self._model.decision_function(X)

        return scores

    @property
    def estimator(self) -> LocalOutlierFactor:
        """
        Return the underlying sklearn estimator.
        """
        return self._model
        
    

    def save(
        self,
        filepath: str | Path,
    ) -> None:
        """
        Save trained model.
        """

        super().save(filepath)

        logger.info(
            "Local Outlier Factor saved -> %s",
            filepath,
        )

    @classmethod
    def load(
        cls,
        filepath: str | Path,
    ) -> "LocalOutlierFactorModel":
        """
        Load a previously saved model.
        """

        model = super().load(filepath)

        if not isinstance(model, cls):
            raise TypeError(
                f"Expected {cls.__name__}, "
                f"got {type(model).__name__}."
            )

        logger.info(
            "Local Outlier Factor loaded <- %s",
            filepath,
        )

        return model

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"n_neighbors={self.config.n_neighbors}, "
            f"contamination={self.config.contamination}, "
            f"novelty={self.config.novelty})"
        )
```

---

### <a id="📄-src-models-model-factory-py"></a>📄 `src/models/model_factory.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/models/model_factory.py`
- **Relative Path**: `src/models`
- **Created**: 2026-07-26 06:19:52 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-26 06:19:52 (Asia/Calcutta / GMT+06:30)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-src-models-one-class-svm-py"></a>📄 `src/models/one_class_svm.py`

**File Info:**
- **Size**: 4.25 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/models/one_class_svm.py`
- **Relative Path**: `src/models`
- **Created**: 2026-07-30 15:36:44 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-30 15:36:44 (Asia/Calcutta / GMT+06:30)
- **MD5**: `71e59b8f07bcbe948d2f7d2082de595b`
- **SHA256**: `6ead7062317fbb395361683a656d10a26aaac4b6df4e3717382d6fb91aa30d29`
- **Encoding**: ASCII

**File code content:**

```python
"""
One-Class SVM anomaly detection model.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from sklearn.svm import OneClassSVM

from src.config.one_class_svm_config import OneClassSVMConfig
from src.models.base_model import BaseAnomalyModel
from src.utils.logger import get_logger

logger = get_logger(__name__)


class OneClassSVMModel(BaseAnomalyModel):
    """
    Wrapper around sklearn's One-Class SVM.

    The wrapper provides a unified interface for all anomaly
    detection models in the framework.

    Predictions
    ----------
    0 -> Normal
    1 -> Anomaly
    """

    def __init__(
        self,
        config: OneClassSVMConfig,
    ) -> None:
        super().__init__(
            model_name="OneClassSVM",
            random_state=config.random_state,
        )

        self.config = config

        self._model = OneClassSVM(
            kernel=config.kernel,
            degree=config.degree,
            gamma=config.gamma,
            coef0=config.coef0,
            tol=config.tol,
            nu=config.nu,
            shrinking=config.shrinking,
            cache_size=config.cache_size,
            verbose=config.verbose,
            max_iter=config.max_iter,
        )

        logger.info("One-Class SVM initialized.")

    def fit(self, X: np.ndarray, y: np.ndarray | None = None)-> "OneClassSVMModel":
        """
        Train the One-Class SVM model.
        """

        X = self._validate_input(X)

        if len(X) > self.config.max_training_samples:
            logger.warning(
                "Dataset contains %d samples. "
                "Sampling %d rows for One-Class SVM training.",
                len(X),
                self.config.max_training_samples,
            )

            rng = np.random.default_rng(self.config.random_state)

            indices = rng.choice(
                len(X),
                self.config.max_training_samples,
                replace=False,
            )

            X = X[indices]

        logger.info("Training One-Class SVM...")

        self._model.fit(X, y)
        self.training_samples = X.shape[0]
        self.training_features = X.shape[1]
        logger.info(
            "Training samples: %d | Features: %d",
            self.training_samples,
            self.training_features,
        )

        self._set_fitted(True)

        logger.info("One-Class SVM training completed successfully.")
        return self

    def predict(
        self,
        X,
    ) -> np.ndarray:
        """
        Predict anomalies.

        Returns
        -------
        ndarray

        0 -> Normal
        1 -> Anomaly
        """

        self._check_is_fitted()

        X = self._validate_input(X)

        predictions = self._model.predict(X)

        predictions = np.where(
            predictions == -1,
            1,
            0,
        )

        return predictions

    def anomaly_score(
        self,
        X,
    ) -> np.ndarray:
        """
        Compute anomaly scores.

        Larger score means more anomalous.
        """

        self._check_is_fitted()

        X = self._validate_input(X)

        scores = -self._model.decision_function(X)

        return scores

    @property
    def estimator(self) -> OneClassSVM:
        """
        Return the underlying sklearn estimator.
        """
        return self._model

    def save(
        self,
        filepath: str | Path,
    ) -> None:
        """
        Save trained model.
        """

        super().save(filepath)

        logger.info(
            "One-Class SVM saved -> %s",
            filepath,
        )

    @classmethod
    def load(
        cls,
        filepath: str | Path,
    ) -> "OneClassSVMModel":
        """
        Load a previously saved model.
        """

        model = super().load(filepath)

        if not isinstance(model, cls):
            raise TypeError(
                f"Expected {cls.__name__}, "
                f"got {type(model).__name__}."
            )

        logger.info(
            "One-Class SVM loaded <- %s",
            filepath,
        )

        return model

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"kernel={self.config.kernel}, "
            f"nu={self.config.nu}, "
            f"gamma={self.config.gamma})"
        )
```

---

### <a id="📄-src-pipelines-init-py"></a>📄 `src/pipelines/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/pipelines/__init__.py`
- **Relative Path**: `src/pipelines`
- **Created**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

## 🚫 Binary/Excluded Files

The following files were not included in the text content:

- `src/preprocessing/__pycache__/__init__.cpython-312.pyc`
- `src/preprocessing/__pycache__/cleaner.cpython-312.pyc`
- `src/preprocessing/__pycache__/encoder.cpython-312.pyc`
- `src/preprocessing/__pycache__/loader.cpython-312.pyc`
- `src/preprocessing/__pycache__/scaler.cpython-312.pyc`
- `src/preprocessing/__pycache__/splitter.cpython-312.pyc`

### <a id="📄-src-preprocessing-init-py"></a>📄 `src/preprocessing/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/preprocessing/__init__.py`
- **Relative Path**: `src/preprocessing`
- **Created**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-src-preprocessing-cleaner-py"></a>📄 `src/preprocessing/cleaner.py`

**File Info:**
- **Size**: 2.72 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/preprocessing/cleaner.py`
- **Relative Path**: `src/preprocessing`
- **Created**: 2026-07-25 06:54:00 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 06:54:00 (Asia/Calcutta / GMT+06:30)
- **MD5**: `762df6cd43c41247fc7509e607cd51dd`
- **SHA256**: `89ebc75bdfbeede04b82311f5e7578292decfdf3e785b894229623fbdaeca696`
- **Encoding**: ASCII

**File code content:**

```python
"""
Data cleaning utilities for the Adaptive RL Ensemble Framework.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from src.config.config import config
from src.utils.logger import get_logger
from src.utils.timer import Timer

logger = get_logger()


class DataCleaner:
    """
    Performs basic data cleaning operations.
    """

    def __init__(self, target_column: str | None = None) -> None:
        self.target_column = target_column or config.dataset.target_column

    def remove_duplicates(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Remove duplicate rows.
        """

        with Timer("Removing Duplicates"):

            before = len(dataframe)

            dataframe = dataframe.drop_duplicates()

            removed = before - len(dataframe)

            logger.info(f"Removed {removed} duplicate rows.")

        return dataframe

    def replace_infinities(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Replace positive and negative infinity with NaN.
        """

        with Timer("Replacing Infinite Values"):

            dataframe = dataframe.replace(
                [np.inf, -np.inf],
                np.nan,
            )

        return dataframe

    def remove_missing(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Remove rows containing missing values.
        """

        with Timer("Removing Missing Values"):

            before = len(dataframe)

            dataframe = dataframe.dropna()

            removed = before - len(dataframe)

            logger.info(f"Removed {removed} rows containing missing values.")

        return dataframe

    def remove_constant_columns(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Remove columns containing only one unique value.
        """

        with Timer("Removing Constant Columns"):

            constant_columns = [
                column
                for column in dataframe.columns
                if dataframe[column].nunique() <= 1
            ]

            dataframe = dataframe.drop(
                columns=constant_columns
            )

            logger.info(
                f"Removed {len(constant_columns)} constant columns."
            )

        return dataframe

    def clean(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Complete cleaning pipeline.
        """

        dataframe = self.replace_infinities(dataframe)

        dataframe = self.remove_duplicates(dataframe)

        dataframe = self.remove_missing(dataframe)

        dataframe = self.remove_constant_columns(dataframe)

        logger.info(
            f"Cleaning completed. Final shape: {dataframe.shape}"
        )

        return dataframe
```

---

### <a id="📄-src-preprocessing-encoder-py"></a>📄 `src/preprocessing/encoder.py`

**File Info:**
- **Size**: 2.61 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/preprocessing/encoder.py`
- **Relative Path**: `src/preprocessing`
- **Created**: 2026-07-25 07:00:42 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 07:00:42 (Asia/Calcutta / GMT+06:30)
- **MD5**: `e469324ac33b6d82046b80f2fd6dc9ef`
- **SHA256**: `0417ea60240f6f78ceb5e983bfe2d206423806f9744f3d262ffb876a5e9e7833`
- **Encoding**: ASCII

**File code content:**

```python
"""
Feature and target encoding utilities.
"""

from __future__ import annotations

import pandas as pd
from sklearn.preprocessing import LabelEncoder

from src.utils.logger import get_logger
from src.utils.timer import Timer

logger = get_logger()


class DataEncoder:
    """
    Encodes categorical features and (optionally) the target column.
    """

    def __init__(self, target_column: str | None = None) -> None:
        self.target_column = target_column

        self.target_encoder = LabelEncoder()
        self.feature_encoders: dict[str, LabelEncoder] = {}

    def fit(self, dataframe: pd.DataFrame) -> None:
        """
        Fit encoders on the dataframe.
        """

        categorical_columns = dataframe.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()

        if self.target_column in categorical_columns:
            categorical_columns.remove(self.target_column)

        for column in categorical_columns:
            encoder = LabelEncoder()
            encoder.fit(dataframe[column].astype(str))
            self.feature_encoders[column] = encoder

        if (
            self.target_column is not None
            and self.target_column in dataframe.columns
        ):
            self.target_encoder.fit(
                dataframe[self.target_column].astype(str)
            )

    def transform(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Transform dataframe using fitted encoders.
        """

        dataframe = dataframe.copy()

        with Timer("Encoding Dataset"):

            for column, encoder in self.feature_encoders.items():
                dataframe[column] = encoder.transform(
                    dataframe[column].astype(str)
                )

            if (
                self.target_column is not None
                and self.target_column in dataframe.columns
            ):
                dataframe[self.target_column] = (
                    self.target_encoder.transform(
                        dataframe[self.target_column].astype(str)
                    )
                )

        logger.info("Encoding completed.")

        return dataframe

    def fit_transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Fit and transform dataframe.
        """

        self.fit(dataframe)

        return self.transform(dataframe)

    def inverse_target(self, values):
        """
        Decode encoded target labels.
        """

        if self.target_column is None:
            raise ValueError("Target encoder was not initialized.")

        return self.target_encoder.inverse_transform(values)
```

---

### <a id="📄-src-preprocessing-loader-py"></a>📄 `src/preprocessing/loader.py`

**File Info:**
- **Size**: 2.02 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/preprocessing/loader.py`
- **Relative Path**: `src/preprocessing`
- **Created**: 2026-07-25 06:35:06 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 06:35:06 (Asia/Calcutta / GMT+06:30)
- **MD5**: `cbe64dd465038fa8aaa2c77cc6b92174`
- **SHA256**: `cb2dbe09df25b587510b059da3e1442c55cd01e85a23574ddc530ace658c4c96`
- **Encoding**: ASCII

**File code content:**

```python
"""
Dataset loading utilities for the Adaptive RL Ensemble Framework.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.config.config import config
from src.utils.logger import get_logger
from src.utils.timer import Timer

logger = get_logger()


class DataLoader:
    """
    Loads one or multiple CSV datasets.
    """

    def __init__(self, data_directory: Path | None = None) -> None:
        self.data_directory = data_directory or config.paths.raw_data_dir

    def load_csv(self, filename: str) -> pd.DataFrame:
        """
        Load a single CSV file.

        Parameters
        ----------
        filename : str
            CSV filename.

        Returns
        -------
        pd.DataFrame
        """

        file_path = self.data_directory / filename

        if not file_path.exists():
            raise FileNotFoundError(f"Dataset not found: {file_path}")

        with Timer(f"Loading {filename}"):

            logger.info(f"Reading {file_path}")

            dataframe = pd.read_csv(file_path)

            logger.info(
                f"Loaded {filename} | Shape={dataframe.shape}"
            )

        return dataframe

    def load_multiple(self, filenames: list[str]) -> pd.DataFrame:
        """
        Load multiple CSV files and concatenate them.

        Parameters
        ----------
        filenames : list[str]

        Returns
        -------
        pd.DataFrame
        """

        dataframes = [self.load_csv(file) for file in filenames]

        combined = pd.concat(
            dataframes,
            ignore_index=True,
        )

        logger.info(
            f"Combined dataset shape={combined.shape}"
        )

        return combined

    @staticmethod
    def dataset_summary(dataframe: pd.DataFrame) -> None:
        """
        Print dataset summary.
        """

        logger.info(f"Rows: {len(dataframe)}")
        logger.info(f"Columns: {len(dataframe.columns)}")
        logger.info(f"Memory Usage: {dataframe.memory_usage(deep=True).sum()/1024**2:.2f} MB")
```

---

### <a id="📄-src-preprocessing-scaler-py"></a>📄 `src/preprocessing/scaler.py`

**File Info:**
- **Size**: 4.45 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/preprocessing/scaler.py`
- **Relative Path**: `src/preprocessing`
- **Created**: 2026-07-26 08:33:38 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-26 08:33:38 (Asia/Calcutta / GMT+06:30)
- **MD5**: `3564b6517d9218c5e11ffbe36943325b`
- **SHA256**: `05a5dba9a209b266a086afb80e3912f8b7b0e5235df3bc1161b0ca3eb9364e5e`
- **Encoding**: ASCII

**File code content:**

```python
"""
Feature scaling utilities.
"""

from __future__ import annotations

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import StandardScaler

from src.utils.logger import get_logger
from src.utils.timer import Timer

logger = get_logger()


class DataScaler:
    """
    Scale numerical features using different scaling strategies.

    Supported scalers
    -----------------
    - standard : StandardScaler
    - minmax   : MinMaxScaler
    - robust   : RobustScaler

    Notes
    -----
    The target column is automatically excluded from scaling.
    """

    SUPPORTED_SCALERS = {
        "standard": StandardScaler,
        "minmax": MinMaxScaler,
        "robust": RobustScaler,
    }

    def __init__(
        self,
        method: str = "standard",
        target_column: str | None = None,
    ) -> None:
        """
        Parameters
        ----------
        method : str
            Scaling method.

        target_column : str | None
            Target column to exclude from scaling.
        """

        method = method.lower()

        if method not in self.SUPPORTED_SCALERS:
            raise ValueError(
                f"Unsupported scaler '{method}'. "
                f"Choose from {list(self.SUPPORTED_SCALERS.keys())}"
            )

        self.method = method
        self.target_column = target_column
        self.scaler = self.SUPPORTED_SCALERS[method]()

        self.numeric_columns: list[str] = []

    def fit(
        self,
        dataframe: pd.DataFrame,
    ) -> None:
        """
        Fit the scaler on numerical feature columns.

        Parameters
        ----------
        dataframe : pd.DataFrame
            Input dataframe.
        """

        numeric_columns = dataframe.select_dtypes(
            include="number"
        ).columns.tolist()

        if (
            self.target_column is not None
            and self.target_column in numeric_columns
        ):
            numeric_columns.remove(self.target_column)

        self.numeric_columns = numeric_columns

        self.scaler.fit(
            dataframe[self.numeric_columns]
        )

        logger.info(
            f"Scaler ({self.method}) fitted on "
            f"{len(self.numeric_columns)} feature columns."
        )

    def transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Scale numerical feature columns.

        Parameters
        ----------
        dataframe : pd.DataFrame
            Input dataframe.

        Returns
        -------
        pd.DataFrame
            Scaled dataframe.
        """

        if not self.numeric_columns:
            raise RuntimeError(
                "Scaler has not been fitted."
            )

        dataframe = dataframe.copy()

        with Timer("Scaling Dataset"):

            dataframe[self.numeric_columns] = (
                self.scaler.transform(
                    dataframe[self.numeric_columns]
                )
            )

        logger.info("Scaling completed.")

        return dataframe

    def fit_transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Fit and transform dataframe.

        Parameters
        ----------
        dataframe : pd.DataFrame
            Input dataframe.

        Returns
        -------
        pd.DataFrame
            Scaled dataframe.
        """

        self.fit(dataframe)

        return self.transform(dataframe)

    def inverse_transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Reverse scaling on feature columns.

        Parameters
        ----------
        dataframe : pd.DataFrame
            Scaled dataframe.

        Returns
        -------
        pd.DataFrame
            Original-scale dataframe.
        """

        if not self.numeric_columns:
            raise RuntimeError(
                "Scaler has not been fitted."
            )

        dataframe = dataframe.copy()

        dataframe[self.numeric_columns] = (
            self.scaler.inverse_transform(
                dataframe[self.numeric_columns]
            )
        )

        return dataframe

    def __repr__(self) -> str:
        """
        String representation.
        """

        return (
            f"{self.__class__.__name__}("
            f"method='{self.method}', "
            f"target_column={self.target_column}, "
            f"features={len(self.numeric_columns)})"
        )
```

---

### <a id="📄-src-preprocessing-splitter-py"></a>📄 `src/preprocessing/splitter.py`

**File Info:**
- **Size**: 2.67 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/preprocessing/splitter.py`
- **Relative Path**: `src/preprocessing`
- **Created**: 2026-07-25 07:12:03 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 07:12:03 (Asia/Calcutta / GMT+06:30)
- **MD5**: `23765790a189ad4879d1513f68b2f6a3`
- **SHA256**: `8e1bb0f94d8f6a01b6289505ca6c625530081bb08796108237642c82ac2682a2`
- **Encoding**: ASCII

**File code content:**

```python
"""
Dataset splitting utilities.
"""

from __future__ import annotations

from typing import Optional

import pandas as pd
from sklearn.model_selection import train_test_split

from src.config.config import config
from src.utils.logger import get_logger
from src.utils.timer import Timer

logger = get_logger()


class DataSplitter:
    """
    Split datasets into train, validation, and test sets.
    """

    def __init__(
        self,
        train_size: float = 0.70,
        validation_size: float = 0.15,
        test_size: float = 0.15,
        random_state: Optional[int] = None,
    ) -> None:

        total = train_size + validation_size + test_size

        if abs(total - 1.0) > 1e-6:
            raise ValueError(
                "train_size + validation_size + test_size must equal 1.0"
            )

        self.train_size = train_size
        self.validation_size = validation_size
        self.test_size = test_size
        self.random_state = (
            random_state
            if random_state is not None
            else config.training.random_seed
        )

    def split(
        self,
        dataframe: pd.DataFrame,
        target_column: str | None = None,
        stratify: bool = False,
    ):
        """
        Split a dataframe into train, validation, and test sets.
        """

        with Timer("Dataset Splitting"):

            stratify_values = None

            if (
                stratify
                and target_column is not None
                and target_column in dataframe.columns
            ):
                stratify_values = dataframe[target_column]

            train_df, temp_df = train_test_split(
                dataframe,
                train_size=self.train_size,
                random_state=self.random_state,
                shuffle=True,
                stratify=stratify_values,
            )

            validation_ratio = (
                self.validation_size
                / (self.validation_size + self.test_size)
            )

            temp_stratify = None

            if stratify_values is not None:
                temp_stratify = temp_df[target_column]

            validation_df, test_df = train_test_split(
                temp_df,
                train_size=validation_ratio,
                random_state=self.random_state,
                shuffle=True,
                stratify=temp_stratify,
            )

        logger.info(
            f"Train={len(train_df)} | "
            f"Validation={len(validation_df)} | "
            f"Test={len(test_df)}"
        )

        return (
            train_df.reset_index(drop=True),
            validation_df.reset_index(drop=True),
            test_df.reset_index(drop=True),
        )
```

---

### <a id="📄-src-rl-init-py"></a>📄 `src/rl/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/rl/__init__.py`
- **Relative Path**: `src/rl`
- **Created**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

## 🚫 Binary/Excluded Files

The following files were not included in the text content:

- `src/utils/__pycache__/__init__.cpython-312.pyc`
- `src/utils/__pycache__/logger.cpython-312.pyc`
- `src/utils/__pycache__/seed.cpython-312.pyc`
- `src/utils/__pycache__/timer.cpython-312.pyc`

### <a id="📄-src-utils-init-py"></a>📄 `src/utils/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/utils/__init__.py`
- **Relative Path**: `src/utils`
- **Created**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-src-utils-logger-py"></a>📄 `src/utils/logger.py`

**File Info:**
- **Size**: 1.34 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/utils/logger.py`
- **Relative Path**: `src/utils`
- **Created**: 2026-07-25 06:15:15 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 06:15:15 (Asia/Calcutta / GMT+06:30)
- **MD5**: `1bb91267049603d198f4d4db0dd50afe`
- **SHA256**: `6b067a2c5924ba0da9a2360601f9e2377bc2beed6f446dd5d4ba8452a340103a`
- **Encoding**: ASCII

**File code content:**

```python
"""
Centralized logging utility for the Adaptive RL Ensemble Framework.
"""

from __future__ import annotations

import logging
from pathlib import Path

from src.config.config import config


def get_logger(name: str | None = None) -> logging.Logger:
    """
    Create and configure a logger.

    Parameters
    ----------
    name : str | None
        Name of the logger.

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """

    logger_name = name or config.logging.logger_name
    logger = logging.getLogger(logger_name)

    if logger.hasHandlers():
        return logger

    logger.setLevel(getattr(logging, config.logging.log_level.upper()))

    # Create log directory if it doesn't exist
    Path(config.paths.log_dir).mkdir(parents=True, exist_ok=True)

    log_file = Path(config.paths.log_dir) / config.logging.log_filename

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File Handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger
```

---

### <a id="📄-src-utils-seed-py"></a>📄 `src/utils/seed.py`

**File Info:**
- **Size**: 1.54 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/utils/seed.py`
- **Relative Path**: `src/utils`
- **Created**: 2026-07-25 06:08:56 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 06:08:56 (Asia/Calcutta / GMT+06:30)
- **MD5**: `736dd598034c08b605b4dbb02a318523`
- **SHA256**: `09af2fd60eb52fd805a31a7313356d3cab7f4f5f8f544f12e73ef45c5ac112eb`
- **Encoding**: ASCII

**File code content:**

```python
"""
Utility functions for reproducible experiments.
"""

from __future__ import annotations

import os
import random

import numpy as np
import torch


def set_seed(seed: int = 42, deterministic: bool = True) -> None:
    """
    Set random seed for Python, NumPy, and PyTorch.

    Parameters
    ----------
    seed : int
        Random seed value.
    deterministic : bool
        If True, enables deterministic CUDA behavior for reproducibility.
    """

    random.seed(seed)
    np.random.seed(seed)

    os.environ["PYTHONHASHSEED"] = str(seed)

    torch.manual_seed(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)

    if deterministic:
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    else:
        torch.backends.cudnn.deterministic = False
        torch.backends.cudnn.benchmark = True


def seed_worker(worker_id: int) -> None:
    """
    Seed DataLoader workers for reproducibility.

    Parameters
    ----------
    worker_id : int
        Worker ID assigned by PyTorch DataLoader.
    """

    worker_seed = torch.initial_seed() % (2**32)

    np.random.seed(worker_seed)
    random.seed(worker_seed)


def create_generator(seed: int = 42) -> torch.Generator:
    """
    Create a seeded PyTorch Generator.

    Parameters
    ----------
    seed : int
        Random seed.

    Returns
    -------
    torch.Generator
        Seeded generator.
    """

    generator = torch.Generator()
    generator.manual_seed(seed)
    return generator
```

---

### <a id="📄-src-utils-timer-py"></a>📄 `src/utils/timer.py`

**File Info:**
- **Size**: 1.29 KB
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/utils/timer.py`
- **Relative Path**: `src/utils`
- **Created**: 2026-07-25 06:32:05 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 06:32:05 (Asia/Calcutta / GMT+06:30)
- **MD5**: `ab7f98e8051d1a0b453098eab59a46ba`
- **SHA256**: `4b86d01059d2921c0428d82ba2bbb3614863a21997ac38f0df51a8a81dbdb1eb`
- **Encoding**: ASCII

**File code content:**

```python
"""
Utility for measuring execution time.
"""

from __future__ import annotations

import time
from functools import wraps
from typing import Any, Callable

from src.utils.logger import get_logger

logger = get_logger()


class Timer:
    """
    Context manager for measuring execution time.

    Example
    -------
    with Timer("Data Loading"):
        load_data()
    """

    def __init__(self, name: str = "Operation") -> None:
        self.name = name
        self.start_time: float | None = None

    def __enter__(self) -> "Timer":
        self.start_time = time.perf_counter()
        logger.info(f"{self.name} started.")
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        elapsed = time.perf_counter() - self.start_time
        logger.info(f"{self.name} completed in {elapsed:.4f} seconds.")


def time_function(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator to measure execution time of a function.
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()

        result = func(*args, **kwargs)

        elapsed = time.perf_counter() - start

        logger.info(
            f"{func.__name__} executed in {elapsed:.4f} seconds."
        )

        return result

    return wrapper
```

---

### <a id="📄-src-visualization-init-py"></a>📄 `src/visualization/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/visualization/__init__.py`
- **Relative Path**: `src/visualization`
- **Created**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-src-init-py"></a>📄 `src/__init__.py`

**File Info:**
- **Size**: 0 B
- **Extension**: `.py`
- **Language**: `python`
- **Location**: `src/__init__.py`
- **Relative Path**: `src`
- **Created**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```python

```

---

### <a id="📄-pyproject-toml"></a>📄 `pyproject.toml`

**File Info:**
- **Size**: 344 B
- **Extension**: `.toml`
- **Language**: `text`
- **Location**: `pyproject.toml`
- **Relative Path**: `root`
- **Created**: 2026-07-25 06:12:18 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 06:12:18 (Asia/Calcutta / GMT+06:30)
- **MD5**: `59b4eba74bcf16fd0a74586d1938f3c1`
- **SHA256**: `7c05b492f4cdd99633bc070a8138faf8f07837917375c829b6c8bef017dc9af4`
- **Encoding**: ASCII

**File code content:**

```text
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "adaptive_rl_anomaly_detection"
version = "0.1.0"
description = "Adaptive Reinforcement Learning Ensemble for Network Anomaly Detection"
requires-python = ">=3.12"

[tool.setuptools]
packages = ["src"]

[tool.setuptools.package-dir]
"" = "."
```

---

### <a id="📄-readme-md"></a>📄 `README.md`

**File Info:**
- **Size**: 0 B
- **Extension**: `.md`
- **Language**: `text`
- **Location**: `README.md`
- **Relative Path**: `root`
- **Created**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

````markdown

````

---

### <a id="📄-requirements-txt"></a>📄 `requirements.txt`

**File Info:**
- **Size**: 0 B
- **Extension**: `.txt`
- **Language**: `text`
- **Location**: `requirements.txt`
- **Relative Path**: `root`
- **Created**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 04:41:49 (Asia/Calcutta / GMT+06:30)
- **MD5**: `d41d8cd98f00b204e9800998ecf8427e`
- **SHA256**: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Encoding**: ASCII

**File code content:**

```text

```

---

### <a id="📄-setup-project-sh"></a>📄 `setup_project.sh`

**File Info:**
- **Size**: 1.24 KB
- **Extension**: `.sh`
- **Language**: `bash`
- **Location**: `setup_project.sh`
- **Relative Path**: `root`
- **Created**: 2026-07-25 04:41:32 (Asia/Calcutta / GMT+06:30)
- **Modified**: 2026-07-25 04:41:32 (Asia/Calcutta / GMT+06:30)
- **MD5**: `3760eecb4d48f69b9824a6a7ce3b8e5d`
- **SHA256**: `1bbc61939dde7a49a34868362d5422e1c2c7da79fb503ba3317b24af82fca652`
- **Encoding**: ASCII

**File code content:**

```bash
#!/bin/bash

echo "========================================="
echo "Creating Adaptive RL Project Structure..."
echo "========================================="

# ==========================
# Top-Level Directories
# ==========================
mkdir -p \
datasets/{raw,processed,external} \
notebooks \
configs \
outputs/{figures,metrics,predictions,reports} \
logs \
checkpoints/{isolation_forest,lof,ocsvm,autoencoder,rl} \
tests \
docs \
src/{config,preprocessing,feature_engineering,models,ensemble,rl,evaluation,visualization,utils,pipelines}

# ==========================
# Python Packages
# ==========================
touch \
src/__init__.py \
src/config/__init__.py \
src/preprocessing/__init__.py \
src/feature_engineering/__init__.py \
src/models/__init__.py \
src/ensemble/__init__.py \
src/rl/__init__.py \
src/evaluation/__init__.py \
src/visualization/__init__.py \
src/utils/__init__.py \
src/pipelines/__init__.py

# ==========================
# Root Files
# ==========================
touch README.md
touch requirements.txt
touch .gitignore

echo ""
echo "Project structure created successfully!"
echo ""

if command -v tree >/dev/null 2>&1; then
    tree -L 2
else
    echo "Install 'tree' to view the structure:"
    echo "sudo apt install tree"
fi

```

---

## 🚫 Binary/Excluded Files

The following files were not included in the text content:

- `nohup.out`

