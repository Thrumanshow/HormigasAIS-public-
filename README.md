# HormigasAIS Open Lab

Este repositorio forma parte del ecosistema de automatización e inteligencia colaborativa de HormigasAIS. Aquí exploramos datos, herramientas y experimentos con enfoque en IA, marketing digital y visualización.

## 🔍 Exploraciones actuales

- Automatización con n8n  
- Análisis de comportamiento en email  
- Herramientas SEO e integraciones de datos  

---

## 📂 Datos disponibles

Este repositorio incluye un archivo de dominios utilizados para tráfico de correo electrónico entrante, junto con el nivel de cifrado STARTTLS detectado.

- `google-starttls-domains.xlsx`: archivo original en Excel.
- `google-starttls-domains.csv`: versión exportada en CSV (puede generarse con el script en `/scripts/`).

### 🔄 Conversión de Excel a CSV

Para convertir el archivo a `.csv`, ejecuta el siguiente script:

```bash
python scripts/convert_excel_to_csv.py
