import os

companies = {
    "google.txt": """
Google is a global technology company known for its search engine, cloud computing services, artificial intelligence research, and Android operating system. Founded in 1998 by Larry Page and Sergey Brin, the company has expanded into numerous fields including online advertising, productivity software, and autonomous vehicle technology. Google Cloud provides infrastructure and machine learning solutions for businesses worldwide. The company also develops innovative AI products such as Gemini and TensorFlow. Through continuous investment in research and development, Google remains one of the most influential technology organizations, shaping how billions of people access information, communicate, work, and learn every day.
""",

    "microsoft.txt": """
Microsoft is one of the world's largest software companies, recognized for products such as Windows, Microsoft Office, Azure Cloud, and GitHub. Founded by Bill Gates and Paul Allen in 1975, Microsoft transformed personal computing and enterprise software. The company invests heavily in artificial intelligence, cloud infrastructure, cybersecurity, and developer tools. Azure has become one of the leading cloud platforms globally. Microsoft also owns LinkedIn and has significant involvement in gaming through Xbox. By focusing on productivity, enterprise solutions, and innovation, Microsoft continues to influence businesses, developers, educational institutions, and consumers around the world.
""",

    "amazon.txt": """
Amazon started as an online bookstore and evolved into a global leader in e-commerce, cloud computing, and digital services. Founded by Jeff Bezos in 1994, Amazon serves millions of customers worldwide through its marketplace platform. Amazon Web Services, known as AWS, provides cloud infrastructure for startups, enterprises, and governments. The company also develops smart devices such as Alexa-powered products and Kindle e-readers. Through logistics innovation, automation, and customer-centric strategies, Amazon has redefined online shopping and cloud technology. Its influence extends across retail, entertainment, artificial intelligence, and modern supply chain management practices.
""",

    "apple.txt": """
Apple is a multinational technology company famous for products including the iPhone, iPad, MacBook, Apple Watch, and AirPods. Founded in 1976 by Steve Jobs, Steve Wozniak, and Ronald Wayne, Apple focuses on integrating hardware, software, and services into a seamless ecosystem. The company is known for innovation in user experience, industrial design, and privacy-focused technology. Apple also provides digital services such as iCloud, Apple Music, and the App Store. Through continuous product development and strong brand loyalty, Apple has become one of the most valuable companies in the world and a leader in consumer technology.
""",

    "meta.txt": """
Meta Platforms is a technology company focused on social networking, virtual reality, and digital communication. Founded by Mark Zuckerberg, the company operates Facebook, Instagram, WhatsApp, and Messenger. Meta invests significantly in artificial intelligence and the development of immersive virtual environments known as the metaverse. Through billions of users across its platforms, the company connects people globally for communication, entertainment, and business. Meta's AI research contributes to advancements in language models, computer vision, and recommendation systems. Its products influence digital marketing, social interaction, and content creation on a worldwide scale.
""",

    "nvidia.txt": """
NVIDIA is a leading technology company specializing in graphics processing units, artificial intelligence hardware, and high-performance computing solutions. Founded in 1993, NVIDIA initially focused on graphics cards for gaming but later became a key player in AI and data center technologies. Its GPUs power machine learning applications, scientific research, and cloud computing infrastructure worldwide. The company develops software frameworks such as CUDA, enabling developers to accelerate computational workloads. NVIDIA technology is widely used in autonomous vehicles, robotics, healthcare, and advanced research environments. Its innovations have significantly contributed to the rapid growth of artificial intelligence.
""",

    "openai.txt": """
OpenAI is an artificial intelligence research and deployment company focused on developing advanced AI systems. Founded in 2015, OpenAI has created influential models such as GPT, ChatGPT, and various multimodal AI technologies. The organization aims to ensure that artificial intelligence benefits humanity while promoting safe and responsible development. OpenAI's research covers natural language processing, reinforcement learning, reasoning systems, and AI alignment. Its products are used by developers, businesses, educators, and researchers worldwide. Through continuous innovation and collaboration, OpenAI has become one of the most recognized organizations in the field of artificial intelligence research.
""",

    "oracle.txt": """
Oracle is a major technology company known for database management systems, enterprise software, and cloud computing services. Founded in 1977, Oracle provides solutions that help organizations manage data, business operations, and large-scale applications. Its database products are widely used across industries including finance, healthcare, telecommunications, and government. Oracle Cloud Infrastructure offers computing, storage, and AI services for modern enterprises. The company also develops enterprise resource planning and customer relationship management software. Through decades of innovation in data technologies, Oracle remains an important provider of mission-critical systems for organizations worldwide.
""",

    "ibm.txt": """
IBM, also known as International Business Machines, is one of the oldest and most influential technology companies in the world. Founded in 1911, IBM has contributed to advancements in computing, artificial intelligence, quantum computing, and enterprise technology. The company develops hardware, software, and consulting solutions for organizations across various industries. IBM Research has produced numerous innovations and patents over the decades. Its Watson AI platform helped popularize enterprise artificial intelligence applications. By focusing on business transformation, hybrid cloud infrastructure, and emerging technologies, IBM continues to play a significant role in global technological progress.
""",

    "tesla.txt": """
Tesla is a technology-driven automotive and energy company known for electric vehicles, battery systems, and renewable energy solutions. Founded in 2003, Tesla accelerated the adoption of sustainable transportation through innovative products such as the Model S, Model 3, Model X, and Model Y. The company invests heavily in autonomous driving technology, artificial intelligence, and advanced manufacturing processes. Tesla also develops solar energy products and large-scale battery storage systems. Through continuous innovation and ambitious engineering goals, Tesla has influenced both the automotive industry and the global transition toward cleaner and more sustainable energy sources.
"""
}

os.makedirs("tech_companies", exist_ok=True)

for filename, content in companies.items():
    with open(os.path.join("tech_companies", filename), "w", encoding="utf-8") as f:
        f.write(content.strip())

print("Created 10 text files successfully.")