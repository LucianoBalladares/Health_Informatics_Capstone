# Project Log — Week 1: Data Foundation

---

## Monday, Week 1 — Project Scaffolding (20 Oct 2025)

### Objective

Establish the foundational structure and version control system for the Health Informatics Capstone Project, in alignment with the *Data Foundation* phase of the Project Plan.
This step ensures a reproducible, well-documented environment for the upcoming data acquisition and analysis workflow.

---

### Tasks Completed

**Project Directory Structure**

* Created the full hierarchy of folders: `/data`, `/sql`, `/notebooks`, `/reports`, `/dashboard`, `/docs`.

**Git Repository Initialization**

* Initialized a local Git repository and connected it to a new GitHub remote (`health-informatics-capstone`).

**Core Files Created**

* `.gitignore` excluding `/data/raw`, `/data/interim`, and temporary files.
* `README.md` with project summary and current phase.
* `requirements.txt` with initial Python dependencies.
* Blank `create_schema.sql` as a placeholder for Week 1–Friday.

**Python Environment Setup**

* Created Conda environment `healthinformatics` with Python 3.11.
* Installed libraries: `pandas`, `numpy`, `sqlalchemy`, `matplotlib`, `seaborn`, `jupyter`, `scikit-learn`, `scipy`, `psycopg2-binary`.

**VS Code Configuration**

* Installed extensions: *Python*, *Jupyter*, *Pylance*, *SQLTools*, *Markdown All in One*, *GitHub Pull Requests*.
* Verified interpreter and Jupyter integration.

**Documentation**

* Created `docs/setup_instructions.md` with full environment setup and reproducibility guide.

---

### Observations / Reflections

* Environment setup completed successfully under WSL (Ubuntu); integration with VS Code is seamless.
* GitHub repository is clean and properly structured for version tracking.
* The documentation approach aligns with professional reproducibility standards in data science.
* All preparatory steps completed as defined in the Week 1 – Monday plan item (“Project Scaffolding”).

---

## Tuesday, Week 1 — Database Configuration and Connection Validation (21 Oct 2025)

### Objective

Install, configure, and validate the PostgreSQL database for the Health Informatics Project, ensuring end-to-end connectivity with both Python and Power BI environments.

---

### Tasks Completed

* Installed PostgreSQL 14 under WSL 2 (Ubuntu 22.04).
* Created PostgreSQL user and database (`healthuser` / `healthdb`) with secure credentials stored in `.env`.
* Implemented and tested SQLAlchemy engine connection in Python (`db_connection.py` and `connection_test.ipynb`) using environment variables.
* Verified database connectivity via Jupyter Notebook (`SELECT version();`).
* Configured PostgreSQL to listen on all interfaces (`0.0.0.0`) and confirmed via `netstat` and `ss`.
* Established Windows → WSL port forwarding (`netsh interface portproxy`) and opened corresponding firewall rule for Power BI.
* Installed Power BI Desktop and Npgsql driver; confirmed successful connection.
* Verified SSL/TLS handshake (TLS 1.3) between Power BI and PostgreSQL.
* Confirmed Power BI successfully recognizes the database schema; full pipeline connectivity achieved.

---

### Observations / Reflections

* Secure, fully functioning data pipeline between PostgreSQL, Python, and Power BI established.
* Connection tested and documented, ensuring reproducibility.
* The system is ready for the data ingestion and exploration phases.

---

## Wednesday, Week 1 — Primary Data Sourcing (22 Oct 2025)

### Objective

Identify and acquire the core public datasets forming the analytical foundation of the project:

* Non-GES Surgical Waiting List data (MINSAL / Visor Ciudadano).
* Mortality Statistics (DEIS).

This step aims to establish the primary link between system efficiency (waiting times) and patient outcomes (mortality), as defined in the *Data Foundation* phase.

---

### Tasks Completed

**DEIS – Mortality Dataset**

* Downloaded “Defunciones por Causa 2023–2025 (Cifras Preliminares, Actualización semanal)” from [deis.minsal.cl](https://deis.minsal.cl/#datosabiertos).
* Verified structure (~35,000 entries) and confirmed inclusion of relevant variables:

  ```
  AÑO, FECHA_DEF, SEXO_NOMBRE, EDAD_TIPO, EDAD_CANT, COD_COMUNA, COMUNA,
  NOMBRE_REGION, DIAG1, GLOSA_SUBCATEGORIA_DIAG1, ..., LUGAR_DEFUNCION
  ```
* Confirmed dataset suitability for the mortality analysis phase.
* Conducted quick inspection using Pandas in Jupyter Notebook (`.info()` and `.head()`); verified UTF-8 encoding and delimiter `;`.
* Saved raw copy to `/data/raw/defunciones_2023_2025.csv`.

**Identified Power BI “Visor Ciudadano de Tiempos de Espera”**

* Located the official MINSAL portal displaying national and regional waiting list statistics.
* Verified that it provides the required variables: Región, Servicio de Salud, Tipo de Lista, Especialidad, Casos, Tiempo Mediano.
* Confirmed that no downloadable CSV or API endpoint is available.
* Documented the portal’s URL and metadata for reference in `/docs/data_inventory.md`.

---

### Challenges / Observations

* The waiting list microdata (non-GES) are not directly available for public download.
* The Visor Ciudadano Power BI dashboard is dynamic and updated daily, but backend data are not accessible without a formal request.
* The mortality data from DEIS are comprehensive and clean, suitable for immediate analysis.
* Identified structural barriers to open access in Chilean public health data, relevant for methodological discussion later.

---

### Next Steps

* Draft and submit a formal data access request under Ley 20.285 (Transparencia) to the Subsecretaría de Redes Asistenciales for access to the dataset underlying the *Visor Ciudadano de Tiempos de Espera*.
* Proceed with secondary data acquisition (INE and CASEN) on Thursday.
* Create `docs/data_request_minsal.md` summarizing the request text, dataset description, and metadata.
* Maintain DEIS dataset documentation in `data_inventory.md` and begin schema preparation in `create_schema.sql`.

---

## Thursday, Week 1 — Secondary Data Sourcing and Consolidation (23 Oct 2025)

### Objective

Consolidate acquisition of all datasets (primary and secondary), document their metadata, and prepare for database schema definition.
Pending tasks from Wednesday (waiting list data) are included in today’s agenda.

---

### Tasks Completed  *(to be filled as work progresses)*

* [ ] MINSAL – Waiting List Data review and documentation.
* [ ] Formal transparency request drafted (`/docs/data_request_minsal.md`).
* [ ] INE – Demographic data downloaded (`/data/raw/demografia_ine.csv`).
* [ ] CASEN – Socioeconomic data downloaded (`/data/raw/socioeconomia_casen.csv`).
* [ ] Data inventory updated (`/docs/data_inventory.md`).
* [ ] Initial SQL schema drafted (`/sql/create_schema.sql`).

---

### In Progress / Observations  *(to complete at end of day)*

* Notes on data availability and file structure.
* Observations on encodings, variable naming, and completeness.
* Identification of any placeholders or proxy datasets.

---

### Next Steps  *(to complete at end of day)*

* Finalize the data inventory and verify metadata completeness.
* Prepare Saturday backlog session for inspection of downloaded datasets (`.info()` and `.describe()`).
* Validate that all schema placeholders match the actual data structure.

---
