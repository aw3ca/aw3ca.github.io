import csv

# HTML for the navigation bar
NAVBAR_HTML = """
<div class="website-title">academics/web3/canada</div>
<nav class="navbar">
    <ul>
        <li><a href="index.html">Directory</a></li>
        <li><a href="apply.html">Research Positions</a></li>
    </ul>
</nav>
"""

# HTML for the navigation bar
ABOUT_HTML = """
<div class="info-label">
    <div class="info-title"></div>
    <div class="info-content">
        <p>
            This is a directory of academics working on web3, blockchain, cryptocurriencies, and related technologies at Canadian universities. 
            It is not an official group of any sort.
            It is meant as a convenient reference for companies, media, students, researchers, and others looking for experts.
        </p>
        <p>
            Are you an academic that we missed? Or see someone we missed? Please <a href="mailto:j.clark@concordia.ca">let me know</a>.
        </p>
        <p>
            Are you a student or researcher looking for a research position? Please <a href="apply.html">click here</a>.
        </p>        
    </div>
</div>
"""


# Define the template for the HTML label
HTML_TEMPLATE = """

<div class="label">
    <div class="title">{name}</div>
    <div class="subtitle">{department}</div>
    
    <div class="box">
        <div class="box-title">Research Interests</div>
        <div class="box-content">{research_interests}</div>
    </div>
    <div class="box">
        <div class="box-title">Highlighted Work</div>
        <div class="box-content"><a href="{highlighted_work_url}" target="_blank" class="unstyled-link"><em>{highlighted_work}</em></a></div>
    </div>
    <div class="box">
        <div class="box-title">Contact</div>
        <div class="box-content"><a href="mailto:{contact}" class="unstyled-link">{contact}</a></div>
    </div>
    
    <div class="footer">
        <a class="website-link" href="{website}" target="_blank">
            <div class="website-icon"></div>
            Website
        </a>
        <div>{university}</div>
    </div>
</div>
"""

# Read data from the CSV file
def generate_html_from_csv(csv_file, output_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        profiles = sorted(reader, key=lambda x: x['sort_key'])  # Sort by sort_key
    
        html_profiles = []
        for row in profiles:
            html_profiles.append(HTML_TEMPLATE.format(
                name=row['name'],
                department=row['department'],
                university=row['university'],
                research_interests=row['research_interests'],
                highlighted_work=row['highlighted_work'],
                highlighted_work_url=row['highlighted_work_url'],
                contact=row['contact'],
                website=row['website']
            ))
    
    with open(output_file, 'w') as file:
        file.write("<!DOCTYPE html>\n<html lang='en'>\n<head>\n")
        file.write("<meta charset='UTF-8'>\n<title>Academics/Web3/Canada</title>\n")
        file.write("<link rel='stylesheet' href='styles.css'>\n</head>\n<body>\n")
        file.write(NAVBAR_HTML)  # Add the navigation bar
        file.write("<div class='directory'>\n")
        file.write(ABOUT_HTML)  # Add the about box
        file.write("\n".join(html_profiles))
        file.write("\n</div>\n</body>\n</html>")

# Example usage
generate_html_from_csv('professors.csv', 'index.html')