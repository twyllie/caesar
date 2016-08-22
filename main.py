#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi


# Functions to be used by all classes
def alphabet_position(letter):
    """Returns the relative position of a particular character
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    pos = 0
    for ltr in alphabet:
        if ltr == letter.lower():
            return pos
        pos += 1
    return pos

def rotate_character(char, rot):
    """Returns the character that is the result of moving char by rot
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if char.lower() not in alphabet:
        return char
    mod = (alphabet_position(char) + rot) % len(alphabet)
    if char in alphabet:
        newChar = chr(97 + mod)
    else:
        newChar = chr(65 + mod)
    return newChar

def encrypt(text, rot):
    """Takes a string and rotates each character by a given amount, returns a new string
    """
    newText = ""
    for ltr in text:
        newChar = rotate_character(ltr, rot)
        newText += newChar
    return newText


# Building the bones of the html for the page
html_head ="""
<!DOCTYPE html>
<html>
    <title>Caesar's Legacy</title>
    <body>
"""
html_tail ="""
    </body>
</html>
"""


class MainHandler(webapp2.RequestHandler):
    """Builds the landing page, and handles any returns to it.
    """
    def get(self):
        form = """
        <h3>Enter your text below:</h3>
            <form id ="encryptForm" method="POST" action="/">
                <div>
                <label for="rot">Rotate by:</label>
                <input name="rot" type="text"></input>
                </div>
                <textarea name="text" rows="20" cols="60"></textarea>
                <br>
                <input type="submit"/>
            </form>
        """
        response = html_head + form + html_tail
        self.response.write(response)

    def post(self):
        txt = cgi.escape(self.request.get("text"))
        rot = int(self.request.get("rot"))
        etxt = encrypt(txt, rot)
        form = """
        <h3>Enter your text below:</h3>
            <form id ="encryptForm" method="POST" action="/">
                <div>
                <label for="rot">Rotate by:</label>
                <input name="rot" type="text"></input>
                </div>
                <textarea name="text" rows="20" cols="60">{}</textarea>
                <br>
                <input type="submit"/>
            </form>
        """.format(etxt)
        response = html_head + form + html_tail
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
