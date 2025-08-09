import curses
from curses import wrapper
from random import randint, choice

from Data import question_bank
from time import sleep, time

# colors[0] = red          screen[0] = top_window
# colors[1] = green        screen[1] = answer_window - middle
# colors[2] = blue         screen[2] = question_window - bottom
# colors[3] = yellow       screen[3] = time_window - top left

class QuizBrain:
    def __init__(self, questions):
        """
        Initialize the QuizBrain with a list of questions.

        Parameters:
            questions (list): The list of questions for the quiz.
        """
        self.total_questions = questions
        self.points = 0

    def start_game(self, screen, colors):
        """
        Starts the quiz game by prompting the user to select a mode.

        Parameters:
            screen (list): A list of curses window objects used for displaying different UI sections.
            colors (list): A list of color pairs used for styling text in the UI.

        Modes:
            - 'R': Starts the time-based quiz mode.
            - 'D': Starts the difficulty-based quiz mode.
            - 'Q': Quits the game and displays the total points.
        """
        # ask the user to select mode
        while True:
            display("Type R for Timerun, D for Difficulty, Q to quit", screen[1], colors[0])
            mode_selected = get_input(screen[1], colors[3], mode="M")

            screen[1].clear()

            if mode_selected == "d":
                self.difficulty_mode(screen, colors)
            elif mode_selected == "r":
                self.time_run(screen, colors)
            elif mode_selected == "q":
                display(f"Total Points: {self.points}", screen[2], colors[1])
                display("Good Bye", screen[1], colors[1], wait=2.0)
                break
            else:
                continue

    def difficulty_mode(self, screen, colors):
        """
        Runs the difficulty-based quiz mode.

        Parameters:
            screen (list): A list of curses window objects used for displaying different UI sections.
            colors (list): A list of color pairs used for styling text in the UI.

        This mode prompts the user to select a difficulty (Easy, Medium, or Hard),
        filters questions based on that difficulty, and asks a random number of them.
        The user's score is updated based on correct answers.
        """
        # map each character with a difficulty
        difficulty_map = {"e": "easy", "m": "medium", "h": "hard"}

        # Get the difficulty from the user
        while True:
            display("Select Your Difficulty\nE - Easy\nM - Medium\nH- hard", screen[2], colors[3])
            difficulty = get_input(screen[1], colors[1], mode="D")
            if difficulty in difficulty_map:
                question_difficulty = difficulty_map[difficulty]  # Ignore this error
                break

        # Select only the questions of the user selected difficulty and choose a random number of questions to ask.
        questions_of_difficulty = [question for question in question_bank if question.difficulty == question_difficulty]
        questions_to_ask = randint(3, min(len(questions_of_difficulty), 30))
        asked_questions = []

        # ask user number of questions previously calculated
        while len(asked_questions) < questions_to_ask:
            current_question = choice(questions_of_difficulty)
            if current_question in asked_questions:
                continue  # if question is asked already, choose another question

            display(current_question.text, screen[2], colors[2])
            user_answer = get_input(screen[1], colors[1], mode="Q")

            # check answer is right or wrong
            if current_question.check_answer(user_answer):
                display("That Was The Correct Answer", screen[1], colors[1], wait=1)
                self.points += 1
                display(f"Your Points: {self.points}. Press Any Key To Move On", screen[1], colors[1], getch=True)
            else:
                display("That Was Not The Correct Answer", screen[1], colors[0], wait=1)
                display(f"Your Points: {self.points}. Press Any Key To Move On", screen[1], colors[1], getch=True)
            screen[1].clear()

            asked_questions.append(current_question)

        # cleaning up the leftover text
        screen[2].clear()
        screen[2].refresh()

    def time_run(self, screen, colors):
        """
        Runs the time-based quiz mode.

        Parameters:
            screen (list): A list of curses window objects used for displaying different UI sections.
            colors (list): A list of color pairs used for styling text in the UI.

        This mode gives the user a random time limit (30–90 seconds) to answer
        as many questions as possible. The score is updated for each correct answer.
        Time pauses briefly for feedback messages, and the remaining time is shown.
        """
        time_alloted = randint(30, 90)
        display(f"Press Any Key To Start Time Run. Answer As Many Questions In {time_alloted}s", screen[1], colors[3],
                getch=True)

        # setting No delay to make the time continuously running
        screen[1].nodelay(True)

        # cleaning up the leftover text
        screen[1].clear()
        screen[1].refresh()

        # get current time
        start_time = time()
        deadline = start_time + time_alloted

        asked_questions = []

        while len(asked_questions) < len(self.total_questions):
            if time() - start_time >= time_alloted:
                display("Time Up", screen[1], colors[0], wait=1)

                # cleaning up the leftover text
                screen[1].clear()
                screen[1].refresh()
                break

            current_question = choice(self.total_questions)
            if current_question in asked_questions:
                continue
            display(current_question.text, screen[2], colors[2])
            display(str(int(time() - start_time)), screen[3], colors[3])

            user_answer = get_input(screen[1], colors[1], mode="Q", deadline=deadline, timer_screen=screen[3],
                                    start_time=start_time)

            if user_answer is None:
                continue
            elif user_answer is not None:
                if current_question.check_answer(user_answer):
                    pause = 1
                    display("That Was The Correct Answer", screen[1], colors[1], wait=pause)
                    self.points += 1
                else:
                    pause = 1
                    display("That Was Not The Correct Answer", screen[1], colors[0], wait=pause)

                start_time += pause
                deadline += pause  # Adjust timer to "pause" during message

                pause = 1.5
                display(f"Your Points: {self.points}", screen[1], colors[1], wait=pause)
                start_time += pause
                deadline += pause
                screen[1].clear()

            asked_questions.append(current_question)
        screen[1].nodelay(False)

        # cleaning up the leftover text
        screen[2].clear()
        screen[2].refresh()


