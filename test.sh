#!/bin/bash

mkdir -p ./wiki
cd wiki

declare -a pages=(
  "01_Getting_Started"
  "02_Python_Essentials"
  "03_Machine_Learning_Fundamentals"
  "04_Libraries_and_Tools"
  "05_Model_Development_Pipeline"
  "06_Projects_and_Case_Studies"
  "07_LLMS_and_Generative_AI"
  "08_Deployment_with_MLOps"
  "09_Resources_and_Learning_Paths"
  "10_Reflections_and_Journal"
)

for page in "${pages[@]}"; do
  filename="$page.md"
  echo "# ${page//_/ }" > "$filename"
  echo "_Template auto-generated. Add your notes and code walkthroughs here._" >> "$filename"
done

echo "✅ Wiki skeleton created in ./wiki/"
