import json
import copy

# Read the template JSON file
with open('template.json', 'r') as f:
    template_data = json.load(f)

# Read the settings from another JSON file
with open('settings.json', 'r') as f:
    settings_data = json.load(f)

# Iterate over each set of settings
for settings in settings_data:
    # Create a copy of the template data
    modified_template_data = copy.deepcopy(template_data)

    # Modify the template title
    modified_template_data['data']['907']['post_title'] = settings['templatetitle']

    # Modify the body text
    body_text = modified_template_data['data']['907']['post_content']
    body_text = body_text.replace('one', settings['titlechange'])
    body_text = body_text.replace('five centuries', settings['bodychange'])
    modified_template_data['data']['907']['post_content'] = body_text

    # Generate a unique file name for each modified template
    filename = 'modified_template_{}.json'.format(settings['templatetitle'])

    # Write the modified template to a new file
    with open(filename, 'w') as f:
        json.dump(modified_template_data, f, indent=4)
