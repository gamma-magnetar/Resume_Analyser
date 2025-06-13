{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyNaBpcSPYX61RuKKrmhXbJ0",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "widgets": {
      "application/vnd.jupyter.widget-state+json": {
        "eb88dcec6afc414aa779251be5690ef6": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "FileUploadModel",
          "model_module_version": "1.5.0",
          "state": {
            "_counter": 1,
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "FileUploadModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "FileUploadView",
            "accept": ".pdf",
            "button_style": "",
            "data": [
              null
            ],
            "description": "Upload",
            "description_tooltip": null,
            "disabled": false,
            "error": "",
            "icon": "upload",
            "layout": "IPY_MODEL_0757e1e2d0274007a8c04ba8ea7494d5",
            "metadata": [
              {
                "name": "CV_Mohit_Laddha.pdf",
                "type": "application/pdf",
                "size": 128163,
                "lastModified": 1748703154428
              }
            ],
            "multiple": false,
            "style": "IPY_MODEL_6122b935699c49f09bba466dbc994ed6"
          }
        },
        "0757e1e2d0274007a8c04ba8ea7494d5": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "6122b935699c49f09bba466dbc994ed6": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "ButtonStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "button_color": null,
            "font_weight": ""
          }
        }
      }
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/gamma-magnetar/Attenue/blob/main/Resume_Analyser.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install pdfplumber python-docx reportlab openai"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vxLskpzJi_5A",
        "outputId": "8de7433a-c20a-4fce-9894-37cdb954e228"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: pdfplumber in /usr/local/lib/python3.11/dist-packages (0.11.6)\n",
            "Requirement already satisfied: python-docx in /usr/local/lib/python3.11/dist-packages (1.1.2)\n",
            "Requirement already satisfied: reportlab in /usr/local/lib/python3.11/dist-packages (4.4.1)\n",
            "Requirement already satisfied: openai in /usr/local/lib/python3.11/dist-packages (1.84.0)\n",
            "Requirement already satisfied: pdfminer.six==20250327 in /usr/local/lib/python3.11/dist-packages (from pdfplumber) (20250327)\n",
            "Requirement already satisfied: Pillow>=9.1 in /usr/local/lib/python3.11/dist-packages (from pdfplumber) (11.2.1)\n",
            "Requirement already satisfied: pypdfium2>=4.18.0 in /usr/local/lib/python3.11/dist-packages (from pdfplumber) (4.30.1)\n",
            "Requirement already satisfied: charset-normalizer>=2.0.0 in /usr/local/lib/python3.11/dist-packages (from pdfminer.six==20250327->pdfplumber) (3.4.2)\n",
            "Requirement already satisfied: cryptography>=36.0.0 in /usr/local/lib/python3.11/dist-packages (from pdfminer.six==20250327->pdfplumber) (43.0.3)\n",
            "Requirement already satisfied: lxml>=3.1.0 in /usr/local/lib/python3.11/dist-packages (from python-docx) (5.4.0)\n",
            "Requirement already satisfied: typing-extensions>=4.9.0 in /usr/local/lib/python3.11/dist-packages (from python-docx) (4.14.0)\n",
            "Requirement already satisfied: chardet in /usr/local/lib/python3.11/dist-packages (from reportlab) (5.2.0)\n",
            "Requirement already satisfied: anyio<5,>=3.5.0 in /usr/local/lib/python3.11/dist-packages (from openai) (4.9.0)\n",
            "Requirement already satisfied: distro<2,>=1.7.0 in /usr/local/lib/python3.11/dist-packages (from openai) (1.9.0)\n",
            "Requirement already satisfied: httpx<1,>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from openai) (0.28.1)\n",
            "Requirement already satisfied: jiter<1,>=0.4.0 in /usr/local/lib/python3.11/dist-packages (from openai) (0.10.0)\n",
            "Requirement already satisfied: pydantic<3,>=1.9.0 in /usr/local/lib/python3.11/dist-packages (from openai) (2.11.5)\n",
            "Requirement already satisfied: sniffio in /usr/local/lib/python3.11/dist-packages (from openai) (1.3.1)\n",
            "Requirement already satisfied: tqdm>4 in /usr/local/lib/python3.11/dist-packages (from openai) (4.67.1)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.11/dist-packages (from anyio<5,>=3.5.0->openai) (3.10)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.11/dist-packages (from httpx<1,>=0.23.0->openai) (2025.4.26)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.11/dist-packages (from httpx<1,>=0.23.0->openai) (1.0.9)\n",
            "Requirement already satisfied: h11>=0.16 in /usr/local/lib/python3.11/dist-packages (from httpcore==1.*->httpx<1,>=0.23.0->openai) (0.16.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<3,>=1.9.0->openai) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.33.2 in /usr/local/lib/python3.11/dist-packages (from pydantic<3,>=1.9.0->openai) (2.33.2)\n",
            "Requirement already satisfied: typing-inspection>=0.4.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<3,>=1.9.0->openai) (0.4.1)\n",
            "Requirement already satisfied: cffi>=1.12 in /usr/local/lib/python3.11/dist-packages (from cryptography>=36.0.0->pdfminer.six==20250327->pdfplumber) (1.17.1)\n",
            "Requirement already satisfied: pycparser in /usr/local/lib/python3.11/dist-packages (from cffi>=1.12->cryptography>=36.0.0->pdfminer.six==20250327->pdfplumber) (2.22)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from IPython.display import display\n",
        "from ipywidgets import FileUpload\n",
        "import pdfplumber\n",
        "\n",
        "# Step 1: Upload the file\n",
        "upload = FileUpload(accept='.pdf', multiple=False)\n",
        "display(upload)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 49,
          "referenced_widgets": [
            "eb88dcec6afc414aa779251be5690ef6",
            "0757e1e2d0274007a8c04ba8ea7494d5",
            "6122b935699c49f09bba466dbc994ed6"
          ]
        },
        "id": "hSZlq0erMcRx",
        "outputId": "c8b1d5df-96b3-458c-8178-083119f84b5d"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "FileUpload(value={}, accept='.pdf', description='Upload')"
            ],
            "application/vnd.jupyter.widget-view+json": {
              "version_major": 2,
              "version_minor": 0,
              "model_id": "eb88dcec6afc414aa779251be5690ef6"
            }
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Uploaded resume is parsed and converted into json format"
      ],
      "metadata": {
        "id": "T3DrMLOHqktC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# supports pdf, doc and txt format\n",
        "import pdfplumber\n",
        "import docx\n",
        "\n",
        "def extract_text_from_upload(uploaded_file):\n",
        "    # Get uploaded file name and content\n",
        "    name = list(uploaded_file.value.keys())[0]\n",
        "    content = uploaded_file.value[name]['content']\n",
        "\n",
        "    # Save the uploaded file locally\n",
        "    with open(name, 'wb') as f:\n",
        "        f.write(content)\n",
        "\n",
        "    # Extract text based on file extension\n",
        "    if name.endswith('.pdf'):\n",
        "        with pdfplumber.open(name) as pdf:\n",
        "            return \"\\n\".join([page.extract_text() or \"\" for page in pdf.pages])\n",
        "    elif name.endswith('.docx'):\n",
        "        doc = docx.Document(name)\n",
        "        return \"\\n\".join([para.text for para in doc.paragraphs])\n",
        "    elif name.endswith('.txt'):\n",
        "        with open(name, 'r', encoding='utf-8') as f:\n",
        "            return f.read()\n",
        "    else:\n",
        "        raise ValueError(\"Unsupported file format. Please upload PDF, DOCX, or TXT.\")\n",
        "\n",
        "# Use the function\n",
        "resume_text = extract_text_from_upload(upload)\n",
        "\n",
        "# Preview\n",
        "print(resume_text[:2000])\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9ZkNtQFekcjh",
        "outputId": "c6b819eb-5d27-4df9-a1f1-b1186af5897d"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "MOHIT LADDHA | 22AE10023\n",
            "AEROSPACE ENGINEERING(B.Tech 4Y)\n",
            "Linkedin mohitladdha21@kgpian.iitkgp.ac.in +91 9967011152\n",
            "EDUCATION\n",
            "Year Degree/Exam Institute CGPA/Marks\n",
            "2026 B.TECH IIT Kharagpur 8.37/10\n",
            "2022 HSC (Maharashtra Board) - XII Champions Junior Science College, Kharghar 82.33%\n",
            "2020 AISSE (CBSE) - X New Horizon Public School , Airoli 96.40%\n",
            "AWARDS AND ACHIEVEMENTS\n",
            "• Ranked among the top 1% among 1Million+ students in the highly competitive Joint Entrance Examination Mains\n",
            "• Amongst the top 2% of 2,50,000+ students who appeared for Joint Entrance Examination Advanced (Entrance test for IITs)\n",
            "• Secured a top 0.05% rank and placed 55th out of 2,00,000+ students in the MHT-CET entrance exam showcasing academic excellence\n",
            "SKILLS AND EXPERTISE\n",
            "•Languages and Frameworks : C | C++ | Python | HTML | C++STL | Numpy | Matplotlib | Pandas | Sklearn | Tensorflow | Seaborn | SQL\n",
            "• Softwares : Sublime Text | Canva | Visual Studio Code | Jupyter Notebook | Matlab | Google Colab | MS Office | Streamlit\n",
            "• Machine Learning & AI: Algorithms|Time Series Analysis | Deep Learning |CNN|RNN| NLP (Topic Modeling, Sentiment Analysis) | LDA | NMF\n",
            "• GenAI & LLM Tools: LangChain | Hugging Face Transformers | OpenAI API | Retrieval-Augmented Generation (RAG) |FAISS | LlamaIndex\n",
            "INTERNSHIPS\n",
            "Research Intern | IIM Ahmedabad | Prof. Adrija Majumdar March'24 - May’24\n",
            "Objective:Analysis of Narratives across Green Sustainability and Non-Green Crypto Sustainability\n",
            "• Processed 4.5M+ tweets on proof of stake and sustainable, and 4.74M+ tweets on proof of work and non-sustainable cryptocurrencies\n",
            "• Implemented Latent Dirichlet Allocation (LDA) and Non-Negative Matrix Factorization (NMF) for comprehensive topic modeling\n",
            "• Analyzed data sentiment using McDonald Loughran, TextBlob, and Vader, visualizing outcomes with Matplotlib pie charts\n",
            "Research Consultant | WorldQuant - Brain March'24 - Present\n",
            "Objective : Worked as a Quant Researcher at WorldQuant, developing and back-testing trading strategies on th\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import re\n",
        "import json\n",
        "\n",
        "def parse_resume_to_json(resume_text):\n",
        "    sections = {\n",
        "        \"personal_info\": {},\n",
        "        \"education\": [],\n",
        "        \"experience\": [],\n",
        "        \"skills\": [],\n",
        "        \"projects\": [],\n",
        "        \"certifications\": [],\n",
        "        \"awards\": [],\n",
        "        \"positions_of_responsibility\": [],\n",
        "        \"extracurricular_activities\": [],\n",
        "        \"summary\": \"\",\n",
        "    }\n",
        "\n",
        "    # 1. Extract email and name (simple regex-based)\n",
        "    email_match = re.search(r'[\\w\\.-]+@[\\w\\.-]+', resume_text)\n",
        "    name_match = re.search(r'^[A-Z][a-z]+\\s[A-Z][a-z]+', resume_text)\n",
        "\n",
        "    sections[\"personal_info\"][\"email\"] = email_match.group(0) if email_match else \"\"\n",
        "    sections[\"personal_info\"][\"name\"] = name_match.group(0) if name_match else \"\"\n",
        "\n",
        "    # 2. Split based on headers\n",
        "    lines = resume_text.splitlines()\n",
        "    current_section = None\n",
        "\n",
        "    for line in lines:\n",
        "        clean_line = line.strip()\n",
        "\n",
        "        # Match section headers\n",
        "        section_map = {\n",
        "            \"education\": [\"education\", \"academic\"],\n",
        "            \"experience\": [\"experience\", \"work experience\", \"professional experience\"],\n",
        "            \"skills\": [\"skills\", \"technical skills\"],\n",
        "            \"projects\": [\"projects\"],\n",
        "            \"certifications\": [\"certifications\"],\n",
        "            \"awards\": [\"awards\", \"achievements\"],\n",
        "            \"positions_of_responsibility\": [\"positions of responsibility\", \"leadership\"],\n",
        "            \"extracurricular_activities\": [\"extracurricular\", \"activities\"],\n",
        "            \"summary\": [\"summary\", \"objective\"]\n",
        "        }\n",
        "\n",
        "        matched_section = None\n",
        "        for key, keywords in section_map.items():\n",
        "            for keyword in keywords:\n",
        "                if keyword.lower() in clean_line.lower():\n",
        "                    matched_section = key\n",
        "                    break\n",
        "            if matched_section:\n",
        "                break\n",
        "\n",
        "        if matched_section:\n",
        "            current_section = matched_section\n",
        "            continue\n",
        "\n",
        "        if current_section:\n",
        "            if current_section in [\"skills\"]:\n",
        "                sections[current_section].extend(re.split(r',|\\n|;', clean_line))\n",
        "            elif current_section == \"summary\":\n",
        "                sections[current_section] += clean_line + \" \"\n",
        "            else:\n",
        "                sections[current_section].append(clean_line)\n",
        "\n",
        "    return sections"
      ],
      "metadata": {
        "id": "5KxG0cC5TzWn"
      },
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "resume_data = parse_resume_to_json(resume_text)\n",
        "\n",
        "# Save to JSON file\n",
        "with open(\"structured_resume.json\", \"w\", encoding=\"utf-8\") as f:\n",
        "    json.dump(resume_data, f, indent=2)\n",
        "\n",
        "print(\"✅ Resume has been parsed and saved to 'structured_resume.json'\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uGd2mRcMT38d",
        "outputId": "00bea8f5-2f10-432b-d828-0eb92c7d1f2e"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✅ Resume has been parsed and saved to 'structured_resume.json'\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Saves the json file here and next you can download it from the uploads section."
      ],
      "metadata": {
        "id": "gM0qxvguV54X"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import json\n",
        "import os\n",
        "\n",
        "def save_resume_json(resume_data, output_path=\"structured_resume.json\"):\n",
        "    with open(output_path, \"w\", encoding=\"utf-8\") as f:\n",
        "        json.dump(resume_data, f, indent=2, ensure_ascii=False)\n",
        "    print(f\"✅ Structured resume saved to: {os.path.abspath(output_path)}\")\n",
        "\n",
        "# Example usage\n",
        "resume_data = parse_resume_to_json(resume_text)  # your existing function\n",
        "save_resume_json(resume_data)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YUnElTl9VuZr",
        "outputId": "d16ac849-12f5-4a8d-bfaf-ac6fb52ec64b"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✅ Structured resume saved to: /content/structured_resume.json\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Prompt with gemini with result"
      ],
      "metadata": {
        "id": "Gojy-4WAq41B"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import google.generativeai as genai\n",
        "\n",
        "genai.configure(api_key=\"AIzaSyA1uYTXvYm_ivDI_wQfeDrPuuTybJZ5I9w\")"
      ],
      "metadata": {
        "id": "CdCh39tTM5fD"
      },
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#identifying sections\n",
        "model = genai.GenerativeModel(\"gemini-1.5-flash\")\n",
        "\n",
        "def analyze_resume1(text):\n",
        "    prompt = f\"\"\"You are an expert at analysing resume and giving expert feedbacks. Analyse the following resume content:\n",
        "\n",
        "{text}\n",
        "\n",
        "Tasks:\n",
        "Please Identify and categorise sections like Summary, Skills, Education, Experience, etc.\n",
        "\"\"\"\n",
        "    response = model.generate_content(prompt)\n",
        "    return response.text\n",
        "\n",
        "\n",
        "result_identifying_sections = analyze_resume1(resume_text)\n",
        "print(result_identifying_sections)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 960
        },
        "id": "st49L3BjNCuD",
        "outputId": "645b8028-9941-4e4b-d91b-bb95623b756b"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "This resume is quite comprehensive, showcasing a strong candidate. However, it needs restructuring for improved readability and impact.  Here's a categorized analysis with suggestions:\n",
            "\n",
            "**Current Categorization (with issues):**\n",
            "\n",
            "* **Contact Information:**  Good.\n",
            "* **Education:** Well-structured.\n",
            "* **Awards and Achievements:** Excellent, but could be integrated into a summary.\n",
            "* **Skills and Expertise:**  Good breadth, but needs organization and prioritization.\n",
            "* **Internships:** Well-structured, strong content.\n",
            "* **Projects:** Strong content, but lacks concise descriptions.\n",
            "* **Competition/Conference:** Good, but could be merged with Projects or a new \"Achievements\" section.\n",
            "* **Coursework Information:**  Too detailed for a resume;  select only highly relevant courses.\n",
            "* **Positions of Responsibility:**  Excellent, showcases leadership.\n",
            "* **Extracurricular Activities:**  Good, but could be shortened.\n",
            "\n",
            "\n",
            "**Recommended Restructuring and Improvements:**\n",
            "\n",
            "1. **Summary/Profile (New Section):**  This is crucial.  Create a concise (3-4 sentence) summary highlighting key achievements and career aspirations.  It should immediately grab the recruiter's attention.  Incorporate elements from \"Awards and Achievements\":\n",
            "\n",
            "   > *Example:*  \"Highly motivated and results-oriented Aerospace Engineering student with proven expertise in AI/ML, quantitative finance, and data analytics.  Consistently ranked among the top percentiles in national entrance examinations (JEE Mains, JEE Advanced, MHT-CET) and achieved top 5% globally in the WorldQuant Challenge. Seeking a challenging role leveraging my analytical and technical skills in [Target Industry/Role].\"\n",
            "\n",
            "2. **Skills (Revised Section):**  Group and prioritize skills. Use a format that makes it easy to scan.  Consider separating technical and soft skills.\n",
            "\n",
            "   > *Example:*\n",
            "   > **Technical Skills:**  Python (Pandas, NumPy, Scikit-learn, TensorFlow, etc.), C++, C, Machine Learning (Deep Learning, NLP, Time Series Analysis), Data Visualization (Matplotlib, Seaborn), SQL, Database Management,  GenAI (LangChain, Hugging Face Transformers),  OpenCV, YOLOv8, UNET\n",
            "   > **Software Proficiency:**  MATLAB, Jupyter Notebook, Visual Studio Code, Sublime Text, MS Office Suite,  Canva, Streamlit, Google Colab\n",
            "   > **Soft Skills:**  Leadership, Teamwork, Problem-solving, Communication, Time Management, Project Management\n",
            "\n",
            "\n",
            "3. **Experience (New Section combining Internships and Projects):**  Present experiences using the STAR method (Situation, Task, Action, Result).  Quantify achievements whenever possible.  Combine internships and projects chronologically, highlighting the most relevant ones first.\n",
            "\n",
            "   > *Example (WorldQuant):*  \"**Quant Researcher, WorldQuant - Brain (March 2024 – Present)** Generated 10+ alpha trading strategies for US and Chinese equity markets, consistently outperforming benchmarks.  Achieved Sharpe Ratios exceeding 1.58 and ranked in the top 5% globally in the WorldQuant Challenge (out of 30,000+ participants).\"\n",
            "\n",
            "4. **Education (Keep):** This section is well-formatted.\n",
            "\n",
            "5. **Awards & Recognition (Optional Section):** If space allows, you can create a separate section for awards, but many have already been incorporated in the Summary/Profile.\n",
            "\n",
            "6. **Positions of Responsibility (Revised):**  Focus on quantifiable achievements and impact.\n",
            "\n",
            "   > *Example:*  \"**Secretary, Aquatics Subcommittee, Technology Students' Gymkhana, IIT Kharagpur**  Elected by over 15,000 students, managed a budget of INR 6 Lakhs+, organized 10+ aquatics tournaments, and significantly increased student participation through social media engagement.\"\n",
            "\n",
            "7. **Extracurricular Activities (Shorten):**  Briefly mention 1-2 key achievements to showcase well-roundedness.\n",
            "\n",
            "8. **Remove Coursework Information:**  Unless applying for a very specific role requiring it, this information is not needed on a resume.\n",
            "\n",
            "\n",
            "**Overall Feedback:**\n",
            "\n",
            "This resume demonstrates strong academic achievements and practical skills.  However, by restructuring it as suggested, the candidate can significantly improve its impact and increase the chances of getting noticed by recruiters. The key is to highlight the most relevant achievements and skills concisely, using strong action verbs and quantifiable results. Remember to tailor the resume to each specific job application to highlight the most relevant experiences and skills.\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#detecting missing or underdeveloped sections\n",
        "model = genai.GenerativeModel(\"gemini-1.5-flash\")\n",
        "\n",
        "def analyze_resume2(text):\n",
        "    prompt = f\"\"\"You are an expert at analysing resume and giving expert feedbacks. Analyse the following resume content:\n",
        "\n",
        "{text}\n",
        "\n",
        "Tasks:\n",
        "Detect missing or underdeveloped sections (e.g., no summary, sparse skills) with proper reasoning.\n",
        "\"\"\"\n",
        "    response = model.generate_content(prompt)\n",
        "    return response.text\n",
        "\n",
        "\n",
        "result_missing_sections = analyze_resume2(resume_text)\n",
        "print(result_missing_sections)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 580
        },
        "id": "fpapA01WbCve",
        "outputId": "efcab156-ff89-4af7-8352-d6898add8be7"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "This resume is quite impressive and comprehensive, showcasing a strong academic record and extensive involvement in projects and extracurricular activities. However, several sections could be improved to maximize impact.\n",
            "\n",
            "**Missing or Underdeveloped Sections:**\n",
            "\n",
            "1. **Summary/Objective Statement:**  The resume lacks a compelling summary or objective statement at the beginning.  This is a critical omission.  A strong summary (preferred over an objective statement for someone with Mohit's experience) should be a concise (3-4 sentence) highlight reel of his key skills and accomplishments, tailored to the type of roles he's seeking. It should immediately grab the reader's attention and showcase his value proposition.  For example, it could emphasize his expertise in AI/ML applied to finance and aerospace, highlighting his high-impact projects and internship experiences at IIM Ahmedabad and WorldQuant.\n",
            "\n",
            "2. **Skills Section – Organization and Specificity:** While the skills section lists many technologies, it lacks structure and prioritization.  Grouping skills by category (e.g., Programming Languages, Data Science Tools, Machine Learning Techniques, Deep Learning Frameworks) would improve readability.  Furthermore, instead of simply listing skills, he should quantify them whenever possible. For instance, instead of \"Python,\" he could say \"Python (Proficient in data manipulation, web scraping, and API integration).\"\n",
            "\n",
            "3. **Projects Section –  Improved Quantifiable Results:** The projects are well-described, but the results could be more impactful with quantitative metrics.  For example:\n",
            "\n",
            "    * **AI-Powered Runway Inspection:** Instead of \"90% accuracy,\" specify the type of accuracy (e.g., precision, recall, F1-score) and compare it to a baseline or state-of-the-art method.  Mention the computational resources used (GPU, etc.).\n",
            "    * **Finance Chatbot System:** Quantify the performance of the chatbot.  Did it accurately predict stock prices?  What was the accuracy of its sentiment analysis?  Include user feedback or engagement metrics if available.\n",
            "    * **Attenue:** Specify the accuracy of the face recognition system (e.g., using metrics like precision, recall, or F1-score).  How many faces could it recognize simultaneously? What was the processing time per face?\n",
            "\n",
            "4. **Coursework Information:** This section is useful but could be condensed.  He can remove less relevant courses and focus on those directly related to his target roles (AI/ML, Finance, or Aerospace).  Instead of listing them, he could create a more concise bullet point list highlighting the most relevant skills gained from specific courses.\n",
            "\n",
            "5. **Keywords Optimization:**  The resume needs stronger keyword optimization.  He should carefully research keywords commonly used in job descriptions for his target roles (e.g., \"quantitative researcher,\" \"machine learning engineer,\" \"data scientist,\" \"AI engineer,\" \"aerospace engineer\").  He should strategically incorporate these keywords throughout the resume, particularly in the summary, skills, and projects sections.\n",
            "\n",
            "\n",
            "**Recommendations for Improvement:**\n",
            "\n",
            "* **Tailor the resume:** This resume is quite general. Mohit should create several tailored versions, each optimized for specific job applications. The summary, skills, and projects sections should be adjusted to highlight the most relevant experiences for each target role.\n",
            "* **Use action verbs:** Start each bullet point in the experience sections with strong action verbs (e.g., developed, implemented, analyzed, optimized, designed, led).\n",
            "* **Quantify achievements:** Whenever possible, use numbers and metrics to demonstrate the impact of his work.\n",
            "* **Proofread carefully:** Ensure there are no grammatical errors or typos.\n",
            "* **Use a consistent format:** Maintain a consistent font, font size, and spacing throughout the resume.  Consider using a professional resume template.\n",
            "\n",
            "\n",
            "By addressing these points, Mohit can significantly strengthen his resume and increase his chances of securing interviews.  The current resume is good, but with these improvements, it will become excellent.\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#evaluate clarity....\n",
        "model = genai.GenerativeModel(\"gemini-1.5-flash\")\n",
        "\n",
        "def analyze_resume3(text):\n",
        "    prompt = f\"\"\"You are an expert at analysing resume and giving expert feedbacks. Analyse the following resume content:\n",
        "\n",
        "{text}\n",
        "\n",
        "Tasks:\n",
        "Evaluate clarity, professionalism, and completeness of the resume.\n",
        "\"\"\"\n",
        "    response = model.generate_content(prompt)\n",
        "    return response.text\n",
        "\n",
        "\n",
        "result_clarity = analyze_resume3(resume_text)\n",
        "print(result_clarity)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 834
        },
        "id": "B1Q_DJMGbNVq",
        "outputId": "e2ab8ae7-6f11-448f-a01b-f9cb92765673"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mohit Laddha's resume demonstrates strong technical skills and achievements, but needs refinement for improved clarity, professionalism, and impact.\n",
            "\n",
            "**Strengths:**\n",
            "\n",
            "* **Quantifiable Achievements:**  The resume consistently uses numbers to highlight accomplishments (e.g., \"processed 4.5M+ tweets,\" \"ranked in the top 5%,\" \"98.6% accuracy\"). This is excellent.\n",
            "* **Impressive Projects and Internships:**  The projects showcase a diverse range of skills and applications, particularly in AI/ML and finance.  The internships at IIM Ahmedabad and WorldQuant are highly impressive.\n",
            "* **Detailed Descriptions:** Project descriptions are detailed enough to convey the scope and impact of the work.\n",
            "* **Comprehensive Skill Set:** The skills section covers programming languages, software, ML techniques, and GenAI tools comprehensively.\n",
            "* **Leadership Experience:**  The positions of responsibility section highlights leadership and managerial skills effectively.\n",
            "\n",
            "**Weaknesses and Areas for Improvement:**\n",
            "\n",
            "* **Formatting and Clarity:** The resume lacks consistent formatting.  The \"EDUCATION\" section uses a table, which is good, but the rest of the sections are inconsistent, making it visually unappealing and harder to scan.  Use a consistent format throughout.  Consider using bullet points more consistently within sections to improve readability.\n",
            "\n",
            "* **Objective Statement:** The resume lacks a compelling career objective or summary statement at the beginning.  Instead of just listing his name and contact information, he should add a brief (3-4 line) summary highlighting his key skills and career aspirations.  This will grab the recruiter's attention immediately.\n",
            "\n",
            "* **Keywords:** While the skills section is detailed, strategically incorporating keywords related to target job roles throughout the resume would enhance its searchability by Applicant Tracking Systems (ATS).\n",
            "\n",
            "* **Redundancy:** Some information is slightly redundant. For instance, mentioning \"Python\" multiple times across different sections is unnecessary.  Consolidate these mentions.\n",
            "\n",
            "* **\"AWARDS AND ACHIEVEMENTS\" Section:** While impressive, these achievements could be better integrated into the main body of the resume, possibly within the introduction or under the relevant project/internship descriptions. For example,  mentioning the JEE Advanced rank within the education section would be more effective.\n",
            "\n",
            "* **\"COURSEWORK INFORMATION\" Section:** This section is not essential for a resume unless applying for very specific roles that require a highly detailed course listing.  Consider removing this and instead focusing on the most relevant coursework in the context of the job description within the projects or skills section.  For instance, instead of listing \"Advanced Calculus,\" it might be better to say \"Proficient in advanced mathematical modeling techniques.\"\n",
            "\n",
            "* **Length:** The resume is quite long.  Prioritize the most relevant information for each job application and tailor it accordingly.  Consider condensing some descriptions and removing less impactful extracurricular activities.\n",
            "\n",
            "\n",
            "**Expert Recommendations:**\n",
            "\n",
            "1. **Rewrite the Summary/Objective:** Craft a concise and impactful summary highlighting his core skills and career goals.  For example:  \"Highly motivated and results-oriented Aerospace Engineering graduate with proven expertise in AI/ML, quantitative finance, and data analysis. Seeking a challenging role in [Target Industry/Role] leveraging my skills in developing and deploying innovative solutions.\"\n",
            "\n",
            "2. **Improve Formatting:**  Use a professional resume template with consistent fonts, headings, and spacing.  Employ bullet points effectively to improve readability.\n",
            "\n",
            "3. **Tailor the Resume:**  Don't submit the same resume for every application.  Carefully review the job description and tailor the content, keywords, and order of sections to highlight the most relevant skills and experiences.\n",
            "\n",
            "4. **Refine Project Descriptions:**  Focus on the results and quantifiable impact of each project.  Use action verbs to start each bullet point.\n",
            "\n",
            "5. **Reduce Redundancy:**  Combine information across sections to eliminate repetitive mentions of skills and tools.\n",
            "\n",
            "6. **Proofread Carefully:**  Ensure there are no grammatical errors or typos.\n",
            "\n",
            "\n",
            "By implementing these changes, Mohit can significantly improve the clarity, professionalism, and overall impact of his resume, making it more effective in attracting recruiters' attention and landing interviews.\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#evaluate sentiment....\n",
        "model = genai.GenerativeModel(\"gemini-1.5-flash\")\n",
        "\n",
        "def analyze_resume4(text):\n",
        "    prompt = f\"\"\"You are an expert at analysing resume and giving expert feedbacks. Analyse the following resume content:\n",
        "\n",
        "{text}\n",
        "\n",
        "Tasks:\n",
        "Assess the sentiment of the skills section (e.g., confident, neutral, vague).\n",
        "\"\"\"\n",
        "    response = model.generate_content(prompt)\n",
        "    return response.text\n",
        "\n",
        "\n",
        "result_sentiment = analyze_resume4(resume_text)\n",
        "print(result_sentiment)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 272
        },
        "id": "JNRJoK0SdnY5",
        "outputId": "31767fe0-b3b5-468a-b038-7c9492428b3c"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The sentiment of the Skills and Expertise section is **confident and comprehensive**.  It's not just a list; it's structured and demonstrates a breadth and depth of technical proficiency.  The confident tone stems from several factors:\n",
            "\n",
            "* **Specificity:** Instead of broadly stating \"Machine Learning,\" the section lists specific algorithms, libraries (TensorFlow, PyTorch, etc.), and techniques (NLP, Time Series Analysis). This level of detail showcases a practical understanding beyond theoretical knowledge.\n",
            "\n",
            "* **Extensive Toolset:**  The range of tools listed (software, frameworks, libraries) indicates familiarity with a diverse technological landscape and the ability to adapt to different projects and environments.\n",
            "\n",
            "* **Organized Categorization:** The clear categorization into Languages & Frameworks, Softwares, Machine Learning & AI, and GenAI & LLM Tools helps present the skills in a structured, easy-to-understand manner, further bolstering the confident tone.\n",
            "\n",
            "* **No Vague Claims:**  There are no vague or unsubstantiated claims like \"Proficient in Python\" or \"Familiar with AI.\" The descriptions are precise and suggest hands-on experience.\n",
            "\n",
            "\n",
            "In summary, the section effectively conveys a confident, knowledgeable, and highly capable candidate prepared to contribute across multiple technical domains.  There is no vagueness.  The level of detail creates a strong and positive impact.\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#evaluate strengths....\n",
        "model = genai.GenerativeModel(\"gemini-1.5-flash\")\n",
        "\n",
        "def analyze_resume6(text):\n",
        "    prompt = f\"\"\"You are an expert at analysing resume and giving expert feedbacks. Analyse the following resume content:\n",
        "\n",
        "{text}\n",
        "\n",
        "Tasks:\n",
        "Please Highlight strengths of the resume with reasoning (e.g., well-written sections or standout achievements).\n",
        "\"\"\"\n",
        "    response = model.generate_content(prompt)\n",
        "    return response.text\n",
        "\n",
        "\n",
        "result_strength = analyze_resume6(resume_text)\n",
        "print(result_strength)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 580
        },
        "id": "S0QzTiq0gdAV",
        "outputId": "2ff08ce4-11aa-42b4-a7a7-8665fb1b441d"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mohit Laddha's resume is exceptionally strong, demonstrating a clear path of academic excellence, impressive technical skills, and significant extracurricular involvement.  Here's a breakdown of its strengths with reasoning:\n",
            "\n",
            "**Strengths and Reasoning:**\n",
            "\n",
            "* **Quantifiable Achievements:**  The resume consistently uses numbers to showcase accomplishments.  Instead of simply stating \"high accuracy,\" it specifies \"98.6% accuracy\" in the exoplanet habitability prediction. This quantification applies to internship results (e.g., \"Generated 10+ alphas,\" \"Sharpe Ratio over 1.58\"), project outcomes (e.g., \"90% accuracy\" in FOD detection, \"MSE reduced by 30%\"), and even extracurricular activities (e.g., \"INR 42,000 in revenue,\" \"4957 votes\"). This makes the impact of his work readily apparent.\n",
            "\n",
            "* **Strong Emphasis on Projects and Internships:**  The resume doesn't just list activities; it details the objectives, methods, results, and technologies used in each project and internship. The descriptions are concise yet comprehensive, highlighting impactful contributions.  The projects are diverse, showcasing proficiency across AI/ML, finance, and image processing. The internships at IIM Ahmedabad and WorldQuant carry significant weight and are well-described.\n",
            "\n",
            "* **Well-Structured and Organized:** The resume follows a logical structure, making it easy to read and understand.  Sections are clearly defined and information is presented in a consistent format.  The use of bullet points enhances readability.\n",
            "\n",
            "* **Impressive Skill Set:** The skills section effectively categorizes his technical abilities (programming languages, software, ML/AI techniques, GenAI tools).  The breadth and depth of his technical skills are remarkable for an undergraduate student.  He demonstrates proficiency in both core programming languages and advanced techniques like time series analysis, deep learning, and large language model applications.\n",
            "\n",
            "* **Demonstrated Leadership and Teamwork:** The \"Positions of Responsibility\" and \"Extracurricular Activities\" sections showcase leadership skills and teamwork abilities.  The description of his role as Secretary of the Aquatics Subcommittee quantifies his impact and responsibility.  His extracurricular achievements further demonstrate initiative and the ability to collaborate effectively.\n",
            "\n",
            "* **Effective Use of Keywords:** The resume is likely to be picked up by Applicant Tracking Systems (ATS) because of its clear and consistent use of relevant keywords throughout.  Terms like \"Deep Learning,\" \"Time Series Analysis,\" \"YOLOv8,\" \"LangChain,\" \"Sharpe Ratio,\" are all strategically integrated.\n",
            "\n",
            "* **High-Impact Internships:**  The internships at IIM Ahmedabad and WorldQuant are extremely impressive.  These are highly competitive opportunities, and the detailed descriptions of his contributions demonstrate significant analytical and problem-solving skills. The WorldQuant experience, especially the ranking within the top 5% of 30,000+ participants, is a major highlight.\n",
            "\n",
            "\n",
            "**Areas for Minor Improvement:**\n",
            "\n",
            "* **Objective Statement (Consider Removing):** The resume doesn't include a traditional objective statement, which is generally considered optional and sometimes even detrimental in modern resumes.  The accomplishments speak for themselves.\n",
            "\n",
            "* **Slight Refinement in Formatting:** While the structure is good, minor formatting tweaks could enhance visual appeal. Consider using bolding strategically for emphasis on key achievements within bullet points.\n",
            "\n",
            "\n",
            "**Overall:**\n",
            "\n",
            "This is an exceptional resume.  Mohit Laddha has clearly presented a compelling case for his skills and achievements.  The resume is well-written, well-structured, and effectively showcases his potential to employers.  It's highly likely to impress recruiters and secure him interviews.\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Identify and flag excessive jargon or filler phrases\n",
        "model = genai.GenerativeModel(\"gemini-1.5-flash\")\n",
        "\n",
        "def analyze_resume10(text):\n",
        "    prompt = f\"\"\"You are an expert at analysing resume and giving expert feedbacks. Analyse the following resume content:\n",
        "\n",
        "{text}\n",
        "\n",
        "Tasks:\n",
        "Please Identify and flag excessive jargon or filler phrases in our resume\n",
        "\"\"\"\n",
        "    response = model.generate_content(prompt)\n",
        "    return response.text\n",
        "\n",
        "\n",
        "result_jargon = analyze_resume10(resume_text)\n",
        "print(result_jargon)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 689
        },
        "id": "uqb9lF9ttow3",
        "outputId": "509b698f-f423-47ee-ea08-e22adac7c93d"
      },
      "execution_count": 44,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "This resume is impressively detailed and showcases significant accomplishments, but it suffers from some areas of jargon overload and unnecessary phrasing.  Here's a breakdown with specific suggestions:\n",
            "\n",
            "**Excessive Jargon/Filler Phrases:**\n",
            "\n",
            "* **\"Academic Courses:\"** This section header is redundant. The list itself clearly indicates academic coursework.  Simply list the courses.\n",
            "\n",
            "* **Many technical terms within skills and project descriptions:** While demonstrating expertise is crucial, the sheer density of terms like \"Latent Dirichlet Allocation (LDA),\" \"Non-Negative Matrix Factorization (NMF),\" \"Sharpe Ratio,\" \"MICE,\" \"SMOTE,\" \"YOLOv8,\" \"UNET,\" \"FAISS,\" \"LlamaIndex,\" etc., overwhelms the reader.  Instead of listing every single algorithm or tool, group related technologies (e.g., \"Deep Learning frameworks: TensorFlow, Keras, PyTorch\") and focus on the *impact* of using them rather than just listing them. For example, instead of \"Implemented Latent Dirichlet Allocation (LDA) and Non-Negative Matrix Factorization (NMF) for comprehensive topic modeling,\" try \"Performed topic modeling using advanced techniques to analyze...\"  The reader doesn't need the specific algorithm names unless directly relevant to the specific job.\n",
            "\n",
            "* **Quantifiable achievements are good, but some are over-emphasized:**  Phrases like \"showcasing academic excellence\" and \"significantly enhancing accuracy and reliability\" are weak filler.  The quantifiable results (rank, percentage improvement) speak for themselves. Remove the extra commentary.\n",
            "\n",
            "* **Overuse of \"Developed\" and similar verbs:** The resume repeatedly uses \"developed,\" \"implemented,\" \"created,\" etc. Vary the language to make it more engaging.  Instead of \"Developed a face recognition system,\" consider \"Built a high-accuracy face recognition system...\" or \"Engineered a face recognition system...\"\n",
            "\n",
            "* **\"Objective:\" in internships:** The objectives are largely self-evident from the description that follows. They can be safely omitted or integrated concisely into the bullet points.\n",
            "\n",
            "* **In project descriptions:**  Avoid phrases like \"ensuring high-quality data for better model training and detection\" (this is implied). Focus on the results: \"Achieved 90% accuracy in FOD detection...\"\n",
            "\n",
            "\n",
            "**Specific Examples and Suggestions for Improvement:**\n",
            "\n",
            "* **Internships:** Instead of stating objectives, integrate key accomplishments directly.  For example, the IIM Ahmedabad internship could be rewritten as:\n",
            "\n",
            "> * Analyzed 4.5M+ tweets on proof-of-stake cryptocurrencies and 4.74M+ on proof-of-work cryptocurrencies to compare sustainability narratives.\n",
            "> * Employed topic modeling (LDA and NMF) to identify key themes within the data.\n",
            "> * Utilized sentiment analysis tools (McDonald Loughran, TextBlob, Vader) to assess public opinion, visualizing results using Matplotlib.\n",
            "\n",
            "* **WorldQuant:**  Focus on impact, not just tasks.  \"Generated 10+ alphas outperforming market benchmarks in US and Chinese equity markets\" is much stronger than the original.\n",
            "\n",
            "* **Projects:** Condense technical details; emphasize results.  For the AI-Powered Runway Inspection project, highlight the 90% accuracy and the novel aspects of automated dataset creation.\n",
            "\n",
            "* **Competition/Conference:**  Focus on the results and the novelty of your approach.   Instead of listing the techniques, highlight the 98.6% accuracy achieved.\n",
            "\n",
            "\n",
            "**Overall Recommendation:**\n",
            "\n",
            "This resume needs a significant rewrite to improve readability and reduce jargon. The focus should shift from *what* you did to *how well* you did it and the *impact* of your work.  Quantifiable results are excellent, but they should be presented more concisely and strategically.  A more concise and impactful resume will grab a recruiter's attention far more effectively. Consider using the STAR method (Situation, Task, Action, Result) for structuring your accomplishments to emphasize your contributions even further.\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#ATS friendly formatting\n",
        "model = genai.GenerativeModel(\"gemini-1.5-flash\")\n",
        "\n",
        "def analyze_resume11(text):\n",
        "    prompt = f\"\"\"You are an expert at analysing resume and giving expert feedbacks. Analyse the following resume content:\n",
        "\n",
        "{text}\n",
        "\n",
        "Tasks:\n",
        "Suggest ATS-friendly formatting (e.g., use of keywords, simple headings) improvements for our resume.\n",
        "\"\"\"\n",
        "    response = model.generate_content(prompt)\n",
        "    return response.text\n",
        "\n",
        "\n",
        "result_ats = analyze_resume11(resume_text)\n",
        "print(result_ats)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "NsCAnvbrv8FY",
        "outputId": "c6053d28-4de6-4e85-d4f0-891be3194b5e"
      },
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mohit Laddha's resume is impressive, showcasing strong academic achievements and significant experience in data science and AI. However, it needs restructuring for better ATS compatibility and readability.  Here's a revised version with expert feedback:\n",
            "\n",
            "\n",
            "**Revised Resume Content:**\n",
            "\n",
            "**MOHIT LADDHA** | +91 9967011152 | mohitladdha21@kgpian.iitkgp.ac.in | linkedin.com/in/[LinkedIn Profile URL] (Add your LinkedIn profile URL here)\n",
            "\n",
            "\n",
            "**SUMMARY**\n",
            "\n",
            "Highly motivated and results-oriented Aerospace Engineering student at IIT Kharagpur with proven expertise in data science, machine learning, and AI, demonstrated through internships at IIM Ahmedabad and WorldQuant, and impactful projects.  Consistently ranked among top performers in national-level competitive examinations and possesses strong leadership and teamwork skills.  Seeking a challenging role leveraging analytical abilities and technical skills in [Target Industry/Role].\n",
            "\n",
            "\n",
            "**EDUCATION**\n",
            "\n",
            "* **Indian Institute of Technology (IIT) Kharagpur** | Kharagpur, India\n",
            "    * B.Tech in Aerospace Engineering (Expected Graduation: 2026) | CGPA: 8.37/10\n",
            "* **Champions Junior Science College, Kharghar** | Kharghar, India\n",
            "    * HSC (Maharashtra Board) | 82.33% (2022)\n",
            "* **New Horizon Public School, Airoli** | Airoli, India\n",
            "    * AISSE (CBSE) | 96.40% (2020)\n",
            "\n",
            "\n",
            "**EXPERIENCE**\n",
            "\n",
            "**Research Consultant** | **WorldQuant – Brain** | March 2024 – Present\n",
            "* Developed and back-tested 10+ alpha trading strategies for US and Chinese equity markets using time series analysis, consistently outperforming market benchmarks.\n",
            "* Achieved Sharpe Ratios > 1.58, fitness > 1, and production correlation < 0.7, indicating high-performance and robust strategies.\n",
            "* Ranked in the Top 5% of 30,000+ participants in the WorldQuant Challenge.\n",
            "\n",
            "**Research Intern** | **IIM Ahmedabad** | March 2024 – May 2024  (Prof. Adrija Majumdar)\n",
            "* Analyzed 9.24M+ tweets on cryptocurrency sustainability using natural language processing (NLP) techniques.\n",
            "* Implemented Latent Dirichlet Allocation (LDA) and Non-Negative Matrix Factorization (NMF) for topic modeling.\n",
            "* Performed sentiment analysis using McDonald Loughran, TextBlob, and VADER lexicons, visualizing results with Matplotlib.\n",
            "\n",
            "\n",
            "**PROJECTS**\n",
            "\n",
            "* **AI-Powered Runway Inspection and FOD Detection** (Jan 2025 – Present, Prof. Sandeep Saha)\n",
            "    * Developed an autonomous FOD detection system using YOLOv8 and UNET, achieving 90% accuracy on 3,000 simulated runway images.\n",
            "    * Automated dataset creation with auto-labeling and annotation.\n",
            "    * Optimized deep learning model with OpenCV for enhanced image processing.\n",
            "\n",
            "* **Finance Chatbot System** (Self-Project)\n",
            "    * Developed a modular stock analysis chatbot using Python and LangChain, integrating Grok (xAI) LLMs for technical, fundamental, risk, and sentiment analysis.\n",
            "    * Deployed on Streamlit with real-time audit trails for explainable and interactive stock recommendations.\n",
            "\n",
            "* **Attenue: Smart Attendance System** (Sep 2024 – Nov 2024, Prof. Amardip Ghosh)\n",
            "    * Developed a face recognition system using Python and OpenCV, integrating Raspberry Pi for remote image capture and data transfer.\n",
            "    * Achieved high-accuracy face matching using face_recognition and facial embedding database.\n",
            "\n",
            "\n",
            "**SKILLS**\n",
            "\n",
            "**Programming Languages:** C, C++, Python, SQL\n",
            "**Libraries/Frameworks:**  C++ STL, NumPy, Pandas, Scikit-learn, TensorFlow, Seaborn, Matplotlib, LangChain, Hugging Face Transformers, OpenAI API\n",
            "**Tools/Software:**  Sublime Text, Visual Studio Code, Jupyter Notebook, MATLAB, Google Colab, MS Office, Streamlit, Canva, FAISS, LlamaIndex\n",
            "**Machine Learning/AI:**  Algorithms, Time Series Analysis, Deep Learning (CNN, RNN), NLP (Topic Modeling, Sentiment Analysis, LDA, NMF), Retrieval-Augmented Generation (RAG)\n",
            "\n",
            "\n",
            "**AWARDS AND RECOGNITION**\n",
            "\n",
            "* Ranked among the top 1% (1M+ students) in the Joint Entrance Examination (JEE) Mains.\n",
            "* Ranked among the top 2% (250,000+ students) in the Joint Entrance Examination (JEE) Advanced.\n",
            "* Secured a top 0.05% rank (55th out of 200,000+ students) in the MHT-CET entrance exam.\n",
            "\n",
            "\n",
            "**COMPETITIONS & PUBLICATIONS** (If applicable, add publications here)\n",
            "\n",
            "* **Data Analytics Challenge | NSSC'23:** Achieved 98.6% accuracy predicting exoplanet habitability using a supervised classification model.\n",
            "* **Excavate | Composite'24:** Developed a regression model predicting Dmax of alloys, reducing MSE by 30%.\n",
            "\n",
            "\n",
            "**LEADERSHIP & EXTRA-CURRICULAR ACTIVITIES**\n",
            "\n",
            "* **Secretary, Aquatics Subcommittee, Technology Students' Gymkhana, IIT Kharagpur:** Managed a budget of 6 Lakhs+, organized 10+ tournaments, and secured 4957 votes.\n",
            "* LLR Hall Water Polo Team: Gold Medal in General Championship.\n",
            "* LLR Hall Illumination Event: Runner-up finish.\n",
            "* LLR Hall Street Play: Silver Medal in General Championship.\n",
            "* Co-founded Facto Store, generating INR 42,000 in revenue.\n",
            "\n",
            "\n",
            "**KEYWORDS:** (Consider adding a separate Keywords section at the end, tailored to specific job applications)  Data Science, Machine Learning, AI, Deep Learning, NLP, Time Series Analysis, Python, TensorFlow,  Trading Strategies,  Financial Modeling,  Software Development,  Leadership, Teamwork,  Aerospace Engineering,  High-Performance Computing\n",
            "\n",
            "\n",
            "**Expert Feedback:**\n",
            "\n",
            "* **ATS Optimization:** The revised structure uses clear headings and bolded keywords, improving ATS scannability.  The use of action verbs at the start of bullet points is crucial. Quantifiable achievements are highlighted.\n",
            "* **Improved Readability:** The resume is now more concise and easier to read.  Information is grouped logically.\n",
            "* **Stronger Summary:** The summary provides a concise overview of skills and accomplishments, targeting a specific role (remember to customize this!).\n",
            "* **Keyword Integration:** The keywords are strategically integrated throughout the resume, not just dumped in a separate section.  Tailor these keywords to specific job descriptions you're applying for.\n",
            "* **Targeted Information:**  While the coursework is impressive, it's only necessary if directly relevant to the job application. You can remove it to make space.\n",
            "* **LinkedIn Profile:**  Always include your LinkedIn profile URL. It helps recruiters learn more about you.\n",
            "\n",
            "\n",
            "Remember to tailor this revised resume to each specific job application by adjusting the summary, keywords, and highlighting the most relevant skills and experiences.  Good luck with your job search!\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#flagging jargons\n",
        "model = genai.GenerativeModel(\"gemini-1.5-flash\")\n",
        "\n",
        "def analyze_resume10(text):\n",
        "    prompt = f\"\"\"You are an expert at analysing resume and giving expert feedbacks. Analyse the following resume content:\n",
        "\n",
        "{text}\n",
        "\n",
        "Tasks:\n",
        "Please Identify and flag excessive jargon or filler phrases in our resume\n",
        "\"\"\"\n",
        "    response = model.generate_content(prompt)\n",
        "    return response.text\n",
        "\n",
        "\n",
        "result_jargon = analyze_resume10(resume_text)\n",
        "print(result_jargon)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 562
        },
        "id": "mS9fzEjzt9zp",
        "outputId": "e5296986-75c9-4997-933e-42aa0626b4dc"
      },
      "execution_count": 49,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "This resume is strong, showcasing impressive achievements and skills, but it does contain some areas for improvement regarding jargon and filler phrases.  Here's a breakdown:\n",
            "\n",
            "**Excessive Jargon/Filler Phrases:**\n",
            "\n",
            "* **\"Academic Courses:\"** This section header is redundant. The list of courses speaks for itself.  Simply list the courses.\n",
            "* **\"MOOCs:\"**  While relevant, consider integrating these into the education section or skills section depending on their relevance.  Listing them separately feels a bit like padding.\n",
            "* **Many phrases in the project descriptions:**  Phrases like \"Developed an autonomous FOD detection system using YOLOv8 & UNET, trained on 3,000 simulated runway images for real-time monitoring\" are overloaded with technical detail.  Focus on the *impact* and *results* rather than the specific tools unless they are exceptionally relevant to the target job. For instance, \"Developed a real-time FOD detection system (YOLOv8, UNET) achieving 90% accuracy on a 3,000-image dataset.\" is more concise and impactful.\n",
            "* **Overly detailed descriptions in internships and projects:** While the detail is impressive, some of it is unnecessary for a resume.  For example, in the WorldQuant internship, mentioning the specific Sharpe Ratio, fitness score, and production correlation might impress a quant, but it may not resonate with a recruiter unfamiliar with those metrics. Focus on the high-level achievement (e.g., \"Consistently outperformed market benchmarks, ranking in the top 5% globally\").  Similar edits are needed for other project descriptions.\n",
            "* **\"Showcasing academic excellence\"**: This is a filler phrase; the impressive ranks and percentages speak for themselves.\n",
            "* **\"Ensuring high-quality data for better model training and detection\"**:  This is implied by the actions taken; remove this phrase.\n",
            "* **\"Implementing the one-vs-all classification with 6 binary models\"**:  This is too technical for a resume. Just state the achievement (98.6% accuracy).\n",
            "* **\"Significantly enhancing accuracy and reliability\"**:  Quantify the enhancement. How much was accuracy improved?  Show, don't tell.\n",
            "* **\"Effectively optimizing the parameters\"**: Again, quantify the optimization. How much better were the parameters?\n",
            "* **\"Reducing the mean squared error (MSE) by 30%\"**: This is good; keep this as it quantifies the improvement.\n",
            "* **\"Achieving a final score of 10.3\"**:  Without context, this is meaningless.  Explain what a score of 10.3 represents.\n",
            "\n",
            "\n",
            "**Recommendations:**\n",
            "\n",
            "1. **Quantify achievements wherever possible:** Use numbers to demonstrate impact (e.g., \"increased efficiency by 15%,\" \"reduced costs by $X\").\n",
            "2. **Focus on results, not just tasks:**  Highlight the outcomes of your work, rather than just listing the steps you took.\n",
            "3. **Tailor your resume:** Adjust the content and emphasis based on the specific job you're applying for.  What are the keywords and requirements of the job description?\n",
            "4. **Use action verbs:** Start your bullet points with strong action verbs (e.g., \"developed,\" \"implemented,\" \"analyzed,\" \"optimized\").\n",
            "5. **Streamline the language:** Use concise and precise language, avoiding jargon unless essential for the target audience.\n",
            "6. **Consolidate sections:** Combine the \"Awards and Achievements\" section with the \"Competitions/Conferences\" section as they overlap.  The quantifiable results are already presented in a clear manner.  This will eliminate repetition and enhance readability.\n",
            "\n",
            "\n",
            "By making these changes, Mohit can create a more impactful and reader-friendly resume that highlights his skills and accomplishments effectively.  The core content is excellent; it just needs some strategic editing to maximize its impact.\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#computing resume quality score\n",
        "model = genai.GenerativeModel(\"gemini-1.5-flash\")\n",
        "\n",
        "def analyze_resume5(text):\n",
        "    prompt = f\"\"\"You are an expert at analysing resume and giving expert resume quality score. Analyse the following resume content:\n",
        "\n",
        "{text}\n",
        "\n",
        "Also here are the insights on clarity, professionalism and completeness : {result_clarity}\n",
        "Also here are the insights on sentiment of the skills section : {result_sentiment}\n",
        "Also here are the insights on strengths of our resume : {result_strength}\n",
        "\n",
        "Tasks:\n",
        "Analyse our resume and the various insights provided on them to give a resume quality score based on the following 4 facctors. :\n",
        "1. Section completenss\n",
        "2. context richness\n",
        "3. clarity and professionalism\n",
        "4. Overall resume strength for role and year of experience\n",
        "\n",
        "Also give score breakdown for each section.\n",
        "\"\"\"\n",
        "    response = model.generate_content(prompt)\n",
        "    return response.text\n",
        "\n",
        "\n",
        "result_score = analyze_resume5(resume_text)\n",
        "print(result_score)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 689
        },
        "id": "bboym0aqeEa0",
        "outputId": "ec76d95d-c203-4f92-dd99-dd8d844aeff4"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Based on the provided resume and analysis, here's a quality score breakdown using the four specified factors.  The scoring will be on a scale of 1 to 5, with 5 being the highest.\n",
            "\n",
            "**Resume Quality Score:**\n",
            "\n",
            "* **Section Completeness (4.5/5):**  The resume includes all essential sections (Education, Experience, Skills, Projects, Awards).  While the Coursework section is arguably less crucial and could be removed or condensed, the overall completeness is high.\n",
            "\n",
            "* **Context Richness (4.8/5):**  The resume excels in providing rich context.  Each project, internship, and achievement is described with detail, including quantifiable results and relevant technologies. This allows the reader to understand the impact of Mohit's work.\n",
            "\n",
            "* **Clarity and Professionalism (4.2/5):** While the content is strong, the formatting needs improvement for optimal clarity and professionalism. Inconsistent formatting and potentially slightly verbose descriptions detract from the overall polish.\n",
            "\n",
            "* **Overall Resume Strength (4.9/5):**  Considering Mohit's year of experience (presuming near-graduation), this resume is exceptionally strong. His achievements, especially the internships and project results, are highly impressive and would stand out to recruiters.\n",
            "\n",
            "\n",
            "**Section-wise Score Breakdown:**\n",
            "\n",
            "* **Education (5/5):** Well-structured, clear, and concisely presents academic achievements and qualifications.\n",
            "\n",
            "* **Awards and Achievements (4/5):** Impressive achievements, but could be integrated better into the main body for a stronger impact.\n",
            "\n",
            "* **Skills and Expertise (5/5):**  Comprehensive, detailed, and effectively categorized.  Highlights a strong technical skill set.\n",
            "\n",
            "* **Internships (5/5):**  Excellent descriptions of internships at prestigious institutions, detailing responsibilities and accomplishments with quantifiable results.\n",
            "\n",
            "* **Projects (4.8/5):**  Strong descriptions, but could benefit from slightly more concise bullet points focusing on impact.\n",
            "\n",
            "* **Positions of Responsibility (4.5/5):** Effectively showcases leadership and teamwork skills with quantifiable results.\n",
            "\n",
            "* **Extracurricular Activities (4/5):**  Good to showcase well-roundedness, but some activities could be condensed or removed to maintain brevity.\n",
            "\n",
            "* **Competition/Conference (5/5):**  Excellent demonstration of data analysis skills and competition success.\n",
            "\n",
            "\n",
            "**Overall:**\n",
            "\n",
            "The resume demonstrates a very high level of quality and would be highly competitive for most roles.  The minor formatting issues and potential for slightly more concise wording are the only reasons for not achieving a perfect score across the board.  Addressing the suggestions for improvement in formatting and incorporating the feedback related to integrating awards into the main body and refining some descriptions will further strengthen the already impressive document.\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#evaluate strengths....\n",
        "model = genai.GenerativeModel(\"gemini-1.5-flash\")\n",
        "\n",
        "def analyze_resume7(text):\n",
        "    prompt = f\"\"\"You are an expert at analysing resume and giving expert feedbacks. Analyse the following resume content:\n",
        "\n",
        "{text}\n",
        "\n",
        "Tasks:\n",
        "Please provide actionable improvement suggestions of our resume.\n",
        "\"\"\"\n",
        "    response = model.generate_content(prompt)\n",
        "    return response.text\n",
        "\n",
        "\n",
        "result_improv = analyze_resume7(resume_text)\n",
        "print(result_improv)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 580
        },
        "id": "xhusFc69a6BM",
        "outputId": "666038e2-032b-4489-d2c7-c76db59fd591"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "This resume is impressively detailed and demonstrates a strong candidate, but it can be significantly improved for clarity, conciseness, and recruiter impact.  Here's a breakdown of actionable improvements:\n",
            "\n",
            "**I. Structure and Formatting:**\n",
            "\n",
            "* **Contact Information:**  Move contact information to the top, aligning it to the left.  Consider removing the student ID (22AE10023). It's not relevant to employers.\n",
            "* **Summary/Objective Statement:** Add a compelling summary statement *above* the Education section. This should be a concise (3-4 lines) overview highlighting key skills and career aspirations.  Tailor this to the specific jobs you're applying for. Avoid generic statements.  The current \"Objective\" statements within internships are good; integrate that style into a broader summary. Example:  \"Highly motivated Aerospace Engineering student with proven expertise in AI/ML, quantitative finance, and data analytics, seeking a challenging role in [target industry/role] leveraging skills in model development, data analysis, and algorithm optimization.\"\n",
            "* **Education:** Reverse chronological order is good.  Consider condensing CGPA/Marks into a single line:  \"B.Tech, Aerospace Engineering, IIT Kharagpur, 8.37 CGPA (Expected 2026)\"  (Note: \"Expected\" is crucial since you're not yet graduated.) Similarly, condense high school information.\n",
            "* **Awards and Achievements:**  Quantify achievements whenever possible. For example, instead of \"Ranked among the top 1%,\" try \"Achieved a top 1% rank among 1 million+ students in the Joint Entrance Examination Mains.\"  This is stronger and more impactful.  Group similar achievements.  For instance, combine the JEE Mains, Advanced, and MHT-CET achievements under a single heading, \"Academic Excellence.\"\n",
            "* **Skills and Expertise:** Categorize more effectively.  Break down \"Languages and Frameworks\" into programming languages and data science libraries.  This makes it easier to scan.  Consider using a bulleted list format rather than a continuous string.   Remove software names unless directly relevant to the roles you're targeting (e.g., if applying for a data science role, keep all; for an aerospace engineering role, prioritize relevant ones like MATLAB).\n",
            "* **Internships and Projects:** Use a consistent format –  Company/Organization, Role, Dates, and a concise description (using action verbs and quantifiable results).  Focus on the impact you made, not just your tasks.  Lead with the strongest accomplishment and use the STAR method (Situation, Task, Action, Result) to describe each one.\n",
            "* **Competitions/Conferences:**  Same as internships/projects—focus on results.  Quantify your achievements (e.g., \"Achieved 98.6% accuracy\").\n",
            "* **Coursework Information:**  Unless directly relevant to the target roles, condense or remove this section.  Focus on courses related to your skills and interests mentioned earlier.\n",
            "* **Positions of Responsibility:**  Quantify your impact. Instead of \"Managed a budget of 6 Lakhs+,\" say \"Successfully managed a budget of over 6 Lakhs INR, resulting in [positive outcome, e.g., efficient allocation of resources, increased participation].\"\n",
            "* **Extracurricular Activities:** Condense; focus on leadership skills and relevant experience.\n",
            "\n",
            "**II. Content Improvements:**\n",
            "\n",
            "* **Quantify Everything:** Use numbers to demonstrate your accomplishments whenever possible.  This makes your resume more impactful and easier to understand.\n",
            "* **Action Verbs:** Start each bullet point with a strong action verb (e.g., \"Developed,\" \"Implemented,\" \"Managed,\" \"Optimized\").\n",
            "* **Focus on Results:**  Instead of listing tasks, focus on the results you achieved. What impact did your work have?\n",
            "* **Tailor to Each Job:** Customize your resume for each job application.  Highlight the skills and experiences most relevant to the specific job description.\n",
            "* **Proofread Carefully:**  Ensure your resume is free of grammatical errors and typos.\n",
            "\n",
            "**III.  Specific Examples of Improvement:**\n",
            "\n",
            "* **Instead of:** \"Research Intern | IIM Ahmedabad | Prof. Adrija Majumdar March'24 - May’24  Objective:Analysis of Narratives across Green Sustainability and Non-Green Crypto Sustainability\"\n",
            "* **Use:** \"Research Intern, IIM Ahmedabad (March 2024 – May 2024), Prof. Adrija Majumdar.  Analyzed 9.24M+ tweets on cryptocurrency sustainability (Proof-of-Stake vs. Proof-of-Work) using LDA and NMF topic modeling and sentiment analysis (McDonald Loughran, TextBlob, Vader) to identify key narratives and sentiment shifts.  Visualized findings with Matplotlib to support research conclusions.\"\n",
            "\n",
            "By implementing these changes, you'll transform your resume into a much more effective tool for attracting the attention of recruiters and landing interviews. Remember to tailor it to each specific job application.\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#computing the final output\n",
        "model = genai.GenerativeModel(\"gemini-1.5-flash\")\n",
        "\n",
        "def analyze_resume8(text):\n",
        "    prompt = f\"\"\"You are an expert at analysing resume and giving expert feebdack. Analyse the following resume content:\n",
        "\n",
        "You are given a detailed evaluation of a resume.\n",
        "Here is our resume : {text}\n",
        "Here is our detailed insights on missing and underdeveloped sections : {result_missing_sections}\n",
        "Here is our detailed inisghts on clarity and professionalism : {result_clarity}\n",
        "Here is our detailed insights on assesment of sentiment of skills sections of our resume : {result_sentiment}\n",
        "Here is our detailed insights on resume quality score : {result_score}\n",
        "Here is our detailed insights on strengths of our resume : {result_strength}\n",
        "Here is our detailed insights on improvement suggestions for our resume : {result_improv}\n",
        "Here is our detailed insights on removing jargon and filler phrases : {result_jargon}\n",
        "Here is our detailed insights on ATS friendly formatting : {result_ats}\n",
        "\n",
        "Your task is to extract and present the final findings in a structured JSON format which has been provided below.\n",
        "\n",
        "Here’s an example of the expected JSON output format:\n",
        "\n",
        "{{\n",
        "  \"sections_detected\": [\"Summary\", \"Skills\", \"Experience\", \"Education\"],\n",
        "  \"missing_sections\": [\"Certifications\", \"Projects\"],\n",
        "  \"well_written_sections\": [\n",
        "    \"Experience section has depth in skills\",\n",
        "    \"Solid educational background from top tier institute\"\n",
        "  ],\n",
        "  \"resume_quality_score\": 78,\n",
        "  \"skills_sentiment_summary\": \"Confident and specific, but lacks technical keywords\",\n",
        "  \"improvement_suggestions\": [\n",
        "    \"Add a Certifications section to showcase credentials.\",\n",
        "    \"Incorporate quantifiable achievements in the Experience section.\"\n",
        "  ]\n",
        "  \"Removing jargon and filler phrases recommendation \" : [\"use star method etc.\"]\n",
        "  \"ATS Friendly formatting recommendation \" : [\"use star method etc.\"]\n",
        "}}\n",
        "\n",
        "Now, using the format shown above, convert the following evaluation into JSON. Be concise, output **only valid JSON**, and do not include markdown, extra text, or explanation.\n",
        "\n",
        "\"\"\"\n",
        "    response = model.generate_content(prompt)\n",
        "    return response.text\n",
        "\n",
        "\n",
        "result = analyze_resume8(resume_text)\n",
        "print(result)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 272
        },
        "id": "pQIIvqHshZ-u",
        "outputId": "40582a8a-fd05-4a49-c0e6-e009210e3957"
      },
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "```json\n",
            "{\n",
            "  \"sections_detected\": [\"Summary\", \"Skills\", \"Experience\", \"Education\", \"Awards and Achievements\", \"Internships\", \"Projects\", \"Positions of Responsibility\", \"Extracurricular Activities\", \"Competition/Conference\", \"Coursework Information\"],\n",
            "  \"missing_sections\": [],\n",
            "  \"well_written_sections\": [\"Impressive Projects and Internships\", \"Detailed Descriptions\", \"Comprehensive Skill Set\", \"Quantifiable Achievements\", \"Leadership Experience\"],\n",
            "  \"resume_quality_score\": 94,\n",
            "  \"skills_sentiment_summary\": \"Confident and comprehensive\",\n",
            "  \"improvement_suggestions\": [\"Add a compelling summary statement\", \"Improve Formatting\", \"Tailor the Resume\", \"Refine Project Descriptions\", \"Reduce Redundancy\", \"Proofread Carefully\", \"Quantify achievements\", \"Focus on results\", \"Stronger action verbs\"],\n",
            "  \"Removing jargon and filler phrases recommendation\": [\"Quantify achievements\", \"Focus on results\", \"Tailor your resume\", \"Use action verbs\", \"Streamline the language\", \"Consolidate sections\"],\n",
            "  \"ATS Friendly formatting recommendation\": [\"Use clear headings and bolded keywords\", \"Use action verbs\", \"Quantifiable achievements\", \"Logical grouping of information\", \"Include LinkedIn Profile URL\", \"Keywords section\"]\n",
            "}\n",
            "```\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Converting the result into format"
      ],
      "metadata": {
        "id": "PRUv5bMRrUOn"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "The below code converts our text into json file which is downloadable from the side window"
      ],
      "metadata": {
        "id": "lZPY9lBH1NgL"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import json\n",
        "\n",
        "# Step 1: Run your model and get the result\n",
        "result = analyze_resume8(resume_text)  # This returns a JSON-formatted string\n",
        "\n",
        "# Step 2: Parse the string into a Python dict\n",
        "try:\n",
        "    json_data = json.loads(result)\n",
        "except json.JSONDecodeError as e:\n",
        "    print(\"Error parsing JSON:\", e)\n",
        "    json_data = {}\n",
        "\n",
        "# Step 3: Save the data as a .json file\n",
        "output_filename = \"resume_analysis_output.json\"\n",
        "with open(output_filename, \"w\", encoding=\"utf-8\") as f:\n",
        "    json.dump(json_data, f, indent=2, ensure_ascii=False)\n",
        "\n",
        "print(f\"✅ JSON file saved as: {output_filename}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 53
        },
        "id": "miCLyPJiqSKg",
        "outputId": "a1a092ce-8c71-4cb1-9e53-73b7de4e60bd"
      },
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Error parsing JSON: Expecting value: line 1 column 1 (char 0)\n",
            "✅ JSON file saved as: resume_analysis_output.json\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Below step coverts anlysis into pdf which is downloadable from side window"
      ],
      "metadata": {
        "id": "ncGlT-VX00KC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import json\n",
        "from reportlab.lib.pagesizes import letter\n",
        "from reportlab.lib.styles import getSampleStyleSheet\n",
        "from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer\n",
        "from reportlab.lib.units import inch\n",
        "\n",
        "def generate_pdf_report(data, filename=\"resume_analysis_report.pdf\"):\n",
        "    doc = SimpleDocTemplate(filename, pagesize=letter)\n",
        "    styles = getSampleStyleSheet()\n",
        "    story = []\n",
        "\n",
        "    story.append(Paragraph(\"Resume Analysis Report\", styles['Title']))\n",
        "    story.append(Spacer(1, 0.2 * inch))\n",
        "\n",
        "    # Sections Detected\n",
        "    story.append(Paragraph(\"<b>Sections Detected:</b>\", styles['Heading3']))\n",
        "    story.append(Paragraph(\", \".join(data.get(\"sections_detected\", [])), styles['Normal']))\n",
        "    story.append(Spacer(1, 0.2 * inch))\n",
        "\n",
        "    # Missing Sections\n",
        "    story.append(Paragraph(\"<b>Missing Sections:</b>\", styles['Heading3']))\n",
        "    story.append(Paragraph(\", \".join(data.get(\"missing_sections\", [])) or \"None\", styles['Normal']))\n",
        "    story.append(Spacer(1, 0.2 * inch))\n",
        "\n",
        "    # Well Written Sections\n",
        "    story.append(Paragraph(\"<b>Well-Written Sections:</b>\", styles['Heading3']))\n",
        "    story.append(Paragraph(\", \".join(data.get(\"well_written_sections\", [])), styles['Normal']))\n",
        "    story.append(Spacer(1, 0.2 * inch))\n",
        "\n",
        "    # Resume Score\n",
        "    story.append(Paragraph(\"<b>Resume Quality Score:</b>\", styles['Heading3']))\n",
        "    story.append(Paragraph(str(data.get(\"resume_quality_score\", \"N/A\")), styles['Normal']))\n",
        "    story.append(Spacer(1, 0.2 * inch))\n",
        "\n",
        "    # Sentiment Summary\n",
        "    story.append(Paragraph(\"<b>Skills Sentiment Summary:</b>\", styles['Heading3']))\n",
        "    story.append(Paragraph(data.get(\"skills_sentiment_summary\", \"\"), styles['Normal']))\n",
        "    story.append(Spacer(1, 0.2 * inch))\n",
        "\n",
        "    # Suggestions\n",
        "    story.append(Paragraph(\"<b>Improvement Suggestions:</b>\", styles['Heading3']))\n",
        "    for suggestion in data.get(\"improvement_suggestions\", []):\n",
        "        story.append(Paragraph(f\"- {suggestion}\", styles['Normal']))\n",
        "    story.append(Spacer(1, 0.2 * inch))\n",
        "\n",
        "    # Jargon/Filler Suggestions\n",
        "    story.append(Paragraph(\"<b>Jargon & Filler Reduction:</b>\", styles['Heading3']))\n",
        "    for tip in data.get(\"Removing jargon and filler phrases recommendation\", []):\n",
        "        story.append(Paragraph(f\"- {tip}\", styles['Normal']))\n",
        "    story.append(Spacer(1, 0.2 * inch))\n",
        "\n",
        "    # ATS Recommendations\n",
        "    story.append(Paragraph(\"<b>ATS-Friendly Formatting Tips:</b>\", styles['Heading3']))\n",
        "    for tip in data.get(\"ATS Friendly formatting recommendation\", []):\n",
        "        story.append(Paragraph(f\"- {tip}\", styles['Normal']))\n",
        "    story.append(Spacer(1, 0.2 * inch))\n",
        "\n",
        "    doc.build(story)\n",
        "    print(f\"✅ PDF generated: {filename}\")\n",
        "\n",
        "# ---------- Clean and parse your raw text ----------\n",
        "import re\n",
        "\n",
        "# Suppose `result` is your full model output as a string\n",
        "cleaned_result = re.sub(r\"^```json\\s*|\\s*```$\", \"\", result.strip(), flags=re.DOTALL)\n",
        "\n",
        "# Now parse JSON\n",
        "parsed_result = json.loads(cleaned_result)\n",
        "\n",
        "# Generate PDF\n",
        "generate_pdf_report(parsed_result)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TCwgPM-c0ku-",
        "outputId": "d5e76779-0dcd-44fe-c4e0-215901d65766"
      },
      "execution_count": 58,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✅ PDF generated: resume_analysis_report.pdf\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "result"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 108
        },
        "id": "71dBswSrz-Bx",
        "outputId": "45ecccb8-ec54-4e6f-d6a1-9b94feceb114"
      },
      "execution_count": 56,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'```json\\n{\\n  \"sections_detected\": [\"Summary\", \"Skills\", \"Experience\", \"Education\", \"Awards and Achievements\", \"Internships\", \"Projects\", \"Positions of Responsibility\", \"Extracurricular Activities\", \"Competition/Conference\", \"Coursework Information\"],\\n  \"missing_sections\": [],\\n  \"well_written_sections\": [\"Impressive Projects and Internships\", \"Quantifiable Achievements\", \"Detailed Descriptions\", \"Comprehensive Skill Set\", \"Leadership Experience\"],\\n  \"resume_quality_score\": 94,\\n  \"skills_sentiment_summary\": \"Confident and comprehensive\",\\n  \"improvement_suggestions\": [\"Add a compelling summary statement\", \"Improve Formatting\", \"Tailor the Resume\", \"Refine Project Descriptions\", \"Reduce Redundancy\", \"Proofread Carefully\"],\\n  \"Removing jargon and filler phrases recommendation\": [\"Use stronger action verbs\", \"Focus on results, not just tasks\", \"Quantify achievements\", \"Streamline the language\", \"Tailor your resume\", \"Consolidate sections\"],\\n  \"ATS Friendly formatting recommendation\": [\"Use clear headings and bolded keywords\", \"Use action verbs at the start of bullet points\", \"Highlight quantifiable achievements\", \"Group information logically\", \"Include LinkedIn profile URL\", \"Customize summary and keywords\"]\\n}\\n```\\n'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 56
        }
      ]
    }
  ]
}
