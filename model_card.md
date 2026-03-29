# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

TuneAlign

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

This system generates top 5 song recommendations from an 18-song catalog based on a user's preferred genre, mood, energy level, and acoustic style. It assumes users have stable, consistent preferences, that someone who likes high-energy music always wants high energy, regardless of context like time of day or activity. The system also assumes users prefer moderately happy songs unless specified otherwise (valence default = 0.65). This is for classroom exploration only, designed to understand how content-based filtering works and where biases emerge. It is not intended for real users or production deployment.



---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

Bias: Every user who does not specify valence is assumed to want moderatly happy songs (0.65). This discriminates against users who prefer sad, melancholic, or aggresive music. All recommendations gain hidden bonus points for being "happy".

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested 7 standard profiles (Study Buddy, Gym Enthusiast, Coffee Shop Lover, etc.) and 10 adversarial profiles designed to expose weaknesses (Empty Profile, Nonexistent Genre, Acoustic EDM Paradox, etc.). I looked for whether recommendations matched musical intuition: does a gym enthusiast get high-energy songs, does a study buddy get calm focus music? The biggest surprise was discovering a hidden happiness bias: every user gets recommendations boosted toward valence 0.65 by default, penalizing those who prefer sad or aggressive music. I also found a critical dataset gap—no songs exist between 0.48-0.74 energy, so users wanting "moderate energy" always get poor matches. A weight adjustment experiment (doubling energy importance, halving genre) revealed that when a classical lover requested high energy, they got EDM instead of classical—showing the system can't handle conflicting preferences gracefully.
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
