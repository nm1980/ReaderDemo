from docx import Document
import sys
sys.path.insert(0, "./docx")
import docx
import re
import string
selected_file=""
best_match=""
#Dictonary of jobs with experience, skills, and education key words to look out for when going through the resume
job_lists = {
    "School Bus Driver": {
        "experience": [
            "vehicle inspection", "navigation", "map reading", "transport", "road safety",
            "children", "students", "school district", "school bus", "mornings",
            "evenings", "afternoon", "trips"
        ],
        "skills": [
            "cdl", "cpl", "logistics", "freight", "commercial driver license",
            "school bus endorsement", "passenger endorsement", "radio", "first aid",
            "s endorsement", "p endorsement"
        ],
        "education": [
            "ged", "high school", "school bus driver certification"
        ]
    },

    "Truck Driver": {
        "experience": [
            "vehicle inspection", "navigation", "map reading", "delivery", "cargo",
            "transport", "road safety", "trips"
        ],
        "skills": [
            "cdl", "cpl", "logistics", "freight", "commercial driver license"
        ],
        "education": [
            "ged", "high school"
        ]
    },

    "Warehouse Worker": {
        "experience": [
            "warehouse", "distribution", "physical labor", "lifting", "stocking",
            "loading", "unloading", "assembly"
        ],
        "skills": [
            "inventory", "shipping", "logistics", "packing", "receiving", "order",
            "forklift", "pallet jack", "rf scanner"
        ],
        "education": [
            "ged", "high school"
        ]
    },

    "Office Worker": {
        "experience": [
            "office", "clerical", "reception", "receptionist",
            "documents", "meetings"
        ],
        "skills": [
            "data entry", "microsoft office", "word", "excel", "outlook",
            "filing", "email", "powerpoint", "customer service"
        ],
        "education": [
            "ged", "high school", "associate's", "bachelor's"
        ]
    },

    "Arborist": {
        "experience": [
            "tree care", "landscaping", "climbing", "rigging", "safety"
        ],
        "skills": [
            "chainsaw", "tree climbing", "arboriculture", "aerial lift",
            "pesticide application", "plant health care"
        ],
        "education": [
            "ged", "high school", "certified arborist", "isa certification"
        ]
    },

    "Landscaper": {
        "experience": [
            "outdoor work", "groundskeeping", "gardening", "seasonal maintenance",
            "equipment handling", "physical labor", "trimming", "client properties",
            "landscaping"
        ],
        "skills": [
            "lawn care", "hedge trimming", "mowing", "weed control",
            "irrigation systems", "planting", "mulching", "edging",
            "fertilization", "landscape design"
        ],
        "education": [
            "high school", "ged", "horticulture"
        ]
    },

    "Carpenter": {
        "experience": [
            "residential projects", "remodeling", "commercial buildings", "flooring",
            "doors", "windows", "roofing", "cabinetry", "finishing", "jobsite work"
        ],
        "skills": [
            "framing", "measuring", "cutting", "blueprints", "power tools",
            "saw", "woodworking", "construction", "nails", "joinery"
        ],
        "education": [
            "high school", "ged", "carpentry school", "apprenticeship"
        ]
    },

    "Delivery Driver": {
        "experience": [
            "package delivery", "food delivery", "last mile delivery", "routes",
            "vehicle operation", "doorstep delivery", "scan and drop",
            "delivery logs", "urban delivery"
        ],
        "skills": [
            "navigation", "customer service", "time management", "loading",
            "driving", "delivery tracking", "route planning", "vehicle inspection",
            "communication", "problem solving"
        ],
        "education": [
            "high school", "ged"
        ]
    },

    "Kitchen Helper": {
        "experience": [
            "restaurant", "cafeteria", "fast-paced environment", "line cook assistance",
            "clean kitchen", "team support", "food handling", "fast food"
        ],
        "skills": [
            "food prep", "cleaning", "dishwashing", "knife skills", "sanitation",
            "plating", "safety standards", "inventory stocking", "kitchen support",
            "trash disposal"
        ],
        "education": [
            "high school", "ged", "culinary school"
        ]
    },

    "Tech Support": {
        "experience": [
            "help desk", "phone support", "remote access", "issue resolution",
            "technical documentation", "desktop support", "os support",
            "application troubleshooting", "user training"
        ],
        "skills": [
            "troubleshooting", "hardware", "software", "customer service",
            "remote support", "ticketing systems", "windows", "networking",
            "email setup", "diagnostics"
        ],
        "education": [
            "high school", "ged", "associate's degree", "bachelor's degree",
            "information technology"
        ]
    },

    "Shipping Associate": {
        "experience": [
            "warehouse", "shipping department", "ecommerce fulfillment",
            "package prep", "distribution center", "packaging materials",
            "order processing"
        ],
        "skills": [
            "order picking", "labeling", "packing", "shipping systems",
            "rf scanners", "inventory tracking", "barcode scanning",
            "logistics", "palletizing"
        ],
        "education": [
            "high school", "ged"
        ]
    },

    "Forklift Operator": {
        "experience": [
            "warehouse", "shipping and receiving", "distribution",
            "safety procedures", "heavy lifting", "forklift license",
            "logistics support", "forklift operator"
        ],
        "skills": [
            "forklift operation", "pallet stacking", "warehouse safety",
            "inventory movement", "rf scanner", "material handling",
            "loading docks", "shipping", "logistics"
        ],
        "education": [
            "high school", "ged", "forklift certification"
        ]
    }
}
#extracts the text within the resume entered
def read_docx(file_path):
    doc = docx.Document(file_path)
    full_text = []
    #Extracts text from each paragraph in the docx file
    for para in doc.paragraphs:
        full_text.append(para.text)

    return '\n'.join(full_text)

