# shellmates_minictf_web
# CTF Challenge: "Imagination Over Knowledge"

## Description:
In this challenge, you are tasked with discovering a secret flag hidden in a URL. The server uses a simple mechanism to display the flag based on the value provided through the `file` query parameter. However, there is a twist—the flag format is more complex than it seems. You will need to look beyond simple guessing and employ your skills to understand the hint and extract the correct flag.

## Objective:
Find the flag by exploring the hint and the server's response to the `flag` query parameter.

## Hint:
Hint: Which club have you recently joined?
reponse is : shellmates

You can trigger the hint by clicking the "Show Hint" button on the web page.

## URL Structure:
The flag is hidden behind a URL parameter. To reveal the flag, visit the URL with the correct `flag` parameter:

http://your-ctf-server.com/?flag=shellmates
## Server Behavior:
- If the correct `flag` parameter is provided, the flag will be displayed.
- If the wrong `flag` parameter is entered, the server will return an error message, urging the user to try again.
- The hint can be triggered by clicking the "Show Hint" button on the page.

## Flag Format:
The flag follows the pattern:
SHELLMATES{E3MC2_1MAG1NAT10N_1S_P0W3RFUL_42}

## Steps to Solve:
1. **Explore the Page**: Visit the page and read the instructions carefully.
2. **Trigger the Hint**: Click the "Show Hint" button to reveal the clue about Einstein's equation and the importance of imagination over knowledge.
3. **Manipulate the URL**: Use the hint to figure out the correct `flag` parameter to input into the URL.
4. **Submit the Flag**: Once you have the correct parameter, submit the flag in the format `SHELLMATES{...}`.

## Challenges/Takeaways:
- Using hints effectively to uncover a solution.
- Manipulating query parameters in a web-based CTF challenge.

Good luck, and remember: imagination is the key to solving this challenge!
