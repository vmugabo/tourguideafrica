# Main entry of the program

from guide_africa.utils import app_introduction, request_handler

# Print app Introductions
app_introduction()

# Handle Requests for the user, as the user wants
while True:
    request_handler()
