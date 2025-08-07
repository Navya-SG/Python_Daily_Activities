'''values = [10, 25, 67, 35, 42, 92]
values.sort()
search_val = 25
low = 0
high = len(values) - 1

while low <= high:
    mid = (low + high) // 2
    if values[mid] == search_val:
        print(f"Found {search_val} at index {mid} in sorted list")
        break
    elif values[mid] < search_val:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not found")
'''
'''
Industry Investment
Anaconda, a major player in Python-based data science, raised $150 million to accelerate AI development using Python 3.
The company is now valued at $1.5 billion, reflecting Python’s central role in enterprise AI and analytics 3. - exolain in simple words
🔹 Anaconda is a company that builds tools for data science and machine learning using Python.
🔹 In 2025, they received $150 million from investors. This money will help them make better tools and software for AI (Artificial Intelligence).
🔹 Because of this investment, Anaconda is now worth $1.5 billion — showing how important Python has become in big companies that use AI and data.

Here’s a simple explanation of how the new AI tool from UC San Diego can detect skin cancer using just 40 dermoscopy images:

🧠 What’s the Problem?
Normally, to train an AI to detect skin cancer, doctors need thousands of labeled images. Each image must be carefully marked to show which parts are healthy and which parts might be cancerous. This takes a lot of time, money, and expert effort.

💡 What Did UC San Diego Do?
Researchers created an AI system called GenSeg that can learn from just a few examples — as few as 40 images 1 2 3.

🔍 How Does It Work?
Start with 40 expert-labeled images of skin lesions (from dermoscopy scans).
The AI uses those to generate synthetic images — fake but realistic examples.
It trains itself using both the real and synthetic images.
A feedback loop helps the AI improve by adjusting the synthetic images based on how well it’s learning.
This way, the AI becomes smart enough to spot skin cancer even with very little data.

🏥 Why Is This Important?
Faster diagnosis: Doctors can get help from AI without waiting for huge datasets.
Cheaper: Clinics don’t need expensive data collection.
More accessible: Even small hospitals or rural clinics can use this technology.
Early detection: Catching skin cancer early can save lives.'''

