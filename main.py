import textwrap
import langextract as lx

# Define the extraction prompt in English
# This prompt instructs the model to extract a comprehensive list of 46 PII types,
# use exact text, avoid overlaps, and add meaningful attributes for context.
prompt_description = textwrap.dedent("""\
    Extract all 46 types of Personally Identifiable Information (PII) in their order of appearance.
    PII categories include: personal names, demographic data (age, gender, origin), contact details (email, phone), unique identifiers (SSN, passport, account numbers), location data (address, IP), online credentials (username, password), and temporal information (date, time).
    - Use the exact text for extractions.
    - Do not paraphrase or overlap entities.
    - Provide meaningful attributes for each entity to add context.""")

# Provide high-quality examples covering all 46 PII types
# Examples are in both English and Korean to improve model versatility.
examples = [
    # Example 1: Korean - General Profile
    lx.data.ExampleData(
        text="""이름은 홍길동(남성, 35세)이며, 서울 출신입니다. 그의 주민등록번호는 900101-1234567이고, 직업은 변호사입니다. 
        연락처는 010-1234-5678, 이메일은 gildong.hong@lawfirm.example.com 입니다. 
        그는 1990년 1월 1일에 태어났으며, 기혼 상태입니다.""",
        extractions=[
            lx.data.Extraction(
                extraction_class="Name Family",
                extraction_text="홍",
                attributes={"language": "Korean"},
            ),
            lx.data.Extraction(
                extraction_class="Name Given",
                extraction_text="길동",
                attributes={"language": "Korean"},
            ),
            lx.data.Extraction(
                extraction_class="Gender",
                extraction_text="남성",
                attributes={"type": "biological_sex"},
            ),
            lx.data.Extraction(
                extraction_class="Age",
                extraction_text="35세",
                attributes={"unit": "years"},
            ),
            lx.data.Extraction(
                extraction_class="Location City",
                extraction_text="서울",
                attributes={"context": "birthplace"},
            ),
            lx.data.Extraction(
                extraction_class="Origin",
                extraction_text="서울 출신",
                attributes={"granularity": "city_level"},
            ),
            lx.data.Extraction(
                extraction_class="Social Security Number",
                extraction_text="900101-1234567",
                attributes={"country": "South Korea"},
            ),
            lx.data.Extraction(
                extraction_class="Occupation",
                extraction_text="변호사",
                attributes={"field": "legal"},
            ),
            lx.data.Extraction(
                extraction_class="Phone Number",
                extraction_text="010-1234-5678",
                attributes={"type": "mobile"},
            ),
            lx.data.Extraction(
                extraction_class="Email Address",
                extraction_text="gildong.hong@lawfirm.example.com",
                attributes={"domain_type": "corporate"},
            ),
            lx.data.Extraction(
                extraction_class="Date of Birth",
                extraction_text="1990년 1월 1일",
                attributes={"format": "YYYY-MM-DD"},
            ),
            lx.data.Extraction(
                extraction_class="Marital Status",
                extraction_text="기혼",
                attributes={"status": "married"},
            ),
        ],
    ),
    # Example 2: English - Official/Medical Record
    lx.data.ExampleData(
        text="""Patient John Smith, a US citizen, visited Dr. Emily White at Seoul Mercy Hospital on 2025-09-18. 
        His passport number is A12345678 and his health insurance number is H-98765. 
        He is a follower of Buddhism and speaks English fluently.""",
        extractions=[
            lx.data.Extraction(
                extraction_class="Name",
                extraction_text="John Smith",
                attributes={"role": "patient"},
            ),
            lx.data.Extraction(
                extraction_class="Location Country",
                extraction_text="US",
                attributes={"context": "citizenship"},
            ),
            lx.data.Extraction(
                extraction_class="Name Medical Professional",
                extraction_text="Emily White",
                attributes={"role": "doctor"},
            ),
            lx.data.Extraction(
                extraction_class="Organization Medical Facility",
                extraction_text="Seoul Mercy Hospital",
                attributes={"type": "hospital"},
            ),
            lx.data.Extraction(
                extraction_class="Date",
                extraction_text="2025-09-18",
                attributes={"event": "visit"},
            ),
            lx.data.Extraction(
                extraction_class="Passport Number",
                extraction_text="A12345678",
                attributes={"issuing_country": "USA"},
            ),
            lx.data.Extraction(
                extraction_class="Health Insurance Number",
                extraction_text="H-98765",
                attributes={"provider": "unknown"},
            ),
            lx.data.Extraction(
                extraction_class="Religion",
                extraction_text="Buddhism",
                attributes={"type": "organized_religion"},
            ),
            lx.data.Extraction(
                extraction_class="Language",
                extraction_text="English",
                attributes={"proficiency": "fluent"},
            ),
        ],
    ),
    # Example 3: English - Technical/Financial Log
    lx.data.ExampleData(
        text="""At 3:30 PM, user 'data_wizard_01' logged in from IP 203.0.113.75 to access the report file `Q3_Analysis.pdf` via https://internal.datacorps.com/reports. 
        A $250.00 payment was made from account number 110-234-567890. 
        The session lasted for a duration of 45 minutes. The password hint is 'first pet'. 
        The transaction ID is a numeric PII: 8675309.""",
        extractions=[
            lx.data.Extraction(
                extraction_class="Time",
                extraction_text="3:30 PM",
                attributes={"timezone": "unspecified"},
            ),
            lx.data.Extraction(
                extraction_class="Username",
                extraction_text="data_wizard_01",
                attributes={"system": "internal"},
            ),
            lx.data.Extraction(
                extraction_class="IP Address",
                extraction_text="203.0.113.75",
                attributes={"version": "IPv4"},
            ),
            lx.data.Extraction(
                extraction_class="File name",
                extraction_text="Q3_Analysis.pdf",
                attributes={"extension": ".pdf"},
            ),
            lx.data.Extraction(
                extraction_class="URL",
                extraction_text="https://internal.datacorps.com/reports",
                attributes={"protocol": "HTTPS"},
            ),
            lx.data.Extraction(
                extraction_class="Price",
                extraction_text="$250.00",
                attributes={"currency": "USD"},
            ),
            lx.data.Extraction(
                extraction_class="Account Number",
                extraction_text="110-234-567890",
                attributes={"type": "bank_account"},
            ),
            lx.data.Extraction(
                extraction_class="Duration",
                extraction_text="45 minutes",
                attributes={"unit": "minutes"},
            ),
            lx.data.Extraction(
                extraction_class="Password",
                extraction_text="first pet",
                attributes={"type": "hint"},
            ),
            lx.data.Extraction(
                extraction_class="Numeric PII",
                extraction_text="8675309",
                attributes={"description": "transaction_id"},
            ),
        ],
    ),
    # Example 4: Korean - Detailed Personal & Location Info
    lx.data.ExampleData(
        text="""2025년 5월 1일부터 5월 15일까지의 휴가 기간 동안, 김민준 씨는 대한민국 경기도 고양시 일산서구 주엽로 196 (우: 10381)에 머물렀습니다. 
        그의 운전면허증 번호는 경기10-123456-00이고, 차량 식별 번호는 12가3456입니다. 
        그는 진보 정당을 지지하며, 키가 크다는 신체적 특징이 있습니다. 
        좌표는 37.683, 126.772 입니다.""",
        extractions=[
            lx.data.Extraction(
                extraction_class="Date Interval",
                extraction_text="2025년 5월 1일부터 5월 15일까지",
                attributes={"event": "vacation"},
            ),
            lx.data.Extraction(
                extraction_class="Name",
                extraction_text="김민준",
                attributes={"language": "Korean"},
            ),
            lx.data.Extraction(
                extraction_class="Location Country",
                extraction_text="대한민국",
                attributes={"context": "residence"},
            ),
            lx.data.Extraction(
                extraction_class="Location State",
                extraction_text="경기도",
                attributes={"context": "residence"},
            ),
            lx.data.Extraction(
                extraction_class="Location City",
                extraction_text="고양시",
                attributes={"context": "residence"},
            ),
            lx.data.Extraction(
                extraction_class="Location Address Street",
                extraction_text="일산서구 주엽로 196",
                attributes={"context": "residence"},
            ),
            lx.data.Extraction(
                extraction_class="Location Zip Code",
                extraction_text="10381",
                attributes={"context": "residence"},
            ),
            lx.data.Extraction(
                extraction_class="Location Address",
                extraction_text="경기도 고양시 일산서구 주엽로 196 (우: 10381)",
                attributes={"granularity": "full"},
            ),
            lx.data.Extraction(
                extraction_class="Driver's License Number",
                extraction_text="경기10-123456-00",
                attributes={"issuing_authority": "Gyeonggi Police"},
            ),
            lx.data.Extraction(
                extraction_class="Vehicle ID",
                extraction_text="12가3456",
                attributes={"type": "license_plate", "country": "South Korea"},
            ),
            lx.data.Extraction(
                extraction_class="Political Affiliation",
                extraction_text="진보 정당",
                attributes={"stance": "progressive"},
            ),
            lx.data.Extraction(
                extraction_class="Phisical Attributes",
                extraction_text="키가 크다",
                attributes={"category": "height"},
            ),
            lx.data.Extraction(
                extraction_class="Location Coordinates",
                extraction_text="37.683, 126.772",
                attributes={"format": "lat, long"},
            ),
        ],
    ),
    # Example 5: English - Social/Lifestyle Profile
    lx.data.ExampleData(
        text="""This person identifies as homosexual. They are a Leo, work for the organization 'Global Charity Foundation', and attended the 'Music Fest 2025' event.""",
        extractions=[
            lx.data.Extraction(
                extraction_class="Sexuality",
                extraction_text="homosexual",
                attributes={"type": "sexual_orientation"},
            ),
            lx.data.Extraction(
                extraction_class="Zodiac Sign",
                extraction_text="Leo",
                attributes={"system": "western_astrology"},
            ),
            lx.data.Extraction(
                extraction_class="Organization",
                extraction_text="Global Charity Foundation",
                attributes={"type": "non-profit"},
            ),
            lx.data.Extraction(
                extraction_class="Event",
                extraction_text="Music Fest 2025",
                attributes={"category": "festival"},
            ),
        ],
    ),
]

