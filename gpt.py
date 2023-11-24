from openai import OpenAI

EXAMPLE_RESPONSE = """
CSC 560: Special Topics in Databases
09/23 - Syllabus, Intro to Data Mining, Web Mining
09/28 - Recap: Classification Stage 1: due/ Stage 2: proposal
09/30 - Recap: Clustering
10/05 - Web Mining: Intro
10/07 - Web Structure Mining
10/12 - Web Content Mining
10/14 - FURLOUGH
10/19 - Web Usage Mining Stage 2: due
10/21 - Proposals Stage 3: project implementation
10/26 - Classification: Support Vector Machines
10/28 - Classification: Support Vector Machines
11/02 - Generative models, E-M algorithms
11/04 - User Modeling/Opinion Mining/Recommendations
11/09 - Student Presentations Stage 3: status update
11/11 - Veteran’s Day (no class)
11/16 - FURLOUGH
11/18 - Student Presentations
11/23 - Student Presentations
11/25 - Thanksgiving
11/30 - Student Presentations
12/02 - Student Presentations Stage 3: reports due
"""

def response(input_text):
    # client = OpenAI()

    # response = client.chat.completions.create(
    # model="gpt-3.5-turbo",
    # messages=[
    #     {
    #     "role": "system",
    #     "content": "You will be given text, and you will extract dates from the text and what things/events occur on those respective dates. You will ONLY display those dates and events line by line in the format as follows:\"MM/YY - Event\". MM/YY is numerical."
    #     },
    #     {
    #     "role": "user",
    #     "content": input_text
    #     }
    # ],
    # temperature=0,
    # max_tokens=350,
    # top_p=1.0,
    # frequency_penalty=0,
    # presence_penalty=0
    # )

    return EXAMPLE_RESPONSE