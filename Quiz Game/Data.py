class Question:
    def __init__(self, q_text, q_answer, diff):
        """
        Initializes a Question instance (Question as object).

        Args:
            q_text (str): The question text.
            q_answer (bool): The correct answer.
            diff (str): The difficulty level of the question.
        """
        self.text = q_text
        self.answer = q_answer
        self.difficulty = diff

    def check_answer(self, user_answer):
        """
        Checks if the user's answer matches the correct answer.

        Args:
            user_answer (bool): The answer provided by the user.

        Returns:
            bool: True if the user's answer is correct, False otherwise.
        """
        if user_answer == self.answer:
            return True
        else:
            return False


questions = [
    # Easy (12)
    {"text": "The Earth revolves around the Sun.", "answer": True, "difficulty": "easy"},
    {"text": "Fish can live out of water indefinitely.", "answer": False, "difficulty": "easy"},
    {"text": "Humans have five senses.", "answer": True, "difficulty": "easy"},
    {"text": "The sun rises in the west.", "answer": False, "difficulty": "easy"},
    {"text": "Water freezes at 0 degrees Celsius.", "answer": True, "difficulty": "easy"},
    {"text": "Cats are herbivores.", "answer": False, "difficulty": "easy"},
    {"text": "The color of the sky is blue on a clear day.", "answer": True, "difficulty": "easy"},
    {"text": "Birds can breathe underwater.", "answer": False, "difficulty": "easy"},
    {"text": "The largest mammal is the blue whale.", "answer": True, "difficulty": "easy"},
    {"text": "Antarctica is the hottest continent.", "answer": False, "difficulty": "easy"},
    {"text": "Lightning is a form of electricity.", "answer": True, "difficulty": "easy"},
    {"text": "Plants produce oxygen during photosynthesis.", "answer": True, "difficulty": "easy"},

    # Medium (12)
    {"text": "The speed of sound is faster in water than in air.", "answer": True, "difficulty": "medium"},
    {"text": "Venus is the closest planet to the Sun.", "answer": False, "difficulty": "medium"},
    {"text": "The capital city of Australia is Sydney.", "answer": False, "difficulty": "medium"},
    {"text": "Light behaves as both a particle and a wave.", "answer": True, "difficulty": "medium"},
    {"text": "A heptagon has eight sides.", "answer": False, "difficulty": "medium"},
    {"text": "Blood is red because of iron.", "answer": True, "difficulty": "medium"},
    {"text": "The Great Barrier Reef is located off the coast of South Africa.", "answer": False, "difficulty": "medium"},
    {"text": "Sharks are mammals.", "answer": False, "difficulty": "medium"},
    {"text": "Mount Kilimanjaro is the tallest mountain in Africa.", "answer": True, "difficulty": "medium"},
    {"text": "Einstein developed the theory of general relativity.", "answer": True, "difficulty": "medium"},
    {"text": "The chemical formula for table salt is NaCl.", "answer": True, "difficulty": "medium"},
    {"text": "Octopuses have three hearts.", "answer": True, "difficulty": "medium"},

    # Hard (12)
    {"text": "String theory proposes that fundamental particles are one-dimensional strings.", "answer": True, "difficulty": "hard"},
    {"text": "The Mandelbrot set is a famous fractal in mathematics.", "answer": True, "difficulty": "hard"},
    {"text": "Electrons have a positive electric charge.", "answer": False, "difficulty": "hard"},
    {"text": "The speed of light in vacuum is exactly 299,792,458 meters per second.", "answer": True, "difficulty": "hard"},
    {"text": "Schrödinger's cat thought experiment illustrates quantum superposition.", "answer": True, "difficulty": "hard"},
    {"text": "The entropy of a perfectly ordered crystal at absolute zero is zero.", "answer": True, "difficulty": "hard"},
    {"text": "In general relativity, gravity is described as a force between masses.", "answer": False, "difficulty": "hard"},
    {"text": "The Fibonacci sequence starts with 0 and 1.", "answer": True, "difficulty": "hard"},
    {"text": "A black hole's event horizon is the point beyond which nothing can escape.", "answer": True, "difficulty": "hard"},
    {"text": "The Navier-Stokes equations describe the motion of fluids.", "answer": True, "difficulty": "hard"},
    {"text": "In quantum mechanics, particles can exist in multiple states simultaneously.", "answer": True, "difficulty": "hard"},
    {"text": "The Higgs boson was discovered at the Large Hadron Collider.", "answer": True, "difficulty": "hard"},
]

# List to hold the objects of all the questions.
question_bank = []

# Making objects of every question and appending it to the question bank.
for q in questions:
    question = Question(q["text"], q["answer"], q["difficulty"])
    question_bank.append(question)
