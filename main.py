from flask import Flask

quotes = ["And now here is my secret, a very simple secret: It is only with the heart that one can see rightly; what is essential is invisible to the eye. - Antoine de Saint-Exupéry, The Little Prince",
"All grown ups were once children, but only few of them remember it. - Antoine de Saint-Exupéry, The Little Prince",
"It is the time you have wasted for your rose that makes your rose so important. - Antoine de Saint-Exupéry, The Little Prince",
"The most beautiful things in the world cannot be seen or touched, they are felt with the heart. - Antoine de Saint-Exupéry, The Little Prince",
"You become responsible, forever, for what you have tamed. - Antoine de Saint-Exupéry, The Little Prince",
"But if you tame me, then we shall need each other. To me, you will be unique in all the world. To you, I shall be unique in all the world. ― Antoine de Saint-Exupéry, The Little Prince",
"Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to them. - Antoine de Saint-Exupéry, The Little Prince",
"You - you alone will have the stars as no one else has them...In one of the stars I shall be living. In one of them I shall be laughing. And so it will be as if all the stars were laughing, when you look at the sky at night...You - only you - will have stars that can laugh. - Antoine de Saint-Exupéry, The Little Prince",
"Well, I must endure the presence of a few caterpillars if I wish to become acquainted with the butterflies. - Antoine de Saint-Exupéry, The Little Prince"] 

app = Flask(__name__)

import random

@app.route('/')
def get_quote():
    return random.choice(quotes)

app.run(host='0.0.0.0', port=81)




