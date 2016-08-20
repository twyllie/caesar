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

def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    pos = 0
    for ltr in alphabet:
        if ltr == letter.lower():
            return pos
        pos += 1
    return pos


def rotate_character(char, rot):
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
    newText = ""
    for ltr in text:
        newChar = rotate_character(ltr, rot)
        newText += newChar
    return newText

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
        <div>
            <form id ="encryptForm" method="POST" action="/caesar">
                <input name="rot" type="text"></input>
                <textarea type="text" name="text"></textarea>
                <br>
                <input type="submit"/>
            </form>
        </div>
        """
        response = html_head + form + html_tail
        self.response.write(response)

class CaesarHandler(webapp2.RequestHandler):
    """Handles the data sent through the encryptForm.
    """
    def post(self):
        txt = cgi.escape(self.request.get("text"))
        rot = int(self.request.get("rot"))
        etxt = encrypt(txt, rot)
        response = html_head + "<p>" + etxt + "</p>" + html_tail
        self.response.write(response)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/caesar', CaesarHandler)
], debug=True)
