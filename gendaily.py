# Credit: ChatGPT Mar 14 Version (https://help.openai.com/en/articles/6825453-chatgpt-release-notes). Free Research Preview.

# Initial prompt:
# write a python script that will generate several html files from start_year (hardcoded at the beginning of the script) to end_year (also hardcoded) with the following content, for example for 2020 (the file will have a name 2020.html): "---
# permalink: /daily/2020/
# layout: daily
# year: 2020
# ---
# "

# Final output, with modifications:

import datetime
import os

work_dir = "daily"

start_year = 2008  # Update with desired starting year
end_year = datetime.datetime.now().year  # Set end_year to current year

for year in range(start_year, end_year):
    filename = str(year) + '.html'
    with open(os.path.join(work_dir, filename), 'w') as file:
        file.write('---\n')
        file.write('permalink: /daily/' + str(year) + '/\n')
        file.write('layout: daily\n')
        file.write('title: Daily ' + str(year) + '\n')
        file.write('year: ' + str(year) + '\n')
        file.write('---\n')