#cleans up the text from the resume by converting all letters to lowercase and removing numbers
def clean_text(text):
    #lowercase conversion
    text = text.lower()
    #digit removal
    text = re.sub(r'\d+', '', text)
    #punctuation removal
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# combines the text from the skills, experience, and education sections into one string
def combine_resume_info(sections):
    return ' '.join([sections['skills'], sections['experience'], sections['education']])

#extracts the sections from the resume text based on the key words
def get_matched_keywords(flat_resume_text, job_requirements):
    matched_keywords = []

    # Combine all keywords from skills, education, and experience
    all_keywords = []
    for section in ['skills', 'education', 'experience']:
        all_keywords.extend(job_requirements.get(section, []))

    for kw in all_keywords:
        if kw.lower() in flat_resume_text:
            matched_keywords.append(kw)

    print(matched_keywords)
    return matched_keywords


def main():
    global best_match
    path = str(selected_file)
    raw_resume = read_docx(path)
    clean_resume = clean_text(raw_resume).lower()  # lowercase once for easier matching

    match_results = []
    all_match_counts = {}

    # Match resume against all job listings
    for job_title, requirements in job_lists.items():
        matched = get_matched_keywords(clean_resume, requirements)
        match_count = len(matched)
        all_match_counts[job_title] = match_count

    # Scores based on amount of matching keywords from each job listing
    max_matches = max(all_match_counts.values()) if all_match_counts else 1

    for job_title, match_count in all_match_counts.items():
        relative_score = (match_count / max_matches) * 100 if max_matches else 0
        match_results.append((job_title, relative_score))

    # Displays the top 3 results
    match_results.sort(key=lambda x: x[1], reverse=True)
    top_matches = match_results[:3]
    best_match = top_matches[0][0]
    print("\nTop 3 Job Matches (relative to best match):\n")
    for job, score in top_matches:
        print(f"{job}: {score:.2f}% relative match")

    if top_matches and top_matches[0][1] > 0:
        print("Recommended Job: "+ best_match)
    else:
        print("\n No suitable job match found.")