def display(text, screen, colors, wait = 0.0, getch = False):
    """
    Displays centered text on the given curses screen with specified colors and optional delay or key wait.

    Parameters:
        text (str): The text to be displayed.
        screen (curses.window): The curses window where the text will be rendered.
        colors (int): The color pair attribute to apply to the text.
        wait (float, optional): Number of seconds to wait after displaying the text. Defaults to 0.0.
        getch (bool, optional): If True, waits for a key press after displaying. Defaults to False.
    """
    # Get max height and width of the screen being used
    y, x = screen.getmaxyx()

    # clear screen and add string
    screen.clear()
    screen.addstr(y//2, x // 2 - (len(text)//2), text, colors | curses.A_BOLD | curses.A_ITALIC)
    screen.refresh()
    sleep(wait) # wait only if the user wants else wait for 0.0s

    # wait for a keypress to continue if applicable
    if getch:
        screen.getch()



def get_input(screen, colors, mode, deadline=None, timer_screen=None, start_time=None):
    """
    Waits for and processes a keypress from the user based on the specified input mode.

    Parameters:
        screen (curses.window): The curses window from which to read user input.
        colors (int): The color pair used for any visual feedback (e.g., True/False confirmation).
        mode (str): Determines the type of input expected.
                    "Q" - Quiz input: expects 't' for True or 'f' for False.
                    "M" - Mode selection: expects 'd', 'r', or 'q'.
                    "D" - Difficulty selection: expects 'e', 'm', or 'h'.
        deadline (float, optional): Unix timestamp representing the time limit. If passed, input is skipped after timeout.
        timer_screen (curses.window, optional): Window where elapsed time should be displayed (used in timed mode).
        start_time (float, optional): The timestamp when the timer started, used to calculate and display elapsed time.

    Returns:
        Depends on the mode:
            - bool: True or False in "Q" mode.
            - str: Character ('d', 'r', 'q', 'e', 'm', 'h') in "M" or "D" mode.
            - None: If deadline has passed before a valid input is received.
    """
    while True:
        if deadline and time() >= deadline:
            return None

        if timer_screen and start_time is not None:
            elapsed_time = int(time() - start_time)
            timer_screen.clear()
            timer_screen.addstr(0, 0, str(elapsed_time), colors)
            timer_screen.refresh()

        try:
            ch = screen.getch()
            if ch == -1:
                sleep(0.05)
                continue

            ch = chr(ch).lower()
        except (ValueError, TypeError):
            continue

        if mode == "Q":
            if ch == "f":
                display("False", screen, colors, 0.5)
                return False
            elif ch == "t":
                display("True", screen, colors, 0.5)
                return True
        elif mode == "M":
            if ch in ("d", "r", "q"):
                return ch
        elif mode == "D":
            if ch in ("e", "m", "h"):
                return ch


def main(stdscr):
    # Getting Max Height and Width
    H, W = stdscr.getmaxyx()

    # Initializing Colors
    Red = (curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK), curses.color_pair(1))[1]
    Green = (curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK), curses.color_pair(2))[1]
    Blue = (curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK), curses.color_pair(3))[1]
    Yellow = (curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK), curses.color_pair(4))[1]
    Total_colors = [Red, Green, Blue, Yellow]

    # Creating Windows to use
    top_window = curses.newwin(3, W-1, 0, 0)
    answer_window = curses.newwin(H // 2, W - 1, 4, 0)
    question_window = curses.newwin(H - (H // 2), W - 1, H // 2, 0)
    time_window = curses.newwin(1, 3, 0, 0)
    Total_windows = [top_window, answer_window, question_window, time_window]

    # create object and call method to play quiz
    quiz = QuizBrain(question_bank)
    quiz.start_game(Total_windows, Total_colors)


wrapper(main)