# Read the sample text file
with open("sample.txt", "r", encoding="utf-8") as f:
    sample_text = f.read()

# Extract PII from the sample text using the defined prompt and examples
result = lx.extract(
    text_or_documents=sample_text,
    prompt_description=prompt_description,
    examples=examples,
    model_id="gemma3:4b",
    model_url="http://localhost:11434",
    extraction_passes=3,  # Improves recall through multiple passes
    max_workers=3,  # Parallel processing for speed
    max_char_buffer=1000,  # Smaller contexts for better accuracy
)

# Display the results
print(f"Extracted {len(result.extractions)} entities:\n")
for extraction in result.extractions:
    print(f"• {extraction.extraction_class}: '{extraction.extraction_text}'")
    if extraction.attributes:
        for key, value in extraction.attributes.items():
            print(f"  - {key}: {value}")

# Save results to JSONL
lx.io.save_annotated_documents(
    [result], output_name="results.jsonl", output_dir="."
)

# Generate interactive visualization
html_content = lx.visualize("results.jsonl")

# Display in a Jupyter notebook
print("Interactive visualization (hover over highlights to see attributes):")
html_content

# Save visualization to file (for downloading)
with open("index.html", "w", encoding="utf-8") as f:
    # Handle both Jupyter (HTML object) and non-Jupyter (string) environments
    if hasattr(html_content, "data"):
        f.write(html_content.data)
    else:
        f.write(html_content)
print("✅ Visualization saved to 'index.html'")
print("You can download this file from the Files panel on the left.")