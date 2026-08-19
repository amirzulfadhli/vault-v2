# Autonomous Categorization Guidelines

When processing raw text files from `inbox/`, analyze the text and automatically save the output as a nested Markdown file under `content/` based on these taxonomy rules:

## Categorization Taxonomy:
1. **Programming Languages (`content/programming/`)**
   - Save path: `content/programming/{language}/{topic}.md`
   - Example categories: `c++`, `python`, `rust`, `javascript`

2. **Science (`content/science/`)**
   - Save path: `content/science/{field}/{topic}.md`
   - Sub-fields:
     - `biology` -> (`human`, `cell`, `plant`, `animal`)
     - `physics` -> (`gravity`, `newtons-law`, `force`, `quantum`)
     - `chemistry` -> (`acid`, `bond`, `thermodynamics`)

3. **Agriculture & IoT (`content/agriculture-iot/`)**
   - Save path: `content/agriculture-iot/{topic}.md`

4. **Finance & Budget (`content/finance/`)**
   - Save path: `content/finance/{topic}.md`

## File Formatting Rules:
- Ensure the destination sub-folders are created automatically.
- Every generated file MUST include frontmatter tags matching its subject:
  ```yaml
  ---
  title: "Note Title"
  tags:
    - programming/python
    - science/physics/gravity
  ---
