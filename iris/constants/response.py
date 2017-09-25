"""Return canned default response to make it more ai like. """
import random


class CannedResponse:
    default_responses = ["Did you say something?",
                         "Sorry! I missed that. Can you repeat that again?",
                         "Pardon!", "I did not catch that",
                         "I will need something to work on",
                         "You need to give me more than that",
                         "I am listening..."]

    def get_default_canned_response(self):
        return random.choice(self.default_responses)
        pass
