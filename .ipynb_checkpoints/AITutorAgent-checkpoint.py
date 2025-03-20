import random

class AIMLTutor:
    def __init__(self):
        self.topics = {
            "supervised_learning": {
                "explanation": "Supervised learning uses labeled data to train models. Example: Predicting exam grades based on study hours.",
                "example_problem": "If a model is trained to predict pizza prices based on size, is this supervised learning? (Yes/No)"
            },
            "neural_network": {
                "explanation": "A neural network is like a brain with layers! Input (data) → Hidden layers (processing) → Output (prediction).",
                "example_problem": "How many layers are in a basic neural network? (a) 1 (b) 2 (c) 3"
            }
        }

    def explain_concept(self, topic):
        return self.topics.get(topic, {}).get("explanation", "Topic not found.")

    def generate_problem(self, topic):
        problem = self.topics.get(topic, {}).get("example_problem", "No problem available.")
        answer = "Yes" if "supervised" in topic else "c"  # Simplified for demo
        return problem, answer

    def start_lesson(self):
        print("🌟 Welcome to AI Tutor! Let's learn AI/ML. Type 'exit' to quit.")
        while True:
            print("\nTopics: supervised_learning, neural_network")
            topic = input("Choose a topic: ").lower()
            if topic == "exit":
                break
            if topic not in self.topics:
                print("Topic not found. Try again!")
                continue
            
            # Explain concept
            print("\n" + self.explain_concept(topic))
            
            # Generate problem
            problem, answer = self.generate_problem(topic)
            user_answer = input(f"\nProblem: {problem}\nYour answer: ")
            
            if user_answer.lower() == answer.lower():
                print("✅ Correct! Awesome!")
            else:
                print(f"❌ The answer is {answer}. Let's review the concept!")

# Run the tutor
tutor = AIMLTutor()
tutor.start_lesson()